import {
  DocNode,
  DocNodeInterface,
  TsTypeDef,
} from "https://deno.land/x/deno_doc@0.125.0/types.d.ts";

const nodes = JSON.parse(Deno.readTextFileSync("3_types.json")) as DocNode[];

let code = `import datetime
from typing import Annotated, Any, List, Literal, Optional, TypeAlias, Union


FileSource = Union[str, bytes]

class _Type:
    _client: Any

    def __repr__(self) -> str:
        return "{}({})".format(
            self.__class__.__name__,
            ", ".join(
                map(
                    lambda v: "=".join(v),
                    [[k, repr(v)] for k, v in self.__dict__.items() if not k.startswith("_")],
                )
            ),
        )

`;

const extensions = Deno.readTextFileSync("mtkruto/_type_extensions.py").split(
  "\n",
);

function getExtensions(t: string) {
  let count = false;
  const lines = new Array<string>();
  for (const line of extensions) {
    if (line.trim() == `# extend ${t}`) {
      count = true;
      continue;
    } else if (line.trim() == `# endextend`) {
      if (count) {
        break;
      }
      count = false;
      continue;
    }
    if (count) {
      lines.push(line);
    }
  }
  return lines.join("\n");
}

interface Field {
  original: string;
  snake: string;
  type: string;
  optional: boolean;
}

function getFieldsRecursive(name: string): Field[] {
  const mbInterface = nodes.find((v): v is DocNodeInterface =>
    v.name == name && v.kind == "interface"
  );
  if (!mbInterface) {
    return [];
  }
  const fields = new Array<Field>();
  for (const property of mbInterface.interfaceDef.properties) {
    if (property.name == "signal") {
      continue;
    }
    let type = pythonize(property.tsType!);
    if (property.optional) {
      type = `Optional[${type}]`;
    }
    type = `Annotated[${type}, "${property.name}"]`;
    fields.push({
      original: property.name,
      snake: toSnakeCase(property.name),
      type,
      optional: property.optional,
    });
  }
  let extends_ = mbInterface.interfaceDef.extends;
  while (extends_.length) {
    for (const extend of extends_) {
      for (const field of getFieldsRecursive(extend.repr)) {
        if (!fields.find((v) => v.snake == field.snake)) {
          fields.push(field);
        }
      }
    }
    extends_ = [];
  }
  return fields;
}

for (const node of nodes) {
  if (
    node.name.endsWith("Getter") || node.name.endsWith("Resolver") ||
    node.name == "FileId" ||
    node.name == "UpdateMap" ||
    node.name == "FileSource" ||
    node.name == "UpdateIntersection" ||
    node.name == "MessageTypes" ||
    node.name == "ConnectionState" ||
    node.name == "UpdateConnectionState" ||
    node.name == "AuthorizationState" ||
    node.name == "UpdateAuthorizationState"
  ) {
    continue;
  }
  if (node.kind == "interface") {
    code += `class ${node.name}${
      node.interfaceDef.extends.length
        ? `(${node.interfaceDef.extends.map((v) => v.repr).join(", ")})`
        : "(_Type)"
    }:
`;

    let fields = new Array<Field>();

    const discriminators = new Array<string>();

    for (const property of node.interfaceDef.properties) {
      if (property.name == "signal") {
        continue;
      }
      if (
        property.jsDoc?.tags?.some((v) =>
          v.kind == "unsupported" && v.value == "@discriminator"
        )
      ) {
        discriminators.push(property.name);
      }
      let type = pythonize(property.tsType!);
      if (property.optional) {
        type = `Optional[${type}]`;
      }
      type = `Annotated[${type}, "${property.name}"]`;
      code += `    ${toSnakeCase(property.name)}: ${type}`;
      fields.push({
        original: property.name,
        snake: toSnakeCase(property.name),
        type,
        optional: property.optional,
      });
      code += "\n";
    }

    fields = getFieldsRecursive(node.name);
    code += "    def __init__(self, ";
    for (const field of fields.filter((v) => !v.optional)) {
      code += `${field.snake}: ${field.type}, `;
    }
    const optionalFields = fields.filter((v) => v.optional);
    if (optionalFields.length) {
      code += "*, ";
    }
    for (const field of optionalFields) {
      code += `${field.snake}: ${field.type} = None, `;
    }
    code += "):\n";
    for (const field of fields) {
      code += `        self.${field.snake} = ${field.snake}\n`;
    }

    if (discriminators.length) {
      code += `    __discriminators__ = [${
        discriminators.map((v) => `"${v}"`).join(", ")
      }]\n`;
    }
    code += getExtensions(node.name);
    code += "\n";
  } else if (node.kind == "typeAlias") {
    if (node.typeAliasDef.tsType.kind == "union") {
      code += `${node.name}: TypeAlias = Union[${
        node.typeAliasDef.tsType.union.map((v) => pythonize(v, false)).filter(
          (v) =>
            v != "UpdateAuthorizationState" && v != "UpdateConnectionState",
        ).join(", ")
      }]`;
      code += "\n\n";
    } else {
      code += `${node.name}: TypeAlias = ${
        pythonize(node.typeAliasDef.tsType)
      }\n\n`;
    }
  }
}

function toSnakeCase(name: string) {
  if (name == "from") {
    name = "from_";
  }
  return name.replace(/([A-Z])/g, "_$1").toLowerCase();
}

function pythonize(type: TsTypeDef, q = true): string {
  if (type.kind == "keyword") {
    return type.keyword == "boolean"
      ? "bool"
      : type.keyword == "string"
      ? "str"
      : type.keyword == "number"
      ? "int"
      : type.keyword == "null"
      ? "None"
      : type.keyword;
  } else if (type.kind == "literal") {
    if (type.literal.kind == "string") {
      return `Literal["${type.literal.string}"]`;
    } else if (type.literal.kind == "boolean") {
      return `Literal[${type.literal.boolean ? "True" : "False"}]`;
    }
  }

  if (type.kind == "array") {
    return `list[${pythonize(type.array)}]`;
  }

  if (type.repr == "Date") {
    return "datetime.datetime";
  }

  if (type.kind == "typeRef" && type.typeRef.typeName == "Omit") {
    return pythonize(type.typeRef.typeParams![0]);
  }

  if (
    type.kind == "typeRef" && type.typeRef.typeName == "Record" &&
    type.typeRef.typeParams &&
    type.typeRef.typeParams.every((v) => v.repr == "never")
  ) {
    return "dict[str, Any]";
  }

  if (type.repr == "File") {
    return "Any";
  }

  if (type.repr) {
    if (!q) {
      return type.repr;
    }
    return `"${type.repr}"`;
  } else {
    return "Any";
  }
}

Deno.writeTextFileSync("mtkruto/types.py", code);
