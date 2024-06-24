import datetime
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
                    [
                        [k, repr(v)]
                        for k, v in self.__dict__.items()
                        if not k.startswith("_")
                    ],
                )
            ),
        )


class Birthday(_Type):
    day: Annotated[int, "day"]
    month: Annotated[int, "month"]
    year: Annotated[Optional[int], "year"]


class BotCommand(_Type):
    command: Annotated[str, "command"]
    description: Annotated[str, "description"]


class CallbackQueryAnswer(_Type):
    alert: Annotated[bool, "alert"]
    text: Annotated[str, "text"]
    url: Annotated[str, "url"]


class CallbackQueryQuestionGame(_Type):
    type: Annotated[Literal["game"], "type"]
    __discriminators__ = ["type"]


class CallbackQueryQuestionPassword(_Type):
    type: Annotated[Literal["password"], "type"]
    data: Annotated[str, "data"]
    password: Annotated[str, "password"]
    __discriminators__ = ["type"]


class CallbackQueryQuestionButton(_Type):
    type: Annotated[Literal["button"], "type"]
    data: Annotated[str, "data"]
    __discriminators__ = ["type"]


CallbackQueryQuestion: TypeAlias = Union[
    CallbackQueryQuestionGame,
    CallbackQueryQuestionPassword,
    CallbackQueryQuestionButton,
]

ChatAction: TypeAlias = Union[
    Literal["type"],
    Literal["uploadPhoto"],
    Literal["recordVideo"],
    Literal["uploadVideo"],
    Literal["recordVoice"],
    Literal["uploadAudio"],
    Literal["uploadDocument"],
    Literal["chooseSticker"],
    Literal["findLocation"],
    Literal["recordVideoNote"],
    Literal["uploadVideoNote"],
]


class ChatAdministratorRights(_Type):
    is_anonymous: Annotated[bool, "isAnonymous"]
    can_manage_chat: Annotated[bool, "canManageChat"]
    can_delete_messages: Annotated[bool, "canDeleteMessages"]
    can_manage_video_chats: Annotated[bool, "canManageVideoChats"]
    can_restrict_members: Annotated[bool, "canRestrictMembers"]
    can_promote_members: Annotated[bool, "canPromoteMembers"]
    can_change_info: Annotated[bool, "canChangeInfo"]
    can_invite_users: Annotated[bool, "canInviteUsers"]
    can_post_messages: Annotated[Optional[bool], "canPostMessages"]
    can_edit_messages: Annotated[Optional[bool], "canEditMessages"]
    can_pin_messages: Annotated[Optional[bool], "canPinMessages"]
    can_manage_topics: Annotated[Optional[bool], "canManageTopics"]


class ChatMemberRights(_Type):
    can_send_messages: Annotated[Optional[bool], "canSendMessages"]
    can_send_audio: Annotated[Optional[bool], "canSendAudio"]
    can_send_documents: Annotated[Optional[bool], "canSendDocuments"]
    can_send_photos: Annotated[Optional[bool], "canSendPhotos"]
    can_send_videos: Annotated[Optional[bool], "canSendVideos"]
    can_send_video_notes: Annotated[Optional[bool], "canSendVideoNotes"]
    can_send_voice: Annotated[Optional[bool], "canSendVoice"]
    can_send_polls: Annotated[Optional[bool], "canSendPolls"]
    can_send_stickers: Annotated[Optional[bool], "canSendStickers"]
    can_send_animations: Annotated[Optional[bool], "canSendAnimations"]
    can_send_games: Annotated[Optional[bool], "canSendGames"]
    can_send_inline_bot_results: Annotated[Optional[bool], "canSendInlineBotResults"]
    can_add_web_page_previews: Annotated[Optional[bool], "canAddWebPagePreviews"]
    can_change_info: Annotated[Optional[bool], "canChangeInfo"]
    can_invite_users: Annotated[Optional[bool], "canInviteUsers"]
    can_pin_messages: Annotated[Optional[bool], "canPinMessages"]
    can_manage_topics: Annotated[Optional[bool], "canManageTopics"]


class ChatPhoto(_Type):
    small_file_id: Annotated[str, "smallFileId"]
    small_file_unique_id: Annotated[str, "smallFileUniqueId"]
    big_file_id: Annotated[str, "bigFileId"]
    big_file_unique_id: Annotated[str, "bigFileUniqueId"]
    has_video: Annotated[bool, "hasVideo"]
    personal: Annotated[bool, "personal"]


ConnectionStateNotConnected: TypeAlias = Literal["notConnected"]

ConnectionStateUpdating: TypeAlias = Literal["updating"]

ConnectionStateReady: TypeAlias = Literal["ready"]


class Contact(_Type):
    phone_number: Annotated[str, "phoneNumber"]
    first_name: Annotated[str, "firstName"]
    last_name: Annotated[Optional[str], "lastName"]
    user_id: Annotated[Optional[int], "userId"]
    vcard: Annotated[Optional[str], "vcard"]


class Dice(_Type):
    emoji: Annotated[str, "emoji"]
    value: Annotated[int, "value"]


class GiveawayParameters(_Type):
    boosted_chat_id: Annotated[int, "boostedChatId"]
    additional_chat_ids: Annotated[list[int], "additionalChatIds"]
    winner_selection_date: Annotated[datetime.datetime, "winnerSelectionDate"]
    only_new_members: Annotated[bool, "onlyNewMembers"]
    countries: Annotated[list[str], "countries"]


ID: TypeAlias = Union[int, str, Literal["me"]]


class Invoice(_Type):
    title: Annotated[str, "title"]
    description: Annotated[str, "description"]
    start_parameter: Annotated[str, "startParameter"]
    currency: Annotated[str, "currency"]
    total_amount: Annotated[int, "totalAmount"]


class KeyboardButtonPollType(_Type):
    type: Annotated[Optional[Any], "type"]


class LinkPreview(_Type):
    disable: Annotated[Optional[bool], "disable"]
    url: Annotated[Optional[str], "url"]
    small_media: Annotated[Optional[bool], "smallMedia"]
    large_media: Annotated[Optional[bool], "largeMedia"]
    above_text: Annotated[Optional[bool], "aboveText"]


class LiveStreamChannel(_Type):
    id: Annotated[int, "id"]
    scale: Annotated[int, "scale"]
    timestamp: Annotated[int, "timestamp"]


class Location(_Type):
    latitude: Annotated[int, "latitude"]
    longitude: Annotated[int, "longitude"]
    horizontal_accuracy: Annotated[Optional[int], "horizontalAccuracy"]
    live_period: Annotated[Optional[int], "livePeriod"]
    heading: Annotated[Optional[int], "heading"]
    proximity_alert_radius: Annotated[Optional[int], "proximityAlertRadius"]


class LoginUrl(_Type):
    url: Annotated[str, "url"]
    forward_text: Annotated[Optional[str], "forwardText"]
    bot_username: Annotated[Optional[str], "botUsername"]
    request_write_access: Annotated[Optional[bool], "requestWriteAccess"]


class MaskPosition(_Type):
    point: Annotated[Any, "point"]
    x_shift: Annotated[int, "xShift"]
    y_shift: Annotated[int, "yShift"]
    scale: Annotated[int, "scale"]


MessageEntityType: TypeAlias = Union[
    Literal["mention"],
    Literal["hashtag"],
    Literal["botCommand"],
    Literal["url"],
    Literal["email"],
    Literal["bold"],
    Literal["italic"],
    Literal["code"],
    Literal["pre"],
    Literal["textLink"],
    Literal["textMention"],
    Literal["cashtag"],
    Literal["phoneNumber"],
    Literal["underline"],
    Literal["strikethrough"],
    Literal["blockquote"],
    Literal["bankCard"],
    Literal["spoiler"],
    Literal["customEmoji"],
]


class _MessageEntityBase(_Type):
    type: Annotated["MessageEntityType", "type"]
    offset: Annotated[int, "offset"]
    length: Annotated[int, "length"]


class MessageEntityMention(_MessageEntityBase):
    type: Annotated[Literal["mention"], "type"]
    __discriminators__ = ["type"]


class MessageEntityHashtag(_MessageEntityBase):
    type: Annotated[Literal["hashtag"], "type"]
    __discriminators__ = ["type"]


class MessageEntityBotCommand(_MessageEntityBase):
    type: Annotated[Literal["botCommand"], "type"]
    __discriminators__ = ["type"]


class MessageEntityURL(_MessageEntityBase):
    type: Annotated[Literal["url"], "type"]
    __discriminators__ = ["type"]


class MessageEntityEmailAddress(_MessageEntityBase):
    type: Annotated[Literal["email"], "type"]
    __discriminators__ = ["type"]


class MessageEntityBold(_MessageEntityBase):
    type: Annotated[Literal["bold"], "type"]
    __discriminators__ = ["type"]


class MessageEntityItalic(_MessageEntityBase):
    type: Annotated[Literal["italic"], "type"]
    __discriminators__ = ["type"]


class MessageEntityPre(_MessageEntityBase):
    type: Annotated[Literal["pre"], "type"]
    language: Annotated[str, "language"]
    __discriminators__ = ["type"]


class MessageEntityCode(_MessageEntityBase):
    type: Annotated[Literal["code"], "type"]
    __discriminators__ = ["type"]


class MessageEntityTextLink(_MessageEntityBase):
    type: Annotated[Literal["textLink"], "type"]
    url: Annotated[str, "url"]
    __discriminators__ = ["type"]


class MessageEntityTextMention(_MessageEntityBase):
    type: Annotated[Literal["textMention"], "type"]
    user_id: Annotated[int, "userId"]
    __discriminators__ = ["type"]


class MessageEntityCashtag(_MessageEntityBase):
    type: Annotated[Literal["cashtag"], "type"]
    __discriminators__ = ["type"]


class MessageEntityPhoneNumber(_MessageEntityBase):
    type: Annotated[Literal["phoneNumber"], "type"]
    __discriminators__ = ["type"]


class MessageEntityUnderline(_MessageEntityBase):
    type: Annotated[Literal["underline"], "type"]
    __discriminators__ = ["type"]


class MessageEntityStrikethrough(_MessageEntityBase):
    type: Annotated[Literal["strikethrough"], "type"]
    __discriminators__ = ["type"]


class MessageEntityBlockquote(_MessageEntityBase):
    type: Annotated[Literal["blockquote"], "type"]
    __discriminators__ = ["type"]


class MessageEntityBankCard(_MessageEntityBase):
    type: Annotated[Literal["bankCard"], "type"]
    __discriminators__ = ["type"]


class MessageEntitySpoiler(_MessageEntityBase):
    type: Annotated[Literal["spoiler"], "type"]
    __discriminators__ = ["type"]


