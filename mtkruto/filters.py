from typing import Any, Callable, List, Union

from .types import (
    MessageAnimation,
    MessageAudio,
    MessageAutoDeleteTimerChanged,
    MessageChannelCreated,
    MessageChatMigratedFrom,
    MessageChatMigratedTo,
    MessageContact,
    MessageDeletedChatPhoto,
    MessageDice,
    MessageDocument,
    MessageForumTopicClosed,
    MessageForumTopicCreated,
    MessageForumTopicEdited,
    MessageForumTopicReopened,
    MessageGame,
    MessageGiveaway,
    MessageGroupCreated,
    MessageLeftChatMember,
    MessageLink,
    MessageLocation,
    MessageNewChatMembers,
    MessageNewChatPhoto,
    MessageNewChatTitle,
    MessagePhoto,
    MessagePinnedMessage,
    MessagePoll,
    MessageSticker,
    MessageSuccessfulPayment,
    MessageSupergroupCreated,
    MessageText,
    MessageUnsupported,
    MessageUserShared,
    MessageVenue,
    MessageVideo,
    MessageVideoChatEnded,
    MessageVideoChatScheduled,
    MessageVideoChatStarted,
    MessageVideoNote,
    MessageVoice,
    MessageWriteAccessAllowed,
)


class Filter:
    def __init__(self, filter_: Callable[[Any], bool]) -> None:
        self._filter = filter_

    def __call__(self, arg: Any) -> bool:
        return self._filter(arg)

    def __invert__(self) -> "Filter":
        return Filter(lambda v: not self(v))

    def __and__(self, other: "Filter") -> "Filter":
        return Filter(lambda v: self(v) and other(v))

    def __or__(self, other: "Filter") -> "Filter":
        return Filter(lambda v: self(v) or other(v))


text = Filter(lambda v: isinstance(v, MessageText))
"""
Text messages
"""

link = Filter(lambda v: isinstance(v, MessageLink))
"""
Messages containing only a link preview
"""

photo = Filter(lambda v: isinstance(v, MessagePhoto))
"""
Photo messages
"""

document = Filter(lambda v: isinstance(v, MessageDocument))
"""
Document messages
"""

video = Filter(lambda v: isinstance(v, MessageVideo))
"""
Video messages
"""

sticker = Filter(lambda v: isinstance(v, MessageSticker))
"""
Sticker messages
"""

animation = Filter(lambda v: isinstance(v, MessageAnimation))
"""
Animation messages
"""

voice = Filter(lambda v: isinstance(v, MessageVoice))
"""
Voice messages
"""

audio = Filter(lambda v: isinstance(v, MessageAudio))
"""
Audio messages
"""

dice = Filter(lambda v: isinstance(v, MessageDice))
"""
Dice messages
"""

video_note = Filter(lambda v: isinstance(v, MessageVideoNote))
"""
Video note messages
"""

contact = Filter(lambda v: isinstance(v, MessageContact))
"""
Messages that share a contact
"""

game = Filter(lambda v: isinstance(v, MessageGame))
"""
Messages that share a game
"""

poll = Filter(lambda v: isinstance(v, MessagePoll))
"""
Poll messages
"""

venue = Filter(lambda v: isinstance(v, MessageVenue))
"""
Venue messages
"""

location = Filter(lambda v: isinstance(v, MessageLocation))
"""
Location messages
"""

successful_payment = Filter(lambda v: isinstance(v, MessageSuccessfulPayment))
"""
Successful payment messages
"""

new_chat_members = Filter(lambda v: isinstance(v, MessageNewChatMembers))
"""
Service message: new chat members
"""

left_chat_member = Filter(lambda v: isinstance(v, MessageLeftChatMember))
"""
Service message: left chat members
"""

new_chat_title = Filter(lambda v: isinstance(v, MessageNewChatTitle))
"""
Service message: new chat title
"""

new_chat_photo = Filter(lambda v: isinstance(v, MessageNewChatPhoto))
"""
Service message: new chat photo
"""

deleted_chat_photo = Filter(lambda v: isinstance(v, MessageDeletedChatPhoto))
"""
Service message: deleted chat photo
"""

group_created = Filter(lambda v: isinstance(v, MessageGroupCreated))
"""
Service message: group created
"""

supergroup_created = Filter(lambda v: isinstance(v, MessageSupergroupCreated))
"""
Service message: supergroup created
"""

channel_created = Filter(lambda v: isinstance(v, MessageChannelCreated))
"""
Service message: channel created
"""

auto_delete_timer_changed = Filter(
    lambda v: isinstance(v, MessageAutoDeleteTimerChanged)
)
"""
Service message: auto delete timer changed
"""

