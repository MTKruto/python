from datetime import datetime
from typing import Literal, Optional, Union

from ._utils import satisfies_discriminators, to, transform
from .types import MessageEntityBold, Update, UpdateMessageReactions


def test_transform() -> None:
    left = {"createdAt": {"_": "date", "value": "2024-05-08T09:39:10.307+00:00"}}
    right = {"createdAt": datetime.fromisoformat("2024-05-08T09:39:10.307+00:00")}
    assert transform({**left}) == right
    assert transform({**right}) == left


def test_to() -> None:
    assert to(int, 1, None) == 1
    assert to(str, "", None) == ""
    assert not to(bool, False, None)
    assert to(bool, True, None)
    assert to(Literal[True], True, None)
    assert to(Literal["MTKruto"], "MTKruto", None) == "MTKruto"
    assert to(list[int], [1, 2, 3], None) == [1, 2, 3]
    assert to(list[int], None, None) is None
    assert to(Union[int, str], None, None) is None
    assert to(Union[int, None], 1, None) == 1
    assert to(Union[int, None], None, None) is None
    assert to(Optional[int], 1, None) == 1
    assert to(Optional[int], None, None) is None
    assert to(Union[int, str], None, None) is None
    assert to(Union[int, str, Literal["me"]], "me", None) == "me"
    assert isinstance(
        to(Update, {"messageReactions": {}}, None), UpdateMessageReactions
    )


def test_satisfies_discriminators() -> None:
    assert satisfies_discriminators(UpdateMessageReactions, {"messageReactions": {}})
    assert not satisfies_discriminators(UpdateMessageReactions, {"editedMessage": {}})
    assert not satisfies_discriminators(MessageEntityBold, {"type": "mention"})
    assert satisfies_discriminators(MessageEntityBold, {"type": "bold"})