class MessageEntityCustomEmoji(_MessageEntityBase):
    type: Annotated[Literal["customEmoji"], "type"]
    custom_emoji_id: Annotated[str, "customEmojiId"]
    __discriminators__ = ["type"]


MessageEntity: TypeAlias = Union[
    MessageEntityMention,
    MessageEntityHashtag,
    MessageEntityBotCommand,
    MessageEntityURL,
    MessageEntityEmailAddress,
    MessageEntityBold,
    MessageEntityItalic,
    MessageEntityCode,
    MessageEntityPre,
    MessageEntityTextLink,
    MessageEntityTextMention,
    MessageEntityCashtag,
    MessageEntityPhoneNumber,
    MessageEntityUnderline,
    MessageEntityStrikethrough,
    MessageEntityBlockquote,
    MessageEntityBankCard,
    MessageEntitySpoiler,
    MessageEntityCustomEmoji,
]


class MessageReference(_Type):
    chat_id: Annotated[int, "chatId"]
    message_id: Annotated[int, "messageId"]


MessageSearchFilter: TypeAlias = Union[
    Literal["empty"],
    Literal["animations"],
    Literal["audios"],
    Literal["documents"],
    Literal["photos"],
    Literal["videos"],
    Literal["voiceMessages"],
    Literal["photosAndVideos"],
    Literal["links"],
    Literal["chatPhotos"],
    Literal["videoNotes"],
    Literal["voiceMessagesAndVideoNotes"],
    Literal["mentions"],
    Literal["pinned"],
]


class MiniAppInfo(_Type):
    url: Annotated[str, "url"]


class NetworkStatisticsEntry(_Type):
    sent: Annotated[int, "sent"]
    received: Annotated[int, "received"]


class OpeningHours(_Type):
    timezone: Annotated[str, "timezone"]
    intervals: Annotated[list[Any], "intervals"]


ParseMode: TypeAlias = Union[Literal["HTML"], Literal["Markdown"], None]


class PriceTag(_Type):
    label: Annotated[str, "label"]
    amount: Annotated[int, "amount"]


class ReactionEmoji(_Type):
    type: Annotated[Literal["emoji"], "type"]
    emoji: Annotated[str, "emoji"]


class ReactionCustomEmoji(_Type):
    type: Annotated[Literal["customEmoji"], "type"]
    id: Annotated[str, "id"]


Reaction: TypeAlias = Union[ReactionEmoji, ReactionCustomEmoji]


class RestrictionReason(_Type):
    platform: Annotated[str, "platform"]
    reason: Annotated[str, "reason"]
    text: Annotated[str, "text"]


SelfDestructAfterOpen: TypeAlias = Literal["afterOpen"]

SelfDestructAfterSeconds: TypeAlias = int

SelfDestructOption: TypeAlias = Union[SelfDestructAfterOpen, SelfDestructAfterSeconds]


class ShippingAddress(_Type):
    country_code: Annotated[str, "countryCode"]
    state: Annotated[str, "state"]
    city: Annotated[str, "city"]
    street_line1: Annotated[str, "streetLine1"]
    street_line2: Annotated[str, "streetLine2"]
    post_code: Annotated[str, "postCode"]


class StoryReference(_Type):
    chat_id: Annotated[int, "chatId"]
    story_id: Annotated[int, "storyId"]


