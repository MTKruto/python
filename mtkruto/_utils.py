from datetime import datetime
from typing import (
    Any,
    Literal,
    Union,
    get_args,
    get_origin,
    get_type_hints,
)

from .types import _Type


def transform(a: Any) -> Any:
    if isinstance(a, dict):
        to_delete = []
        for key in a:
            if (
                isinstance(a[key], dict)
                and "_" in a[key]
                and a[key]["_"] == "date"
                and "value" in a[key]
                and isinstance(a[key]["value"], str)
            ):
                a[key] = datetime.fromisoformat(a[key]["value"])
            elif isinstance(a[key], datetime):
                a[key] = {
                    "_": "date",
                    "value": a[key].isoformat(timespec="milliseconds"),
                }
            elif isinstance(a[key], dict):
                transform(a[key])
            elif a[key] is None:
                to_delete.append(key)
        for k in to_delete:
            del a[k]
    return a


PRIMITIVES = {datetime, int, str, bool}


def to(type_: Any, value: Any, client: Any) -> Any:
    # NoneType
    if type_ == type(None) or value is None:
        return

    # primitives
    if type_ in PRIMITIVES:
        return value

    # lists
    if get_origin(type_) is list:
        if not isinstance(value, list):
            return
        type_ = get_args(type_)[0]
        return [to(type_, i, client) for i in value]

    # literals
    if get_origin(type_) is Literal:
        return value

    # unions
    if get_origin(type_) is Union:
        args = get_args(type_)

        # optional
        if args[0] != type(None) and args[1] == type(None):
            return to(args[0], value, client)

        if any(map(lambda v: v in PRIMITIVES, args)):
            return value

        for arg in args:
            if satisfies_discriminators(arg, value):
                return to(arg, value, client)

        raise ValueError("Type instantiation failed")

    # actual types
    kwargs = {}
    for k, field in get_type_hints(type_, include_extras=True).items():
        if k.startswith("_"):
            continue
        type__, key = get_args(field)
        kwargs[k] = to(type__, value.pop(key, None), client)

    try:
        instance = type_(**kwargs)
    except TypeError:
        return value

    if client:
        instance._client = client

    return instance


def satisfies_discriminators(of: Any, value: Any) -> bool:
    if not hasattr(of, "__discriminators__"):
        return False
    a = of.__annotations__
    for d in of.__discriminators__:
        if d not in value:
            return False
        try:
            annotation = [v for v in a.values() if v.__metadata__[0] == d][0].__args__[
                0
            ]
            if get_origin(annotation) is Literal:
                if value[d] != annotation.__args__[0]:
                    return False
        except IndexError:
            continue
    return True


def default(o: Any) -> Any:
    if not isinstance(o, _Type):
        raise TypeError
    j = {}
    for k, field in get_type_hints(o.__class__, include_extras=True).items():
        if k.startswith("_"):
            continue
        _, key = get_args(field)
        if hasattr(o, k):
            j[key] = getattr(o, k)
    return j
