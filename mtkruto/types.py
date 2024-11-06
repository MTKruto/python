import datetime
from typing import Annotated, Any, List, Literal, Optional, Union

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

    def __init__(
        self,
        day: Annotated[int, "day"],
        month: Annotated[int, "month"],
        *,
        year: Annotated[Optional[int], "year"] = None,
    ):
        self.day = day
        self.month = month
        self.year = year


class BotCommand(_Type):
    command: Annotated[str, "command"]
    description: Annotated[str, "description"]

    def __init__(
        self,
        command: Annotated[str, "command"],
        description: Annotated[str, "description"],
    ):
        self.command = command
        self.description = description


class CallbackQueryAnswer(_Type):
    alert: Annotated[bool, "alert"]
    text: Annotated[str, "text"]
    url: Annotated[str, "url"]

    def __init__(
        self,
        alert: Annotated[bool, "alert"],
        text: Annotated[str, "text"],
        url: Annotated[str, "url"],
    ):
        self.alert = alert
        self.text = text
        self.url = url


class CallbackQueryQuestionGame(_Type):
    type: Annotated[Literal["game"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["game"], "type"],
    ):
        self.type = type

    __discriminators__ = ["type"]


class CallbackQueryQuestionPassword(_Type):
    type: Annotated[Literal["password"], "type"]
    data: Annotated[str, "data"]
    password: Annotated[str, "password"]

    def __init__(
        self,
        type: Annotated[Literal["password"], "type"],
        data: Annotated[str, "data"],
        password: Annotated[str, "password"],
    ):
        self.type = type
        self.data = data
        self.password = password

    __discriminators__ = ["type"]


class CallbackQueryQuestionButton(_Type):
    type: Annotated[Literal["button"], "type"]
    data: Annotated[str, "data"]

    def __init__(
        self,
        type: Annotated[Literal["button"], "type"],
        data: Annotated[str, "data"],
    ):
        self.type = type
        self.data = data

    __discriminators__ = ["type"]


CallbackQueryQuestion = Union[
    CallbackQueryQuestionGame,
    CallbackQueryQuestionPassword,
    CallbackQueryQuestionButton,
]

