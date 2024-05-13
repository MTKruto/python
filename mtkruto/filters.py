from typing import Any, Callable

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
link = Filter(lambda v: isinstance(v, MessageLink))
photo = Filter(lambda v: isinstance(v, MessagePhoto))
document = Filter(lambda v: isinstance(v, MessageDocument))
video = Filter(lambda v: isinstance(v, MessageVideo))
sticker = Filter(lambda v: isinstance(v, MessageSticker))
animation = Filter(lambda v: isinstance(v, MessageAnimation))
voice = Filter(lambda v: isinstance(v, MessageVoice))
audio = Filter(lambda v: isinstance(v, MessageAudio))
dice = Filter(lambda v: isinstance(v, MessageDice))
video_note = Filter(lambda v: isinstance(v, MessageVideoNote))
contact = Filter(lambda v: isinstance(v, MessageContact))
game = Filter(lambda v: isinstance(v, MessageGame))
poll = Filter(lambda v: isinstance(v, MessagePoll))
venue = Filter(lambda v: isinstance(v, MessageVenue))
location = Filter(lambda v: isinstance(v, MessageLocation))
new_chat_members = Filter(lambda v: isinstance(v, MessageNewChatMembers))
left_chat_member = Filter(lambda v: isinstance(v, MessageLeftChatMember))
new_chat_title = Filter(lambda v: isinstance(v, MessageNewChatTitle))
new_chat_photo = Filter(lambda v: isinstance(v, MessageNewChatPhoto))
deleted_chat_photo = Filter(lambda v: isinstance(v, MessageDeletedChatPhoto))
group_created = Filter(lambda v: isinstance(v, MessageGroupCreated))
supergroup_created = Filter(lambda v: isinstance(v, MessageSupergroupCreated))
channel_created = Filter(lambda v: isinstance(v, MessageChannelCreated))
auto_delete_timer_changed = Filter(
    lambda v: isinstance(v, MessageAutoDeleteTimerChanged)
)
chat_migrated_to = Filter(lambda v: isinstance(v, MessageChatMigratedTo))
chat_migrated_from = Filter(lambda v: isinstance(v, MessageChatMigratedFrom))
pinned_message = Filter(lambda v: isinstance(v, MessagePinnedMessage))
user_chared = Filter(lambda v: isinstance(v, MessageUserShared))
write_access_allowed = Filter(lambda v: isinstance(v, MessageWriteAccessAllowed))
forum_topic_created = Filter(lambda v: isinstance(v, MessageForumTopicCreated))
forum_topic_edited = Filter(lambda v: isinstance(v, MessageForumTopicEdited))
forum_topic_closed = Filter(lambda v: isinstance(v, MessageForumTopicClosed))
forum_topic_reopened = Filter(lambda v: isinstance(v, MessageForumTopicReopened))
video_chat_scheduled = Filter(lambda v: isinstance(v, MessageVideoChatScheduled))
video_chat_started = Filter(lambda v: isinstance(v, MessageVideoChatStarted))
video_chat_ended = Filter(lambda v: isinstance(v, MessageVideoChatEnded))
giveaway = Filter(lambda v: isinstance(v, MessageGiveaway))
unsupported = Filter(lambda v: isinstance(v, MessageUnsupported))


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
out = Filter(lambda v: hasattr(v, "out"))
bot = Filter(lambda v: hasattr(v, "from_") and v.from_.is_bot)
via_bot = Filter(lambda v: hasattr(v, "via_bot"))
sender_chat = Filter(lambda v: hasattr(v, "sender_chat"))
media_group = Filter(lambda v: hasattr(v, "media_group_id"))
reply = Filter(
    lambda v: hasattr(v, "reply_to_message_id") or hasattr(v, "reply_to_message")
)
reply_quote = Filter(lambda v: hasattr(v, "reply_quote"))
forward = Filter(lambda v: hasattr(v, "forward_date"))
topic = Filter(lambda v: hasattr(v, "is_topic_message"))
private = Filter(lambda v: hasattr(v, "chat") and v.chat.type == "private")
group = Filter(lambda v: hasattr(v, "chat") and v.chat.type in {"group", "supergroup"})
channel = Filter(lambda v: hasattr(v, "chat") and v.chat.type == "channel")