class Thumbnail(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    width: Annotated[int, "width"]
    height: Annotated[int, "height"]
    file_size: Annotated[int, "fileSize"]


class _VideoChatCommon(_Type):
    id: Annotated[str, "id"]


class _VideoChatNotEndedCommon(_Type):
    title: Annotated[str, "title"]
    live_stream: Annotated[bool, "liveStream"]
    participant_count: Annotated[int, "participantCount"]


class VideoChatActive(_VideoChatCommon, _VideoChatNotEndedCommon):
    type: Annotated[Literal["active"], "type"]
    recording: Annotated[bool, "recording"]


class VideoChatScheduled(_VideoChatCommon, _VideoChatNotEndedCommon):
    type: Annotated[Literal["scheduled"], "type"]
    scheduled_for: Annotated[datetime.datetime, "scheduledFor"]


class VideoChatEnded(_VideoChatCommon):
    type: Annotated[Literal["ended"], "type"]
    duration: Annotated[int, "duration"]


VideoChat: TypeAlias = Union[VideoChatActive, VideoChatScheduled, VideoChatEnded]


class Voice(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    duration: Annotated[int, "duration"]
    mime_type: Annotated[str, "mimeType"]
    file_size: Annotated[int, "fileSize"]


class Animation(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    width: Annotated[int, "width"]
    height: Annotated[int, "height"]
    duration: Annotated[int, "duration"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]
    file_name: Annotated[Optional[str], "fileName"]
    mime_type: Annotated[str, "mimeType"]
    file_size: Annotated[int, "fileSize"]


class Audio(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    duration: Annotated[int, "duration"]
    performer: Annotated[Optional[str], "performer"]
    title: Annotated[Optional[str], "title"]
    mime_type: Annotated[str, "mimeType"]
    file_size: Annotated[int, "fileSize"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]


class BotCommandScopeDefault(_Type):
    type: Annotated[Literal["default"], "type"]
    __discriminators__ = ["type"]


class BotCommandScopeAllPrivateChats(_Type):
    type: Annotated[Literal["allPrivateChats"], "type"]
    __discriminators__ = ["type"]


class BotCommandScopeAllGroupChats(_Type):
    type: Annotated[Literal["allGroupChats"], "type"]
    __discriminators__ = ["type"]


class BotCommandScopeAllChatAdministrators(_Type):
    type: Annotated[Literal["allChatAdministrators"], "type"]
    __discriminators__ = ["type"]


class BotCommandScopeChat(_Type):
    type: Annotated[Literal["chat"], "type"]
    chat_id: Annotated["ID", "chatId"]
    __discriminators__ = ["type"]


class BotCommandScopeChatAdministrators(_Type):
    type: Annotated[Literal["chatAdministrators"], "type"]
    chat_id: Annotated["ID", "chatId"]
    __discriminators__ = ["type"]


class BotCommandScopeChatMember(_Type):
    type: Annotated[Literal["chatMember"], "type"]
    chat_id: Annotated["ID", "chatId"]
    user_id: Annotated[int, "userId"]
    __discriminators__ = ["type"]


BotCommandScope: TypeAlias = Union[
    BotCommandScopeDefault,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeChat,
    BotCommandScopeChatAdministrators,
    BotCommandScopeChatMember,
]

ChatType: TypeAlias = Union[
    Literal["private"], Literal["group"], Literal["supergroup"], Literal["channel"]
]


class _ChatPBase(_Type):
    id: Annotated[int, "id"]
    type: Annotated["ChatType", "type"]
    color: Annotated[int, "color"]

    async def ban_member(
        self,
        member_id: ID,
        *,
        until_date: Optional[datetime.datetime] = None,
        delete_messages: Optional[bool] = None,
    ) -> None:
        return await self._client.ban_chat_member(
            self.id, member_id, until_date=until_date, delete_messages=delete_messages
        )

    async def unban_member(self, member_id: ID) -> None:
        return await self._client.unban_chat_member(self.id, member_id)

    async def create_invite_link(
        self,
        *,
        title: Optional[str] = None,
        expire_at: Optional[datetime.datetime] = None,
        limits: Optional[int] = None,
        require_approval: Optional[bool] = None,
    ) -> "InviteLink":
        return await self._client.create_invite_link(
            self.id,
            title=title,
            expire_at=expire_at,
            limits=limits,
            require_approval=require_approval,
        )

    async def delete_photo(self) -> None:
        return await self._client.delete_chat_photo(self.id)

    async def delete_sticker_set(self) -> None:
        return await self._client.delete_chat_sticker_set(self.id)

    async def disable_join_requests(self) -> None:
        return await self._client.disable_join_requests(self.id)

    async def enable_join_requests(self) -> None:
        return await self._client.enable_join_requests(self.id)

    async def get_administrators(self) -> List["ChatMember"]:
        return await self._client.get_chat_administrators(self.id)

    async def get_member(self, user_id: ID) -> "ChatMember":
        return await self._client.get_chat_member(self.id, user_id)

    async def get_created_invite_links(
        self,
        *,
        by: Optional["ID"] = None,
        limit: Optional[int] = None,
        revoked: Optional[bool] = None,
        after_date: Optional[datetime.datetime] = None,
        after_invite_link: Optional[str] = None,
    ) -> List["InviteLink"]:
        return await self._client.get_created_invite_links(
            self.id,
            by=by,
            limit=limit,
            revoked=revoked,
            after_date=after_date,
            after_invite_link=after_invite_link,
        )

    async def get_history(
        self,
        *,
        after: Optional["Message"] = None,
        limit: Optional[int] = None,
    ) -> List["Message"]:
        return await self._client.get_history(self.id, after=after, limit=limit)

    async def join(self) -> None:
        return await self._client.join_chat(self.id)

    async def leave(self) -> None:
        return await self._client.leave_chat(self.id)

    async def kick_member(self, member_id: ID) -> None:
        return await self._client.kick_chat_member(self.id, member_id)

    async def set_available_reactions(
        self,
        available_reactions: Union[Literal["none", "all"], List[Reaction]],
    ) -> None:
        return await self._client.set_available_reactions(self.id, available_reactions)

    async def set_boosts_required_to_circumvent_restrictions(self, boosts: int) -> None:
        return await self._client.set_boosts_required_to_circumvent_restrictions(
            self.id, boosts
        )

    async def set_member_rights(
        self,
        member_id: ID,
        *,
        rights: Optional[ChatMemberRights] = None,
        until_date: Optional[datetime.datetime] = None,
    ) -> None:
        return await self._client.set_chat_member_rights(
            self.id, member_id, rights=rights, until_date=until_date
        )

    async def set_photo(
        self,
        photo: FileSource,
        *,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
    ) -> None:
        return await self._client.set_chat_photo(
            self.id,
            photo,
            file_name=file_name,
            mime_type=mime_type,
            chunk_size=chunk_size,
        )

    async def set_sticker_set(self, set_name: str) -> None:
        return await self._client.set_chat_sticker_set(self.id, set_name)


class ChatPPrivate(_ChatPBase):
    type: Annotated[Literal["private"], "type"]
    is_bot: Annotated[Optional[bool], "isBot"]
    first_name: Annotated[str, "firstName"]
    last_name: Annotated[Optional[str], "lastName"]
    username: Annotated[Optional[str], "username"]
    also: Annotated[Optional[list[str]], "also"]
    is_scam: Annotated[bool, "isScam"]
    is_fake: Annotated[bool, "isFake"]
    is_support: Annotated[bool, "isSupport"]
    is_verified: Annotated[bool, "isVerified"]
    is_restricted: Annotated[Optional[bool], "isRestricted"]
    restriction_reason: Annotated[
        Optional[list["RestrictionReason"]], "restrictionReason"
    ]
    __discriminators__ = ["type"]


class ChatPGroup(_ChatPBase):
    type: Annotated[Literal["group"], "type"]
    title: Annotated[str, "title"]
    is_creator: Annotated[bool, "isCreator"]
    __discriminators__ = ["type"]


class ChatPChannelBase(_ChatPBase):
    title: Annotated[str, "title"]
    username: Annotated[Optional[str], "username"]
    also: Annotated[Optional[list[str]], "also"]
    is_scam: Annotated[bool, "isScam"]
    is_fake: Annotated[bool, "isFake"]
    is_verified: Annotated[bool, "isVerified"]
    is_restricted: Annotated[bool, "isRestricted"]
    restriction_reason: Annotated[
        Optional[list["RestrictionReason"]], "restrictionReason"
    ]


class ChatPChannel(ChatPChannelBase):
    type: Annotated[Literal["channel"], "type"]
    __discriminators__ = ["type"]


class ChatPSupergroup(ChatPChannelBase):
    type: Annotated[Literal["supergroup"], "type"]
    is_forum: Annotated[bool, "isForum"]
    __discriminators__ = ["type"]


ChatP: TypeAlias = Union[ChatPPrivate, ChatPGroup, ChatPSupergroup, ChatPChannel]


class Document(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]
    file_name: Annotated[str, "fileName"]
    mime_type: Annotated[str, "mimeType"]
    file_size: Annotated[int, "fileSize"]


class Giveaway(_Type):
    parameters: Annotated["GiveawayParameters", "parameters"]
    winner_count: Annotated[int, "winnerCount"]
    month_count: Annotated[int, "monthCount"]


class InlineQueryResultButton(_Type):
    text: Annotated[str, "text"]
    mini_app: Annotated[Optional["MiniAppInfo"], "miniApp"]
    start_parameter: Annotated[Optional[str], "startParameter"]


class _InputMediaCommon(_Type):
    file_name: Annotated[Optional[str], "fileName"]
    mime_type: Annotated[Optional[str], "mimeType"]
    chunk_size: Annotated[Optional[int], "chunkSize"]


class InputMediaAnimation(_InputMediaCommon):
    animation: Annotated["FileSource", "animation"]
    thumbnail: Annotated[Optional["FileSource"], "thumbnail"]
    caption: Annotated[Optional[str], "caption"]
    duration: Annotated[Optional[int], "duration"]
    width: Annotated[Optional[int], "width"]
    height: Annotated[Optional[int], "height"]
    has_spoiler: Annotated[Optional[bool], "hasSpoiler"]


class InputMediaAudio(_InputMediaCommon):
    audio: Annotated["FileSource", "audio"]
    thumbnail: Annotated[Optional["FileSource"], "thumbnail"]
    caption: Annotated[Optional[str], "caption"]
    duration: Annotated[Optional[int], "duration"]
    performer: Annotated[Optional[str], "performer"]
    title: Annotated[Optional[str], "title"]


class InputMediaDocument(_InputMediaCommon):
    document: Annotated["FileSource", "document"]
    thumbnail: Annotated[Optional["FileSource"], "thumbnail"]
    caption: Annotated[Optional[str], "caption"]


class InputMediaPhoto(_InputMediaCommon):
    photo: Annotated["FileSource", "photo"]
    width: Annotated[Optional[int], "width"]
    height: Annotated[Optional[int], "height"]
    caption: Annotated[Optional[str], "caption"]
    has_spoiler: Annotated[Optional[bool], "hasSpoiler"]
    self_destruct: Annotated[Optional["SelfDestructOption"], "selfDestruct"]


class InputMediaVideo(_InputMediaCommon):
    video: Annotated["FileSource", "video"]
    thumbnail: Annotated[Optional["FileSource"], "thumbnail"]
    duration: Annotated[Optional[int], "duration"]
    width: Annotated[Optional[int], "width"]
    height: Annotated[Optional[int], "height"]
    supports_streaming: Annotated[Optional[bool], "supportsStreaming"]
    caption: Annotated[Optional[str], "caption"]
    has_spoiler: Annotated[Optional[bool], "hasSpoiler"]
    self_destruct: Annotated[Optional["SelfDestructOption"], "selfDestruct"]


InputMedia: TypeAlias = Union[
    InputMediaAnimation,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
]


class InputStoryContentPhoto(_Type):
    photo: Annotated["FileSource", "photo"]
    attached_sticker_file_ids: Annotated[Optional[list[str]], "attachedStickerFileIds"]
    __discriminators__ = ["photo"]


class InputStoryContentVideo(_Type):
    video: Annotated["FileSource", "video"]
    attached_sticker_file_ids: Annotated[Optional[list[str]], "attachedStickerFileIds"]
    duration: Annotated[int, "duration"]
    animation: Annotated[Optional[bool], "animation"]
    __discriminators__ = ["video"]


InputStoryContent: TypeAlias = Union[InputStoryContentPhoto, InputStoryContentVideo]


class KeyboardButtonText(_Type):
    text: Annotated[str, "text"]


class KeyboardButtonRequestUser(KeyboardButtonText):
    request_user: Annotated[Any, "requestUser"]


class KeyboardButtonRequestChat(KeyboardButtonText):
    request_chat: Annotated[Any, "requestChat"]


class KeyboardButtonRequestContact(KeyboardButtonText):
    request_contact: Annotated[Literal[True], "requestContact"]


class KeyboardButtonRequestLocation(KeyboardButtonText):
    request_location: Annotated[Literal[True], "requestLocation"]


class KeyboardButtonRequestPoll(KeyboardButtonText):
    request_poll: Annotated["KeyboardButtonPollType", "requestPoll"]


class KeyboardButtonMiniApp(KeyboardButtonText):
    mini_app: Annotated["MiniAppInfo", "miniApp"]


KeyboardButton: TypeAlias = Union[
    KeyboardButtonText,
    KeyboardButtonRequestUser,
    KeyboardButtonRequestChat,
    KeyboardButtonRequestContact,
    KeyboardButtonRequestLocation,
    KeyboardButtonRequestPoll,
    KeyboardButtonMiniApp,
]


class MessageContentContact(_Type):
    type: Annotated[Literal["contact"], "type"]
    phone_number: Annotated[str, "phoneNumber"]
    first_name: Annotated[str, "firstName"]
    last_name: Annotated[Optional[str], "lastName"]
    vcard: Annotated[Optional[str], "vcard"]


class MessageContentLocation(_Type):
    type: Annotated[Literal["text"], "type"]
    latitude: Annotated[int, "latitude"]
    longitude: Annotated[int, "longitude"]
    horizontal_accuracy: Annotated[Optional[int], "horizontalAccuracy"]
    live_period: Annotated[Optional[int], "livePeriod"]
    heading: Annotated[Optional[int], "heading"]
    proximity_alert_radius: Annotated[Optional[int], "proximityAlertRadius"]


class MessageContentVenue(_Type):
    type: Annotated[Literal["venue"], "type"]
    latitude: Annotated[int, "latitude"]
    longitude: Annotated[int, "longitude"]
    title: Annotated[str, "title"]
    address: Annotated[str, "address"]
    foursquare_id: Annotated[Optional[str], "foursquareId"]
    foursquare_type: Annotated[Optional[str], "foursquareType"]
    google_place_id: Annotated[Optional[str], "googlePlaceId"]
    google_place_type: Annotated[Optional[str], "googlePlaceType"]


class MessageContentText(_Type):
    type: Annotated[Literal["text"], "type"]
    text: Annotated[str, "text"]
    parse_mode: Annotated[Optional["ParseMode"], "parseMode"]
    entities: Annotated[Optional[list["MessageEntity"]], "entities"]
    link_preview: Annotated[Optional["LinkPreview"], "linkPreview"]


class MessageContentInvoice(_Type):
    type: Annotated[Literal["invoice"], "type"]
    title: Annotated[str, "title"]
    description: Annotated[str, "description"]
    payload: Annotated[str, "payload"]
    provider_token: Annotated[str, "providerToken"]
    currency: Annotated[str, "currency"]
    prices: Annotated[list["PriceTag"], "prices"]
    max_tip_amount: Annotated[Optional[int], "maxTipAmount"]
    suggested_tip_amounts: Annotated[Optional[list[int]], "suggestedTipAmounts"]
    provider_data: Annotated[Optional[str], "providerData"]
    photo_url: Annotated[Optional[str], "photoUrl"]
    photo_size: Annotated[Optional[int], "photoSize"]
    photo_width: Annotated[Optional[int], "photoWidth"]
    photo_height: Annotated[Optional[int], "photoHeight"]
    need_name: Annotated[Optional[bool], "needName"]
    need_phone_number: Annotated[Optional[bool], "needPhoneNumber"]
    need_email: Annotated[Optional[bool], "needEmail"]
    need_shipping_a_address: Annotated[Optional[bool], "needShippingAAddress"]
    send_phone_number_to_porvider: Annotated[
        Optional[bool], "sendPhoneNumberToPorvider"
    ]
    send_email_to_provider: Annotated[Optional[bool], "sendEmailToProvider"]
    is_flexible: Annotated[Optional[bool], "isFlexible"]


MessageContent: TypeAlias = Union[
    MessageContentText,
    MessageContentLocation,
    MessageContentVenue,
    MessageContentContact,
    MessageContentInvoice,
]


class MessageReaction(_Type):
    reaction: Annotated["Reaction", "reaction"]
    count: Annotated[int, "count"]
    choosers: Annotated[list[int], "choosers"]
    chosen: Annotated[bool, "chosen"]


class NetworkStatistics(_Type):
    messages: Annotated["NetworkStatisticsEntry", "messages"]
    cdn: Annotated["NetworkStatisticsEntry", "cdn"]


class OrderInfo(_Type):
    name: Annotated[Optional[str], "name"]
    phone_number: Annotated[Optional[str], "phoneNumber"]
    email: Annotated[Optional[str], "email"]
    shipping_address: Annotated[Optional["ShippingAddress"], "shippingAddress"]


class Photo(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    width: Annotated[int, "width"]
    height: Annotated[int, "height"]
    file_size: Annotated[int, "fileSize"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]


class PollOption(_Type):
    text: Annotated[str, "text"]
    entities: Annotated[list["MessageEntity"], "entities"]
    voter_count: Annotated[int, "voterCount"]


class ReactionCount(_Type):
    reaction: Annotated["Reaction", "reaction"]
    count: Annotated[int, "count"]


class ReplyQuote(_Type):
    offset: Annotated[int, "offset"]
    text: Annotated[str, "text"]
    entities: Annotated[list["MessageEntity"], "entities"]


class Sticker(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    type: Annotated[Any, "type"]
    width: Annotated[int, "width"]
    height: Annotated[int, "height"]
    is_animated: Annotated[bool, "isAnimated"]
    is_video: Annotated[bool, "isVideo"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]
    emoji: Annotated[Optional[str], "emoji"]
    set_name: Annotated[Optional[str], "setName"]
    premium_animation: Annotated[Optional[Any], "premiumAnimation"]
    mask_position: Annotated[Optional["MaskPosition"], "maskPosition"]
    custom_emoji_id: Annotated[Optional[str], "customEmojiId"]
    needs_repainting: Annotated[Optional[bool], "needsRepainting"]
    file_size: Annotated[Optional[int], "fileSize"]


class StoryPrivacyEveryone(_Type):
    everyone_except: Annotated[list[int], "everyoneExcept"]
    __discriminators__ = ["everyoneExcept"]


class StoryPrivacyConctacts(_Type):
    contacts_except: Annotated[list[int], "contactsExcept"]
    __discriminators__ = ["contactsExcept"]


class StoryPrivacyCloseFriends(_Type):
    close_friends: Annotated[Literal[True], "closeFriends"]
    __discriminators__ = ["closeFriends"]


class StoryPrivacyOnly(_Type):
    only: Annotated[list[int], "only"]
    __discriminators__ = ["only"]


StoryPrivacy: TypeAlias = Union[
    StoryPrivacyEveryone,
    StoryPrivacyConctacts,
    StoryPrivacyCloseFriends,
    StoryPrivacyOnly,
]


class StoryReaction(_Type):
    reaction: Annotated["Reaction", "reaction"]
    count: Annotated[int, "count"]
    chosen: Annotated[bool, "chosen"]


class User(_Type):
    id: Annotated[int, "id"]
    color: Annotated[int, "color"]
    is_bot: Annotated[bool, "isBot"]
    first_name: Annotated[str, "firstName"]
    last_name: Annotated[Optional[str], "lastName"]
    username: Annotated[Optional[str], "username"]
    also: Annotated[Optional[list[str]], "also"]
    photo: Annotated[Optional["ChatPhoto"], "photo"]
    language_code: Annotated[Optional[str], "languageCode"]
    is_scam: Annotated[bool, "isScam"]
    is_fake: Annotated[bool, "isFake"]
    is_premium: Annotated[bool, "isPremium"]
    is_verified: Annotated[bool, "isVerified"]
    is_support: Annotated[bool, "isSupport"]
    added_to_attachment_menu: Annotated[bool, "addedToAttachmentMenu"]

    async def block(self) -> None:
        return await self._client.block_user(self.id)

    async def unblock(self) -> None:
        return await self._client.unblock_user(self.id)

    @property
    def mention(
        self, name: Optional[str] = None, parse_mode: Optional["ParseMode"] = None
    ) -> str:
        return (
            "[{n}](tg://user?id={i})"
            if parse_mode == "Markdown"
            else "<a href=tg://user?id={i}>{n}</a>"
        ).format(n=name or self.first_name, i=self.id)

    @property
    def full_name(self) -> str:
        if getattr(self, "last_name"):
            return "{f} {l}".format(f=self.first_name, l=self.last_name)
        return self.first_name


class Venue(_Type):
    location: Annotated["Location", "location"]
    title: Annotated[str, "title"]
    address: Annotated[str, "address"]
    foursquare_id: Annotated[Optional[str], "foursquareId"]
    foursquare_type: Annotated[Optional[str], "foursquareType"]


class Video(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    width: Annotated[int, "width"]
    height: Annotated[int, "height"]
    duration: Annotated[int, "duration"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]
    file_name: Annotated[Optional[str], "fileName"]
    mime_type: Annotated[str, "mimeType"]
    file_size: Annotated[int, "fileSize"]


class VideoNote(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    length: Annotated[int, "length"]
    duration: Annotated[int, "duration"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]
    file_name: Annotated[Optional[str], "fileName"]
    file_size: Annotated[int, "fileSize"]


class BusinessConnection(_Type):
    id: Annotated[str, "id"]
    user: Annotated["User", "user"]
    date: Annotated[datetime.datetime, "date"]
    can_reply: Annotated[bool, "canReply"]
    is_enabled: Annotated[bool, "isEnabled"]


class ChatBase(_Type):
    photo: Annotated[Optional["Photo"], "photo"]


class ChatChannel(ChatBase, ChatPChannel):
    video_chat_id: Annotated[Optional[str], "videoChatId"]


class ChatSupergroup(ChatBase, ChatPSupergroup):
    video_chat_id: Annotated[Optional[str], "videoChatId"]


class ChatGroup(ChatBase, ChatPGroup):
    video_chat_id: Annotated[Optional[str], "videoChatId"]


class ChatPrivate(ChatBase, ChatPPrivate):
    birthday: Annotated[Optional["Birthday"], "birthday"]
    address: Annotated[Optional[str], "address"]
    location: Annotated[Optional["Location"], "location"]
    opening_hours: Annotated[Optional["OpeningHours"], "openingHours"]


Chat: TypeAlias = Union[ChatChannel, ChatSupergroup, ChatGroup, ChatPrivate]

ChatMemberStatus: TypeAlias = Union[
    Literal["creator"],
    Literal["administrator"],
    Literal["member"],
    Literal["restricted"],
    Literal["left"],
    Literal["banned"],
]


class _ChatMemberBase(_Type):
    status: Annotated["ChatMemberStatus", "status"]
    user: Annotated["User", "user"]


class ChatMemberCreator(_ChatMemberBase):
    status: Annotated[Literal["creator"], "status"]
    is_anonymous: Annotated[bool, "isAnonymous"]
    title: Annotated[Optional[str], "title"]


class ChatMemberAdministrator(_ChatMemberBase):
    status: Annotated[Literal["administrator"], "status"]
    rights: Annotated["ChatAdministratorRights", "rights"]
    title: Annotated[Optional[str], "title"]


class ChatMemberMember(_ChatMemberBase):
    status: Annotated[Literal["member"], "status"]


class ChatMemberRestricted(_ChatMemberBase):
    status: Annotated[Literal["restricted"], "status"]
    is_member: Annotated[bool, "isMember"]
    rights: Annotated["ChatMemberRights", "rights"]
    until_date: Annotated[Optional[datetime.datetime], "untilDate"]


class ChatMemberLeft(_ChatMemberBase):
    status: Annotated[Literal["left"], "status"]


class ChatMemberBanned(_ChatMemberBase):
    status: Annotated[Literal["banned"], "status"]
    until_date: Annotated[Optional[datetime.datetime], "untilDate"]


ChatMember: TypeAlias = Union[
    ChatMemberCreator,
    ChatMemberAdministrator,
    ChatMemberMember,
    ChatMemberRestricted,
    ChatMemberLeft,
    ChatMemberBanned,
]


class ChosenInlineResult(_Type):
    result_id: Annotated[str, "resultId"]
    from_: Annotated["User", "from"]
    location: Annotated[Optional["Location"], "location"]
    inline_message_id: Annotated[Optional[str], "inlineMessageId"]
    query: Annotated[str, "query"]


class Game(_Type):
    title: Annotated[str, "title"]
    description: Annotated[str, "description"]
    photo: Annotated["Photo", "photo"]
    text: Annotated[Optional[str], "text"]
    text_entities: Annotated[Optional[list["MessageEntity"]], "textEntities"]
    animation: Annotated[Optional["Animation"], "animation"]


class InactiveChat(_Type):
    last_activity: Annotated[datetime.datetime, "lastActivity"]
    chat: Annotated["ChatP", "chat"]


class _InlineKeyboardButtonBase(_Type):
    text: Annotated[str, "text"]


class InlineKeyboardButtonURL(_InlineKeyboardButtonBase):
    url: Annotated[str, "url"]
    __discriminators__ = ["url"]


class InlineKeyboardButtonCallback(_InlineKeyboardButtonBase):
    callback_data: Annotated[str, "callbackData"]
    __discriminators__ = ["callbackData"]


class InlineKeyboardButtonMiniApp(_InlineKeyboardButtonBase):
    mini_app: Annotated["MiniAppInfo", "miniApp"]
    __discriminators__ = ["miniApp"]


class InlineKeyboardButtonLogin(_InlineKeyboardButtonBase):
    login_url: Annotated["LoginUrl", "loginUrl"]
    __discriminators__ = ["loginUrl"]


class InlineKeyboardButtonSwitchInline(_InlineKeyboardButtonBase):
    switch_inline_query: Annotated[str, "switchInlineQuery"]
    __discriminators__ = ["switchInlineQuery"]


class InlineKeyboardButtonSwitchInlineCurrent(_InlineKeyboardButtonBase):
    switch_inline_query_current_chat: Annotated[str, "switchInlineQueryCurrentChat"]
    __discriminators__ = ["switchInlineQueryCurrentChat"]


class InlineKeyboardButtonGame(_InlineKeyboardButtonBase):
    callback_game: Annotated[dict[str, Any], "callbackGame"]
    __discriminators__ = ["callbackGame"]


class InlineKeyboardButtonPay(_InlineKeyboardButtonBase):
    pay: Annotated[bool, "pay"]
    __discriminators__ = ["pay"]


InlineKeyboardButton: TypeAlias = Union[
    InlineKeyboardButtonURL,
    InlineKeyboardButtonCallback,
    InlineKeyboardButtonMiniApp,
    InlineKeyboardButtonLogin,
    InlineKeyboardButtonSwitchInline,
    InlineKeyboardButtonSwitchInlineCurrent,
    InlineKeyboardButtonGame,
    InlineKeyboardButtonPay,
]


class InlineQuery(_Type):
    id: Annotated[str, "id"]
    from_: Annotated["User", "from"]
    query: Annotated[str, "query"]
    offset: Annotated[str, "offset"]
    chat_type: Annotated[Optional[Any], "chatType"]
    location: Annotated[Optional["Location"], "location"]

    async def answer(
        self,
        results: List["InlineQueryResult"],
        *,
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        is_gallery: Optional[bool] = None,
        button: Optional[InlineQueryResultButton] = None,
    ) -> None:
        return await self._client.answer_inline_query(
            self.id,
            results,
            cache_time=cache_time,
            is_personal=is_personal,
            next_offset=next_offset,
            is_gallery=is_gallery,
            button=button,
        )


class InviteLink(_Type):
    invite_link: Annotated[str, "inviteLink"]
    creator: Annotated["User", "creator"]
    requires_approval: Annotated[bool, "requiresApproval"]
    revoked: Annotated[bool, "revoked"]
    title: Annotated[Optional[str], "title"]
    expires_at: Annotated[Optional[datetime.datetime], "expiresAt"]
    limit: Annotated[Optional[int], "limit"]
    pending_join_request_count: Annotated[Optional[int], "pendingJoinRequestCount"]


class MessageInteractions(_Type):
    chat_id: Annotated[int, "chatId"]
    message_id: Annotated[int, "messageId"]
    reactions: Annotated[list["MessageReaction"], "reactions"]
    views: Annotated[int, "views"]
    forwards: Annotated[int, "forwards"]


class MessageReactionCount(_Type):
    chat: Annotated["ChatP", "chat"]
    message_id: Annotated[int, "messageId"]
    date: Annotated[datetime.datetime, "date"]
    reactions: Annotated[list["ReactionCount"], "reactions"]


class MessageReactions(_Type):
    chat: Annotated["ChatP", "chat"]
    message_id: Annotated[int, "messageId"]
    user: Annotated[Optional["User"], "user"]
    actor_chat: Annotated[Optional["ChatP"], "actorChat"]
    date: Annotated[datetime.datetime, "date"]
    old_reactions: Annotated[list["Reaction"], "oldReactions"]
    new_reactions: Annotated[list["Reaction"], "newReactions"]


class Poll(_Type):
    id: Annotated[str, "id"]
    question: Annotated[str, "question"]
    question_entities: Annotated[list["MessageEntity"], "questionEntities"]
    options: Annotated[list["PollOption"], "options"]
    total_voter_count: Annotated[int, "totalVoterCount"]
    is_closed: Annotated[bool, "isClosed"]
    is_anonymous: Annotated[bool, "isAnonymous"]
    type: Annotated[Any, "type"]
    allow_multiple_answers: Annotated[Optional[bool], "allowMultipleAnswers"]
    correct_option_index: Annotated[Optional[int], "correctOptionIndex"]
    explanation: Annotated[Optional[str], "explanation"]
    explanation_entities: Annotated[
        Optional[list["MessageEntity"]], "explanationEntities"
    ]
    open_period: Annotated[Optional[int], "openPeriod"]
    close_date: Annotated[Optional[datetime.datetime], "closeDate"]


class PreCheckoutQuery(_Type):
    id: Annotated[str, "id"]
    from_: Annotated["User", "from"]
    currency: Annotated[str, "currency"]
    total_amount: Annotated[int, "totalAmount"]
    invoice_payload: Annotated[str, "invoicePayload"]
    shipping_option_id: Annotated[Optional[str], "shippingOptionId"]
    order_info: Annotated[Optional["OrderInfo"], "orderInfo"]


class StoryContentPhoto(_Type):
    photo: Annotated["Photo", "photo"]
    __discriminators__ = ["photo"]


class StoryContentVideo(_Type):
    video: Annotated["Video", "video"]
    __discriminators__ = ["video"]


class StoryContentUnsupported(_Type):
    unsupported: Annotated[Literal[True], "unsupported"]
    __discriminators__ = ["unsupported"]


StoryContent: TypeAlias = Union[
    StoryContentPhoto, StoryContentVideo, StoryContentUnsupported
]


class StoryInteractions(_Type):
    reactions: Annotated[Optional[list["StoryReaction"]], "reactions"]
    reaction_count: Annotated[Optional[int], "reactionCount"]
    views: Annotated[int, "views"]
    forwards: Annotated[int, "forwards"]


class StoryInteractiveAreaPosition(_Type):
    x_percentage: Annotated[int, "xPercentage"]
    y_percentage: Annotated[int, "yPercentage"]
    width_percentage: Annotated[int, "widthPercentage"]
    height_percentage: Annotated[int, "heightPercentage"]
    rotation_angle: Annotated[int, "rotationAngle"]


class _StoryInteractiveAreaPositionCommon(_Type):
    position: Annotated["StoryInteractiveAreaPosition", "position"]


class StoryInteractiveAreaLocation(_StoryInteractiveAreaPositionCommon):
    location: Annotated["Location", "location"]


class StoryInteractiveAreaVenue(_StoryInteractiveAreaPositionCommon):
    venue: Annotated["Venue", "venue"]


class StoryInteractiveAreaReaction(_StoryInteractiveAreaPositionCommon):
    reaction: Annotated["Reaction", "reaction"]
    count: Annotated[Optional[int], "count"]
    dark: Annotated[Optional[bool], "dark"]
    flipped: Annotated[Optional[bool], "flipped"]


class StoryInteractiveAreaMessage(_StoryInteractiveAreaPositionCommon):
    message_reference: Annotated["MessageReference", "messageReference"]


StoryInteractiveArea: TypeAlias = Union[
    StoryInteractiveAreaLocation,
    StoryInteractiveAreaVenue,
    StoryInteractiveAreaReaction,
    StoryInteractiveAreaMessage,
]


class SuccessfulPayment(_Type):
    currency: Annotated[str, "currency"]
    total_amount: Annotated[int, "totalAmount"]
    invoice_payload: Annotated[str, "invoicePayload"]
    telegram_payment_charge_id: Annotated[str, "telegramPaymentChargeId"]
    provider_payment_charge_id: Annotated[str, "providerPaymentChargeId"]
    shipping_option_id: Annotated[Optional[str], "shippingOptionId"]
    order_info: Annotated[Optional["OrderInfo"], "orderInfo"]


class ChatMemberUpdated(_Type):
    chat: Annotated["ChatP", "chat"]
    from_: Annotated["User", "from"]
    date: Annotated[datetime.datetime, "date"]
    old_chat_member: Annotated["ChatMember", "oldChatMember"]
    new_chat_member: Annotated["ChatMember", "newChatMember"]
    invite_link: Annotated[Optional["InviteLink"], "inviteLink"]
    via_shared_folder: Annotated[Optional[bool], "viaSharedFolder"]


class ReplyMarkupInlineKeyboard(_Type):
    inline_keyboard: Annotated[list[list["InlineKeyboardButton"]], "inlineKeyboard"]
    __discriminators__ = ["inlineKeyboard"]


class ReplyMarkupKeyboard(_Type):
    keyboard: Annotated[list[list["KeyboardButton"]], "keyboard"]
    is_persistent: Annotated[Optional[bool], "isPersistent"]
    resize_keyboard: Annotated[Optional[bool], "resizeKeyboard"]
    one_time_keyboard: Annotated[Optional[bool], "oneTimeKeyboard"]
    input_field_placeholder: Annotated[Optional[str], "inputFieldPlaceholder"]
    selective: Annotated[Optional[bool], "selective"]
    __discriminators__ = ["keyboard"]


class ReplyMarkupRemoveKeyboard(_Type):
    remove_keyboard: Annotated[Literal[True], "removeKeyboard"]
    selective: Annotated[Optional[bool], "selective"]
    __discriminators__ = ["removeKeyboard"]


class ReplyMarkupForceReply(_Type):
    force_reply: Annotated[Literal[True], "forceReply"]
    input_field_placeholder: Annotated[Optional[str], "inputFieldPlaceholder"]
    selective: Annotated[Optional[bool], "selective"]
    __discriminators__ = ["forceReply"]


ReplyMarkup: TypeAlias = Union[
    ReplyMarkupInlineKeyboard,
    ReplyMarkupKeyboard,
    ReplyMarkupRemoveKeyboard,
    ReplyMarkupForceReply,
]


class Story(_Type):
    out: Annotated[bool, "out"]
    id: Annotated[int, "id"]
    chat: Annotated["ChatP", "chat"]
    date: Annotated[datetime.datetime, "date"]
    edited: Annotated[bool, "edited"]
    content: Annotated["StoryContent", "content"]
    interactive_areas: Annotated[list["StoryInteractiveArea"], "interactiveAreas"]
    highlighted: Annotated[bool, "highlighted"]
    interactions: Annotated[Optional["StoryInteractions"], "interactions"]
    privacy: Annotated[Optional["StoryPrivacy"], "privacy"]
    caption: Annotated[Optional[str], "caption"]
    caption_entities: Annotated[Optional[list["MessageEntity"]], "captionEntities"]


InlineQueryResultType: TypeAlias = Union[
    Literal["article"],
    Literal["audio"],
    Literal["document"],
    Literal["gif"],
    Literal["mpeg4Gif"],
    Literal["photo"],
    Literal["sticker"],
    Literal["video"],
    Literal["voice"],
    Literal["game"],
    Literal["location"],
    Literal["venue"],
]


class _InlineQueryResultBase(_Type):
    type: Annotated["InlineQueryResultType", "type"]
    id: Annotated[str, "id"]


class _InlineQueryResultCaptionCommon(_Type):
    caption: Annotated[Optional[str], "caption"]
    parse_mode: Annotated[Optional["ParseMode"], "parseMode"]
    caption_entities: Annotated[Optional[list["MessageEntity"]], "captionEntities"]


class _InlineQueryResultMessageContentReplyMarkupCommon(_Type):
    message_content: Annotated[Optional["MessageContent"], "messageContent"]
    reply_markup: Annotated[Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"]


class _InlineQueryResultThumbnailCommon(_Type):
    thumbnail_url: Annotated[Optional[str], "thumbnailUrl"]
    thumbnail_width: Annotated[Optional[str], "thumbnailWidth"]
    thumbnail_height: Annotated[Optional[str], "thumbnailHeight"]


class InlineQueryResultArticle(
    _InlineQueryResultBase, _InlineQueryResultThumbnailCommon
):
    type: Annotated[Literal["article"], "type"]
    title: Annotated[str, "title"]
    message_content: Annotated["MessageContent", "messageContent"]
    description: Annotated[Optional[str], "description"]
    reply_markup: Annotated[Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"]
    url: Annotated[Optional[str], "url"]
    hide_url: Annotated[Optional[bool], "hideUrl"]
    __discriminators__ = ["type"]


class InlineQueryResultAudio(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["audio"], "type"]
    title: Annotated[str, "title"]
    url: Annotated[str, "url"]
    performer: Annotated[Optional[str], "performer"]
    audio_duration: Annotated[Optional[int], "audioDuration"]
    __discriminators__ = ["type"]


class InlineQueryResultCachedAudio(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["audio"], "type"]
    file_id: Annotated[str, "fileId"]
    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedDocument(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["document"], "type"]
    file_id: Annotated[str, "fileId"]
    description: Annotated[Optional[str], "description"]
    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedGif(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["gif"], "type"]
    file_id: Annotated[str, "fileId"]
    title: Annotated[Optional[str], "title"]
    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedMpeg4Gif(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["mpeg4Gif"], "type"]
    file_id: Annotated[str, "fileId"]
    title: Annotated[Optional[str], "title"]
    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedPhoto(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["photo"], "type"]
    file_id: Annotated[str, "fileId"]
    thumbnails: Annotated[Optional[list["Thumbnail"]], "thumbnails"]
    title: Annotated[Optional[str], "title"]
    description: Annotated[Optional[str], "description"]
    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedSticker(
    _InlineQueryResultBase, _InlineQueryResultMessageContentReplyMarkupCommon
):
    type: Annotated[Literal["sticker"], "type"]
    file_id: Annotated[str, "fileId"]
    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedVideo(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["video"], "type"]
    title: Annotated[str, "title"]
    file_id: Annotated[str, "fileId"]
    description: Annotated[Optional[str], "description"]
    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedVoice(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["voice"], "type"]
    title: Annotated[str, "title"]
    file_id: Annotated[str, "fileId"]
    __discriminators__ = ["type", "fileId"]


class InlineQueryResultContact(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
    _InlineQueryResultThumbnailCommon,
):
    type: Annotated[Literal["game"], "type"]
    phone_number: Annotated[str, "phoneNumber"]
    first_name: Annotated[str, "firstName"]
    last_name: Annotated[Optional[str], "lastName"]
    vcard: Annotated[Optional[str], "vcard"]
    __discriminators__ = ["type"]


class InlineQueryResultDocument(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
    _InlineQueryResultThumbnailCommon,
):
    type: Annotated[Literal["document"], "type"]
    title: Annotated[str, "title"]
    url: Annotated[str, "url"]
    __discriminators__ = ["type", "url"]


class InlineQueryResultGame(_InlineQueryResultBase):
    type: Annotated[Literal["game"], "type"]
    game_short_name: Annotated[str, "gameShortName"]
    reply_markup: Annotated[Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"]
    __discriminators__ = ["type"]


class InlineQueryResultGif(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["gif"], "type"]
    title: Annotated[Optional[str], "title"]
    url: Annotated[str, "url"]
    width: Annotated[Optional[int], "width"]
    height: Annotated[Optional[int], "height"]
    duration: Annotated[Optional[int], "duration"]
    thumbnail_url: Annotated[Optional[str], "thumbnailUrl"]
    thumbnail_mime_type: Annotated[Optional[str], "thumbnailMimeType"]
    __discriminators__ = ["type", "url"]


class InlineQueryResultLocation(
    _InlineQueryResultBase,
    _InlineQueryResultMessageContentReplyMarkupCommon,
    _InlineQueryResultThumbnailCommon,
):
    type: Annotated[Literal["location"], "type"]
    title: Annotated[str, "title"]
    latitude: Annotated[int, "latitude"]
    longitude: Annotated[int, "longitude"]
    horizontal_accuracy: Annotated[Optional[int], "horizontalAccuracy"]
    live_period: Annotated[Optional[int], "livePeriod"]
    heading: Annotated[Optional[int], "heading"]
    proximity_alert_radius: Annotated[Optional[int], "proximityAlertRadius"]
    __discriminators__ = ["type"]


class InlineQueryResultMpeg4Gif(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["mpeg4Gif"], "type"]
    url: Annotated[str, "url"]
    title: Annotated[Optional[str], "title"]
    width: Annotated[Optional[int], "width"]
    height: Annotated[Optional[int], "height"]
    duration: Annotated[Optional[int], "duration"]
    thumbnail_url: Annotated[Optional[str], "thumbnailUrl"]
    thumbnail_mime_type: Annotated[Optional[str], "thumbnailMimeType"]
    __discriminators__ = ["type", "url"]


class InlineQueryResultPhoto(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["photo"], "type"]
    url: Annotated[str, "url"]
    thumbnail_url: Annotated[str, "thumbnailUrl"]
    title: Annotated[Optional[str], "title"]
    description: Annotated[Optional[str], "description"]
    width: Annotated[Optional[int], "width"]
    height: Annotated[Optional[int], "height"]
    __discriminators__ = ["type", "url"]


class InlineQueryResultVenue(
    _InlineQueryResultBase,
    _InlineQueryResultMessageContentReplyMarkupCommon,
    _InlineQueryResultThumbnailCommon,
):
    type: Annotated[Literal["venue"], "type"]
    title: Annotated[str, "title"]
    latitude: Annotated[int, "latitude"]
    longitude: Annotated[int, "longitude"]
    address: Annotated[str, "address"]
    foursquare_id: Annotated[Optional[str], "foursquareId"]
    foursquare_type: Annotated[Optional[str], "foursquareType"]
    __discriminators__ = ["type"]


class InlineQueryResultVideo(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["video"], "type"]
    title: Annotated[str, "title"]
    description: Annotated[Optional[str], "description"]
    url: Annotated[str, "url"]
    mime_type: Annotated[str, "mimeType"]
    thumbnail_url: Annotated[str, "thumbnailUrl"]
    width: Annotated[Optional[int], "width"]
    height: Annotated[Optional[int], "height"]
    video_duration: Annotated[Optional[int], "videoDuration"]
    __discriminators__ = ["type", "url"]


class InlineQueryResultVoice(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["voice"], "type"]
    title: Annotated[str, "title"]
    url: Annotated[str, "url"]
    voice_duration: Annotated[Optional[int], "voiceDuration"]
    __discriminators__ = ["type", "url"]


InlineQueryResult: TypeAlias = Union[
    InlineQueryResultCachedAudio,
    InlineQueryResultCachedDocument,
    InlineQueryResultCachedGif,
    InlineQueryResultCachedMpeg4Gif,
    InlineQueryResultCachedPhoto,
    InlineQueryResultCachedSticker,
    InlineQueryResultCachedVideo,
    InlineQueryResultCachedVoice,
    InlineQueryResultArticle,
    InlineQueryResultAudio,
    InlineQueryResultContact,
    InlineQueryResultGame,
    InlineQueryResultDocument,
    InlineQueryResultGif,
    InlineQueryResultLocation,
    InlineQueryResultMpeg4Gif,
    InlineQueryResultPhoto,
    InlineQueryResultVenue,
    InlineQueryResultVideo,
    InlineQueryResultVoice,
]


class _MessageBase(_Type):
    out: Annotated[bool, "out"]
    id: Annotated[int, "id"]
    thread_id: Annotated[Optional[int], "threadId"]
    from_: Annotated[Optional["User"], "from"]
    sender_chat: Annotated[Optional["ChatP"], "senderChat"]
    date: Annotated[datetime.datetime, "date"]
    chat: Annotated["ChatP", "chat"]
    link: Annotated[Optional[str], "link"]
    forward_from: Annotated[Optional["User"], "forwardFrom"]
    forward_from_chat: Annotated[Optional["ChatP"], "forwardFromChat"]
    forward_id: Annotated[Optional[int], "forwardId"]
    forward_signature: Annotated[Optional[str], "forwardSignature"]
    forward_sender_name: Annotated[Optional[str], "forwardSenderName"]
    forward_date: Annotated[Optional[datetime.datetime], "forwardDate"]
    is_topic_message: Annotated[bool, "isTopicMessage"]
    is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"]
    reply_to_message: Annotated[Optional["Message"], "replyToMessage"]
    reply_to_message_id: Annotated[Optional[int], "replyToMessageId"]
    reactions: Annotated[Optional[list["MessageReaction"]], "reactions"]
    reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"]
    via_bot: Annotated[Optional["User"], "viaBot"]
    edit_date: Annotated[Optional[datetime.datetime], "editDate"]
    has_protected_content: Annotated[Optional[bool], "hasProtectedContent"]
    media_group_id: Annotated[Optional[str], "mediaGroupId"]
    author_signature: Annotated[Optional[str], "authorSignature"]
    views: Annotated[Optional[int], "views"]
    forwards: Annotated[Optional[int], "forwards"]
    reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"]
    business_connection_id: Annotated[Optional[str], "businessConnectionId"]
    sender_boost_count: Annotated[Optional[int], "senderBoostCount"]
    via_business_bot: Annotated[Optional["User"], "viaBusinessBot"]

    async def reply(
        self,
        text: str,
        *,
        parse_mode: Optional[ParseMode] = None,
        entities: Optional[list[MessageEntity]] = None,
        link_preview: Optional[LinkPreview] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageText":
        return await self._client.send_message(
            self.chat.id,
            text,
            parse_mode=parse_mode,
            entities=entities,
            link_preview=link_preview,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=self.id,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def delete(self, *, only_for_me: Optional[bool] = False) -> None:
        return await self._client.delete_message(
            self.chat.id, self.id, only_for_me=only_for_me
        )

    async def reply_voice(
        self,
        voice: FileSource,
        *,
        duration: Optional[Union[int, float]] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        parse_mode: Optional[ParseMode] = None,
        thumbnail: Optional[FileSource] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageVoice":
        return await self._client.send_voice(
            self.chat.id,
            voice,
            duration=duration,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            thumbnail=thumbnail,
            file_name=file_name,
            mime_type=mime_type,
            chunk_size=chunk_size,
            disable_notifaction=disable_notifaction,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_video_note(
        self,
        video_note: FileSource,
        *,
        duration: Optional[Union[int, float]] = None,
        length: Optional[Union[int, float]] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        parse_mode: Optional[ParseMode] = None,
        thumbnail: Optional[FileSource] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageVideoNote":
        return await self._client.send_video_note(
            self.chat.id,
            video_note,
            duration=duration,
            length=length,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            thumbnail=thumbnail,
            file_name=file_name,
            mime_type=mime_type,
            chunk_size=chunk_size,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_video(
        self,
        video: FileSource,
        *,
        duration: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        height: Optional[Union[int, float]] = None,
        supports_streaming: Optional[bool] = None,
        self_destruct: Optional[SelfDestructOption] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        parse_mode: Optional[ParseMode] = None,
        thumbnail: Optional[FileSource] = None,
        has_spoiler: Optional[bool] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageVideo":
        return await self._client.send_video(
            self.chat.id,
            video,
            duration=duration,
            width=width,
            height=height,
            supports_streaming=supports_streaming,
            self_destruct=self_destruct,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            thumbnail=thumbnail,
            has_spoiler=has_spoiler,
            file_name=file_name,
            mime_type=mime_type,
            chunk_size=chunk_size,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_venue(
        self,
        latitude: Union[int, float],
        longitude: Union[int, float],
        title: str,
        address: str,
        *,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageVenue":
        return await self._client.send_venue(
            self.chat.id,
            latitude,
            longitude,
            title,
            address,
            foursquare_id=foursquare_id,
            foursquare_type=foursquare_type,
            disable_notifaction=disable_notifaction,
            protect_content=protect_content,
            reply_to_message_id=self.id,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_sticker(
        self,
        sticker: FileSource,
        *,
        emoji: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageSticker":
        return await self._client.send_sticker(
            self.chat.id,
            sticker,
            emoji=emoji,
            file_name=file_name,
            mime_type=mime_type,
            chunk_size=chunk_size,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_poll(
        self,
        question: str,
        options: List[str],
        *,
        is_anonymous: Optional[bool] = None,
        type: Optional[Literal["quiz", "regular"]] = None,
        allow_multiple_answers: Optional[bool] = None,
        correct_option_index: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[ParseMode] = None,
        explanation_entities: Optional[List[MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[datetime.datetime] = None,
        is_closed: Optional[bool] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessagePoll":
        return await self._client.send_poll(
            self.chat.id,
            question,
            options,
            is_anonymous=is_anonymous,
            type=type,
            allow_multiple_answers=allow_multiple_answers,
            correct_option_index=correct_option_index,
            explanation=explanation,
            explanation_parse_mode=explanation_parse_mode,
            explanation_entities=explanation_entities,
            open_period=open_period,
            close_date=close_date,
            is_closed=is_closed,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_photo(
        self,
        photo: FileSource,
        *,
        self_destruct: Optional[SelfDestructOption] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        parse_mode: Optional[ParseMode] = None,
        has_spoiler: Optional[bool] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessagePhoto":
        return await self._client.send_photo(
            self.chat.id,
            photo,
            self_destruct=self_destruct,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            has_spoiler=has_spoiler,
            file_name=file_name,
            mime_type=mime_type,
            chunk_size=chunk_size,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_location(
        self,
        latitude: Union[int, float],
        longitude: Union[int, float],
        *,
        horizontal_accuracy: Optional[Union[int, float]] = None,
        live_period: Optional[Union[int, float]] = None,
        heading: Optional[Union[int, float]] = None,
        proximity_alert_radius: Optional[Union[int, float]] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageLocation":
        return await self._client.send_location(
            self.chat.id,
            latitude,
            longitude,
            horizontal_accuracy=horizontal_accuracy,
            live_period=live_period,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_document(
        self,
        document: FileSource,
        *,
        caption: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        parse_mode: Optional[ParseMode] = None,
        thumbnail: Optional[FileSource] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageDocument":
        return await self._client.send_document(
            self.chat.id,
            document,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            thumbnail=thumbnail,
            file_name=file_name,
            mime_type=mime_type,
            chunk_size=chunk_size,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_dice(
        self,
        emoji: Literal["🎲", "🎯", "🏀", "⚽", "🎳", "🎰"],
        *,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageDice":
        return await self._client.send_dice(
            self.chat.id,
            emoji,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_contact(
        self,
        first_name: str,
        number: str,
        *,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageContact":
        return await self._client.send_contact(
            self.chat.id,
            first_name,
            number,
            last_name=last_name,
            vcard=vcard,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_chat_action(
        self,
        action: ChatAction,
        message_thread_id: Optional[int] = None,
    ) -> None:
        return await self._client.send_chat_action(
            self.chat.id, action, message_thread_id=message_thread_id
        )

    async def reply_audio(
        self,
        audio: FileSource,
        *,
        duration: Optional[Union[int, float]] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        parse_mode: Optional[ParseMode] = None,
        thumbnail: Optional[FileSource] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageAudio":
        return await self._client.send_audio(
            self.chat.id,
            audio,
            duration=duration,
            performer=performer,
            title=title,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            thumbnail=thumbnail,
            file_name=file_name,
            mime_type=mime_type,
            chunk_size=chunk_size,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def reply_animation(
        self,
        animation: FileSource,
        *,
        duration: Optional[Union[int, float]] = None,
        width: Optional[Union[int, float]] = None,
        height: Optional[Union[int, float]] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        parse_mode: Optional[ParseMode] = None,
        thumbnail: Optional[FileSource] = None,
        has_spoiler: Optional[bool] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageAnimation":
        return await self._client.send_animation(
            self.id,
            animation,
            duration=duration,
            width=width,
            height=height,
            caption=caption,
            caption_entities=caption_entities,
            parse_mode=parse_mode,
            thumbnail=thumbnail,
            has_spoiler=has_spoiler,
            file_name=file_name,
            mime_type=mime_type,
            chunk_size=chunk_size,
            disable_notifaction=disable_notifaction,
            reply_to_message_id=self.id,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            reply_markup=reply_markup,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def pin(
        self,
        *,
        both_sides: Optional[bool] = None,
        disable_notifaction: Optional[bool] = None,
    ) -> None:
        return await self._client.pin_message(
            self.chat.id,
            self.id,
            both_sides=both_sides,
            disable_notifaction=disable_notifaction,
        )

    async def unpin(
        self,
    ) -> None:
        return await self._client.unpin_message(self.chat.id, self.id)

    async def stop_poll(
        self,
        *,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> Poll:
        return await self._client.stop_poll(
            self.chat.id, self.id, reply_markup=reply_markup
        )

    async def forward(
        self,
        to_chat: ID,
        *,
        drop_sender_name: Optional[bool] = None,
        drop_caption: Optional[bool] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
    ) -> "Message":
        return await self._client.forward_message(
            self.chat.id,
            to_chat,
            self.id,
            drop_sender_name=drop_sender_name,
            drop_caption=drop_caption,
            disable_notifaction=disable_notifaction,
            protect_content=protect_content,
            reply_quote=reply_quote,
            message_thread_id=message_thread_id,
            send_as=send_as,
            business_connection_id=getattr(self, "business_connection_id", None),
        )

    async def edit_text(
        self,
        text: str,
        *,
        parse_mode: Optional[ParseMode] = None,
        entities: Optional[List[MessageEntity]] = None,
        link_preview: Optional[LinkPreview] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageText":
        return await self._client.edit_message_text(
            self.chat.id,
            self.id,
            text,
            parse_mode=parse_mode,
            entities=entities,
            link_preview=link_preview,
            reply_markup=reply_markup,
        )

    edit = edit_text

    async def edit_reply_markup(
        self,
        *,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "Message":
        return await self._client.edit_message_reply_markup(
            self.chat.id, self.id, reply_markup=reply_markup
        )

    async def edit_media(
        self,
        media: InputMedia,
        *,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "Message":
        return await self._client.edit_message_media(
            self.chat.id, self.id, media, reply_markup=reply_markup
        )

    async def edit_live_location(
        self,
        latitude: Union[int, float],
        longitude: Union[int, float],
        *,
        horizontal_accuracy: Optional[Union[int, float]] = None,
        heading: Optional[Union[int, float]] = None,
        proximity_alert_radius: Optional[Union[int, float]] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> "MessageLocation":
        return await self._client.edit_message_live_location(
            self.chat.id,
            self.id,
            latitude,
            longitude,
            horizontal_accuracy=horizontal_accuracy,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            reply_markup=reply_markup,
        )

    async def react(
        self,
        reactions: Union[Reaction, List[Reaction]],
        *,
        big: Optional[bool] = None,
        add_to_recents: Optional[bool] = None,
    ) -> None:
        if isinstance(reactions, list):
            return await self._client.set_reactions(
                self.chat.id, self.id, reactions, big=big
            )

        return await self._client.add_reaction(
            self.chat.id, self.id, reactions, big=big, add_to_recents=add_to_recents
        )

    async def unreact(
        self,
        reaction: Reaction,
    ) -> None:
        return await self._client.remove_reaction(self.chat.id, self.id, reaction)


class _MessageMediaBase(_MessageBase):
    caption: Annotated[Optional[str], "caption"]
    caption_entities: Annotated[Optional[list["MessageEntity"]], "captionEntities"]
    has_media_spoiler: Annotated[Optional[bool], "hasMediaSpoiler"]


class MessageText(_MessageBase):
    text: Annotated[str, "text"]
    entities: Annotated[list["MessageEntity"], "entities"]
    link_preview: Annotated[Optional["LinkPreview"], "linkPreview"]
    __discriminators__ = ["text", "entities"]


class MessageLink(_MessageBase):
    link_preview: Annotated[Any, "linkPreview"]
    __discriminators__ = ["linkPreview"]


class MessagePhoto(_MessageMediaBase):
    photo: Annotated["Photo", "photo"]
    __discriminators__ = ["photo"]


class MessageDocument(_MessageMediaBase):
    document: Annotated["Document", "document"]
    __discriminators__ = ["document"]


class MessageVideo(_MessageMediaBase):
    video: Annotated["Video", "video"]
    __discriminators__ = ["video"]


class MessageSticker(_MessageBase):
    sticker: Annotated["Sticker", "sticker"]
    __discriminators__ = ["sticker"]


class MessageAnimation(_MessageMediaBase):
    animation: Annotated["Animation", "animation"]
    __discriminators__ = ["animation"]


class MessageVoice(_MessageMediaBase):
    voice: Annotated["Voice", "voice"]
    __discriminators__ = ["voice"]


class MessageAudio(_MessageMediaBase):
    audio: Annotated["Audio", "audio"]
    __discriminators__ = ["audio"]


class MessageDice(_MessageBase):
    dice: Annotated["Dice", "dice"]
    __discriminators__ = ["dice"]


class MessageVideoNote(_MessageBase):
    video_note: Annotated["VideoNote", "videoNote"]
    __discriminators__ = ["videoNote"]


class MessageContact(_MessageBase):
    contact: Annotated["Contact", "contact"]
    __discriminators__ = ["contact"]


class MessageGame(_MessageBase):
    game: Annotated["Game", "game"]
    __discriminators__ = ["game"]


class MessagePoll(_MessageBase):
    poll: Annotated["Poll", "poll"]
    __discriminators__ = ["poll"]


class MessageInvoice(_MessageBase):
    invoice: Annotated["Invoice", "invoice"]
    __discriminators__ = ["invoice"]


class MessageVenue(_MessageBase):
    venue: Annotated["Venue", "venue"]
    __discriminators__ = ["venue"]


class MessageLocation(_MessageBase):
    location: Annotated["Location", "location"]
    __discriminators__ = ["location"]


class MessageNewChatMembers(_MessageBase):
    new_chat_members: Annotated[list["User"], "newChatMembers"]
    __discriminators__ = ["newChatMembers"]


class MessageLeftChatMember(_MessageBase):
    left_chat_member: Annotated["User", "leftChatMember"]
    __discriminators__ = ["leftChatMember"]


class MessageNewChatTitle(_MessageBase):
    new_chat_title: Annotated[str, "newChatTitle"]
    __discriminators__ = ["newChatTitle"]


class MessageNewChatPhoto(_MessageBase):
    new_chat_photo: Annotated["Photo", "newChatPhoto"]
    __discriminators__ = ["newChatPhoto"]


class MessageDeletedChatPhoto(_MessageBase):
    deleted_chat_photo: Annotated[Literal[True], "deletedChatPhoto"]
    __discriminators__ = ["deletedChatPhoto"]


class MessageGroupCreated(_MessageBase):
    group_created: Annotated[Literal[True], "groupCreated"]
    new_chat_members: Annotated[list["User"], "newChatMembers"]
    __discriminators__ = ["groupCreated", "newChatMembers"]


class MessageSupergroupCreated(_MessageBase):
    supergroup_created: Annotated[Literal[True], "supergroupCreated"]
    __discriminators__ = ["supergroupCreated"]


class MessageChannelCreated(_MessageBase):
    channel_created: Annotated[Literal[True], "channelCreated"]
    __discriminators__ = ["channelCreated"]


class MessageAutoDeleteTimerChanged(_MessageBase):
    new_auto_delete_time: Annotated[int, "newAutoDeleteTime"]
    __discriminators__ = ["newAutoDeleteTime"]


class MessageChatMigratedTo(_MessageBase):
    chat_migrated_to: Annotated[int, "chatMigratedTo"]
    __discriminators__ = ["chatMigratedTo"]


class MessageChatMigratedFrom(_MessageBase):
    chat_migrated_from: Annotated[int, "chatMigratedFrom"]
    __discriminators__ = ["chatMigratedFrom"]


class MessagePinnedMessage(_MessageBase):
    pinned_message: Annotated["Message", "pinnedMessage"]
    __discriminators__ = ["pinnedMessage"]


class MessageUserShared(_MessageBase):
    user_shared: Annotated[Any, "userShared"]
    __discriminators__ = ["userShared"]


class MessageWriteAccessAllowed(_MessageBase):
    write_access_allowed: Annotated[Any, "writeAccessAllowed"]
    __discriminators__ = ["writeAccessAllowed"]


class MessageForumTopicCreated(_MessageBase):
    forum_topic_created: Annotated[Any, "forumTopicCreated"]
    __discriminators__ = ["forumTopicCreated"]


class MessageForumTopicEdited(_MessageBase):
    forum_topic_edited: Annotated[Any, "forumTopicEdited"]
    __discriminators__ = ["forumTopicEdited"]


class MessageForumTopicClosed(_MessageBase):
    forum_topic_closed: Annotated[Literal[True], "forumTopicClosed"]
    __discriminators__ = ["forumTopicClosed"]


class MessageForumTopicReopened(_MessageBase):
    forum_topic_reopened: Annotated[Literal[True], "forumTopicReopened"]
    __discriminators__ = ["forumTopicReopened"]


class MessageVideoChatScheduled(_MessageBase):
    video_chat_scheduled: Annotated[Any, "videoChatScheduled"]
    __discriminators__ = ["videoChatScheduled"]


class MessageVideoChatStarted(_MessageBase):
    video_chat_started: Annotated[Literal[True], "videoChatStarted"]
    __discriminators__ = ["videoChatStarted"]


class MessageVideoChatEnded(_MessageBase):
    video_chat_ended: Annotated[Any, "videoChatEnded"]
    __discriminators__ = ["videoChatEnded"]


class MessageGiveaway(_MessageBase):
    giveaway: Annotated["Giveaway", "giveaway"]
    __discriminators__ = ["giveaway"]


class MessageUnsupported(_MessageBase):
    unsupported: Annotated[Literal[True], "unsupported"]
    __discriminators__ = ["unsupported"]


class MessageSuccessfulPayment(_MessageBase):
    successful_payment: Annotated["SuccessfulPayment", "successfulPayment"]
    __discriminators__ = ["successfulPayment"]


Message: TypeAlias = Union[
    MessageText,
    MessageLink,
    MessagePhoto,
    MessageDocument,
    MessageVideo,
    MessageSticker,
    MessageAnimation,
    MessageVoice,
    MessageAudio,
    MessageDice,
    MessageVideoNote,
    MessageContact,
    MessageGame,
    MessagePoll,
    MessageInvoice,
    MessageVenue,
    MessageLocation,
    MessageNewChatMembers,
    MessageLeftChatMember,
    MessageNewChatTitle,
    MessageNewChatPhoto,
    MessageDeletedChatPhoto,
    MessageGroupCreated,
    MessageSupergroupCreated,
    MessageChannelCreated,
    MessageAutoDeleteTimerChanged,
    MessageChatMigratedTo,
    MessageChatMigratedFrom,
    MessagePinnedMessage,
    MessageUserShared,
    MessageWriteAccessAllowed,
    MessageForumTopicCreated,
    MessageForumTopicEdited,
    MessageForumTopicClosed,
    MessageForumTopicReopened,
    MessageVideoChatScheduled,
    MessageVideoChatStarted,
    MessageVideoChatEnded,
    MessageGiveaway,
    MessageUnsupported,
    MessageSuccessfulPayment,
]


class CallbackQuery(_Type):
    id: Annotated[str, "id"]
    from_: Annotated["User", "from"]
    message: Annotated[Optional["Message"], "message"]
    inline_message_id: Annotated[Optional[str], "inlineMessageId"]
    chat_instance: Annotated[str, "chatInstance"]
    data: Annotated[Optional[str], "data"]
    game_short_name: Annotated[Optional[str], "gameShortName"]

    async def answer(
        self,
        *,
        text: Optional[str] = None,
        alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
    ) -> None:
        await self._client.answer_callback_query(
            self.id, text=text, alert=alert, url=url, cache_time=cache_time
        )

    async def edit_message_text(
        self,
        text: str,
        *,
        parse_mode: Optional[ParseMode] = None,
        entities: Optional[List[MessageEntity]] = None,
        link_preview: Optional[LinkPreview] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> None:
        if self.inline_message_id:
            await self._client.edit_inline_message_text(
                self.inline_message_id,
                text,
                parse_mode=parse_mode,
                entities=entities,
                link_preview=link_preview,
                reply_markup=reply_markup,
            )

    async def edit_message_reply_markup(
        self, *, reply_markup: Optional[ReplyMarkup] = None
    ) -> None:
        if self.inline_message_id:
            await self._client.edit_inline_message_reply_markup(
                self.inline_message_id, reply_markup=reply_markup
            )

    async def edit_message_media(
        self, media: InputMedia, *, reply_markup: Optional[ReplyMarkup] = None
    ) -> None:
        if self.inline_message_id:
            await self._client.edit_inline_message_media(
                self.inline_message_id, media, reply_markup=reply_markup
            )

    async def edit_message_live_location(
        self,
        latitude: Union[int, float],
        longitude: Union[int, float],
        *,
        horizontal_accuracy: Optional[Union[int, float]] = None,
        heading: Optional[Union[int, float]] = None,
        proximity_alert_radius: Optional[Union[int, float]] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> None:
        if self.inline_message_id:
            await self._client.edit_inline_message_live_location(
                self.inline_message_id,
                latitude,
                longitude,
                horizontal_accuracy=horizontal_accuracy,
                heading=heading,
                proximity_alert_radius=proximity_alert_radius,
                reply_markup=reply_markup,
            )


class ChatListItem(_Type):
    chat: Annotated["ChatP", "chat"]
    order: Annotated[str, "order"]
    pinned: Annotated[int, "pinned"]
    last_message: Annotated[Optional["Message"], "lastMessage"]


class InlineQueryAnswer(_Type):
    id: Annotated[str, "id"]
    results: Annotated[list["InlineQueryResult"], "results"]
    next_offset: Annotated[Optional[str], "nextOffset"]


class UpdateNewMessage(_Type):
    message: Annotated["Message", "message"]
    __discriminators__ = ["message"]


class UpdateEditedMessage(_Type):
    edited_message: Annotated["Message", "editedMessage"]
    __discriminators__ = ["editedMessage"]


class UpdateDeletedMessages(_Type):
    deleted_messages: Annotated[list["MessageReference"], "deletedMessages"]
    business_connection_id: Annotated[Optional[str], "businessConnectionId"]
    __discriminators__ = ["deletedMessages"]


class UpdateCallbackQuery(_Type):
    callback_query: Annotated["CallbackQuery", "callbackQuery"]
    __discriminators__ = ["callbackQuery"]


class UpdateInlineQuery(_Type):
    inline_query: Annotated["InlineQuery", "inlineQuery"]
    __discriminators__ = ["inlineQuery"]


class UpdateChosenInlineResult(_Type):
    chosen_inline_result: Annotated["ChosenInlineResult", "chosenInlineResult"]
    __discriminators__ = ["chosenInlineResult"]


class UpdateNewChat(_Type):
    new_chat: Annotated["ChatListItem", "newChat"]
    __discriminators__ = ["newChat"]


class UpdateEditedChat(_Type):
    edited_chat: Annotated["ChatListItem", "editedChat"]
    __discriminators__ = ["editedChat"]


class UpdateDeletedChat(_Type):
    deleted_chat: Annotated[Any, "deletedChat"]
    __discriminators__ = ["deletedChat"]


class UpdateMessageInteractions(_Type):
    message_interactions: Annotated["MessageInteractions", "messageInteractions"]
    __discriminators__ = ["messageInteractions"]


class UpdateMessageReactionCount(_Type):
    message_reaction_count: Annotated["MessageReactionCount", "messageReactionCount"]
    __discriminators__ = ["messageReactionCount"]


class UpdateMessageReactions(_Type):
    message_reactions: Annotated["MessageReactions", "messageReactions"]
    __discriminators__ = ["messageReactions"]


class UpdateChatMember(_Type):
    chat_member: Annotated["ChatMemberUpdated", "chatMember"]
    __discriminators__ = ["chatMember"]


class UpdateMyChatMember(_Type):
    my_chat_member: Annotated["ChatMemberUpdated", "myChatMember"]
    __discriminators__ = ["myChatMember"]


class UpdateDeletedStory(_Type):
    deleted_story: Annotated["StoryReference", "deletedStory"]
    __discriminators__ = ["deletedStory"]


class UpdateNewStory(_Type):
    story: Annotated["Story", "story"]
    __discriminators__ = ["story"]


class UpdateBusinessConnection(_Type):
    business_connection: Annotated["BusinessConnection", "businessConnection"]
    __discriminators__ = ["businessConnection"]


class UpdateVideoChat(_Type):
    video_chat: Annotated["VideoChat", "videoChat"]
    __discriminators__ = ["videoChat"]


class UpdatePreCheckoutQuery(_Type):
    pre_checkout_query: Annotated["PreCheckoutQuery", "preCheckoutQuery"]
    __discriminators__ = ["preCheckoutQuery"]


Update: TypeAlias = Union[
    UpdateNewMessage,
    UpdateEditedMessage,
    UpdateDeletedMessages,
    UpdateCallbackQuery,
    UpdateInlineQuery,
    UpdateChosenInlineResult,
    UpdateNewChat,
    UpdateEditedChat,
    UpdateDeletedChat,
    UpdateMessageInteractions,
    UpdateMessageReactionCount,
    UpdateMessageReactions,
    UpdateChatMember,
    UpdateMyChatMember,
    UpdateDeletedStory,
    UpdateNewStory,
    UpdateBusinessConnection,
    UpdateVideoChat,
    UpdatePreCheckoutQuery,
]