chat_migrated_to = Filter(lambda v: isinstance(v, MessageChatMigratedTo))
"""
Service message: chat migrated to
"""

chat_migrated_from = Filter(lambda v: isinstance(v, MessageChatMigratedFrom))
"""
Service message: chat migrated from
"""

pinned_message = Filter(lambda v: isinstance(v, MessagePinnedMessage))
"""
Service message: pinned message
"""

user_chared = Filter(lambda v: isinstance(v, MessageUserShared))
"""
Service message: user shared
"""

write_access_allowed = Filter(lambda v: isinstance(v, MessageWriteAccessAllowed))
"""
Service message: write access allowed
"""

forum_topic_created = Filter(lambda v: isinstance(v, MessageForumTopicCreated))
"""
Service message: forum topic created
"""

forum_topic_edited = Filter(lambda v: isinstance(v, MessageForumTopicEdited))
"""
Service message: forum topic edited
"""

forum_topic_closed = Filter(lambda v: isinstance(v, MessageForumTopicClosed))
"""
Service message: forum topic closed
"""

forum_topic_reopened = Filter(lambda v: isinstance(v, MessageForumTopicReopened))
"""
Service message: forum topic reopened
"""

video_chat_scheduled = Filter(lambda v: isinstance(v, MessageVideoChatScheduled))
"""
Service message: video chat scheduled
"""

video_chat_started = Filter(lambda v: isinstance(v, MessageVideoChatStarted))
"""
Service message: video chat started
"""

video_chat_ended = Filter(lambda v: isinstance(v, MessageVideoChatEnded))
"""
Service message: video chat ended
"""

giveaway = Filter(lambda v: isinstance(v, MessageGiveaway))
"""
Messages about giveaways
"""

unsupported = Filter(lambda v: isinstance(v, MessageUnsupported))
"""
Unsupported messages
"""


# Some additional filters
service = (
    new_chat_members
    | left_chat_member
    | new_chat_title
    | new_chat_photo
    | deleted_chat_photo
    | group_created
    | supergroup_created
    | channel_created
    | auto_delete_timer_changed
    | chat_migrated_to
    | chat_migrated_from
    | pinned_message
    | user_chared
    | write_access_allowed
    | forum_topic_created
    | forum_topic_edited
    | forum_topic_closed
    | forum_topic_reopened
    | video_chat_scheduled
    | video_chat_started
    | video_chat_ended
)
"""
Service messages
"""

out = Filter(lambda v: hasattr(v, "out"))
"""
Messages that were sent by the current account
"""

bot = Filter(lambda v: hasattr(v, "from_") and v.from_.is_bot)
"""
Messages that were sent by bots
"""

via_bot = Filter(lambda v: hasattr(v, "via_bot"))
"""
Messages that were sent via inline bots
"""

sender_chat = Filter(lambda v: hasattr(v, "sender_chat"))
"""
Messages that were sent on behalf of chats
"""

media_group = Filter(lambda v: hasattr(v, "media_group_id"))
"""
Messages that are part of a media group
"""

reply = Filter(lambda v: hasattr(v, "reply_to_message_id"))
"""
Messages that are a reply to another message
"""

reply_quote = Filter(lambda v: hasattr(v, "reply_quote"))
"""Messages that have a reply_quote"""

forward = Filter(lambda v: hasattr(v, "forward_date"))
"""Messages that have been forwarded"""

topic = Filter(lambda v: hasattr(v, "is_topic_message"))
"""Updates from forums"""

private = Filter(lambda v: hasattr(v, "chat") and v.chat.type == "private")
"""Updates from private chats"""

group = Filter(lambda v: hasattr(v, "chat") and v.chat.type in {"group", "supergroup"})
"""Updates from groups and supergroups"""

channel = Filter(lambda v: hasattr(v, "chat") and v.chat.type == "channel")
"""Updates from channels"""


def user(ids: Union[str, int, List[Union[str, int]]]) -> Filter:
    """Filter messages coming from one or more users"""
    ids = (
        [ids.lower() if isinstance(ids, str) else ids]
        if not isinstance(ids, list)
        else [i.lower() if isinstance(i, str) else i for i in ids]
    )

    return Filter(
        lambda v: getattr(v, "from_")
        and (
            v.from_.id in ids or (v.from_.username and v.from_.username.lower() in ids)
        )
    )


def chat(ids: Union[str, int, List[Union[str, int]]]) -> Filter:
    """Filter messages coming from one or more chats"""
    ids = (
        [ids.lower() if isinstance(ids, str) else ids]
        if not isinstance(ids, list)
        else [i.lower() if isinstance(i, str) else i for i in ids]
    )

    return Filter(
        lambda v: getattr(v, "chat")
        and (v.chat.id in ids or (v.chat.username and v.chat.username.lower() in ids))
    )