ChatAction = Union[
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

    def __init__(
        self,
        is_anonymous: Annotated[bool, "isAnonymous"],
        can_manage_chat: Annotated[bool, "canManageChat"],
        can_delete_messages: Annotated[bool, "canDeleteMessages"],
        can_manage_video_chats: Annotated[bool, "canManageVideoChats"],
        can_restrict_members: Annotated[bool, "canRestrictMembers"],
        can_promote_members: Annotated[bool, "canPromoteMembers"],
        can_change_info: Annotated[bool, "canChangeInfo"],
        can_invite_users: Annotated[bool, "canInviteUsers"],
        *,
        can_post_messages: Annotated[Optional[bool], "canPostMessages"] = None,
        can_edit_messages: Annotated[Optional[bool], "canEditMessages"] = None,
        can_pin_messages: Annotated[Optional[bool], "canPinMessages"] = None,
        can_manage_topics: Annotated[Optional[bool], "canManageTopics"] = None,
    ):
        self.is_anonymous = is_anonymous
        self.can_manage_chat = can_manage_chat
        self.can_delete_messages = can_delete_messages
        self.can_manage_video_chats = can_manage_video_chats
        self.can_restrict_members = can_restrict_members
        self.can_promote_members = can_promote_members
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_post_messages = can_post_messages
        self.can_edit_messages = can_edit_messages
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics


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

    def __init__(
        self,
        *,
        can_send_messages: Annotated[Optional[bool], "canSendMessages"] = None,
        can_send_audio: Annotated[Optional[bool], "canSendAudio"] = None,
        can_send_documents: Annotated[Optional[bool], "canSendDocuments"] = None,
        can_send_photos: Annotated[Optional[bool], "canSendPhotos"] = None,
        can_send_videos: Annotated[Optional[bool], "canSendVideos"] = None,
        can_send_video_notes: Annotated[Optional[bool], "canSendVideoNotes"] = None,
        can_send_voice: Annotated[Optional[bool], "canSendVoice"] = None,
        can_send_polls: Annotated[Optional[bool], "canSendPolls"] = None,
        can_send_stickers: Annotated[Optional[bool], "canSendStickers"] = None,
        can_send_animations: Annotated[Optional[bool], "canSendAnimations"] = None,
        can_send_games: Annotated[Optional[bool], "canSendGames"] = None,
        can_send_inline_bot_results: Annotated[
            Optional[bool], "canSendInlineBotResults"
        ] = None,
        can_add_web_page_previews: Annotated[
            Optional[bool], "canAddWebPagePreviews"
        ] = None,
        can_change_info: Annotated[Optional[bool], "canChangeInfo"] = None,
        can_invite_users: Annotated[Optional[bool], "canInviteUsers"] = None,
        can_pin_messages: Annotated[Optional[bool], "canPinMessages"] = None,
        can_manage_topics: Annotated[Optional[bool], "canManageTopics"] = None,
    ):
        self.can_send_messages = can_send_messages
        self.can_send_audio = can_send_audio
        self.can_send_documents = can_send_documents
        self.can_send_photos = can_send_photos
        self.can_send_videos = can_send_videos
        self.can_send_video_notes = can_send_video_notes
        self.can_send_voice = can_send_voice
        self.can_send_polls = can_send_polls
        self.can_send_stickers = can_send_stickers
        self.can_send_animations = can_send_animations
        self.can_send_games = can_send_games
        self.can_send_inline_bot_results = can_send_inline_bot_results
        self.can_add_web_page_previews = can_add_web_page_previews
        self.can_change_info = can_change_info
        self.can_invite_users = can_invite_users
        self.can_pin_messages = can_pin_messages
        self.can_manage_topics = can_manage_topics


class ChatPhoto(_Type):
    small_file_id: Annotated[str, "smallFileId"]
    small_file_unique_id: Annotated[str, "smallFileUniqueId"]
    big_file_id: Annotated[str, "bigFileId"]
    big_file_unique_id: Annotated[str, "bigFileUniqueId"]
    has_video: Annotated[bool, "hasVideo"]
    personal: Annotated[bool, "personal"]

    def __init__(
        self,
        small_file_id: Annotated[str, "smallFileId"],
        small_file_unique_id: Annotated[str, "smallFileUniqueId"],
        big_file_id: Annotated[str, "bigFileId"],
        big_file_unique_id: Annotated[str, "bigFileUniqueId"],
        has_video: Annotated[bool, "hasVideo"],
        personal: Annotated[bool, "personal"],
    ):
        self.small_file_id = small_file_id
        self.small_file_unique_id = small_file_unique_id
        self.big_file_id = big_file_id
        self.big_file_unique_id = big_file_unique_id
        self.has_video = has_video
        self.personal = personal


ConnectionStateNotConnected = Literal["notConnected"]

ConnectionStateUpdating = Literal["updating"]

ConnectionStateReady = Literal["ready"]


class Contact(_Type):
    phone_number: Annotated[str, "phoneNumber"]
    first_name: Annotated[str, "firstName"]
    last_name: Annotated[Optional[str], "lastName"]
    user_id: Annotated[Optional[int], "userId"]
    vcard: Annotated[Optional[str], "vcard"]

    def __init__(
        self,
        phone_number: Annotated[str, "phoneNumber"],
        first_name: Annotated[str, "firstName"],
        *,
        last_name: Annotated[Optional[str], "lastName"] = None,
        user_id: Annotated[Optional[int], "userId"] = None,
        vcard: Annotated[Optional[str], "vcard"] = None,
    ):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.vcard = vcard


class Dice(_Type):
    emoji: Annotated[str, "emoji"]
    value: Annotated[int, "value"]

    def __init__(
        self,
        emoji: Annotated[str, "emoji"],
        value: Annotated[int, "value"],
    ):
        self.emoji = emoji
        self.value = value


class FailedInvitation(_Type):
    user_id: Annotated[int, "userId"]
    premium_required_to_invite: Annotated[bool, "premiumRequiredToInvite"]
    premium_required_to_send_message: Annotated[bool, "premiumRequiredToSendMessage"]

    def __init__(
        self,
        user_id: Annotated[int, "userId"],
        premium_required_to_invite: Annotated[bool, "premiumRequiredToInvite"],
        premium_required_to_send_message: Annotated[
            bool, "premiumRequiredToSendMessage"
        ],
    ):
        self.user_id = user_id
        self.premium_required_to_invite = premium_required_to_invite
        self.premium_required_to_send_message = premium_required_to_send_message


class GiveawayParameters(_Type):
    boosted_chat_id: Annotated[int, "boostedChatId"]
    additional_chat_ids: Annotated[list[int], "additionalChatIds"]
    winner_selection_date: Annotated[datetime.datetime, "winnerSelectionDate"]
    only_new_members: Annotated[bool, "onlyNewMembers"]
    countries: Annotated[list[str], "countries"]

    def __init__(
        self,
        boosted_chat_id: Annotated[int, "boostedChatId"],
        additional_chat_ids: Annotated[list[int], "additionalChatIds"],
        winner_selection_date: Annotated[datetime.datetime, "winnerSelectionDate"],
        only_new_members: Annotated[bool, "onlyNewMembers"],
        countries: Annotated[list[str], "countries"],
    ):
        self.boosted_chat_id = boosted_chat_id
        self.additional_chat_ids = additional_chat_ids
        self.winner_selection_date = winner_selection_date
        self.only_new_members = only_new_members
        self.countries = countries


ID = Union[int, str, Literal["me"]]


class Invoice(_Type):
    title: Annotated[str, "title"]
    description: Annotated[str, "description"]
    start_parameter: Annotated[str, "startParameter"]
    currency: Annotated[str, "currency"]
    total_amount: Annotated[int, "totalAmount"]

    def __init__(
        self,
        title: Annotated[str, "title"],
        description: Annotated[str, "description"],
        start_parameter: Annotated[str, "startParameter"],
        currency: Annotated[str, "currency"],
        total_amount: Annotated[int, "totalAmount"],
    ):
        self.title = title
        self.description = description
        self.start_parameter = start_parameter
        self.currency = currency
        self.total_amount = total_amount


class KeyboardButtonPollType(_Type):
    type: Annotated[Optional[Any], "type"]

    def __init__(
        self,
        *,
        type: Annotated[Optional[Any], "type"] = None,
    ):
        self.type = type


class LinkPreview(_Type):
    disable: Annotated[Optional[bool], "disable"]
    url: Annotated[Optional[str], "url"]
    small_media: Annotated[Optional[bool], "smallMedia"]
    large_media: Annotated[Optional[bool], "largeMedia"]
    above_text: Annotated[Optional[bool], "aboveText"]

    def __init__(
        self,
        *,
        disable: Annotated[Optional[bool], "disable"] = None,
        url: Annotated[Optional[str], "url"] = None,
        small_media: Annotated[Optional[bool], "smallMedia"] = None,
        large_media: Annotated[Optional[bool], "largeMedia"] = None,
        above_text: Annotated[Optional[bool], "aboveText"] = None,
    ):
        self.disable = disable
        self.url = url
        self.small_media = small_media
        self.large_media = large_media
        self.above_text = above_text


class LiveStreamChannel(_Type):
    id: Annotated[int, "id"]
    scale: Annotated[int, "scale"]
    timestamp: Annotated[int, "timestamp"]

    def __init__(
        self,
        id: Annotated[int, "id"],
        scale: Annotated[int, "scale"],
        timestamp: Annotated[int, "timestamp"],
    ):
        self.id = id
        self.scale = scale
        self.timestamp = timestamp


class Location(_Type):
    latitude: Annotated[int, "latitude"]
    longitude: Annotated[int, "longitude"]
    horizontal_accuracy: Annotated[Optional[int], "horizontalAccuracy"]
    live_period: Annotated[Optional[int], "livePeriod"]
    heading: Annotated[Optional[int], "heading"]
    proximity_alert_radius: Annotated[Optional[int], "proximityAlertRadius"]

    def __init__(
        self,
        latitude: Annotated[int, "latitude"],
        longitude: Annotated[int, "longitude"],
        *,
        horizontal_accuracy: Annotated[Optional[int], "horizontalAccuracy"] = None,
        live_period: Annotated[Optional[int], "livePeriod"] = None,
        heading: Annotated[Optional[int], "heading"] = None,
        proximity_alert_radius: Annotated[Optional[int], "proximityAlertRadius"] = None,
    ):
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius


class LoginUrl(_Type):
    url: Annotated[str, "url"]
    forward_text: Annotated[Optional[str], "forwardText"]
    bot_username: Annotated[Optional[str], "botUsername"]
    request_write_access: Annotated[Optional[bool], "requestWriteAccess"]

    def __init__(
        self,
        url: Annotated[str, "url"],
        *,
        forward_text: Annotated[Optional[str], "forwardText"] = None,
        bot_username: Annotated[Optional[str], "botUsername"] = None,
        request_write_access: Annotated[Optional[bool], "requestWriteAccess"] = None,
    ):
        self.url = url
        self.forward_text = forward_text
        self.bot_username = bot_username
        self.request_write_access = request_write_access


class MaskPosition(_Type):
    point: Annotated[Any, "point"]
    x_shift: Annotated[int, "xShift"]
    y_shift: Annotated[int, "yShift"]
    scale: Annotated[int, "scale"]

    def __init__(
        self,
        point: Annotated[Any, "point"],
        x_shift: Annotated[int, "xShift"],
        y_shift: Annotated[int, "yShift"],
        scale: Annotated[int, "scale"],
    ):
        self.point = point
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.scale = scale


MessageEntityType = Union[
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

    def __init__(
        self,
        type: Annotated["MessageEntityType", "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length


class MessageEntityMention(_MessageEntityBase):
    type: Annotated[Literal["mention"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["mention"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityHashtag(_MessageEntityBase):
    type: Annotated[Literal["hashtag"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["hashtag"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityBotCommand(_MessageEntityBase):
    type: Annotated[Literal["botCommand"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["botCommand"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityURL(_MessageEntityBase):
    type: Annotated[Literal["url"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["url"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityEmailAddress(_MessageEntityBase):
    type: Annotated[Literal["email"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["email"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityBold(_MessageEntityBase):
    type: Annotated[Literal["bold"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["bold"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityItalic(_MessageEntityBase):
    type: Annotated[Literal["italic"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["italic"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityPre(_MessageEntityBase):
    type: Annotated[Literal["pre"], "type"]
    language: Annotated[str, "language"]

    def __init__(
        self,
        type: Annotated[Literal["pre"], "type"],
        language: Annotated[str, "language"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.language = language
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityCode(_MessageEntityBase):
    type: Annotated[Literal["code"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["code"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityTextLink(_MessageEntityBase):
    type: Annotated[Literal["textLink"], "type"]
    url: Annotated[str, "url"]

    def __init__(
        self,
        type: Annotated[Literal["textLink"], "type"],
        url: Annotated[str, "url"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.url = url
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityTextMention(_MessageEntityBase):
    type: Annotated[Literal["textMention"], "type"]
    user_id: Annotated[int, "userId"]

    def __init__(
        self,
        type: Annotated[Literal["textMention"], "type"],
        user_id: Annotated[int, "userId"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.user_id = user_id
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityCashtag(_MessageEntityBase):
    type: Annotated[Literal["cashtag"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["cashtag"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityPhoneNumber(_MessageEntityBase):
    type: Annotated[Literal["phoneNumber"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["phoneNumber"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityUnderline(_MessageEntityBase):
    type: Annotated[Literal["underline"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["underline"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityStrikethrough(_MessageEntityBase):
    type: Annotated[Literal["strikethrough"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["strikethrough"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityBlockquote(_MessageEntityBase):
    type: Annotated[Literal["blockquote"], "type"]
    collapsible: Annotated[Optional[Literal[True]], "collapsible"]

    def __init__(
        self,
        type: Annotated[Literal["blockquote"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
        *,
        collapsible: Annotated[Optional[Literal[True]], "collapsible"] = None,
    ):
        self.type = type
        self.collapsible = collapsible
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityBankCard(_MessageEntityBase):
    type: Annotated[Literal["bankCard"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["bankCard"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntitySpoiler(_MessageEntityBase):
    type: Annotated[Literal["spoiler"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["spoiler"], "type"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


class MessageEntityCustomEmoji(_MessageEntityBase):
    type: Annotated[Literal["customEmoji"], "type"]
    custom_emoji_id: Annotated[str, "customEmojiId"]

    def __init__(
        self,
        type: Annotated[Literal["customEmoji"], "type"],
        custom_emoji_id: Annotated[str, "customEmojiId"],
        offset: Annotated[int, "offset"],
        length: Annotated[int, "length"],
    ):
        self.type = type
        self.custom_emoji_id = custom_emoji_id
        self.offset = offset
        self.length = length

    __discriminators__ = ["type"]


MessageEntity = Union[
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

    def __init__(
        self,
        chat_id: Annotated[int, "chatId"],
        message_id: Annotated[int, "messageId"],
    ):
        self.chat_id = chat_id
        self.message_id = message_id


MessageSearchFilter = Union[
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

    def __init__(
        self,
        url: Annotated[str, "url"],
    ):
        self.url = url


class NetworkStatisticsEntry(_Type):
    sent: Annotated[int, "sent"]
    received: Annotated[int, "received"]

    def __init__(
        self,
        sent: Annotated[int, "sent"],
        received: Annotated[int, "received"],
    ):
        self.sent = sent
        self.received = received


class OpeningHours(_Type):
    timezone: Annotated[str, "timezone"]
    intervals: Annotated[list[Any], "intervals"]

    def __init__(
        self,
        timezone: Annotated[str, "timezone"],
        intervals: Annotated[list[Any], "intervals"],
    ):
        self.timezone = timezone
        self.intervals = intervals


ParseMode = Union[Literal["HTML"], Literal["Markdown"], None]


class PriceTag(_Type):
    label: Annotated[str, "label"]
    amount: Annotated[int, "amount"]

    def __init__(
        self,
        label: Annotated[str, "label"],
        amount: Annotated[int, "amount"],
    ):
        self.label = label
        self.amount = amount


class RefundedPayment(_Type):
    currency: Annotated[str, "currency"]
    total_amount: Annotated[int, "totalAmount"]
    invoice_payload: Annotated[str, "invoicePayload"]
    telegram_payment_charge_id: Annotated[str, "telegramPaymentChargeId"]
    provider_payment_charge_id: Annotated[Optional[str], "providerPaymentChargeId"]

    def __init__(
        self,
        currency: Annotated[str, "currency"],
        total_amount: Annotated[int, "totalAmount"],
        invoice_payload: Annotated[str, "invoicePayload"],
        telegram_payment_charge_id: Annotated[str, "telegramPaymentChargeId"],
        *,
        provider_payment_charge_id: Annotated[
            Optional[str], "providerPaymentChargeId"
        ] = None,
    ):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id


class ReactionEmoji(_Type):
    type: Annotated[Literal["emoji"], "type"]
    emoji: Annotated[str, "emoji"]

    def __init__(
        self,
        type: Annotated[Literal["emoji"], "type"],
        emoji: Annotated[str, "emoji"],
    ):
        self.type = type
        self.emoji = emoji


class ReactionCustom(_Type):
    type: Annotated[Literal["custom"], "type"]
    id: Annotated[str, "id"]

    def __init__(
        self,
        type: Annotated[Literal["custom"], "type"],
        id: Annotated[str, "id"],
    ):
        self.type = type
        self.id = id


class ReactionPaid(_Type):
    type: Annotated[Literal["paid"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["paid"], "type"],
    ):
        self.type = type


Reaction = Union[ReactionEmoji, ReactionCustom, ReactionPaid]


class RestrictionReason(_Type):
    platform: Annotated[str, "platform"]
    reason: Annotated[str, "reason"]
    text: Annotated[str, "text"]

    def __init__(
        self,
        platform: Annotated[str, "platform"],
        reason: Annotated[str, "reason"],
        text: Annotated[str, "text"],
    ):
        self.platform = platform
        self.reason = reason
        self.text = text


SelfDestructAfterOpen = Literal["afterOpen"]

SelfDestructAfterSeconds = int

SelfDestructOption = Union[SelfDestructAfterOpen, SelfDestructAfterSeconds]


class ShippingAddress(_Type):
    country_code: Annotated[str, "countryCode"]
    state: Annotated[str, "state"]
    city: Annotated[str, "city"]
    street_line1: Annotated[str, "streetLine1"]
    street_line2: Annotated[str, "streetLine2"]
    post_code: Annotated[str, "postCode"]

    def __init__(
        self,
        country_code: Annotated[str, "countryCode"],
        state: Annotated[str, "state"],
        city: Annotated[str, "city"],
        street_line1: Annotated[str, "streetLine1"],
        street_line2: Annotated[str, "streetLine2"],
        post_code: Annotated[str, "postCode"],
    ):
        self.country_code = country_code
        self.state = state
        self.city = city
        self.street_line1 = street_line1
        self.street_line2 = street_line2
        self.post_code = post_code


class StoryReference(_Type):
    chat_id: Annotated[int, "chatId"]
    story_id: Annotated[int, "storyId"]

    def __init__(
        self,
        chat_id: Annotated[int, "chatId"],
        story_id: Annotated[int, "storyId"],
    ):
        self.chat_id = chat_id
        self.story_id = story_id


class SwitchInlineQueryChosenChats(_Type):
    query: Annotated[str, "query"]
    allow_users: Annotated[Optional[bool], "allowUsers"]
    allow_bots: Annotated[Optional[bool], "allowBots"]
    allow_groups: Annotated[Optional[bool], "allowGroups"]
    allow_channels: Annotated[Optional[bool], "allowChannels"]

    def __init__(
        self,
        query: Annotated[str, "query"],
        *,
        allow_users: Annotated[Optional[bool], "allowUsers"] = None,
        allow_bots: Annotated[Optional[bool], "allowBots"] = None,
        allow_groups: Annotated[Optional[bool], "allowGroups"] = None,
        allow_channels: Annotated[Optional[bool], "allowChannels"] = None,
    ):
        self.query = query
        self.allow_users = allow_users
        self.allow_bots = allow_bots
        self.allow_groups = allow_groups
        self.allow_channels = allow_channels


class Thumbnail(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    width: Annotated[int, "width"]
    height: Annotated[int, "height"]
    file_size: Annotated[int, "fileSize"]

    def __init__(
        self,
        file_id: Annotated[str, "fileId"],
        file_unique_id: Annotated[str, "fileUniqueId"],
        width: Annotated[int, "width"],
        height: Annotated[int, "height"],
        file_size: Annotated[int, "fileSize"],
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size


class _VideoChatCommon(_Type):
    id: Annotated[str, "id"]

    def __init__(
        self,
        id: Annotated[str, "id"],
    ):
        self.id = id


class _VideoChatNotEndedCommon(_Type):
    title: Annotated[str, "title"]
    live_stream: Annotated[bool, "liveStream"]
    participant_count: Annotated[int, "participantCount"]

    def __init__(
        self,
        title: Annotated[str, "title"],
        live_stream: Annotated[bool, "liveStream"],
        participant_count: Annotated[int, "participantCount"],
    ):
        self.title = title
        self.live_stream = live_stream
        self.participant_count = participant_count


class VideoChatActive(_VideoChatCommon, _VideoChatNotEndedCommon):
    type: Annotated[Literal["active"], "type"]
    recording: Annotated[bool, "recording"]

    def __init__(
        self,
        type: Annotated[Literal["active"], "type"],
        recording: Annotated[bool, "recording"],
        id: Annotated[str, "id"],
        title: Annotated[str, "title"],
        live_stream: Annotated[bool, "liveStream"],
        participant_count: Annotated[int, "participantCount"],
    ):
        self.type = type
        self.recording = recording
        self.id = id
        self.title = title
        self.live_stream = live_stream
        self.participant_count = participant_count


class VideoChatScheduled(_VideoChatCommon, _VideoChatNotEndedCommon):
    type: Annotated[Literal["scheduled"], "type"]
    scheduled_for: Annotated[datetime.datetime, "scheduledFor"]

    def __init__(
        self,
        type: Annotated[Literal["scheduled"], "type"],
        scheduled_for: Annotated[datetime.datetime, "scheduledFor"],
        id: Annotated[str, "id"],
        title: Annotated[str, "title"],
        live_stream: Annotated[bool, "liveStream"],
        participant_count: Annotated[int, "participantCount"],
    ):
        self.type = type
        self.scheduled_for = scheduled_for
        self.id = id
        self.title = title
        self.live_stream = live_stream
        self.participant_count = participant_count


class VideoChatEnded(_VideoChatCommon):
    type: Annotated[Literal["ended"], "type"]
    duration: Annotated[int, "duration"]

    def __init__(
        self,
        type: Annotated[Literal["ended"], "type"],
        duration: Annotated[int, "duration"],
        id: Annotated[str, "id"],
    ):
        self.type = type
        self.duration = duration
        self.id = id


VideoChat = Union[VideoChatActive, VideoChatScheduled, VideoChatEnded]


class Voice(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    duration: Annotated[int, "duration"]
    mime_type: Annotated[str, "mimeType"]
    file_size: Annotated[int, "fileSize"]

    def __init__(
        self,
        file_id: Annotated[str, "fileId"],
        file_unique_id: Annotated[str, "fileUniqueId"],
        duration: Annotated[int, "duration"],
        mime_type: Annotated[str, "mimeType"],
        file_size: Annotated[int, "fileSize"],
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size


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

    def __init__(
        self,
        file_id: Annotated[str, "fileId"],
        file_unique_id: Annotated[str, "fileUniqueId"],
        width: Annotated[int, "width"],
        height: Annotated[int, "height"],
        duration: Annotated[int, "duration"],
        thumbnails: Annotated[list["Thumbnail"], "thumbnails"],
        mime_type: Annotated[str, "mimeType"],
        file_size: Annotated[int, "fileSize"],
        *,
        file_name: Annotated[Optional[str], "fileName"] = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnails = thumbnails
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Audio(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    duration: Annotated[int, "duration"]
    performer: Annotated[Optional[str], "performer"]
    title: Annotated[Optional[str], "title"]
    mime_type: Annotated[str, "mimeType"]
    file_size: Annotated[int, "fileSize"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]

    def __init__(
        self,
        file_id: Annotated[str, "fileId"],
        file_unique_id: Annotated[str, "fileUniqueId"],
        duration: Annotated[int, "duration"],
        mime_type: Annotated[str, "mimeType"],
        file_size: Annotated[int, "fileSize"],
        thumbnails: Annotated[list["Thumbnail"], "thumbnails"],
        *,
        performer: Annotated[Optional[str], "performer"] = None,
        title: Annotated[Optional[str], "title"] = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size
        self.thumbnails = thumbnails


class BotCommandScopeDefault(_Type):
    type: Annotated[Literal["default"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["default"], "type"],
    ):
        self.type = type

    __discriminators__ = ["type"]


class BotCommandScopeAllPrivateChats(_Type):
    type: Annotated[Literal["allPrivateChats"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["allPrivateChats"], "type"],
    ):
        self.type = type

    __discriminators__ = ["type"]


class BotCommandScopeAllGroupChats(_Type):
    type: Annotated[Literal["allGroupChats"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["allGroupChats"], "type"],
    ):
        self.type = type

    __discriminators__ = ["type"]


class BotCommandScopeAllChatAdministrators(_Type):
    type: Annotated[Literal["allChatAdministrators"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["allChatAdministrators"], "type"],
    ):
        self.type = type

    __discriminators__ = ["type"]


class BotCommandScopeChat(_Type):
    type: Annotated[Literal["chat"], "type"]
    chat_id: Annotated["ID", "chatId"]

    def __init__(
        self,
        type: Annotated[Literal["chat"], "type"],
        chat_id: Annotated["ID", "chatId"],
    ):
        self.type = type
        self.chat_id = chat_id

    __discriminators__ = ["type"]


class BotCommandScopeChatAdministrators(_Type):
    type: Annotated[Literal["chatAdministrators"], "type"]
    chat_id: Annotated["ID", "chatId"]

    def __init__(
        self,
        type: Annotated[Literal["chatAdministrators"], "type"],
        chat_id: Annotated["ID", "chatId"],
    ):
        self.type = type
        self.chat_id = chat_id

    __discriminators__ = ["type"]


class BotCommandScopeChatMember(_Type):
    type: Annotated[Literal["chatMember"], "type"]
    chat_id: Annotated["ID", "chatId"]
    user_id: Annotated[int, "userId"]

    def __init__(
        self,
        type: Annotated[Literal["chatMember"], "type"],
        chat_id: Annotated["ID", "chatId"],
        user_id: Annotated[int, "userId"],
    ):
        self.type = type
        self.chat_id = chat_id
        self.user_id = user_id

    __discriminators__ = ["type"]


BotCommandScope = Union[
    BotCommandScopeDefault,
    BotCommandScopeAllPrivateChats,
    BotCommandScopeAllGroupChats,
    BotCommandScopeAllChatAdministrators,
    BotCommandScopeChat,
    BotCommandScopeChatAdministrators,
    BotCommandScopeChatMember,
]

ChatType = Union[
    Literal["private"], Literal["group"], Literal["supergroup"], Literal["channel"]
]


class _ChatPBase(_Type):
    id: Annotated[int, "id"]
    type: Annotated["ChatType", "type"]
    color: Annotated[int, "color"]

    def __init__(
        self,
        id: Annotated[int, "id"],
        type: Annotated["ChatType", "type"],
        color: Annotated[int, "color"],
    ):
        self.id = id
        self.type = type
        self.color = color

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

    def __init__(
        self,
        type: Annotated[Literal["private"], "type"],
        first_name: Annotated[str, "firstName"],
        is_scam: Annotated[bool, "isScam"],
        is_fake: Annotated[bool, "isFake"],
        is_support: Annotated[bool, "isSupport"],
        is_verified: Annotated[bool, "isVerified"],
        id: Annotated[int, "id"],
        color: Annotated[int, "color"],
        *,
        is_bot: Annotated[Optional[bool], "isBot"] = None,
        last_name: Annotated[Optional[str], "lastName"] = None,
        username: Annotated[Optional[str], "username"] = None,
        also: Annotated[Optional[list[str]], "also"] = None,
        is_restricted: Annotated[Optional[bool], "isRestricted"] = None,
        restriction_reason: Annotated[
            Optional[list["RestrictionReason"]], "restrictionReason"
        ] = None,
    ):
        self.type = type
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.also = also
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_support = is_support
        self.is_verified = is_verified
        self.is_restricted = is_restricted
        self.restriction_reason = restriction_reason
        self.id = id
        self.color = color

    __discriminators__ = ["type"]


class ChatPGroup(_ChatPBase):
    type: Annotated[Literal["group"], "type"]
    title: Annotated[str, "title"]
    is_creator: Annotated[bool, "isCreator"]

    def __init__(
        self,
        type: Annotated[Literal["group"], "type"],
        title: Annotated[str, "title"],
        is_creator: Annotated[bool, "isCreator"],
        id: Annotated[int, "id"],
        color: Annotated[int, "color"],
    ):
        self.type = type
        self.title = title
        self.is_creator = is_creator
        self.id = id
        self.color = color

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

    def __init__(
        self,
        title: Annotated[str, "title"],
        is_scam: Annotated[bool, "isScam"],
        is_fake: Annotated[bool, "isFake"],
        is_verified: Annotated[bool, "isVerified"],
        is_restricted: Annotated[bool, "isRestricted"],
        id: Annotated[int, "id"],
        type: Annotated["ChatType", "type"],
        color: Annotated[int, "color"],
        *,
        username: Annotated[Optional[str], "username"] = None,
        also: Annotated[Optional[list[str]], "also"] = None,
        restriction_reason: Annotated[
            Optional[list["RestrictionReason"]], "restrictionReason"
        ] = None,
    ):
        self.title = title
        self.username = username
        self.also = also
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_verified = is_verified
        self.is_restricted = is_restricted
        self.restriction_reason = restriction_reason
        self.id = id
        self.type = type
        self.color = color


class ChatPChannel(ChatPChannelBase):
    type: Annotated[Literal["channel"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["channel"], "type"],
        title: Annotated[str, "title"],
        is_scam: Annotated[bool, "isScam"],
        is_fake: Annotated[bool, "isFake"],
        is_verified: Annotated[bool, "isVerified"],
        is_restricted: Annotated[bool, "isRestricted"],
        id: Annotated[int, "id"],
        color: Annotated[int, "color"],
        *,
        username: Annotated[Optional[str], "username"] = None,
        also: Annotated[Optional[list[str]], "also"] = None,
        restriction_reason: Annotated[
            Optional[list["RestrictionReason"]], "restrictionReason"
        ] = None,
    ):
        self.type = type
        self.title = title
        self.username = username
        self.also = also
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_verified = is_verified
        self.is_restricted = is_restricted
        self.restriction_reason = restriction_reason
        self.id = id
        self.color = color

    __discriminators__ = ["type"]


class ChatPSupergroup(ChatPChannelBase):
    type: Annotated[Literal["supergroup"], "type"]
    is_forum: Annotated[bool, "isForum"]

    def __init__(
        self,
        type: Annotated[Literal["supergroup"], "type"],
        is_forum: Annotated[bool, "isForum"],
        title: Annotated[str, "title"],
        is_scam: Annotated[bool, "isScam"],
        is_fake: Annotated[bool, "isFake"],
        is_verified: Annotated[bool, "isVerified"],
        is_restricted: Annotated[bool, "isRestricted"],
        id: Annotated[int, "id"],
        color: Annotated[int, "color"],
        *,
        username: Annotated[Optional[str], "username"] = None,
        also: Annotated[Optional[list[str]], "also"] = None,
        restriction_reason: Annotated[
            Optional[list["RestrictionReason"]], "restrictionReason"
        ] = None,
    ):
        self.type = type
        self.is_forum = is_forum
        self.title = title
        self.username = username
        self.also = also
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_verified = is_verified
        self.is_restricted = is_restricted
        self.restriction_reason = restriction_reason
        self.id = id
        self.color = color

    __discriminators__ = ["type"]


ChatP = Union[ChatPPrivate, ChatPGroup, ChatPSupergroup, ChatPChannel]


class Document(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]
    file_name: Annotated[str, "fileName"]
    mime_type: Annotated[str, "mimeType"]
    file_size: Annotated[int, "fileSize"]

    def __init__(
        self,
        file_id: Annotated[str, "fileId"],
        file_unique_id: Annotated[str, "fileUniqueId"],
        thumbnails: Annotated[list["Thumbnail"], "thumbnails"],
        file_name: Annotated[str, "fileName"],
        mime_type: Annotated[str, "mimeType"],
        file_size: Annotated[int, "fileSize"],
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.thumbnails = thumbnails
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class Giveaway(_Type):
    parameters: Annotated["GiveawayParameters", "parameters"]
    winner_count: Annotated[int, "winnerCount"]
    premium_month_count: Annotated[Optional[int], "premiumMonthCount"]
    star_count: Annotated[Optional[int], "starCount"]

    def __init__(
        self,
        parameters: Annotated["GiveawayParameters", "parameters"],
        winner_count: Annotated[int, "winnerCount"],
        *,
        premium_month_count: Annotated[Optional[int], "premiumMonthCount"] = None,
        star_count: Annotated[Optional[int], "starCount"] = None,
    ):
        self.parameters = parameters
        self.winner_count = winner_count
        self.premium_month_count = premium_month_count
        self.star_count = star_count


class InlineQueryResultButton(_Type):
    text: Annotated[str, "text"]
    mini_app: Annotated[Optional["MiniAppInfo"], "miniApp"]
    start_parameter: Annotated[Optional[str], "startParameter"]

    def __init__(
        self,
        text: Annotated[str, "text"],
        *,
        mini_app: Annotated[Optional["MiniAppInfo"], "miniApp"] = None,
        start_parameter: Annotated[Optional[str], "startParameter"] = None,
    ):
        self.text = text
        self.mini_app = mini_app
        self.start_parameter = start_parameter


class _InputMediaCommon(_Type):
    file_name: Annotated[Optional[str], "fileName"]
    mime_type: Annotated[Optional[str], "mimeType"]
    chunk_size: Annotated[Optional[int], "chunkSize"]
    caption: Annotated[Optional[str], "caption"]
    caption_entities: Annotated[Optional[list["MessageEntity"]], "captionEntities"]
    parse_mode: Annotated[Optional["ParseMode"], "parseMode"]

    def __init__(
        self,
        *,
        file_name: Annotated[Optional[str], "fileName"] = None,
        mime_type: Annotated[Optional[str], "mimeType"] = None,
        chunk_size: Annotated[Optional[int], "chunkSize"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
    ):
        self.file_name = file_name
        self.mime_type = mime_type
        self.chunk_size = chunk_size
        self.caption = caption
        self.caption_entities = caption_entities
        self.parse_mode = parse_mode


class InputMediaAnimation(_InputMediaCommon):
    animation: Annotated["FileSource", "animation"]
    thumbnail: Annotated[Optional["FileSource"], "thumbnail"]
    duration: Annotated[Optional[int], "duration"]
    width: Annotated[Optional[int], "width"]
    height: Annotated[Optional[int], "height"]
    has_spoiler: Annotated[Optional[bool], "hasSpoiler"]

    def __init__(
        self,
        animation: Annotated["FileSource", "animation"],
        *,
        thumbnail: Annotated[Optional["FileSource"], "thumbnail"] = None,
        duration: Annotated[Optional[int], "duration"] = None,
        width: Annotated[Optional[int], "width"] = None,
        height: Annotated[Optional[int], "height"] = None,
        has_spoiler: Annotated[Optional[bool], "hasSpoiler"] = None,
        file_name: Annotated[Optional[str], "fileName"] = None,
        mime_type: Annotated[Optional[str], "mimeType"] = None,
        chunk_size: Annotated[Optional[int], "chunkSize"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
    ):
        self.animation = animation
        self.thumbnail = thumbnail
        self.duration = duration
        self.width = width
        self.height = height
        self.has_spoiler = has_spoiler
        self.file_name = file_name
        self.mime_type = mime_type
        self.chunk_size = chunk_size
        self.caption = caption
        self.caption_entities = caption_entities
        self.parse_mode = parse_mode

    __discriminators__ = ["animation"]


class InputMediaAudio(_InputMediaCommon):
    audio: Annotated["FileSource", "audio"]
    thumbnail: Annotated[Optional["FileSource"], "thumbnail"]
    duration: Annotated[Optional[int], "duration"]
    performer: Annotated[Optional[str], "performer"]
    title: Annotated[Optional[str], "title"]

    def __init__(
        self,
        audio: Annotated["FileSource", "audio"],
        *,
        thumbnail: Annotated[Optional["FileSource"], "thumbnail"] = None,
        duration: Annotated[Optional[int], "duration"] = None,
        performer: Annotated[Optional[str], "performer"] = None,
        title: Annotated[Optional[str], "title"] = None,
        file_name: Annotated[Optional[str], "fileName"] = None,
        mime_type: Annotated[Optional[str], "mimeType"] = None,
        chunk_size: Annotated[Optional[int], "chunkSize"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
    ):
        self.audio = audio
        self.thumbnail = thumbnail
        self.duration = duration
        self.performer = performer
        self.title = title
        self.file_name = file_name
        self.mime_type = mime_type
        self.chunk_size = chunk_size
        self.caption = caption
        self.caption_entities = caption_entities
        self.parse_mode = parse_mode

    __discriminators__ = ["audio"]


class InputMediaDocument(_InputMediaCommon):
    document: Annotated["FileSource", "document"]
    thumbnail: Annotated[Optional["FileSource"], "thumbnail"]

    def __init__(
        self,
        document: Annotated["FileSource", "document"],
        *,
        thumbnail: Annotated[Optional["FileSource"], "thumbnail"] = None,
        file_name: Annotated[Optional[str], "fileName"] = None,
        mime_type: Annotated[Optional[str], "mimeType"] = None,
        chunk_size: Annotated[Optional[int], "chunkSize"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
    ):
        self.document = document
        self.thumbnail = thumbnail
        self.file_name = file_name
        self.mime_type = mime_type
        self.chunk_size = chunk_size
        self.caption = caption
        self.caption_entities = caption_entities
        self.parse_mode = parse_mode

    __discriminators__ = ["document"]


class InputMediaPhoto(_InputMediaCommon):
    photo: Annotated["FileSource", "photo"]
    width: Annotated[Optional[int], "width"]
    height: Annotated[Optional[int], "height"]
    has_spoiler: Annotated[Optional[bool], "hasSpoiler"]
    self_destruct: Annotated[Optional["SelfDestructOption"], "selfDestruct"]

    def __init__(
        self,
        photo: Annotated["FileSource", "photo"],
        *,
        width: Annotated[Optional[int], "width"] = None,
        height: Annotated[Optional[int], "height"] = None,
        has_spoiler: Annotated[Optional[bool], "hasSpoiler"] = None,
        self_destruct: Annotated[Optional["SelfDestructOption"], "selfDestruct"] = None,
        file_name: Annotated[Optional[str], "fileName"] = None,
        mime_type: Annotated[Optional[str], "mimeType"] = None,
        chunk_size: Annotated[Optional[int], "chunkSize"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
    ):
        self.photo = photo
        self.width = width
        self.height = height
        self.has_spoiler = has_spoiler
        self.self_destruct = self_destruct
        self.file_name = file_name
        self.mime_type = mime_type
        self.chunk_size = chunk_size
        self.caption = caption
        self.caption_entities = caption_entities
        self.parse_mode = parse_mode

    __discriminators__ = ["photo"]


class InputMediaVideo(_InputMediaCommon):
    video: Annotated["FileSource", "video"]
    thumbnail: Annotated[Optional["FileSource"], "thumbnail"]
    duration: Annotated[Optional[int], "duration"]
    width: Annotated[Optional[int], "width"]
    height: Annotated[Optional[int], "height"]
    supports_streaming: Annotated[Optional[bool], "supportsStreaming"]
    has_spoiler: Annotated[Optional[bool], "hasSpoiler"]
    self_destruct: Annotated[Optional["SelfDestructOption"], "selfDestruct"]

    def __init__(
        self,
        video: Annotated["FileSource", "video"],
        *,
        thumbnail: Annotated[Optional["FileSource"], "thumbnail"] = None,
        duration: Annotated[Optional[int], "duration"] = None,
        width: Annotated[Optional[int], "width"] = None,
        height: Annotated[Optional[int], "height"] = None,
        supports_streaming: Annotated[Optional[bool], "supportsStreaming"] = None,
        has_spoiler: Annotated[Optional[bool], "hasSpoiler"] = None,
        self_destruct: Annotated[Optional["SelfDestructOption"], "selfDestruct"] = None,
        file_name: Annotated[Optional[str], "fileName"] = None,
        mime_type: Annotated[Optional[str], "mimeType"] = None,
        chunk_size: Annotated[Optional[int], "chunkSize"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
    ):
        self.video = video
        self.thumbnail = thumbnail
        self.duration = duration
        self.width = width
        self.height = height
        self.supports_streaming = supports_streaming
        self.has_spoiler = has_spoiler
        self.self_destruct = self_destruct
        self.file_name = file_name
        self.mime_type = mime_type
        self.chunk_size = chunk_size
        self.caption = caption
        self.caption_entities = caption_entities
        self.parse_mode = parse_mode

    __discriminators__ = ["video"]


InputMedia = Union[
    InputMediaAnimation,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
]


class InputStoryContentPhoto(_Type):
    photo: Annotated["FileSource", "photo"]
    attached_sticker_file_ids: Annotated[Optional[list[str]], "attachedStickerFileIds"]

    def __init__(
        self,
        photo: Annotated["FileSource", "photo"],
        *,
        attached_sticker_file_ids: Annotated[
            Optional[list[str]], "attachedStickerFileIds"
        ] = None,
    ):
        self.photo = photo
        self.attached_sticker_file_ids = attached_sticker_file_ids

    __discriminators__ = ["photo"]


class InputStoryContentVideo(_Type):
    video: Annotated["FileSource", "video"]
    attached_sticker_file_ids: Annotated[Optional[list[str]], "attachedStickerFileIds"]
    duration: Annotated[int, "duration"]
    animation: Annotated[Optional[bool], "animation"]

    def __init__(
        self,
        video: Annotated["FileSource", "video"],
        duration: Annotated[int, "duration"],
        *,
        attached_sticker_file_ids: Annotated[
            Optional[list[str]], "attachedStickerFileIds"
        ] = None,
        animation: Annotated[Optional[bool], "animation"] = None,
    ):
        self.video = video
        self.attached_sticker_file_ids = attached_sticker_file_ids
        self.duration = duration
        self.animation = animation

    __discriminators__ = ["video"]


InputStoryContent = Union[InputStoryContentPhoto, InputStoryContentVideo]


class KeyboardButtonText(_Type):
    text: Annotated[str, "text"]

    def __init__(
        self,
        text: Annotated[str, "text"],
    ):
        self.text = text

    __discriminators__ = ["text"]


class KeyboardButtonRequestUser(KeyboardButtonText):
    request_user: Annotated[Any, "requestUser"]

    def __init__(
        self,
        request_user: Annotated[Any, "requestUser"],
        text: Annotated[str, "text"],
    ):
        self.request_user = request_user
        self.text = text

    __discriminators__ = ["requestUser"]


class KeyboardButtonRequestChat(KeyboardButtonText):
    request_chat: Annotated[Any, "requestChat"]

    def __init__(
        self,
        request_chat: Annotated[Any, "requestChat"],
        text: Annotated[str, "text"],
    ):
        self.request_chat = request_chat
        self.text = text

    __discriminators__ = ["requestChat"]


class KeyboardButtonRequestContact(KeyboardButtonText):
    request_contact: Annotated[Literal[True], "requestContact"]

    def __init__(
        self,
        request_contact: Annotated[Literal[True], "requestContact"],
        text: Annotated[str, "text"],
    ):
        self.request_contact = request_contact
        self.text = text

    __discriminators__ = ["requestContact"]


class KeyboardButtonRequestLocation(KeyboardButtonText):
    request_location: Annotated[Literal[True], "requestLocation"]

    def __init__(
        self,
        request_location: Annotated[Literal[True], "requestLocation"],
        text: Annotated[str, "text"],
    ):
        self.request_location = request_location
        self.text = text

    __discriminators__ = ["requestLocation"]


class KeyboardButtonRequestPoll(KeyboardButtonText):
    request_poll: Annotated["KeyboardButtonPollType", "requestPoll"]

    def __init__(
        self,
        request_poll: Annotated["KeyboardButtonPollType", "requestPoll"],
        text: Annotated[str, "text"],
    ):
        self.request_poll = request_poll
        self.text = text

    __discriminators__ = ["requestPoll"]


class KeyboardButtonMiniApp(KeyboardButtonText):
    mini_app: Annotated["MiniAppInfo", "miniApp"]

    def __init__(
        self,
        mini_app: Annotated["MiniAppInfo", "miniApp"],
        text: Annotated[str, "text"],
    ):
        self.mini_app = mini_app
        self.text = text

    __discriminators__ = ["miniApp"]


KeyboardButton = Union[
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

    def __init__(
        self,
        type: Annotated[Literal["contact"], "type"],
        phone_number: Annotated[str, "phoneNumber"],
        first_name: Annotated[str, "firstName"],
        *,
        last_name: Annotated[Optional[str], "lastName"] = None,
        vcard: Annotated[Optional[str], "vcard"] = None,
    ):
        self.type = type
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard


class MessageContentLocation(_Type):
    type: Annotated[Literal["text"], "type"]
    latitude: Annotated[int, "latitude"]
    longitude: Annotated[int, "longitude"]
    horizontal_accuracy: Annotated[Optional[int], "horizontalAccuracy"]
    live_period: Annotated[Optional[int], "livePeriod"]
    heading: Annotated[Optional[int], "heading"]
    proximity_alert_radius: Annotated[Optional[int], "proximityAlertRadius"]

    def __init__(
        self,
        type: Annotated[Literal["text"], "type"],
        latitude: Annotated[int, "latitude"],
        longitude: Annotated[int, "longitude"],
        *,
        horizontal_accuracy: Annotated[Optional[int], "horizontalAccuracy"] = None,
        live_period: Annotated[Optional[int], "livePeriod"] = None,
        heading: Annotated[Optional[int], "heading"] = None,
        proximity_alert_radius: Annotated[Optional[int], "proximityAlertRadius"] = None,
    ):
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius


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

    def __init__(
        self,
        type: Annotated[Literal["venue"], "type"],
        latitude: Annotated[int, "latitude"],
        longitude: Annotated[int, "longitude"],
        title: Annotated[str, "title"],
        address: Annotated[str, "address"],
        *,
        foursquare_id: Annotated[Optional[str], "foursquareId"] = None,
        foursquare_type: Annotated[Optional[str], "foursquareType"] = None,
        google_place_id: Annotated[Optional[str], "googlePlaceId"] = None,
        google_place_type: Annotated[Optional[str], "googlePlaceType"] = None,
    ):
        self.type = type
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.google_place_id = google_place_id
        self.google_place_type = google_place_type


class MessageContentText(_Type):
    type: Annotated[Literal["text"], "type"]
    text: Annotated[str, "text"]
    parse_mode: Annotated[Optional["ParseMode"], "parseMode"]
    entities: Annotated[Optional[list["MessageEntity"]], "entities"]
    link_preview: Annotated[Optional["LinkPreview"], "linkPreview"]

    def __init__(
        self,
        type: Annotated[Literal["text"], "type"],
        text: Annotated[str, "text"],
        *,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        entities: Annotated[Optional[list["MessageEntity"]], "entities"] = None,
        link_preview: Annotated[Optional["LinkPreview"], "linkPreview"] = None,
    ):
        self.type = type
        self.text = text
        self.parse_mode = parse_mode
        self.entities = entities
        self.link_preview = link_preview


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

    def __init__(
        self,
        type: Annotated[Literal["invoice"], "type"],
        title: Annotated[str, "title"],
        description: Annotated[str, "description"],
        payload: Annotated[str, "payload"],
        provider_token: Annotated[str, "providerToken"],
        currency: Annotated[str, "currency"],
        prices: Annotated[list["PriceTag"], "prices"],
        *,
        max_tip_amount: Annotated[Optional[int], "maxTipAmount"] = None,
        suggested_tip_amounts: Annotated[
            Optional[list[int]], "suggestedTipAmounts"
        ] = None,
        provider_data: Annotated[Optional[str], "providerData"] = None,
        photo_url: Annotated[Optional[str], "photoUrl"] = None,
        photo_size: Annotated[Optional[int], "photoSize"] = None,
        photo_width: Annotated[Optional[int], "photoWidth"] = None,
        photo_height: Annotated[Optional[int], "photoHeight"] = None,
        need_name: Annotated[Optional[bool], "needName"] = None,
        need_phone_number: Annotated[Optional[bool], "needPhoneNumber"] = None,
        need_email: Annotated[Optional[bool], "needEmail"] = None,
        need_shipping_a_address: Annotated[
            Optional[bool], "needShippingAAddress"
        ] = None,
        send_phone_number_to_porvider: Annotated[
            Optional[bool], "sendPhoneNumberToPorvider"
        ] = None,
        send_email_to_provider: Annotated[Optional[bool], "sendEmailToProvider"] = None,
        is_flexible: Annotated[Optional[bool], "isFlexible"] = None,
    ):
        self.type = type
        self.title = title
        self.description = description
        self.payload = payload
        self.provider_token = provider_token
        self.currency = currency
        self.prices = prices
        self.max_tip_amount = max_tip_amount
        self.suggested_tip_amounts = suggested_tip_amounts
        self.provider_data = provider_data
        self.photo_url = photo_url
        self.photo_size = photo_size
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.need_name = need_name
        self.need_phone_number = need_phone_number
        self.need_email = need_email
        self.need_shipping_a_address = need_shipping_a_address
        self.send_phone_number_to_porvider = send_phone_number_to_porvider
        self.send_email_to_provider = send_email_to_provider
        self.is_flexible = is_flexible


MessageContent = Union[
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

    def __init__(
        self,
        reaction: Annotated["Reaction", "reaction"],
        count: Annotated[int, "count"],
        choosers: Annotated[list[int], "choosers"],
        chosen: Annotated[bool, "chosen"],
    ):
        self.reaction = reaction
        self.count = count
        self.choosers = choosers
        self.chosen = chosen


class NetworkStatistics(_Type):
    messages: Annotated["NetworkStatisticsEntry", "messages"]
    cdn: Annotated["NetworkStatisticsEntry", "cdn"]

    def __init__(
        self,
        messages: Annotated["NetworkStatisticsEntry", "messages"],
        cdn: Annotated["NetworkStatisticsEntry", "cdn"],
    ):
        self.messages = messages
        self.cdn = cdn


class OrderInfo(_Type):
    name: Annotated[Optional[str], "name"]
    phone_number: Annotated[Optional[str], "phoneNumber"]
    email: Annotated[Optional[str], "email"]
    shipping_address: Annotated[Optional["ShippingAddress"], "shippingAddress"]

    def __init__(
        self,
        *,
        name: Annotated[Optional[str], "name"] = None,
        phone_number: Annotated[Optional[str], "phoneNumber"] = None,
        email: Annotated[Optional[str], "email"] = None,
        shipping_address: Annotated[
            Optional["ShippingAddress"], "shippingAddress"
        ] = None,
    ):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.shipping_address = shipping_address


class Photo(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    width: Annotated[int, "width"]
    height: Annotated[int, "height"]
    file_size: Annotated[int, "fileSize"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]

    def __init__(
        self,
        file_id: Annotated[str, "fileId"],
        file_unique_id: Annotated[str, "fileUniqueId"],
        width: Annotated[int, "width"],
        height: Annotated[int, "height"],
        file_size: Annotated[int, "fileSize"],
        thumbnails: Annotated[list["Thumbnail"], "thumbnails"],
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.file_size = file_size
        self.thumbnails = thumbnails


class PollOption(_Type):
    text: Annotated[str, "text"]
    entities: Annotated[list["MessageEntity"], "entities"]
    voter_count: Annotated[int, "voterCount"]

    def __init__(
        self,
        text: Annotated[str, "text"],
        entities: Annotated[list["MessageEntity"], "entities"],
        voter_count: Annotated[int, "voterCount"],
    ):
        self.text = text
        self.entities = entities
        self.voter_count = voter_count


class ReactionCount(_Type):
    reaction: Annotated["Reaction", "reaction"]
    count: Annotated[int, "count"]

    def __init__(
        self,
        reaction: Annotated["Reaction", "reaction"],
        count: Annotated[int, "count"],
    ):
        self.reaction = reaction
        self.count = count


class ReplyQuote(_Type):
    offset: Annotated[int, "offset"]
    text: Annotated[str, "text"]
    entities: Annotated[list["MessageEntity"], "entities"]

    def __init__(
        self,
        offset: Annotated[int, "offset"],
        text: Annotated[str, "text"],
        entities: Annotated[list["MessageEntity"], "entities"],
    ):
        self.offset = offset
        self.text = text
        self.entities = entities


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

    def __init__(
        self,
        file_id: Annotated[str, "fileId"],
        file_unique_id: Annotated[str, "fileUniqueId"],
        type: Annotated[Any, "type"],
        width: Annotated[int, "width"],
        height: Annotated[int, "height"],
        is_animated: Annotated[bool, "isAnimated"],
        is_video: Annotated[bool, "isVideo"],
        thumbnails: Annotated[list["Thumbnail"], "thumbnails"],
        *,
        emoji: Annotated[Optional[str], "emoji"] = None,
        set_name: Annotated[Optional[str], "setName"] = None,
        premium_animation: Annotated[Optional[Any], "premiumAnimation"] = None,
        mask_position: Annotated[Optional["MaskPosition"], "maskPosition"] = None,
        custom_emoji_id: Annotated[Optional[str], "customEmojiId"] = None,
        needs_repainting: Annotated[Optional[bool], "needsRepainting"] = None,
        file_size: Annotated[Optional[int], "fileSize"] = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.type = type
        self.width = width
        self.height = height
        self.is_animated = is_animated
        self.is_video = is_video
        self.thumbnails = thumbnails
        self.emoji = emoji
        self.set_name = set_name
        self.premium_animation = premium_animation
        self.mask_position = mask_position
        self.custom_emoji_id = custom_emoji_id
        self.needs_repainting = needs_repainting
        self.file_size = file_size


class StoryPrivacyEveryone(_Type):
    everyone_except: Annotated[list[int], "everyoneExcept"]

    def __init__(
        self,
        everyone_except: Annotated[list[int], "everyoneExcept"],
    ):
        self.everyone_except = everyone_except

    __discriminators__ = ["everyoneExcept"]


class StoryPrivacyConctacts(_Type):
    contacts_except: Annotated[list[int], "contactsExcept"]

    def __init__(
        self,
        contacts_except: Annotated[list[int], "contactsExcept"],
    ):
        self.contacts_except = contacts_except

    __discriminators__ = ["contactsExcept"]


class StoryPrivacyCloseFriends(_Type):
    close_friends: Annotated[Literal[True], "closeFriends"]

    def __init__(
        self,
        close_friends: Annotated[Literal[True], "closeFriends"],
    ):
        self.close_friends = close_friends

    __discriminators__ = ["closeFriends"]


class StoryPrivacyOnly(_Type):
    only: Annotated[list[int], "only"]

    def __init__(
        self,
        only: Annotated[list[int], "only"],
    ):
        self.only = only

    __discriminators__ = ["only"]


StoryPrivacy = Union[
    StoryPrivacyEveryone,
    StoryPrivacyConctacts,
    StoryPrivacyCloseFriends,
    StoryPrivacyOnly,
]


class StoryReaction(_Type):
    reaction: Annotated["Reaction", "reaction"]
    count: Annotated[int, "count"]
    chosen: Annotated[bool, "chosen"]

    def __init__(
        self,
        reaction: Annotated["Reaction", "reaction"],
        count: Annotated[int, "count"],
        chosen: Annotated[bool, "chosen"],
    ):
        self.reaction = reaction
        self.count = count
        self.chosen = chosen


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

    def __init__(
        self,
        id: Annotated[int, "id"],
        color: Annotated[int, "color"],
        is_bot: Annotated[bool, "isBot"],
        first_name: Annotated[str, "firstName"],
        is_scam: Annotated[bool, "isScam"],
        is_fake: Annotated[bool, "isFake"],
        is_premium: Annotated[bool, "isPremium"],
        is_verified: Annotated[bool, "isVerified"],
        is_support: Annotated[bool, "isSupport"],
        added_to_attachment_menu: Annotated[bool, "addedToAttachmentMenu"],
        *,
        last_name: Annotated[Optional[str], "lastName"] = None,
        username: Annotated[Optional[str], "username"] = None,
        also: Annotated[Optional[list[str]], "also"] = None,
        photo: Annotated[Optional["ChatPhoto"], "photo"] = None,
        language_code: Annotated[Optional[str], "languageCode"] = None,
    ):
        self.id = id
        self.color = color
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.also = also
        self.photo = photo
        self.language_code = language_code
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_premium = is_premium
        self.is_verified = is_verified
        self.is_support = is_support
        self.added_to_attachment_menu = added_to_attachment_menu

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

    @property
    def profile_link(self) -> Optional[str]:
        return None if not self.username else f"https://t.me/{self.username}"


class Venue(_Type):
    location: Annotated["Location", "location"]
    title: Annotated[str, "title"]
    address: Annotated[str, "address"]
    foursquare_id: Annotated[Optional[str], "foursquareId"]
    foursquare_type: Annotated[Optional[str], "foursquareType"]

    def __init__(
        self,
        location: Annotated["Location", "location"],
        title: Annotated[str, "title"],
        address: Annotated[str, "address"],
        *,
        foursquare_id: Annotated[Optional[str], "foursquareId"] = None,
        foursquare_type: Annotated[Optional[str], "foursquareType"] = None,
    ):
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type


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

    def __init__(
        self,
        file_id: Annotated[str, "fileId"],
        file_unique_id: Annotated[str, "fileUniqueId"],
        width: Annotated[int, "width"],
        height: Annotated[int, "height"],
        duration: Annotated[int, "duration"],
        thumbnails: Annotated[list["Thumbnail"], "thumbnails"],
        mime_type: Annotated[str, "mimeType"],
        file_size: Annotated[int, "fileSize"],
        *,
        file_name: Annotated[Optional[str], "fileName"] = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnails = thumbnails
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size


class VideoNote(_Type):
    file_id: Annotated[str, "fileId"]
    file_unique_id: Annotated[str, "fileUniqueId"]
    length: Annotated[int, "length"]
    duration: Annotated[int, "duration"]
    thumbnails: Annotated[list["Thumbnail"], "thumbnails"]
    file_name: Annotated[Optional[str], "fileName"]
    file_size: Annotated[int, "fileSize"]

    def __init__(
        self,
        file_id: Annotated[str, "fileId"],
        file_unique_id: Annotated[str, "fileUniqueId"],
        length: Annotated[int, "length"],
        duration: Annotated[int, "duration"],
        thumbnails: Annotated[list["Thumbnail"], "thumbnails"],
        file_size: Annotated[int, "fileSize"],
        *,
        file_name: Annotated[Optional[str], "fileName"] = None,
    ):
        self.file_id = file_id
        self.file_unique_id = file_unique_id
        self.length = length
        self.duration = duration
        self.thumbnails = thumbnails
        self.file_name = file_name
        self.file_size = file_size


class BusinessConnection(_Type):
    id: Annotated[str, "id"]
    user: Annotated["User", "user"]
    date: Annotated[datetime.datetime, "date"]
    can_reply: Annotated[bool, "canReply"]
    is_enabled: Annotated[bool, "isEnabled"]

    def __init__(
        self,
        id: Annotated[str, "id"],
        user: Annotated["User", "user"],
        date: Annotated[datetime.datetime, "date"],
        can_reply: Annotated[bool, "canReply"],
        is_enabled: Annotated[bool, "isEnabled"],
    ):
        self.id = id
        self.user = user
        self.date = date
        self.can_reply = can_reply
        self.is_enabled = is_enabled


class ChatBase(_Type):
    photo: Annotated[Optional["Photo"], "photo"]

    def __init__(
        self,
        *,
        photo: Annotated[Optional["Photo"], "photo"] = None,
    ):
        self.photo = photo


class ChatChannel(ChatBase, ChatPChannel):
    video_chat_id: Annotated[Optional[str], "videoChatId"]

    def __init__(
        self,
        type: Annotated[Literal["channel"], "type"],
        title: Annotated[str, "title"],
        is_scam: Annotated[bool, "isScam"],
        is_fake: Annotated[bool, "isFake"],
        is_verified: Annotated[bool, "isVerified"],
        is_restricted: Annotated[bool, "isRestricted"],
        id: Annotated[int, "id"],
        color: Annotated[int, "color"],
        *,
        video_chat_id: Annotated[Optional[str], "videoChatId"] = None,
        photo: Annotated[Optional["Photo"], "photo"] = None,
        username: Annotated[Optional[str], "username"] = None,
        also: Annotated[Optional[list[str]], "also"] = None,
        restriction_reason: Annotated[
            Optional[list["RestrictionReason"]], "restrictionReason"
        ] = None,
    ):
        self.video_chat_id = video_chat_id
        self.photo = photo
        self.type = type
        self.title = title
        self.username = username
        self.also = also
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_verified = is_verified
        self.is_restricted = is_restricted
        self.restriction_reason = restriction_reason
        self.id = id
        self.color = color


class ChatSupergroup(ChatBase, ChatPSupergroup):
    video_chat_id: Annotated[Optional[str], "videoChatId"]

    def __init__(
        self,
        type: Annotated[Literal["supergroup"], "type"],
        is_forum: Annotated[bool, "isForum"],
        title: Annotated[str, "title"],
        is_scam: Annotated[bool, "isScam"],
        is_fake: Annotated[bool, "isFake"],
        is_verified: Annotated[bool, "isVerified"],
        is_restricted: Annotated[bool, "isRestricted"],
        id: Annotated[int, "id"],
        color: Annotated[int, "color"],
        *,
        video_chat_id: Annotated[Optional[str], "videoChatId"] = None,
        photo: Annotated[Optional["Photo"], "photo"] = None,
        username: Annotated[Optional[str], "username"] = None,
        also: Annotated[Optional[list[str]], "also"] = None,
        restriction_reason: Annotated[
            Optional[list["RestrictionReason"]], "restrictionReason"
        ] = None,
    ):
        self.video_chat_id = video_chat_id
        self.photo = photo
        self.type = type
        self.is_forum = is_forum
        self.title = title
        self.username = username
        self.also = also
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_verified = is_verified
        self.is_restricted = is_restricted
        self.restriction_reason = restriction_reason
        self.id = id
        self.color = color


class ChatGroup(ChatBase, ChatPGroup):
    video_chat_id: Annotated[Optional[str], "videoChatId"]

    def __init__(
        self,
        type: Annotated[Literal["group"], "type"],
        title: Annotated[str, "title"],
        is_creator: Annotated[bool, "isCreator"],
        id: Annotated[int, "id"],
        color: Annotated[int, "color"],
        *,
        video_chat_id: Annotated[Optional[str], "videoChatId"] = None,
        photo: Annotated[Optional["Photo"], "photo"] = None,
    ):
        self.video_chat_id = video_chat_id
        self.photo = photo
        self.type = type
        self.title = title
        self.is_creator = is_creator
        self.id = id
        self.color = color


class ChatPrivate(ChatBase, ChatPPrivate):
    birthday: Annotated[Optional["Birthday"], "birthday"]
    address: Annotated[Optional[str], "address"]
    location: Annotated[Optional["Location"], "location"]
    opening_hours: Annotated[Optional["OpeningHours"], "openingHours"]
    has_main_mini_app: Annotated[Optional[bool], "hasMainMiniApp"]

    def __init__(
        self,
        type: Annotated[Literal["private"], "type"],
        first_name: Annotated[str, "firstName"],
        is_scam: Annotated[bool, "isScam"],
        is_fake: Annotated[bool, "isFake"],
        is_support: Annotated[bool, "isSupport"],
        is_verified: Annotated[bool, "isVerified"],
        id: Annotated[int, "id"],
        color: Annotated[int, "color"],
        *,
        birthday: Annotated[Optional["Birthday"], "birthday"] = None,
        address: Annotated[Optional[str], "address"] = None,
        location: Annotated[Optional["Location"], "location"] = None,
        opening_hours: Annotated[Optional["OpeningHours"], "openingHours"] = None,
        has_main_mini_app: Annotated[Optional[bool], "hasMainMiniApp"] = None,
        photo: Annotated[Optional["Photo"], "photo"] = None,
        is_bot: Annotated[Optional[bool], "isBot"] = None,
        last_name: Annotated[Optional[str], "lastName"] = None,
        username: Annotated[Optional[str], "username"] = None,
        also: Annotated[Optional[list[str]], "also"] = None,
        is_restricted: Annotated[Optional[bool], "isRestricted"] = None,
        restriction_reason: Annotated[
            Optional[list["RestrictionReason"]], "restrictionReason"
        ] = None,
    ):
        self.birthday = birthday
        self.address = address
        self.location = location
        self.opening_hours = opening_hours
        self.has_main_mini_app = has_main_mini_app
        self.photo = photo
        self.type = type
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.also = also
        self.is_scam = is_scam
        self.is_fake = is_fake
        self.is_support = is_support
        self.is_verified = is_verified
        self.is_restricted = is_restricted
        self.restriction_reason = restriction_reason
        self.id = id
        self.color = color


Chat = Union[ChatChannel, ChatSupergroup, ChatGroup, ChatPrivate]

ChatMemberStatus = Union[
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

    def __init__(
        self,
        status: Annotated["ChatMemberStatus", "status"],
        user: Annotated["User", "user"],
    ):
        self.status = status
        self.user = user


class ChatMemberCreator(_ChatMemberBase):
    status: Annotated[Literal["creator"], "status"]
    is_anonymous: Annotated[bool, "isAnonymous"]
    title: Annotated[Optional[str], "title"]

    def __init__(
        self,
        status: Annotated[Literal["creator"], "status"],
        is_anonymous: Annotated[bool, "isAnonymous"],
        user: Annotated["User", "user"],
        *,
        title: Annotated[Optional[str], "title"] = None,
    ):
        self.status = status
        self.is_anonymous = is_anonymous
        self.title = title
        self.user = user


class ChatMemberAdministrator(_ChatMemberBase):
    status: Annotated[Literal["administrator"], "status"]
    rights: Annotated["ChatAdministratorRights", "rights"]
    title: Annotated[Optional[str], "title"]

    def __init__(
        self,
        status: Annotated[Literal["administrator"], "status"],
        rights: Annotated["ChatAdministratorRights", "rights"],
        user: Annotated["User", "user"],
        *,
        title: Annotated[Optional[str], "title"] = None,
    ):
        self.status = status
        self.rights = rights
        self.title = title
        self.user = user


class ChatMemberMember(_ChatMemberBase):
    status: Annotated[Literal["member"], "status"]

    def __init__(
        self,
        status: Annotated[Literal["member"], "status"],
        user: Annotated["User", "user"],
    ):
        self.status = status
        self.user = user


class ChatMemberRestricted(_ChatMemberBase):
    status: Annotated[Literal["restricted"], "status"]
    is_member: Annotated[bool, "isMember"]
    rights: Annotated["ChatMemberRights", "rights"]
    until_date: Annotated[Optional[datetime.datetime], "untilDate"]

    def __init__(
        self,
        status: Annotated[Literal["restricted"], "status"],
        is_member: Annotated[bool, "isMember"],
        rights: Annotated["ChatMemberRights", "rights"],
        user: Annotated["User", "user"],
        *,
        until_date: Annotated[Optional[datetime.datetime], "untilDate"] = None,
    ):
        self.status = status
        self.is_member = is_member
        self.rights = rights
        self.until_date = until_date
        self.user = user


class ChatMemberLeft(_ChatMemberBase):
    status: Annotated[Literal["left"], "status"]

    def __init__(
        self,
        status: Annotated[Literal["left"], "status"],
        user: Annotated["User", "user"],
    ):
        self.status = status
        self.user = user


class ChatMemberBanned(_ChatMemberBase):
    status: Annotated[Literal["banned"], "status"]
    until_date: Annotated[Optional[datetime.datetime], "untilDate"]

    def __init__(
        self,
        status: Annotated[Literal["banned"], "status"],
        user: Annotated["User", "user"],
        *,
        until_date: Annotated[Optional[datetime.datetime], "untilDate"] = None,
    ):
        self.status = status
        self.until_date = until_date
        self.user = user


ChatMember = Union[
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

    def __init__(
        self,
        result_id: Annotated[str, "resultId"],
        from_: Annotated["User", "from"],
        query: Annotated[str, "query"],
        *,
        location: Annotated[Optional["Location"], "location"] = None,
        inline_message_id: Annotated[Optional[str], "inlineMessageId"] = None,
    ):
        self.result_id = result_id
        self.from_ = from_
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query


class _ForwardHeaderCommon(_Type):
    date: Annotated[datetime.datetime, "date"]

    def __init__(
        self,
        date: Annotated[datetime.datetime, "date"],
    ):
        self.date = date


class ForwardHeaderUser(_ForwardHeaderCommon):
    type: Annotated[Literal["user"], "type"]
    user: Annotated["User", "user"]

    def __init__(
        self,
        type: Annotated[Literal["user"], "type"],
        user: Annotated["User", "user"],
        date: Annotated[datetime.datetime, "date"],
    ):
        self.type = type
        self.user = user
        self.date = date

    __discriminators__ = ["type"]


class ForwardHeaderChannel(_ForwardHeaderCommon):
    type: Annotated[Literal["channel"], "type"]
    chat: Annotated["ChatPChannel", "chat"]
    message_id: Annotated[int, "messageId"]
    author_signature: Annotated[Optional[str], "authorSignature"]

    def __init__(
        self,
        type: Annotated[Literal["channel"], "type"],
        chat: Annotated["ChatPChannel", "chat"],
        message_id: Annotated[int, "messageId"],
        date: Annotated[datetime.datetime, "date"],
        *,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
    ):
        self.type = type
        self.chat = chat
        self.message_id = message_id
        self.author_signature = author_signature
        self.date = date

    __discriminators__ = ["type"]


class ForwardHeaderSupergroup(_ForwardHeaderCommon):
    type: Annotated[Literal["supergroup"], "type"]
    chat: Annotated["ChatPSupergroup", "chat"]
    title: Annotated[Optional[str], "title"]

    def __init__(
        self,
        type: Annotated[Literal["supergroup"], "type"],
        chat: Annotated["ChatPSupergroup", "chat"],
        date: Annotated[datetime.datetime, "date"],
        *,
        title: Annotated[Optional[str], "title"] = None,
    ):
        self.type = type
        self.chat = chat
        self.title = title
        self.date = date


class ForwardHeaderHidden(_ForwardHeaderCommon):
    type: Annotated[Literal["hidden"], "type"]
    name: Annotated[str, "name"]

    def __init__(
        self,
        type: Annotated[Literal["hidden"], "type"],
        name: Annotated[str, "name"],
        date: Annotated[datetime.datetime, "date"],
    ):
        self.type = type
        self.name = name
        self.date = date


class ForwardHeaderUnsupported(_ForwardHeaderCommon):
    type: Annotated[Literal["unsupported"], "type"]

    def __init__(
        self,
        type: Annotated[Literal["unsupported"], "type"],
        date: Annotated[datetime.datetime, "date"],
    ):
        self.type = type
        self.date = date


ForwardHeader = Union[
    ForwardHeaderUser,
    ForwardHeaderChannel,
    ForwardHeaderSupergroup,
    ForwardHeaderHidden,
    ForwardHeaderUnsupported,
]


class Game(_Type):
    title: Annotated[str, "title"]
    description: Annotated[str, "description"]
    photo: Annotated["Photo", "photo"]
    text: Annotated[Optional[str], "text"]
    text_entities: Annotated[Optional[list["MessageEntity"]], "textEntities"]
    animation: Annotated[Optional["Animation"], "animation"]

    def __init__(
        self,
        title: Annotated[str, "title"],
        description: Annotated[str, "description"],
        photo: Annotated["Photo", "photo"],
        *,
        text: Annotated[Optional[str], "text"] = None,
        text_entities: Annotated[
            Optional[list["MessageEntity"]], "textEntities"
        ] = None,
        animation: Annotated[Optional["Animation"], "animation"] = None,
    ):
        self.title = title
        self.description = description
        self.photo = photo
        self.text = text
        self.text_entities = text_entities
        self.animation = animation


class InactiveChat(_Type):
    last_activity: Annotated[datetime.datetime, "lastActivity"]
    chat: Annotated["ChatP", "chat"]

    def __init__(
        self,
        last_activity: Annotated[datetime.datetime, "lastActivity"],
        chat: Annotated["ChatP", "chat"],
    ):
        self.last_activity = last_activity
        self.chat = chat


class _InlineKeyboardButtonBase(_Type):
    text: Annotated[str, "text"]

    def __init__(
        self,
        text: Annotated[str, "text"],
    ):
        self.text = text


class InlineKeyboardButtonURL(_InlineKeyboardButtonBase):
    url: Annotated[str, "url"]

    def __init__(
        self,
        url: Annotated[str, "url"],
        text: Annotated[str, "text"],
    ):
        self.url = url
        self.text = text

    __discriminators__ = ["url"]


class InlineKeyboardButtonCallback(_InlineKeyboardButtonBase):
    callback_data: Annotated[str, "callbackData"]

    def __init__(
        self,
        callback_data: Annotated[str, "callbackData"],
        text: Annotated[str, "text"],
    ):
        self.callback_data = callback_data
        self.text = text

    __discriminators__ = ["callbackData"]


class InlineKeyboardButtonMiniApp(_InlineKeyboardButtonBase):
    mini_app: Annotated["MiniAppInfo", "miniApp"]

    def __init__(
        self,
        mini_app: Annotated["MiniAppInfo", "miniApp"],
        text: Annotated[str, "text"],
    ):
        self.mini_app = mini_app
        self.text = text

    __discriminators__ = ["miniApp"]


class InlineKeyboardButtonLogin(_InlineKeyboardButtonBase):
    login_url: Annotated["LoginUrl", "loginUrl"]

    def __init__(
        self,
        login_url: Annotated["LoginUrl", "loginUrl"],
        text: Annotated[str, "text"],
    ):
        self.login_url = login_url
        self.text = text

    __discriminators__ = ["loginUrl"]


class InlineKeyboardButtonSwitchInline(_InlineKeyboardButtonBase):
    switch_inline_query: Annotated[str, "switchInlineQuery"]

    def __init__(
        self,
        switch_inline_query: Annotated[str, "switchInlineQuery"],
        text: Annotated[str, "text"],
    ):
        self.switch_inline_query = switch_inline_query
        self.text = text

    __discriminators__ = ["switchInlineQuery"]


class InlineKeyboardButtonSwitchInlineCurrent(_InlineKeyboardButtonBase):
    switch_inline_query_current_chat: Annotated[str, "switchInlineQueryCurrentChat"]

    def __init__(
        self,
        switch_inline_query_current_chat: Annotated[
            str, "switchInlineQueryCurrentChat"
        ],
        text: Annotated[str, "text"],
    ):
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.text = text

    __discriminators__ = ["switchInlineQueryCurrentChat"]


class InlineKeyboardButtonSwitchInlineChosen(_InlineKeyboardButtonBase):
    switch_inline_query_chosen_chats: Annotated[Any, "switchInlineQueryChosenChats"]

    def __init__(
        self,
        switch_inline_query_chosen_chats: Annotated[
            Any, "switchInlineQueryChosenChats"
        ],
        text: Annotated[str, "text"],
    ):
        self.switch_inline_query_chosen_chats = switch_inline_query_chosen_chats
        self.text = text

    __discriminators__ = ["switchInlineQueryChosenChats"]


class InlineKeyboardButtonGame(_InlineKeyboardButtonBase):
    callback_game: Annotated[dict[str, Any], "callbackGame"]

    def __init__(
        self,
        callback_game: Annotated[dict[str, Any], "callbackGame"],
        text: Annotated[str, "text"],
    ):
        self.callback_game = callback_game
        self.text = text

    __discriminators__ = ["callbackGame"]


class InlineKeyboardButtonPay(_InlineKeyboardButtonBase):
    pay: Annotated[bool, "pay"]

    def __init__(
        self,
        pay: Annotated[bool, "pay"],
        text: Annotated[str, "text"],
    ):
        self.pay = pay
        self.text = text

    __discriminators__ = ["pay"]


class InlineKeyboardButtonCopy(_InlineKeyboardButtonBase):
    copy: Annotated[str, "copy"]

    def __init__(
        self,
        copy: Annotated[str, "copy"],
        text: Annotated[str, "text"],
    ):
        self.copy = copy
        self.text = text

    __discriminators__ = ["copy"]


InlineKeyboardButton = Union[
    InlineKeyboardButtonURL,
    InlineKeyboardButtonCallback,
    InlineKeyboardButtonMiniApp,
    InlineKeyboardButtonLogin,
    InlineKeyboardButtonSwitchInline,
    InlineKeyboardButtonSwitchInlineCurrent,
    InlineKeyboardButtonSwitchInlineChosen,
    InlineKeyboardButtonGame,
    InlineKeyboardButtonPay,
    InlineKeyboardButtonCopy,
]


class InlineQuery(_Type):
    id: Annotated[str, "id"]
    from_: Annotated["User", "from"]
    query: Annotated[str, "query"]
    offset: Annotated[str, "offset"]
    chat_type: Annotated[Optional[Any], "chatType"]
    location: Annotated[Optional["Location"], "location"]

    def __init__(
        self,
        id: Annotated[str, "id"],
        from_: Annotated["User", "from"],
        query: Annotated[str, "query"],
        offset: Annotated[str, "offset"],
        *,
        chat_type: Annotated[Optional[Any], "chatType"] = None,
        location: Annotated[Optional["Location"], "location"] = None,
    ):
        self.id = id
        self.from_ = from_
        self.query = query
        self.offset = offset
        self.chat_type = chat_type
        self.location = location

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
    subscription_price: Annotated[Optional[int], "subscriptionPrice"]
    subscription_expires_in: Annotated[Optional[int], "subscriptionExpiresIn"]

    def __init__(
        self,
        invite_link: Annotated[str, "inviteLink"],
        creator: Annotated["User", "creator"],
        requires_approval: Annotated[bool, "requiresApproval"],
        revoked: Annotated[bool, "revoked"],
        *,
        title: Annotated[Optional[str], "title"] = None,
        expires_at: Annotated[Optional[datetime.datetime], "expiresAt"] = None,
        limit: Annotated[Optional[int], "limit"] = None,
        pending_join_request_count: Annotated[
            Optional[int], "pendingJoinRequestCount"
        ] = None,
        subscription_price: Annotated[Optional[int], "subscriptionPrice"] = None,
        subscription_expires_in: Annotated[
            Optional[int], "subscriptionExpiresIn"
        ] = None,
    ):
        self.invite_link = invite_link
        self.creator = creator
        self.requires_approval = requires_approval
        self.revoked = revoked
        self.title = title
        self.expires_at = expires_at
        self.limit = limit
        self.pending_join_request_count = pending_join_request_count
        self.subscription_price = subscription_price
        self.subscription_expires_in = subscription_expires_in


class MessageInteractions(_Type):
    chat_id: Annotated[int, "chatId"]
    message_id: Annotated[int, "messageId"]
    reactions: Annotated[list["MessageReaction"], "reactions"]
    views: Annotated[int, "views"]
    forwards: Annotated[int, "forwards"]

    def __init__(
        self,
        chat_id: Annotated[int, "chatId"],
        message_id: Annotated[int, "messageId"],
        reactions: Annotated[list["MessageReaction"], "reactions"],
        views: Annotated[int, "views"],
        forwards: Annotated[int, "forwards"],
    ):
        self.chat_id = chat_id
        self.message_id = message_id
        self.reactions = reactions
        self.views = views
        self.forwards = forwards


class MessageReactionCount(_Type):
    chat: Annotated["ChatP", "chat"]
    message_id: Annotated[int, "messageId"]
    date: Annotated[datetime.datetime, "date"]
    reactions: Annotated[list["ReactionCount"], "reactions"]

    def __init__(
        self,
        chat: Annotated["ChatP", "chat"],
        message_id: Annotated[int, "messageId"],
        date: Annotated[datetime.datetime, "date"],
        reactions: Annotated[list["ReactionCount"], "reactions"],
    ):
        self.chat = chat
        self.message_id = message_id
        self.date = date
        self.reactions = reactions


class MessageReactions(_Type):
    chat: Annotated["ChatP", "chat"]
    message_id: Annotated[int, "messageId"]
    user: Annotated[Optional["User"], "user"]
    actor_chat: Annotated[Optional["ChatP"], "actorChat"]
    date: Annotated[datetime.datetime, "date"]
    old_reactions: Annotated[list["Reaction"], "oldReactions"]
    new_reactions: Annotated[list["Reaction"], "newReactions"]

    def __init__(
        self,
        chat: Annotated["ChatP", "chat"],
        message_id: Annotated[int, "messageId"],
        date: Annotated[datetime.datetime, "date"],
        old_reactions: Annotated[list["Reaction"], "oldReactions"],
        new_reactions: Annotated[list["Reaction"], "newReactions"],
        *,
        user: Annotated[Optional["User"], "user"] = None,
        actor_chat: Annotated[Optional["ChatP"], "actorChat"] = None,
    ):
        self.chat = chat
        self.message_id = message_id
        self.user = user
        self.actor_chat = actor_chat
        self.date = date
        self.old_reactions = old_reactions
        self.new_reactions = new_reactions


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

    def __init__(
        self,
        id: Annotated[str, "id"],
        question: Annotated[str, "question"],
        question_entities: Annotated[list["MessageEntity"], "questionEntities"],
        options: Annotated[list["PollOption"], "options"],
        total_voter_count: Annotated[int, "totalVoterCount"],
        is_closed: Annotated[bool, "isClosed"],
        is_anonymous: Annotated[bool, "isAnonymous"],
        type: Annotated[Any, "type"],
        *,
        allow_multiple_answers: Annotated[
            Optional[bool], "allowMultipleAnswers"
        ] = None,
        correct_option_index: Annotated[Optional[int], "correctOptionIndex"] = None,
        explanation: Annotated[Optional[str], "explanation"] = None,
        explanation_entities: Annotated[
            Optional[list["MessageEntity"]], "explanationEntities"
        ] = None,
        open_period: Annotated[Optional[int], "openPeriod"] = None,
        close_date: Annotated[Optional[datetime.datetime], "closeDate"] = None,
    ):
        self.id = id
        self.question = question
        self.question_entities = question_entities
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allow_multiple_answers = allow_multiple_answers
        self.correct_option_index = correct_option_index
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date


class PreCheckoutQuery(_Type):
    id: Annotated[str, "id"]
    from_: Annotated["User", "from"]
    currency: Annotated[str, "currency"]
    total_amount: Annotated[int, "totalAmount"]
    invoice_payload: Annotated[str, "invoicePayload"]
    shipping_option_id: Annotated[Optional[str], "shippingOptionId"]
    order_info: Annotated[Optional["OrderInfo"], "orderInfo"]

    def __init__(
        self,
        id: Annotated[str, "id"],
        from_: Annotated["User", "from"],
        currency: Annotated[str, "currency"],
        total_amount: Annotated[int, "totalAmount"],
        invoice_payload: Annotated[str, "invoicePayload"],
        *,
        shipping_option_id: Annotated[Optional[str], "shippingOptionId"] = None,
        order_info: Annotated[Optional["OrderInfo"], "orderInfo"] = None,
    ):
        self.id = id
        self.from_ = from_
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info


class ReplyToMessage(_Type):
    message_id: Annotated[int, "messageId"]
    quote: Annotated[Optional["ReplyQuote"], "quote"]

    def __init__(
        self,
        message_id: Annotated[int, "messageId"],
        *,
        quote: Annotated[Optional["ReplyQuote"], "quote"] = None,
    ):
        self.message_id = message_id
        self.quote = quote

    __discriminators__ = ["messageId"]


class ReplyToStory(_Type):
    chat_id: Annotated["ID", "chatId"]
    story_id: Annotated[int, "storyId"]

    def __init__(
        self,
        chat_id: Annotated["ID", "chatId"],
        story_id: Annotated[int, "storyId"],
    ):
        self.chat_id = chat_id
        self.story_id = story_id

    __discriminators__ = ["storyId"]


ReplyTo = Union[ReplyToMessage, ReplyToStory]


class StoryContentPhoto(_Type):
    photo: Annotated["Photo", "photo"]

    def __init__(
        self,
        photo: Annotated["Photo", "photo"],
    ):
        self.photo = photo

    __discriminators__ = ["photo"]


class StoryContentVideo(_Type):
    video: Annotated["Video", "video"]

    def __init__(
        self,
        video: Annotated["Video", "video"],
    ):
        self.video = video

    __discriminators__ = ["video"]


class StoryContentUnsupported(_Type):
    unsupported: Annotated[Literal[True], "unsupported"]

    def __init__(
        self,
        unsupported: Annotated[Literal[True], "unsupported"],
    ):
        self.unsupported = unsupported

    __discriminators__ = ["unsupported"]


StoryContent = Union[StoryContentPhoto, StoryContentVideo, StoryContentUnsupported]


class StoryInteractions(_Type):
    reactions: Annotated[Optional[list["StoryReaction"]], "reactions"]
    reaction_count: Annotated[Optional[int], "reactionCount"]
    views: Annotated[int, "views"]
    forwards: Annotated[int, "forwards"]

    def __init__(
        self,
        views: Annotated[int, "views"],
        forwards: Annotated[int, "forwards"],
        *,
        reactions: Annotated[Optional[list["StoryReaction"]], "reactions"] = None,
        reaction_count: Annotated[Optional[int], "reactionCount"] = None,
    ):
        self.reactions = reactions
        self.reaction_count = reaction_count
        self.views = views
        self.forwards = forwards


class StoryInteractiveAreaPosition(_Type):
    x_percentage: Annotated[int, "xPercentage"]
    y_percentage: Annotated[int, "yPercentage"]
    width_percentage: Annotated[int, "widthPercentage"]
    height_percentage: Annotated[int, "heightPercentage"]
    rotation_angle: Annotated[int, "rotationAngle"]

    def __init__(
        self,
        x_percentage: Annotated[int, "xPercentage"],
        y_percentage: Annotated[int, "yPercentage"],
        width_percentage: Annotated[int, "widthPercentage"],
        height_percentage: Annotated[int, "heightPercentage"],
        rotation_angle: Annotated[int, "rotationAngle"],
    ):
        self.x_percentage = x_percentage
        self.y_percentage = y_percentage
        self.width_percentage = width_percentage
        self.height_percentage = height_percentage
        self.rotation_angle = rotation_angle


class _StoryInteractiveAreaPositionCommon(_Type):
    position: Annotated["StoryInteractiveAreaPosition", "position"]

    def __init__(
        self,
        position: Annotated["StoryInteractiveAreaPosition", "position"],
    ):
        self.position = position


class StoryInteractiveAreaLocation(_StoryInteractiveAreaPositionCommon):
    location: Annotated["Location", "location"]

    def __init__(
        self,
        location: Annotated["Location", "location"],
        position: Annotated["StoryInteractiveAreaPosition", "position"],
    ):
        self.location = location
        self.position = position


class StoryInteractiveAreaVenue(_StoryInteractiveAreaPositionCommon):
    venue: Annotated["Venue", "venue"]

    def __init__(
        self,
        venue: Annotated["Venue", "venue"],
        position: Annotated["StoryInteractiveAreaPosition", "position"],
    ):
        self.venue = venue
        self.position = position


class StoryInteractiveAreaReaction(_StoryInteractiveAreaPositionCommon):
    reaction: Annotated["Reaction", "reaction"]
    count: Annotated[Optional[int], "count"]
    dark: Annotated[Optional[bool], "dark"]
    flipped: Annotated[Optional[bool], "flipped"]

    def __init__(
        self,
        reaction: Annotated["Reaction", "reaction"],
        position: Annotated["StoryInteractiveAreaPosition", "position"],
        *,
        count: Annotated[Optional[int], "count"] = None,
        dark: Annotated[Optional[bool], "dark"] = None,
        flipped: Annotated[Optional[bool], "flipped"] = None,
    ):
        self.reaction = reaction
        self.count = count
        self.dark = dark
        self.flipped = flipped
        self.position = position


class StoryInteractiveAreaMessage(_StoryInteractiveAreaPositionCommon):
    message_reference: Annotated["MessageReference", "messageReference"]

    def __init__(
        self,
        message_reference: Annotated["MessageReference", "messageReference"],
        position: Annotated["StoryInteractiveAreaPosition", "position"],
    ):
        self.message_reference = message_reference
        self.position = position


StoryInteractiveArea = Union[
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

    def __init__(
        self,
        currency: Annotated[str, "currency"],
        total_amount: Annotated[int, "totalAmount"],
        invoice_payload: Annotated[str, "invoicePayload"],
        telegram_payment_charge_id: Annotated[str, "telegramPaymentChargeId"],
        provider_payment_charge_id: Annotated[str, "providerPaymentChargeId"],
        *,
        shipping_option_id: Annotated[Optional[str], "shippingOptionId"] = None,
        order_info: Annotated[Optional["OrderInfo"], "orderInfo"] = None,
    ):
        self.currency = currency
        self.total_amount = total_amount
        self.invoice_payload = invoice_payload
        self.telegram_payment_charge_id = telegram_payment_charge_id
        self.provider_payment_charge_id = provider_payment_charge_id
        self.shipping_option_id = shipping_option_id
        self.order_info = order_info


class ChatMemberUpdated(_Type):
    chat: Annotated["ChatP", "chat"]
    from_: Annotated["User", "from"]
    date: Annotated[datetime.datetime, "date"]
    old_chat_member: Annotated["ChatMember", "oldChatMember"]
    new_chat_member: Annotated["ChatMember", "newChatMember"]
    invite_link: Annotated[Optional["InviteLink"], "inviteLink"]
    via_shared_folder: Annotated[Optional[bool], "viaSharedFolder"]

    def __init__(
        self,
        chat: Annotated["ChatP", "chat"],
        from_: Annotated["User", "from"],
        date: Annotated[datetime.datetime, "date"],
        old_chat_member: Annotated["ChatMember", "oldChatMember"],
        new_chat_member: Annotated["ChatMember", "newChatMember"],
        *,
        invite_link: Annotated[Optional["InviteLink"], "inviteLink"] = None,
        via_shared_folder: Annotated[Optional[bool], "viaSharedFolder"] = None,
    ):
        self.chat = chat
        self.from_ = from_
        self.date = date
        self.old_chat_member = old_chat_member
        self.new_chat_member = new_chat_member
        self.invite_link = invite_link
        self.via_shared_folder = via_shared_folder


class JoinRequest(_Type):
    chat: Annotated["ChatP", "chat"]
    user: Annotated["User", "user"]
    date: Annotated[datetime.datetime, "date"]
    bio: Annotated[Optional[str], "bio"]
    invite_link: Annotated[Optional["InviteLink"], "inviteLink"]

    def __init__(
        self,
        chat: Annotated["ChatP", "chat"],
        user: Annotated["User", "user"],
        date: Annotated[datetime.datetime, "date"],
        *,
        bio: Annotated[Optional[str], "bio"] = None,
        invite_link: Annotated[Optional["InviteLink"], "inviteLink"] = None,
    ):
        self.chat = chat
        self.user = user
        self.date = date
        self.bio = bio
        self.invite_link = invite_link


class ReplyMarkupInlineKeyboard(_Type):
    inline_keyboard: Annotated[list[list["InlineKeyboardButton"]], "inlineKeyboard"]

    def __init__(
        self,
        inline_keyboard: Annotated[
            list[list["InlineKeyboardButton"]], "inlineKeyboard"
        ],
    ):
        self.inline_keyboard = inline_keyboard

    __discriminators__ = ["inlineKeyboard"]


class ReplyMarkupKeyboard(_Type):
    keyboard: Annotated[list[list["KeyboardButton"]], "keyboard"]
    is_persistent: Annotated[Optional[bool], "isPersistent"]
    resize_keyboard: Annotated[Optional[bool], "resizeKeyboard"]
    one_time_keyboard: Annotated[Optional[bool], "oneTimeKeyboard"]
    input_field_placeholder: Annotated[Optional[str], "inputFieldPlaceholder"]
    selective: Annotated[Optional[bool], "selective"]

    def __init__(
        self,
        keyboard: Annotated[list[list["KeyboardButton"]], "keyboard"],
        *,
        is_persistent: Annotated[Optional[bool], "isPersistent"] = None,
        resize_keyboard: Annotated[Optional[bool], "resizeKeyboard"] = None,
        one_time_keyboard: Annotated[Optional[bool], "oneTimeKeyboard"] = None,
        input_field_placeholder: Annotated[
            Optional[str], "inputFieldPlaceholder"
        ] = None,
        selective: Annotated[Optional[bool], "selective"] = None,
    ):
        self.keyboard = keyboard
        self.is_persistent = is_persistent
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    __discriminators__ = ["keyboard"]


class ReplyMarkupRemoveKeyboard(_Type):
    remove_keyboard: Annotated[Literal[True], "removeKeyboard"]
    selective: Annotated[Optional[bool], "selective"]

    def __init__(
        self,
        remove_keyboard: Annotated[Literal[True], "removeKeyboard"],
        *,
        selective: Annotated[Optional[bool], "selective"] = None,
    ):
        self.remove_keyboard = remove_keyboard
        self.selective = selective

    __discriminators__ = ["removeKeyboard"]


class ReplyMarkupForceReply(_Type):
    force_reply: Annotated[Literal[True], "forceReply"]
    input_field_placeholder: Annotated[Optional[str], "inputFieldPlaceholder"]
    selective: Annotated[Optional[bool], "selective"]

    def __init__(
        self,
        force_reply: Annotated[Literal[True], "forceReply"],
        *,
        input_field_placeholder: Annotated[
            Optional[str], "inputFieldPlaceholder"
        ] = None,
        selective: Annotated[Optional[bool], "selective"] = None,
    ):
        self.force_reply = force_reply
        self.input_field_placeholder = input_field_placeholder
        self.selective = selective

    __discriminators__ = ["forceReply"]


ReplyMarkup = Union[
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

    def __init__(
        self,
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        chat: Annotated["ChatP", "chat"],
        date: Annotated[datetime.datetime, "date"],
        edited: Annotated[bool, "edited"],
        content: Annotated["StoryContent", "content"],
        interactive_areas: Annotated[list["StoryInteractiveArea"], "interactiveAreas"],
        highlighted: Annotated[bool, "highlighted"],
        *,
        interactions: Annotated[Optional["StoryInteractions"], "interactions"] = None,
        privacy: Annotated[Optional["StoryPrivacy"], "privacy"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
    ):
        self.out = out
        self.id = id
        self.chat = chat
        self.date = date
        self.edited = edited
        self.content = content
        self.interactive_areas = interactive_areas
        self.highlighted = highlighted
        self.interactions = interactions
        self.privacy = privacy
        self.caption = caption
        self.caption_entities = caption_entities


InlineQueryResultType = Union[
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

    def __init__(
        self,
        type: Annotated["InlineQueryResultType", "type"],
        id: Annotated[str, "id"],
    ):
        self.type = type
        self.id = id


class _InlineQueryResultCaptionCommon(_Type):
    caption: Annotated[Optional[str], "caption"]
    parse_mode: Annotated[Optional["ParseMode"], "parseMode"]
    caption_entities: Annotated[Optional[list["MessageEntity"]], "captionEntities"]

    def __init__(
        self,
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
    ):
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities


class _InlineQueryResultMessageContentReplyMarkupCommon(_Type):
    message_content: Annotated[Optional["MessageContent"], "messageContent"]
    reply_markup: Annotated[Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"]

    def __init__(
        self,
        *,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.message_content = message_content
        self.reply_markup = reply_markup


class _InlineQueryResultThumbnailCommon(_Type):
    thumbnail_url: Annotated[Optional[str], "thumbnailUrl"]
    thumbnail_width: Annotated[Optional[str], "thumbnailWidth"]
    thumbnail_height: Annotated[Optional[str], "thumbnailHeight"]

    def __init__(
        self,
        *,
        thumbnail_url: Annotated[Optional[str], "thumbnailUrl"] = None,
        thumbnail_width: Annotated[Optional[str], "thumbnailWidth"] = None,
        thumbnail_height: Annotated[Optional[str], "thumbnailHeight"] = None,
    ):
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height


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

    def __init__(
        self,
        type: Annotated[Literal["article"], "type"],
        title: Annotated[str, "title"],
        message_content: Annotated["MessageContent", "messageContent"],
        id: Annotated[str, "id"],
        *,
        description: Annotated[Optional[str], "description"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
        url: Annotated[Optional[str], "url"] = None,
        hide_url: Annotated[Optional[bool], "hideUrl"] = None,
        thumbnail_url: Annotated[Optional[str], "thumbnailUrl"] = None,
        thumbnail_width: Annotated[Optional[str], "thumbnailWidth"] = None,
        thumbnail_height: Annotated[Optional[str], "thumbnailHeight"] = None,
    ):
        self.type = type
        self.title = title
        self.message_content = message_content
        self.description = description
        self.reply_markup = reply_markup
        self.url = url
        self.hide_url = hide_url
        self.id = id
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

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

    def __init__(
        self,
        type: Annotated[Literal["audio"], "type"],
        title: Annotated[str, "title"],
        url: Annotated[str, "url"],
        id: Annotated[str, "id"],
        *,
        performer: Annotated[Optional[str], "performer"] = None,
        audio_duration: Annotated[Optional[int], "audioDuration"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.title = title
        self.url = url
        self.performer = performer
        self.audio_duration = audio_duration
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

    __discriminators__ = ["type"]


class InlineQueryResultCachedAudio(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["audio"], "type"]
    file_id: Annotated[str, "fileId"]

    def __init__(
        self,
        type: Annotated[Literal["audio"], "type"],
        file_id: Annotated[str, "fileId"],
        id: Annotated[str, "id"],
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.file_id = file_id
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedDocument(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["document"], "type"]
    file_id: Annotated[str, "fileId"]
    description: Annotated[Optional[str], "description"]

    def __init__(
        self,
        type: Annotated[Literal["document"], "type"],
        file_id: Annotated[str, "fileId"],
        id: Annotated[str, "id"],
        *,
        description: Annotated[Optional[str], "description"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.file_id = file_id
        self.description = description
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedGif(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["gif"], "type"]
    file_id: Annotated[str, "fileId"]
    title: Annotated[Optional[str], "title"]

    def __init__(
        self,
        type: Annotated[Literal["gif"], "type"],
        file_id: Annotated[str, "fileId"],
        id: Annotated[str, "id"],
        *,
        title: Annotated[Optional[str], "title"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.file_id = file_id
        self.title = title
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedMpeg4Gif(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["mpeg4Gif"], "type"]
    file_id: Annotated[str, "fileId"]
    title: Annotated[Optional[str], "title"]

    def __init__(
        self,
        type: Annotated[Literal["mpeg4Gif"], "type"],
        file_id: Annotated[str, "fileId"],
        id: Annotated[str, "id"],
        *,
        title: Annotated[Optional[str], "title"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.file_id = file_id
        self.title = title
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

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

    def __init__(
        self,
        type: Annotated[Literal["photo"], "type"],
        file_id: Annotated[str, "fileId"],
        id: Annotated[str, "id"],
        *,
        thumbnails: Annotated[Optional[list["Thumbnail"]], "thumbnails"] = None,
        title: Annotated[Optional[str], "title"] = None,
        description: Annotated[Optional[str], "description"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.file_id = file_id
        self.thumbnails = thumbnails
        self.title = title
        self.description = description
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedSticker(
    _InlineQueryResultBase, _InlineQueryResultMessageContentReplyMarkupCommon
):
    type: Annotated[Literal["sticker"], "type"]
    file_id: Annotated[str, "fileId"]

    def __init__(
        self,
        type: Annotated[Literal["sticker"], "type"],
        file_id: Annotated[str, "fileId"],
        id: Annotated[str, "id"],
        *,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.file_id = file_id
        self.id = id
        self.message_content = message_content
        self.reply_markup = reply_markup

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

    def __init__(
        self,
        type: Annotated[Literal["video"], "type"],
        title: Annotated[str, "title"],
        file_id: Annotated[str, "fileId"],
        id: Annotated[str, "id"],
        *,
        description: Annotated[Optional[str], "description"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.title = title
        self.file_id = file_id
        self.description = description
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

    __discriminators__ = ["type", "fileId"]


class InlineQueryResultCachedVoice(
    _InlineQueryResultBase,
    _InlineQueryResultCaptionCommon,
    _InlineQueryResultMessageContentReplyMarkupCommon,
):
    type: Annotated[Literal["voice"], "type"]
    title: Annotated[str, "title"]
    file_id: Annotated[str, "fileId"]

    def __init__(
        self,
        type: Annotated[Literal["voice"], "type"],
        title: Annotated[str, "title"],
        file_id: Annotated[str, "fileId"],
        id: Annotated[str, "id"],
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.title = title
        self.file_id = file_id
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

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

    def __init__(
        self,
        type: Annotated[Literal["game"], "type"],
        phone_number: Annotated[str, "phoneNumber"],
        first_name: Annotated[str, "firstName"],
        id: Annotated[str, "id"],
        *,
        last_name: Annotated[Optional[str], "lastName"] = None,
        vcard: Annotated[Optional[str], "vcard"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
        thumbnail_url: Annotated[Optional[str], "thumbnailUrl"] = None,
        thumbnail_width: Annotated[Optional[str], "thumbnailWidth"] = None,
        thumbnail_height: Annotated[Optional[str], "thumbnailHeight"] = None,
    ):
        self.type = type
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.vcard = vcard
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

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

    def __init__(
        self,
        type: Annotated[Literal["document"], "type"],
        title: Annotated[str, "title"],
        url: Annotated[str, "url"],
        id: Annotated[str, "id"],
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
        thumbnail_url: Annotated[Optional[str], "thumbnailUrl"] = None,
        thumbnail_width: Annotated[Optional[str], "thumbnailWidth"] = None,
        thumbnail_height: Annotated[Optional[str], "thumbnailHeight"] = None,
    ):
        self.type = type
        self.title = title
        self.url = url
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

    __discriminators__ = ["type", "url"]


class InlineQueryResultGame(_InlineQueryResultBase):
    type: Annotated[Literal["game"], "type"]
    game_short_name: Annotated[str, "gameShortName"]
    reply_markup: Annotated[Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"]

    def __init__(
        self,
        type: Annotated[Literal["game"], "type"],
        game_short_name: Annotated[str, "gameShortName"],
        id: Annotated[str, "id"],
        *,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.game_short_name = game_short_name
        self.reply_markup = reply_markup
        self.id = id

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

    def __init__(
        self,
        type: Annotated[Literal["gif"], "type"],
        url: Annotated[str, "url"],
        id: Annotated[str, "id"],
        *,
        title: Annotated[Optional[str], "title"] = None,
        width: Annotated[Optional[int], "width"] = None,
        height: Annotated[Optional[int], "height"] = None,
        duration: Annotated[Optional[int], "duration"] = None,
        thumbnail_url: Annotated[Optional[str], "thumbnailUrl"] = None,
        thumbnail_mime_type: Annotated[Optional[str], "thumbnailMimeType"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.title = title
        self.url = url
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail_url = thumbnail_url
        self.thumbnail_mime_type = thumbnail_mime_type
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

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

    def __init__(
        self,
        type: Annotated[Literal["location"], "type"],
        title: Annotated[str, "title"],
        latitude: Annotated[int, "latitude"],
        longitude: Annotated[int, "longitude"],
        id: Annotated[str, "id"],
        *,
        horizontal_accuracy: Annotated[Optional[int], "horizontalAccuracy"] = None,
        live_period: Annotated[Optional[int], "livePeriod"] = None,
        heading: Annotated[Optional[int], "heading"] = None,
        proximity_alert_radius: Annotated[Optional[int], "proximityAlertRadius"] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
        thumbnail_url: Annotated[Optional[str], "thumbnailUrl"] = None,
        thumbnail_width: Annotated[Optional[str], "thumbnailWidth"] = None,
        thumbnail_height: Annotated[Optional[str], "thumbnailHeight"] = None,
    ):
        self.type = type
        self.title = title
        self.latitude = latitude
        self.longitude = longitude
        self.horizontal_accuracy = horizontal_accuracy
        self.live_period = live_period
        self.heading = heading
        self.proximity_alert_radius = proximity_alert_radius
        self.id = id
        self.message_content = message_content
        self.reply_markup = reply_markup
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

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

    def __init__(
        self,
        type: Annotated[Literal["mpeg4Gif"], "type"],
        url: Annotated[str, "url"],
        id: Annotated[str, "id"],
        *,
        title: Annotated[Optional[str], "title"] = None,
        width: Annotated[Optional[int], "width"] = None,
        height: Annotated[Optional[int], "height"] = None,
        duration: Annotated[Optional[int], "duration"] = None,
        thumbnail_url: Annotated[Optional[str], "thumbnailUrl"] = None,
        thumbnail_mime_type: Annotated[Optional[str], "thumbnailMimeType"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.url = url
        self.title = title
        self.width = width
        self.height = height
        self.duration = duration
        self.thumbnail_url = thumbnail_url
        self.thumbnail_mime_type = thumbnail_mime_type
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

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

    def __init__(
        self,
        type: Annotated[Literal["photo"], "type"],
        url: Annotated[str, "url"],
        thumbnail_url: Annotated[str, "thumbnailUrl"],
        id: Annotated[str, "id"],
        *,
        title: Annotated[Optional[str], "title"] = None,
        description: Annotated[Optional[str], "description"] = None,
        width: Annotated[Optional[int], "width"] = None,
        height: Annotated[Optional[int], "height"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.url = url
        self.thumbnail_url = thumbnail_url
        self.title = title
        self.description = description
        self.width = width
        self.height = height
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

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

    def __init__(
        self,
        type: Annotated[Literal["venue"], "type"],
        title: Annotated[str, "title"],
        latitude: Annotated[int, "latitude"],
        longitude: Annotated[int, "longitude"],
        address: Annotated[str, "address"],
        id: Annotated[str, "id"],
        *,
        foursquare_id: Annotated[Optional[str], "foursquareId"] = None,
        foursquare_type: Annotated[Optional[str], "foursquareType"] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
        thumbnail_url: Annotated[Optional[str], "thumbnailUrl"] = None,
        thumbnail_width: Annotated[Optional[str], "thumbnailWidth"] = None,
        thumbnail_height: Annotated[Optional[str], "thumbnailHeight"] = None,
    ):
        self.type = type
        self.title = title
        self.latitude = latitude
        self.longitude = longitude
        self.address = address
        self.foursquare_id = foursquare_id
        self.foursquare_type = foursquare_type
        self.id = id
        self.message_content = message_content
        self.reply_markup = reply_markup
        self.thumbnail_url = thumbnail_url
        self.thumbnail_width = thumbnail_width
        self.thumbnail_height = thumbnail_height

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

    def __init__(
        self,
        type: Annotated[Literal["video"], "type"],
        title: Annotated[str, "title"],
        url: Annotated[str, "url"],
        mime_type: Annotated[str, "mimeType"],
        thumbnail_url: Annotated[str, "thumbnailUrl"],
        id: Annotated[str, "id"],
        *,
        description: Annotated[Optional[str], "description"] = None,
        width: Annotated[Optional[int], "width"] = None,
        height: Annotated[Optional[int], "height"] = None,
        video_duration: Annotated[Optional[int], "videoDuration"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.title = title
        self.description = description
        self.url = url
        self.mime_type = mime_type
        self.thumbnail_url = thumbnail_url
        self.width = width
        self.height = height
        self.video_duration = video_duration
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

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

    def __init__(
        self,
        type: Annotated[Literal["voice"], "type"],
        title: Annotated[str, "title"],
        url: Annotated[str, "url"],
        id: Annotated[str, "id"],
        *,
        voice_duration: Annotated[Optional[int], "voiceDuration"] = None,
        caption: Annotated[Optional[str], "caption"] = None,
        parse_mode: Annotated[Optional["ParseMode"], "parseMode"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        message_content: Annotated[Optional["MessageContent"], "messageContent"] = None,
        reply_markup: Annotated[
            Optional["ReplyMarkupInlineKeyboard"], "replyMarkup"
        ] = None,
    ):
        self.type = type
        self.title = title
        self.url = url
        self.voice_duration = voice_duration
        self.id = id
        self.caption = caption
        self.parse_mode = parse_mode
        self.caption_entities = caption_entities
        self.message_content = message_content
        self.reply_markup = reply_markup

    __discriminators__ = ["type", "url"]


InlineQueryResult = Union[
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
    forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"]
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
    effect_id: Annotated[Optional[str], "effectId"]
    scheduled: Annotated[Optional[bool], "scheduled"]

    def __init__(
        self,
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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
            reply_to=ReplyToMessage(message_id=self.id, quote=reply_quote),
            protect_content=protect_content,
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

    @property
    def message_link(self) -> Optional[str]:
        if self.chat.type == "private":
            return None
        elif not getattr(self.chat, "username", None):
            return "https://t.me/c/{}/{}".format(
                str(self.chat.id).replace("-100", ""), self.id
            )
        else:
            return "https://t.me/{}/{}".format(getattr(self.chat, "username"), self.id)


class _MessageMediaBase(_MessageBase):
    caption: Annotated[Optional[str], "caption"]
    caption_entities: Annotated[Optional[list["MessageEntity"]], "captionEntities"]
    has_media_spoiler: Annotated[Optional[bool], "hasMediaSpoiler"]

    def __init__(
        self,
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        has_media_spoiler: Annotated[Optional[bool], "hasMediaSpoiler"] = None,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.caption = caption
        self.caption_entities = caption_entities
        self.has_media_spoiler = has_media_spoiler
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled


class MessageText(_MessageBase):
    text: Annotated[str, "text"]
    entities: Annotated[list["MessageEntity"], "entities"]
    link_preview: Annotated[Optional["LinkPreview"], "linkPreview"]

    def __init__(
        self,
        text: Annotated[str, "text"],
        entities: Annotated[list["MessageEntity"], "entities"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        link_preview: Annotated[Optional["LinkPreview"], "linkPreview"] = None,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.text = text
        self.entities = entities
        self.link_preview = link_preview
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["text", "entities"]


class MessageLink(_MessageBase):
    link_preview: Annotated[Any, "linkPreview"]

    def __init__(
        self,
        link_preview: Annotated[Any, "linkPreview"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.link_preview = link_preview
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["linkPreview"]


class MessagePhoto(_MessageMediaBase):
    photo: Annotated["Photo", "photo"]

    def __init__(
        self,
        photo: Annotated["Photo", "photo"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        has_media_spoiler: Annotated[Optional[bool], "hasMediaSpoiler"] = None,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.photo = photo
        self.caption = caption
        self.caption_entities = caption_entities
        self.has_media_spoiler = has_media_spoiler
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["photo"]


class MessageDocument(_MessageMediaBase):
    document: Annotated["Document", "document"]

    def __init__(
        self,
        document: Annotated["Document", "document"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        has_media_spoiler: Annotated[Optional[bool], "hasMediaSpoiler"] = None,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.document = document
        self.caption = caption
        self.caption_entities = caption_entities
        self.has_media_spoiler = has_media_spoiler
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["document"]


class MessageVideo(_MessageMediaBase):
    video: Annotated["Video", "video"]

    def __init__(
        self,
        video: Annotated["Video", "video"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        has_media_spoiler: Annotated[Optional[bool], "hasMediaSpoiler"] = None,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.video = video
        self.caption = caption
        self.caption_entities = caption_entities
        self.has_media_spoiler = has_media_spoiler
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["video"]


class MessageSticker(_MessageBase):
    sticker: Annotated["Sticker", "sticker"]

    def __init__(
        self,
        sticker: Annotated["Sticker", "sticker"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.sticker = sticker
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["sticker"]


class MessageAnimation(_MessageMediaBase):
    animation: Annotated["Animation", "animation"]

    def __init__(
        self,
        animation: Annotated["Animation", "animation"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        has_media_spoiler: Annotated[Optional[bool], "hasMediaSpoiler"] = None,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.animation = animation
        self.caption = caption
        self.caption_entities = caption_entities
        self.has_media_spoiler = has_media_spoiler
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["animation"]


class MessageVoice(_MessageMediaBase):
    voice: Annotated["Voice", "voice"]

    def __init__(
        self,
        voice: Annotated["Voice", "voice"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        has_media_spoiler: Annotated[Optional[bool], "hasMediaSpoiler"] = None,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.voice = voice
        self.caption = caption
        self.caption_entities = caption_entities
        self.has_media_spoiler = has_media_spoiler
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["voice"]


class MessageAudio(_MessageMediaBase):
    audio: Annotated["Audio", "audio"]

    def __init__(
        self,
        audio: Annotated["Audio", "audio"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        caption: Annotated[Optional[str], "caption"] = None,
        caption_entities: Annotated[
            Optional[list["MessageEntity"]], "captionEntities"
        ] = None,
        has_media_spoiler: Annotated[Optional[bool], "hasMediaSpoiler"] = None,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.audio = audio
        self.caption = caption
        self.caption_entities = caption_entities
        self.has_media_spoiler = has_media_spoiler
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["audio"]


class MessageDice(_MessageBase):
    dice: Annotated["Dice", "dice"]

    def __init__(
        self,
        dice: Annotated["Dice", "dice"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.dice = dice
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["dice"]


class MessageVideoNote(_MessageBase):
    video_note: Annotated["VideoNote", "videoNote"]

    def __init__(
        self,
        video_note: Annotated["VideoNote", "videoNote"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.video_note = video_note
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["videoNote"]


class MessageContact(_MessageBase):
    contact: Annotated["Contact", "contact"]

    def __init__(
        self,
        contact: Annotated["Contact", "contact"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.contact = contact
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["contact"]


class MessageGame(_MessageBase):
    game: Annotated["Game", "game"]

    def __init__(
        self,
        game: Annotated["Game", "game"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.game = game
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["game"]


class MessagePoll(_MessageBase):
    poll: Annotated["Poll", "poll"]

    def __init__(
        self,
        poll: Annotated["Poll", "poll"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.poll = poll
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["poll"]


class MessageInvoice(_MessageBase):
    invoice: Annotated["Invoice", "invoice"]

    def __init__(
        self,
        invoice: Annotated["Invoice", "invoice"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.invoice = invoice
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["invoice"]


class MessageVenue(_MessageBase):
    venue: Annotated["Venue", "venue"]

    def __init__(
        self,
        venue: Annotated["Venue", "venue"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.venue = venue
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["venue"]


class MessageLocation(_MessageBase):
    location: Annotated["Location", "location"]

    def __init__(
        self,
        location: Annotated["Location", "location"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.location = location
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["location"]


class MessageNewChatMembers(_MessageBase):
    new_chat_members: Annotated[list["User"], "newChatMembers"]

    def __init__(
        self,
        new_chat_members: Annotated[list["User"], "newChatMembers"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.new_chat_members = new_chat_members
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["newChatMembers"]


class MessageLeftChatMember(_MessageBase):
    left_chat_member: Annotated["User", "leftChatMember"]

    def __init__(
        self,
        left_chat_member: Annotated["User", "leftChatMember"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.left_chat_member = left_chat_member
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["leftChatMember"]


class MessageNewChatTitle(_MessageBase):
    new_chat_title: Annotated[str, "newChatTitle"]

    def __init__(
        self,
        new_chat_title: Annotated[str, "newChatTitle"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.new_chat_title = new_chat_title
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["newChatTitle"]


class MessageNewChatPhoto(_MessageBase):
    new_chat_photo: Annotated["Photo", "newChatPhoto"]

    def __init__(
        self,
        new_chat_photo: Annotated["Photo", "newChatPhoto"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.new_chat_photo = new_chat_photo
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["newChatPhoto"]


class MessageDeletedChatPhoto(_MessageBase):
    deleted_chat_photo: Annotated[Literal[True], "deletedChatPhoto"]

    def __init__(
        self,
        deleted_chat_photo: Annotated[Literal[True], "deletedChatPhoto"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.deleted_chat_photo = deleted_chat_photo
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["deletedChatPhoto"]


class MessageGroupCreated(_MessageBase):
    group_created: Annotated[Literal[True], "groupCreated"]
    new_chat_members: Annotated[list["User"], "newChatMembers"]

    def __init__(
        self,
        group_created: Annotated[Literal[True], "groupCreated"],
        new_chat_members: Annotated[list["User"], "newChatMembers"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.group_created = group_created
        self.new_chat_members = new_chat_members
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["groupCreated", "newChatMembers"]


class MessageSupergroupCreated(_MessageBase):
    supergroup_created: Annotated[Literal[True], "supergroupCreated"]

    def __init__(
        self,
        supergroup_created: Annotated[Literal[True], "supergroupCreated"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.supergroup_created = supergroup_created
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["supergroupCreated"]


class MessageChannelCreated(_MessageBase):
    channel_created: Annotated[Literal[True], "channelCreated"]

    def __init__(
        self,
        channel_created: Annotated[Literal[True], "channelCreated"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.channel_created = channel_created
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["channelCreated"]


class MessageAutoDeleteTimerChanged(_MessageBase):
    new_auto_delete_time: Annotated[int, "newAutoDeleteTime"]

    def __init__(
        self,
        new_auto_delete_time: Annotated[int, "newAutoDeleteTime"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.new_auto_delete_time = new_auto_delete_time
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["newAutoDeleteTime"]


class MessageChatMigratedTo(_MessageBase):
    chat_migrated_to: Annotated[int, "chatMigratedTo"]

    def __init__(
        self,
        chat_migrated_to: Annotated[int, "chatMigratedTo"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.chat_migrated_to = chat_migrated_to
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["chatMigratedTo"]


class MessageChatMigratedFrom(_MessageBase):
    chat_migrated_from: Annotated[int, "chatMigratedFrom"]

    def __init__(
        self,
        chat_migrated_from: Annotated[int, "chatMigratedFrom"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.chat_migrated_from = chat_migrated_from
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["chatMigratedFrom"]


class MessagePinnedMessage(_MessageBase):
    pinned_message: Annotated["Message", "pinnedMessage"]

    def __init__(
        self,
        pinned_message: Annotated["Message", "pinnedMessage"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.pinned_message = pinned_message
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["pinnedMessage"]


class MessageUserShared(_MessageBase):
    user_shared: Annotated[Any, "userShared"]

    def __init__(
        self,
        user_shared: Annotated[Any, "userShared"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.user_shared = user_shared
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["userShared"]


class MessageWriteAccessAllowed(_MessageBase):
    write_access_allowed: Annotated[Any, "writeAccessAllowed"]

    def __init__(
        self,
        write_access_allowed: Annotated[Any, "writeAccessAllowed"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.write_access_allowed = write_access_allowed
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["writeAccessAllowed"]


class MessageForumTopicCreated(_MessageBase):
    forum_topic_created: Annotated[Any, "forumTopicCreated"]

    def __init__(
        self,
        forum_topic_created: Annotated[Any, "forumTopicCreated"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.forum_topic_created = forum_topic_created
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["forumTopicCreated"]


class MessageForumTopicEdited(_MessageBase):
    forum_topic_edited: Annotated[Any, "forumTopicEdited"]

    def __init__(
        self,
        forum_topic_edited: Annotated[Any, "forumTopicEdited"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.forum_topic_edited = forum_topic_edited
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["forumTopicEdited"]


class MessageForumTopicClosed(_MessageBase):
    forum_topic_closed: Annotated[Literal[True], "forumTopicClosed"]

    def __init__(
        self,
        forum_topic_closed: Annotated[Literal[True], "forumTopicClosed"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.forum_topic_closed = forum_topic_closed
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["forumTopicClosed"]


class MessageForumTopicReopened(_MessageBase):
    forum_topic_reopened: Annotated[Literal[True], "forumTopicReopened"]

    def __init__(
        self,
        forum_topic_reopened: Annotated[Literal[True], "forumTopicReopened"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.forum_topic_reopened = forum_topic_reopened
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["forumTopicReopened"]


class MessageVideoChatScheduled(_MessageBase):
    video_chat_scheduled: Annotated[Any, "videoChatScheduled"]

    def __init__(
        self,
        video_chat_scheduled: Annotated[Any, "videoChatScheduled"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.video_chat_scheduled = video_chat_scheduled
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["videoChatScheduled"]


class MessageVideoChatStarted(_MessageBase):
    video_chat_started: Annotated[Literal[True], "videoChatStarted"]

    def __init__(
        self,
        video_chat_started: Annotated[Literal[True], "videoChatStarted"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.video_chat_started = video_chat_started
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["videoChatStarted"]


class MessageVideoChatEnded(_MessageBase):
    video_chat_ended: Annotated[Any, "videoChatEnded"]

    def __init__(
        self,
        video_chat_ended: Annotated[Any, "videoChatEnded"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.video_chat_ended = video_chat_ended
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["videoChatEnded"]


class MessageGiveaway(_MessageBase):
    giveaway: Annotated["Giveaway", "giveaway"]

    def __init__(
        self,
        giveaway: Annotated["Giveaway", "giveaway"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.giveaway = giveaway
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["giveaway"]


class MessageUnsupported(_MessageBase):
    unsupported: Annotated[Literal[True], "unsupported"]

    def __init__(
        self,
        unsupported: Annotated[Literal[True], "unsupported"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.unsupported = unsupported
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["unsupported"]


class MessageSuccessfulPayment(_MessageBase):
    successful_payment: Annotated["SuccessfulPayment", "successfulPayment"]

    def __init__(
        self,
        successful_payment: Annotated["SuccessfulPayment", "successfulPayment"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.successful_payment = successful_payment
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["successfulPayment"]


class MessageRefundedPayment(_MessageBase):
    refunded_payment: Annotated["RefundedPayment", "refundedPayment"]

    def __init__(
        self,
        refunded_payment: Annotated["RefundedPayment", "refundedPayment"],
        out: Annotated[bool, "out"],
        id: Annotated[int, "id"],
        date: Annotated[datetime.datetime, "date"],
        chat: Annotated["ChatP", "chat"],
        is_topic_message: Annotated[bool, "isTopicMessage"],
        *,
        thread_id: Annotated[Optional[int], "threadId"] = None,
        from_: Annotated[Optional["User"], "from"] = None,
        sender_chat: Annotated[Optional["ChatP"], "senderChat"] = None,
        link: Annotated[Optional[str], "link"] = None,
        forward_from: Annotated[Optional["ForwardHeader"], "forwardFrom"] = None,
        is_automatic_forward: Annotated[Optional[bool], "isAutomaticForward"] = None,
        reply_to_message: Annotated[Optional["Message"], "replyToMessage"] = None,
        reply_to_message_id: Annotated[Optional[int], "replyToMessageId"] = None,
        reactions: Annotated[Optional[list["MessageReaction"]], "reactions"] = None,
        reply_quote: Annotated[Optional["ReplyQuote"], "replyQuote"] = None,
        via_bot: Annotated[Optional["User"], "viaBot"] = None,
        edit_date: Annotated[Optional[datetime.datetime], "editDate"] = None,
        has_protected_content: Annotated[Optional[bool], "hasProtectedContent"] = None,
        media_group_id: Annotated[Optional[str], "mediaGroupId"] = None,
        author_signature: Annotated[Optional[str], "authorSignature"] = None,
        views: Annotated[Optional[int], "views"] = None,
        forwards: Annotated[Optional[int], "forwards"] = None,
        reply_markup: Annotated[Optional["ReplyMarkup"], "replyMarkup"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
        sender_boost_count: Annotated[Optional[int], "senderBoostCount"] = None,
        via_business_bot: Annotated[Optional["User"], "viaBusinessBot"] = None,
        effect_id: Annotated[Optional[str], "effectId"] = None,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
    ):
        self.refunded_payment = refunded_payment
        self.out = out
        self.id = id
        self.thread_id = thread_id
        self.from_ = from_
        self.sender_chat = sender_chat
        self.date = date
        self.chat = chat
        self.link = link
        self.forward_from = forward_from
        self.is_topic_message = is_topic_message
        self.is_automatic_forward = is_automatic_forward
        self.reply_to_message = reply_to_message
        self.reply_to_message_id = reply_to_message_id
        self.reactions = reactions
        self.reply_quote = reply_quote
        self.via_bot = via_bot
        self.edit_date = edit_date
        self.has_protected_content = has_protected_content
        self.media_group_id = media_group_id
        self.author_signature = author_signature
        self.views = views
        self.forwards = forwards
        self.reply_markup = reply_markup
        self.business_connection_id = business_connection_id
        self.sender_boost_count = sender_boost_count
        self.via_business_bot = via_business_bot
        self.effect_id = effect_id
        self.scheduled = scheduled

    __discriminators__ = ["refundedPayment"]


Message = Union[
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
    MessageRefundedPayment,
]


class CallbackQuery(_Type):
    id: Annotated[str, "id"]
    from_: Annotated["User", "from"]
    message: Annotated[Optional["Message"], "message"]
    inline_message_id: Annotated[Optional[str], "inlineMessageId"]
    chat_instance: Annotated[str, "chatInstance"]
    data: Annotated[Optional[str], "data"]
    game_short_name: Annotated[Optional[str], "gameShortName"]

    def __init__(
        self,
        id: Annotated[str, "id"],
        from_: Annotated["User", "from"],
        chat_instance: Annotated[str, "chatInstance"],
        *,
        message: Annotated[Optional["Message"], "message"] = None,
        inline_message_id: Annotated[Optional[str], "inlineMessageId"] = None,
        data: Annotated[Optional[str], "data"] = None,
        game_short_name: Annotated[Optional[str], "gameShortName"] = None,
    ):
        self.id = id
        self.from_ = from_
        self.message = message
        self.inline_message_id = inline_message_id
        self.chat_instance = chat_instance
        self.data = data
        self.game_short_name = game_short_name

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

    def __init__(
        self,
        chat: Annotated["ChatP", "chat"],
        order: Annotated[str, "order"],
        pinned: Annotated[int, "pinned"],
        *,
        last_message: Annotated[Optional["Message"], "lastMessage"] = None,
    ):
        self.chat = chat
        self.order = order
        self.pinned = pinned
        self.last_message = last_message


class InlineQueryAnswer(_Type):
    id: Annotated[str, "id"]
    results: Annotated[list["InlineQueryResult"], "results"]
    next_offset: Annotated[Optional[str], "nextOffset"]

    def __init__(
        self,
        id: Annotated[str, "id"],
        results: Annotated[list["InlineQueryResult"], "results"],
        *,
        next_offset: Annotated[Optional[str], "nextOffset"] = None,
    ):
        self.id = id
        self.results = results
        self.next_offset = next_offset


class UpdateNewMessage(_Type):
    message: Annotated["Message", "message"]

    def __init__(
        self,
        message: Annotated["Message", "message"],
    ):
        self.message = message

    __discriminators__ = ["message"]


class UpdateMessageEdited(_Type):
    edited_message: Annotated["Message", "editedMessage"]

    def __init__(
        self,
        edited_message: Annotated["Message", "editedMessage"],
    ):
        self.edited_message = edited_message

    __discriminators__ = ["editedMessage"]


class UpdateMessageScheduled(_Type):
    scheduled_message: Annotated["Message", "scheduledMessage"]

    def __init__(
        self,
        scheduled_message: Annotated["Message", "scheduledMessage"],
    ):
        self.scheduled_message = scheduled_message

    __discriminators__ = ["scheduledMessage"]


class UpdateMessagesDeleted(_Type):
    deleted_messages: Annotated[list["MessageReference"], "deletedMessages"]
    scheduled: Annotated[Optional[bool], "scheduled"]
    business_connection_id: Annotated[Optional[str], "businessConnectionId"]

    def __init__(
        self,
        deleted_messages: Annotated[list["MessageReference"], "deletedMessages"],
        *,
        scheduled: Annotated[Optional[bool], "scheduled"] = None,
        business_connection_id: Annotated[Optional[str], "businessConnectionId"] = None,
    ):
        self.deleted_messages = deleted_messages
        self.scheduled = scheduled
        self.business_connection_id = business_connection_id

    __discriminators__ = ["deletedMessages"]


class UpdateCallbackQuery(_Type):
    callback_query: Annotated["CallbackQuery", "callbackQuery"]

    def __init__(
        self,
        callback_query: Annotated["CallbackQuery", "callbackQuery"],
    ):
        self.callback_query = callback_query

    __discriminators__ = ["callbackQuery"]


class UpdateInlineQuery(_Type):
    inline_query: Annotated["InlineQuery", "inlineQuery"]

    def __init__(
        self,
        inline_query: Annotated["InlineQuery", "inlineQuery"],
    ):
        self.inline_query = inline_query

    __discriminators__ = ["inlineQuery"]


class UpdateChosenInlineResult(_Type):
    chosen_inline_result: Annotated["ChosenInlineResult", "chosenInlineResult"]

    def __init__(
        self,
        chosen_inline_result: Annotated["ChosenInlineResult", "chosenInlineResult"],
    ):
        self.chosen_inline_result = chosen_inline_result

    __discriminators__ = ["chosenInlineResult"]


class UpdateNewChat(_Type):
    new_chat: Annotated["ChatListItem", "newChat"]

    def __init__(
        self,
        new_chat: Annotated["ChatListItem", "newChat"],
    ):
        self.new_chat = new_chat

    __discriminators__ = ["newChat"]


class UpdateEditedChat(_Type):
    edited_chat: Annotated["ChatListItem", "editedChat"]

    def __init__(
        self,
        edited_chat: Annotated["ChatListItem", "editedChat"],
    ):
        self.edited_chat = edited_chat

    __discriminators__ = ["editedChat"]


class UpdateDeletedChat(_Type):
    deleted_chat: Annotated[Any, "deletedChat"]

    def __init__(
        self,
        deleted_chat: Annotated[Any, "deletedChat"],
    ):
        self.deleted_chat = deleted_chat

    __discriminators__ = ["deletedChat"]


class UpdateMessageInteractions(_Type):
    message_interactions: Annotated["MessageInteractions", "messageInteractions"]

    def __init__(
        self,
        message_interactions: Annotated["MessageInteractions", "messageInteractions"],
    ):
        self.message_interactions = message_interactions

    __discriminators__ = ["messageInteractions"]


class UpdateMessageReactionCount(_Type):
    message_reaction_count: Annotated["MessageReactionCount", "messageReactionCount"]

    def __init__(
        self,
        message_reaction_count: Annotated[
            "MessageReactionCount", "messageReactionCount"
        ],
    ):
        self.message_reaction_count = message_reaction_count

    __discriminators__ = ["messageReactionCount"]


class UpdateMessageReactions(_Type):
    message_reactions: Annotated["MessageReactions", "messageReactions"]

    def __init__(
        self,
        message_reactions: Annotated["MessageReactions", "messageReactions"],
    ):
        self.message_reactions = message_reactions

    __discriminators__ = ["messageReactions"]


class UpdateChatMember(_Type):
    chat_member: Annotated["ChatMemberUpdated", "chatMember"]

    def __init__(
        self,
        chat_member: Annotated["ChatMemberUpdated", "chatMember"],
    ):
        self.chat_member = chat_member

    __discriminators__ = ["chatMember"]


class UpdateMyChatMember(_Type):
    my_chat_member: Annotated["ChatMemberUpdated", "myChatMember"]

    def __init__(
        self,
        my_chat_member: Annotated["ChatMemberUpdated", "myChatMember"],
    ):
        self.my_chat_member = my_chat_member

    __discriminators__ = ["myChatMember"]


class UpdateDeletedStory(_Type):
    deleted_story: Annotated["StoryReference", "deletedStory"]

    def __init__(
        self,
        deleted_story: Annotated["StoryReference", "deletedStory"],
    ):
        self.deleted_story = deleted_story

    __discriminators__ = ["deletedStory"]


class UpdateNewStory(_Type):
    story: Annotated["Story", "story"]

    def __init__(
        self,
        story: Annotated["Story", "story"],
    ):
        self.story = story

    __discriminators__ = ["story"]


class UpdateBusinessConnection(_Type):
    business_connection: Annotated["BusinessConnection", "businessConnection"]

    def __init__(
        self,
        business_connection: Annotated["BusinessConnection", "businessConnection"],
    ):
        self.business_connection = business_connection

    __discriminators__ = ["businessConnection"]


class UpdateVideoChat(_Type):
    video_chat: Annotated["VideoChat", "videoChat"]

    def __init__(
        self,
        video_chat: Annotated["VideoChat", "videoChat"],
    ):
        self.video_chat = video_chat

    __discriminators__ = ["videoChat"]


class UpdatePreCheckoutQuery(_Type):
    pre_checkout_query: Annotated["PreCheckoutQuery", "preCheckoutQuery"]

    def __init__(
        self,
        pre_checkout_query: Annotated["PreCheckoutQuery", "preCheckoutQuery"],
    ):
        self.pre_checkout_query = pre_checkout_query

    __discriminators__ = ["preCheckoutQuery"]


class UpdateJoinRequest(_Type):
    join_request: Annotated["JoinRequest", "joinRequest"]

    def __init__(
        self,
        join_request: Annotated["JoinRequest", "joinRequest"],
    ):
        self.join_request = join_request

    __discriminators__ = ["joinRequest"]


Update = Union[
    UpdateNewMessage,
    UpdateMessageEdited,
    UpdateMessageScheduled,
    UpdateMessagesDeleted,
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
    UpdateJoinRequest,
]
