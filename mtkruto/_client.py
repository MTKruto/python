import asyncio
import datetime
import json
import logging
from collections.abc import Callable, Coroutine
from typing import (
    Any,
    AsyncGenerator,
    Generic,
    List,
    Literal,
    Optional,
    TypeVar,
    Union,
    cast,
)
from urllib.parse import urljoin

import aiohttp

from ._utils import default, to, transform
from .errors import InputError, InternalError, StopPropagation, TelegramError
from .filters import Filter
from .types import (
    ID,
    BotCommand,
    BotCommandScope,
    BusinessConnection,
    CallbackQuery,
    CallbackQueryAnswer,
    CallbackQueryQuestion,
    Chat,
    ChatAction,
    ChatListItem,
    ChatMember,
    ChatMemberRights,
    ChatMemberUpdated,
    ChosenInlineResult,
    FailedInvitation,
    FileSource,
    InactiveChat,
    InlineQuery,
    InlineQueryAnswer,
    InlineQueryResult,
    InlineQueryResultButton,
    InputMedia,
    InputStoryContent,
    InviteLink,
    JoinRequest,
    LinkPreview,
    LiveStreamChannel,
    Message,
    MessageAnimation,
    MessageAudio,
    MessageContact,
    MessageDice,
    MessageDocument,
    MessageEntity,
    MessageInteractions,
    MessageInvoice,
    MessageLocation,
    MessagePhoto,
    MessagePoll,
    MessageReactionCount,
    MessageReactions,
    MessageSearchFilter,
    MessageSticker,
    MessageText,
    MessageVenue,
    MessageVideo,
    MessageVideoNote,
    MessageVoice,
    NetworkStatistics,
    ParseMode,
    Poll,
    PreCheckoutQuery,
    PriceTag,
    Reaction,
    ReplyMarkup,
    ReplyQuote,
    ReplyTo,
    SelfDestructOption,
    Sticker,
    Story,
    StoryInteractiveArea,
    StoryPrivacy,
    StoryReference,
    Update,
    UpdateBusinessConnection,
    UpdateCallbackQuery,
    UpdateChatMember,
    UpdateChosenInlineResult,
    UpdateDeletedChat,
    UpdateDeletedStory,
    UpdateEditedChat,
    UpdateInlineQuery,
    UpdateJoinRequest,
    UpdateMessageEdited,
    UpdateMessageInteractions,
    UpdateMessageReactionCount,
    UpdateMessageReactions,
    UpdateMessagesDeleted,
    UpdateMyChatMember,
    UpdateNewChat,
    UpdateNewMessage,
    UpdateNewStory,
    UpdatePreCheckoutQuery,
    UpdateVideoChat,
    User,
    VideoChat,
    VideoChatActive,
    VideoChatScheduled,
)

log = logging.getLogger(__name__)


class Client:
    _running = False
    _handlers = list["Handler[Any]"]()

    def __init__(self, endpoint_url: str) -> None:
        if not endpoint_url.endswith("/"):
            endpoint_url += "/"
        self._endpoint_url = endpoint_url
        self._http_client = aiohttp.ClientSession(
            json_serialize=json.JSONEncoder(default=default).encode
        )

    async def start(self) -> None:
        self._running = True
        try:
            while self._running:
                try:
                    updates = await self.get_updates()
                    for update in updates:
                        for handler in self._handlers:
                            if handler.filter(update):
                                try:
                                    await handler.callback(self, update)
                                except StopPropagation:
                                    break
                                except BaseException as e:
                                    log.exception(
                                        "An error occurred when handling an update.", e
                                    )
                except InputError:
                    raise
                except BaseException as e:
                    log.error("getUpdates failed: %s", e)
                    await asyncio.sleep(5)
        finally:
            self._running = False

    def run(self) -> None:
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        me = loop.run_until_complete(self.get_me())
        log.info("Running as %s", me)
        return loop.run_until_complete(self.start())

    async def _request(
        self,
        method: str,
        *args: Any,
        timeout: Optional[int] = None,
    ) -> Any:
        for arg in args:
            if isinstance(arg, dict):
                transform(arg)
        url = urljoin(self._endpoint_url, "./" + method)
        if len(args) >= 2 and isinstance(args[1], bytes):
            form_data = aiohttp.FormData()
            for arg in args:
                form_data.add_field(
                    "_",
                    arg if isinstance(arg, bytes) else json.dumps(arg, default=default),
                )
            result = await self._http_client.post(
                url,
                data=form_data,
                timeout=timeout,
            )
        else:
            response = await self._http_client.post(url, json=args, timeout=timeout)
            if response.status == 200:
                if response.headers.get("content-type") == "application/json":
                    return transform(await response.json())
                else:
                    return response.content.iter_chunks()
            else:
                data = await response.json()
                if error := response.headers.get("x-error-type"):
                    if "input" in error:
                        raise InputError(data)
                    elif "rpc" in error:
                        raise TelegramError(response.status, data)
                raise InternalError(data)
        return result

    def add_handler(self, handler: "AnyHandler") -> None:
        self._handlers.append(handler)

    def on_update(self) -> Callable[["HandlerCallback[Update]"], None]:
        def decorator(callback: HandlerCallback[Update]) -> None:
            self.add_handler(Handler(lambda _: True, callback))

        return decorator

    def on_new_message(
        self, filter_: Optional[Filter] = None
    ) -> Callable[["HandlerCallback[Any]"], None]:
        def decorator(callback: HandlerCallback[Any]) -> None:
            self.add_handler(NewMessageHandler(callback, filter_))

        return decorator

    def on_edited_message(
        self, filter_: Optional[Filter] = None
    ) -> Callable[["HandlerCallback[Any]"], None]:
        def decorator(callback: HandlerCallback[Any]) -> None:
            self.add_handler(EditedMessageHandler(callback, filter_))

        return decorator

    def on_deleted_messages(
        self,
    ) -> Callable[["HandlerCallback[UpdateMessagesDeleted]"], None]:
        def decorator(callback: HandlerCallback[UpdateMessagesDeleted]) -> None:
            self.add_handler(DeletedMessagesHandler(callback))

        return decorator

    def on_callback_query(self) -> Callable[["HandlerCallback[CallbackQuery]"], None]:
        def decorator(callback: HandlerCallback[CallbackQuery]) -> None:
            self.add_handler(CallbackQueryHandler(callback))

        return decorator

    def on_inline_query(self) -> Callable[["HandlerCallback[InlineQuery]"], None]:
        def decorator(callback: HandlerCallback[InlineQuery]) -> None:
            self.add_handler(InlineQueryHandler(callback))

        return decorator

    def on_chosen_inline_result(
        self,
    ) -> Callable[["HandlerCallback[ChosenInlineResult]"], None]:
        def decorator(callback: HandlerCallback[ChosenInlineResult]) -> None:
            self.add_handler(ChosenInlineResultHandler(callback))

        return decorator

    def on_new_chat(self) -> Callable[["HandlerCallback[ChatListItem]"], None]:
        def decorator(callback: HandlerCallback[ChatListItem]) -> None:
            self.add_handler(NewChatHandler(callback))

        return decorator

    def on_edited_chat(self) -> Callable[["HandlerCallback[ChatListItem]"], None]:
        def decorator(callback: HandlerCallback[ChatListItem]) -> None:
            self.add_handler(EditedChatHandler(callback))

        return decorator

    def on_deleted_chat(self) -> Callable[["HandlerCallback[int]"], None]:
        def decorator(callback: HandlerCallback[int]) -> None:
            self.add_handler(DeletedChatHandler(callback))

        return decorator

    def on_message_interactions(
        self,
    ) -> Callable[["HandlerCallback[MessageInteractions]"], None]:
        def decorator(callback: HandlerCallback[MessageInteractions]) -> None:
            self.add_handler(MessageInteractionsHandler(callback))

        return decorator

    def on_message_reaction_count(
        self,
    ) -> Callable[["HandlerCallback[MessageReactionCount]"], None]:
        def decorator(callback: HandlerCallback[MessageReactionCount]) -> None:
            self.add_handler(MessageReactionCountHandler(callback))

        return decorator

    def on_message_reactions(
        self,
    ) -> Callable[["HandlerCallback[MessageReactions]"], None]:
        def decorator(callback: HandlerCallback[MessageReactions]) -> None:
            self.add_handler(MessageReactionsHandler(callback))

        return decorator

    def on_chat_member(self) -> Callable[["HandlerCallback[ChatMemberUpdated]"], None]:
        def decorator(callback: HandlerCallback[ChatMemberUpdated]) -> None:
            self.add_handler(ChatMemberHandler(callback))

        return decorator

    def on_my_chat_member(
        self,
    ) -> Callable[["HandlerCallback[ChatMemberUpdated]"], None]:
        def decorator(callback: HandlerCallback[ChatMemberUpdated]) -> None:
            self.add_handler(MyChatMemberHandler(callback))

        return decorator

    def on_deleted_story(self) -> Callable[["HandlerCallback[StoryReference]"], None]:
        def decorator(callback: HandlerCallback[StoryReference]) -> None:
            self.add_handler(DeletedStoryHandler(callback))

        return decorator

    def on_new_story(self) -> Callable[["HandlerCallback[Story]"], None]:
        def decorator(callback: HandlerCallback[Story]) -> None:
            self.add_handler(NewStoryHandler(callback))

        return decorator

    def on_business_connection(
        self,
    ) -> Callable[["HandlerCallback[BusinessConnection]"], None]:
        def decorator(callback: HandlerCallback[BusinessConnection]) -> None:
            self.add_handler(BusinessConnectionHandler(callback))

        return decorator

    def on_video_chat(self) -> Callable[["HandlerCallback[VideoChat]"], None]:
        def decorator(callback: HandlerCallback[VideoChat]) -> None:
            self.add_handler(VideoChatHandler(callback))

        return decorator

    def on_pre_checkout_query(
        self,
    ) -> Callable[["HandlerCallback[PreCheckoutQuery]"], None]:
        def decorator(callback: HandlerCallback[PreCheckoutQuery]) -> None:
            self.add_handler(PreCheckoutQueryHandler(callback))

        return decorator

    def on_join_request(
        self,
    ) -> Callable[["HandlerCallback[JoinRequest]"], None]:
        def decorator(callback: HandlerCallback[JoinRequest]) -> None:
            self.add_handler(JoinRequestHandler(callback))

        return decorator

    async def get_updates(self, timeout: Optional[int] = None) -> list[Update]:
        return to(
            list[Update], await self._request("getUpdates", timeout=timeout), self
        )

    async def invoke(self, payload: Any) -> Any:
        return await self._request("invoke", payload)

    ########################### MESSAGES ########################
    async def send_message(
        self,
        chat_id: ID,
        text: str,
        *,
        parse_mode: Optional[ParseMode] = None,
        entities: Optional[list[MessageEntity]] = None,
        link_preview: Optional[LinkPreview] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageText:
        return to(
            MessageText,
            await self._request(
                "sendMessage",
                chat_id,
                text,
                {
                    "parseMode": parse_mode,
                    "entities": entities,
                    "linkPreview": link_preview,
                    "disableNotification": disable_notification,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def delete_message(
        self, chat_id: ID, message_id: int, *, only_for_me: Optional[bool] = False
    ) -> None:
        await self._request(
            "deleteMessage", chat_id, message_id, {"onlyForMe": only_for_me}
        )

    async def delete_messages(
        self,
        chat_id: ID,
        message_ids: List[int],
        *,
        only_for_me: Optional[bool] = False,
    ) -> None:
        await self._request(
            "deleteMessages", chat_id, message_ids, {"onlyForMe": only_for_me}
        )

    async def delete_chat_member_messages(self, chat_id: ID, member_id: ID) -> None:
        await self._request("deleteChatMemberMessages", chat_id, member_id)

    async def send_voice(
        self,
        chat_id: ID,
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
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageVoice:
        return to(
            MessageVoice,
            await self._request(
                "sendVoice",
                chat_id,
                voice,
                {
                    "duration": duration,
                    "caption": caption,
                    "captionEntities": caption_entities,
                    "parseMode": parse_mode,
                    "thumbnail": thumbnail,
                    "fileName": file_name,
                    "mimeType": mime_type,
                    "chunkSize": chunk_size,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_video_note(
        self,
        chat_id: ID,
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
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageVideoNote:
        return to(
            MessageVideoNote,
            await self._request(
                "sendVideoNote",
                chat_id,
                video_note,
                {
                    "duration": duration,
                    "length": length,
                    "caption": caption,
                    "captionEntities": caption_entities,
                    "parseMode": parse_mode,
                    "thumbnail": thumbnail,
                    "fileName": file_name,
                    "mimeType": mime_type,
                    "chunkSize": chunk_size,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_video(
        self,
        chat_id: ID,
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
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
        star_count: Optional[int] = None,
    ) -> MessageVideo:
        return to(
            MessageVideo,
            await self._request(
                "sendVideo",
                chat_id,
                video,
                {
                    "duration": duration,
                    "width": width,
                    "height": height,
                    "supportsStreaming": supports_streaming,
                    "selfDestruct": self_destruct,
                    "caption": caption,
                    "captionEntities": caption_entities,
                    "parseMode": parse_mode,
                    "thumbnail": thumbnail,
                    "hasSpoiler": has_spoiler,
                    "fileName": file_name,
                    "mimeType": mime_type,
                    "chunkSize": chunk_size,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                    "starCount": star_count,
                },
            ),
            self,
        )

    async def send_venue(
        self,
        chat_id: ID,
        latitude: Union[int, float],
        longitude: Union[int, float],
        title: str,
        address: str,
        *,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageVenue:
        return to(
            MessageVenue,
            await self._request(
                "sendVenue",
                chat_id,
                latitude,
                longitude,
                title,
                address,
                {
                    "foursquareId": foursquare_id,
                    "foursquareType": foursquare_type,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_sticker(
        self,
        chat_id: ID,
        sticker: FileSource,
        *,
        emoji: Optional[str] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageSticker:
        return to(
            MessageSticker,
            await self._request(
                "sendSticker",
                chat_id,
                sticker,
                {
                    "emoji": emoji,
                    "fileName": file_name,
                    "mimeType": mime_type,
                    "chunkSize": chunk_size,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_poll(
        self,
        chat_id: ID,
        question: str,
        options: List[str],
        *,
        question_entities: Optional[List[MessageEntity]] = None,
        question_parse_mode: Optional[ParseMode] = None,
        option_parse_mode: Optional[ParseMode] = None,
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
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessagePoll:
        return to(
            MessagePoll,
            await self._request(
                "sendPoll",
                chat_id,
                question,
                options,
                {
                    "questionEntities": question_entities,
                    "questionParseMode": question_parse_mode,
                    "optionParseMode": option_parse_mode,
                    "isAnonymous": is_anonymous,
                    "type": type,
                    "allowMultipleAnswers": allow_multiple_answers,
                    "correctOptionIndex": correct_option_index,
                    "explanation": explanation,
                    "explanationParseMode": explanation_parse_mode,
                    "explanationEntities": explanation_entities,
                    "openPeriod": open_period,
                    "closeDate": close_date,
                    "isClosed": is_closed,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_photo(
        self,
        chat_id: ID,
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
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
        star_count: Optional[int] = None,
    ) -> MessagePhoto:
        return to(
            MessagePhoto,
            await self._request(
                "sendPhoto",
                chat_id,
                photo,
                {
                    "selfDestruct": self_destruct,
                    "caption": caption,
                    "captionEntities": caption_entities,
                    "parseMode": parse_mode,
                    "hasSpoiler": has_spoiler,
                    "fileName": file_name,
                    "mimeType": mime_type,
                    "chunkSize": chunk_size,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                    "starCount": star_count,
                },
            ),
            self,
        )

    async def send_location(
        self,
        chat_id: ID,
        latitude: Union[int, float],
        longitude: Union[int, float],
        *,
        horizontal_accuracy: Optional[Union[int, float]] = None,
        live_period: Optional[Union[int, float]] = None,
        heading: Optional[Union[int, float]] = None,
        proximity_alert_radius: Optional[Union[int, float]] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageLocation:
        return to(
            MessageLocation,
            await self._request(
                "sendLocation",
                chat_id,
                latitude,
                longitude,
                {
                    "horizontalAccuracy": horizontal_accuracy,
                    "livePeriod": live_period,
                    "heading": heading,
                    "proximityAlertRadius": proximity_alert_radius,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_document(
        self,
        chat_id: ID,
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
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageDocument:
        return to(
            MessageDocument,
            await self._request(
                "sendDocument",
                chat_id,
                document,
                {
                    "caption": caption,
                    "captionEntities": caption_entities,
                    "parseMode": parse_mode,
                    "thumbnail": thumbnail,
                    "fileName": file_name,
                    "mimeType": mime_type,
                    "chunkSize": chunk_size,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_media_group(
        self,
        chat_id: ID,
        media: List[InputMedia],
        *,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> List[Message]:
        return to(
            List[Message],
            await self._request(
                "sendMediaGroup",
                chat_id,
                media,
                {
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_dice(
        self,
        chat_id: ID,
        emoji: Literal["🎲", "🎯", "🏀", "⚽", "🎳", "🎰"],
        *,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageDice:
        return to(
            MessageDice,
            await self._request(
                "sendDice",
                chat_id,
                emoji,
                {
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_contact(
        self,
        chat_id: ID,
        first_name: str,
        number: str,
        *,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageContact:
        return to(
            MessageContact,
            await self._request(
                "sendContact",
                chat_id,
                first_name,
                number,
                {
                    "lastName": last_name,
                    "vcard": vcard,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_chat_action(
        self,
        chat_id: ID,
        action: ChatAction,
        message_thread_id: Optional[int] = None,
    ) -> None:
        await self._request(
            "sendChatAction", chat_id, action, {"messageThreadId": message_thread_id}
        )

    async def send_audio(
        self,
        chat_id: ID,
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
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageAudio:
        return to(
            MessageAudio,
            await self._request(
                "sendAudio",
                chat_id,
                audio,
                {
                    "duration": duration,
                    "performer": performer,
                    "title": title,
                    "caption": caption,
                    "captionEntities": caption_entities,
                    "parseMode": parse_mode,
                    "thumbnail": thumbnail,
                    "fileName": file_name,
                    "mimeType": mime_type,
                    "chunkSize": chunk_size,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_animation(
        self,
        chat_id: ID,
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
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageAnimation:
        return to(
            MessageAnimation,
            await self._request(
                "sendAnimation",
                chat_id,
                animation,
                {
                    "duration": duration,
                    "width": width,
                    "height": height,
                    "caption": caption,
                    "captionEntities": caption_entities,
                    "parseMode": parse_mode,
                    "thumbnail": thumbnail,
                    "hasSpoiler": has_spoiler,
                    "fileName": file_name,
                    "mimeType": mime_type,
                    "chunkSize": chunk_size,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def search_messages(
        self,
        chat_id: ID,
        *,
        query: Optional[str] = "",
        from_user: Optional[ID] = None,
        filter: Optional[MessageSearchFilter] = None,
        after: Optional[int] = None,
        thread_id: Optional[int] = None,
        limit: Optional[int] = 100,
    ) -> List[Message]:
        return to(
            list[Message],
            await self._request(
                "searchMessages",
                chat_id,
                query,
                {
                    "from": from_user,
                    "filter": filter,
                    "after": after,
                    "threadId": thread_id,
                    "limit": limit,
                },
            ),
            self,
        )

    async def pin_message(
        self,
        chat_id: ID,
        message_id: int,
        *,
        both_sides: Optional[bool] = None,
        disable_notifaction: Optional[bool] = None,
    ) -> None:
        await self._request(
            "pinMessage",
            chat_id,
            message_id,
            {"bothSides": both_sides, "disableNotifaction": disable_notifaction},
        )

    async def stop_poll(
        self,
        chat_id: ID,
        message_id: int,
        *,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> Poll:
        return to(
            Poll,
            await self._request(
                "stopPoll", chat_id, message_id, {"replyMarkup": reply_markup}
            ),
            self,
        )

    async def unpin_message(self, chat_id: ID, message_id: int) -> None:
        await self._request("unpinMessage", chat_id, message_id)

    async def unpin_messages(self, chat_id: ID) -> None:
        await self._request("unpinMessages", chat_id)

    async def get_messages(self, chat_id: ID, message_ids: List[int]) -> List[Message]:
        r = await self._request("getMessages", chat_id, message_ids)
        return to(List[Message], r, self)

    async def get_message(self, chat_id: ID, message_id: int) -> Union[Message, None]:
        r = await self._request("getMessage", chat_id, message_id)
        return to(Message, r, self) if r else None

    async def forward_messages(
        self,
        from_chat: ID,
        to_chat: ID,
        message_ids: List[int],
        *,
        drop_sender_name: Optional[bool] = None,
        drop_caption: Optional[bool] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        business_connection_id: Optional[str] = None,
    ) -> List[Message]:
        return to(
            List[Message],
            await self._request(
                "forwardMessages",
                from_chat,
                to_chat,
                message_ids,
                {
                    "dropSenderName": drop_sender_name,
                    "dropCaption": drop_caption,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def send_invoice(
        self,
        chat_id: ID,
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List[PriceTag],
        *,
        provider_token: Optional[str] = None,
        max_tip_amount: Optional[int] = None,
        suggested_tip_amounts: Optional[List[int]] = None,
        start_parameter: Optional[str] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        flexible: Optional[bool] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to: Optional[ReplyTo] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        reply_markup: Optional[ReplyMarkup] = None,
        message_effect_id: Optional[int] = None,
        business_connection_id: Optional[str] = None,
    ) -> MessageInvoice:
        return to(
            MessageInvoice,
            await self._request(
                "sendInvoice",
                chat_id,
                title,
                description,
                payload,
                currency,
                prices,
                {
                    "providerToken": provider_token,
                    "maxTipAmount": max_tip_amount,
                    "suggestedTipAmounts": suggested_tip_amounts,
                    "startParameter": start_parameter,
                    "providerData": provider_data,
                    "photoUrl": photo_url,
                    "photoSize": photo_size,
                    "photoWidth": photo_width,
                    "photoHeight": photo_height,
                    "needName": need_name,
                    "needPhoneNumber": need_phone_number,
                    "needEmail": need_email,
                    "needShippingAddress": need_shipping_address,
                    "sendPhoneNumberToProvider": send_phone_number_to_provider,
                    "sendEmailToProvider": send_email_to_provider,
                    "flexible": flexible,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyTo": reply_to,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "replyMarkup": reply_markup,
                    "messageEffectId": message_effect_id,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def forward_message(
        self,
        from_chat: ID,
        to_chat: ID,
        message_id: int,
        *,
        drop_sender_name: Optional[bool] = None,
        drop_caption: Optional[bool] = None,
        disable_notifaction: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_quote: Optional[ReplyQuote] = None,
        message_thread_id: Optional[int] = None,
        send_as: Optional[ID] = None,
        business_connection_id: Optional[str] = None,
    ) -> Message:
        return to(
            Message,
            await self._request(
                "forwardMessage",
                from_chat,
                to_chat,
                message_id,
                {
                    "dropSenderName": drop_sender_name,
                    "dropCaption": drop_caption,
                    "disableNotifaction": disable_notifaction,
                    "protectContent": protect_content,
                    "replyQuote": reply_quote,
                    "messageThreadId": message_thread_id,
                    "sendAs": send_as,
                    "businessConnectionId": business_connection_id,
                },
            ),
            self,
        )

    async def edit_message_text(
        self,
        chat_id: ID,
        message_id: int,
        text: str,
        *,
        parse_mode: Optional[ParseMode] = None,
        entities: Optional[List[MessageEntity]] = None,
        link_preview: Optional[LinkPreview] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> MessageText:
        return to(
            MessageText,
            await self._request(
                "editMessageText",
                chat_id,
                message_id,
                text,
                {
                    "parseMode": parse_mode,
                    "entities": entities,
                    "linkPreview": link_preview,
                    "replyMarkup": reply_markup,
                },
            ),
            self,
        )

    async def edit_message_reply_markup(
        self,
        chat_id: ID,
        message_id: int,
        *,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> Message:
        return to(
            Message,
            await self._request(
                "editMessageReplyMarkup",
                chat_id,
                message_id,
                {"replyMarkup": reply_markup},
            ),
            self,
        )

    async def edit_message_media(
        self,
        chat_id: ID,
        message_id: int,
        media: InputMedia,
        *,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> Message:
        return to(
            Message,
            await self._request(
                "editMessageMedia",
                chat_id,
                message_id,
                media,
                {"replyMarkup": reply_markup},
            ),
            self,
        )

    async def edit_message_live_location(
        self,
        chat_id: ID,
        message_id: int,
        latitude: Union[int, float],
        longitude: Union[int, float],
        *,
        horizontal_accuracy: Optional[Union[int, float]] = None,
        heading: Optional[Union[int, float]] = None,
        proximity_alert_radius: Optional[Union[int, float]] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> MessageLocation:
        return to(
            MessageLocation,
            await self._request(
                "editMessageLiveLocation",
                chat_id,
                message_id,
                latitude,
                longitude,
                {
                    "horizontalAccuracy": horizontal_accuracy,
                    "heading": heading,
                    "proximityAlertRadius": proximity_alert_radius,
                    "replyMarkup": reply_markup,
                },
            ),
            self,
        )

    async def edit_inline_message_text(
        self,
        inline_message_id: str,
        text: str,
        *,
        parse_mode: Optional[ParseMode] = None,
        entities: Optional[List[MessageEntity]] = None,
        link_preview: Optional[LinkPreview] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> None:
        await self._request(
            "editInlineMessageText",
            inline_message_id,
            text,
            {
                "parseMode": parse_mode,
                "entities": entities,
                "linkPreview": link_preview,
                "replyMarkup": reply_markup,
            },
        )

    async def edit_inline_message_reply_markup(
        self,
        inline_message_id: str,
        *,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> None:
        await self._request(
            "editInlineMessageReplyMarkup",
            inline_message_id,
            {"replyMarkup": reply_markup},
        )

    async def edit_inline_message_media(
        self,
        inline_message_id: str,
        media: InputMedia,
        *,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> None:
        await self._request(
            "editInlineMessageMedia",
            inline_message_id,
            media,
            {"replyMarkup": reply_markup},
        )

    async def edit_inline_message_live_location(
        self,
        inline_message_id: str,
        latitude: Union[int, float],
        longitude: Union[int, float],
        *,
        horizontal_accuracy: Optional[Union[int, float]] = None,
        heading: Optional[Union[int, float]] = None,
        proximity_alert_radius: Optional[Union[int, float]] = None,
        reply_markup: Optional[ReplyMarkup] = None,
    ) -> None:
        await self._request(
            "editInlineMessageLiveLocation",
            inline_message_id,
            latitude,
            longitude,
            {
                "horizontalAccuracy": horizontal_accuracy,
                "heading": heading,
                "proximityAlertRadius": proximity_alert_radius,
                "replyMarkup": reply_markup,
            },
        )

    ########################### PAYMENTS ########################
    async def answer_pre_checkout_query(
        self, pre_checkout_query_id: str, ok: bool, *, error: Optional[str] = None
    ) -> None:
        await self._request(
            "answerPreCheckoutQuery", pre_checkout_query_id, ok, {"error": error}
        )

    async def refund_star_payment(
        self, user_id: ID, telegram_payment_charge_id: str
    ) -> None:
        await self._request("refundStarPayment", user_id, telegram_payment_charge_id)

    ########################### REACTIONS ########################
    async def add_reaction(
        self,
        chat_id: ID,
        message_id: int,
        reaction: Reaction,
        *,
        big: Optional[bool] = None,
        add_to_recents: Optional[bool] = None,
    ) -> None:
        await self._request(
            "addReaction",
            chat_id,
            message_id,
            reaction,
            {"big": big, "addToRecents": add_to_recents},
        )

    async def remove_reaction(
        self,
        chat_id: ID,
        message_id: int,
        reaction: Reaction,
    ) -> None:
        await self._request("removeReaction", chat_id, message_id, reaction)

    async def set_reactions(
        self,
        chat_id: ID,
        message_id: int,
        reactions: List[Reaction],
        *,
        big: Optional[bool] = None,
    ) -> None:
        await self._request(
            "setReactions",
            chat_id,
            message_id,
            reactions,
            {
                "big": big,
            },
        )

    ########################### STORIES ########################
    async def add_stories_to_highlights(
        self, chat_id: ID, story_ids: List[int]
    ) -> None:
        await self._request("addStoriesToHighlights", chat_id, story_ids)

    async def add_story_to_highlights(self, chat_id: ID, story_id: int) -> None:
        await self._request("addStoryToHighlights", chat_id, story_id)

    async def create_story(
        self,
        chat_id: ID,
        content: InputStoryContent,
        *,
        interactive_areas: Optional[StoryInteractiveArea] = None,
        privacy: Optional[StoryPrivacy] = None,
        active_for: Optional[int] = None,
        highlight: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        caption: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        parse_mode: Optional[ParseMode] = None,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
    ) -> Story:
        return to(
            Story,
            await self._request(
                "createStory",
                chat_id,
                content,
                {
                    "interactiveAreas": interactive_areas,
                    "privacy": privacy,
                    "activeFor": active_for,
                    "highlight": highlight,
                    "protectContent": protect_content,
                    "caption": caption,
                    "captionEntities": caption_entities,
                    "parseMode": parse_mode,
                    "fileName": file_name,
                    "mimeType": mime_type,
                    "chunkSize": chunk_size,
                },
            ),
            self,
        )

    async def delete_stories(self, chat_id: ID, story_ids: List[int]) -> None:
        await self._request("deleteStories", chat_id, story_ids, self)

    async def delete_story(self, chat_id: ID, story_id: int) -> None:
        await self._request("deleteStory", chat_id, story_id, self)

    async def get_stories(self, chat_id: ID, story_ids: List[int]) -> List[Story]:
        return to(
            List[Story], await self._request("getStories", chat_id, story_ids), self
        )

    async def get_story(self, chat_id: ID, story_id: int) -> Optional[Story]:
        return to(Story, await self._request("getStory", chat_id, story_id), self)

    async def remove_stories_from_highlights(
        self, chat_id: ID, story_ids: List[int]
    ) -> None:
        await self._request("removeStoriesFromHighlights", chat_id, story_ids)

    async def remove_story_from_highlights(self, chat_id: ID, story_id: int) -> None:
        await self._request("removeStoryFromHighlights", chat_id, story_id)

    ########################### UNLISTED ########################
    async def block_user(self, user_id: ID) -> None:
        await self._request("blockUser", user_id)

    async def unblock_user(self, user_id: ID) -> None:
        await self._request("unblockUser", user_id)

    async def get_network_statistics(self) -> NetworkStatistics:
        return to(NetworkStatistics, await self._request("getNetworkStatistics"), self)

    ########################### VIDEO CHATS ########################
    async def download_live_stream_chunk(
        self,
        id: str,
        channel_id: int,
        scale: Union[int, float],
        timestamp: Union[int, float],
        *,
        quality: Optional[Literal["low", "medium", "high"]] = None,
    ) -> AsyncGenerator[bytes, None]:
        async for chunk, _ in await self._request(
            "downloadLiveStreamChunk",
            id,
            channel_id,
            scale,
            timestamp,
            {"quality": quality},
        ):
            if chunk:
                yield chunk

    async def get_live_stream_channels(self, id: str) -> List[LiveStreamChannel]:
        return to(
            List[LiveStreamChannel],
            await self._request("getLiveStreamChannels", id),
            self,
        )

    async def get_video_chat(self, id: str) -> VideoChat:
        return to(VideoChat, await self._request("getVideoChat", id), self)

    async def join_live_stream(self, id: str) -> None:
        await self._request("joinLiveStream", id)

    async def join_video_chat(
        self,
        id: str,
        params: str,
        *,
        join_as: Optional[ID] = None,
        invite_hash: Optional[str] = None,
        audio: Optional[bool] = None,
        video: Optional[bool] = None,
    ) -> str:
        return await self._request(
            "joinVideoChat",
            id,
            params,
            {
                "joinAs": join_as,
                "inviteHash": invite_hash,
                "audio": audio,
                "video": video,
            },
        )

    async def leave_video_chat(self, id: str) -> None:
        await self._request("leaveVideoChat", id)

    async def schedule_video_chat(
        self,
        chat_id: ID,
        start_at: datetime.datetime,
        *,
        title: Optional[str] = None,
        live_stream: Optional[bool] = None,
    ) -> VideoChatScheduled:
        return to(
            VideoChatScheduled,
            await self._request(
                "scheduleVideoChat",
                chat_id,
                start_at,
                {"title": title, "liveStream": live_stream},
            ),
            self,
        )

    async def start_video_chat(
        self,
        chat_id: ID,
        *,
        title: Optional[str] = None,
        live_stream: Optional[bool] = None,
    ) -> VideoChatActive:
        return to(
            VideoChatActive,
            await self._request(
                "startVideoChat", chat_id, {"title": title, "liveStream": live_stream}
            ),
            self,
        )

    ########################### INLINE QUERIES ########################
    async def answer_inline_query(
        self,
        id: str,
        results: List[InlineQueryResult],
        *,
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        is_gallery: Optional[bool] = None,
        button: Optional[InlineQueryResultButton] = None,
    ) -> None:
        await self._request(
            "answerInlineQuery",
            id,
            results,
            {
                "cacheTime": cache_time,
                "isPersonal": is_personal,
                "nextOffset": next_offset,
                "isGallery": is_gallery,
                "button": button,
            },
        )

    async def send_inline_query(
        self,
        user_id: ID,
        chat_id: ID,
        *,
        query: Optional[str] = None,
        offset: Optional[str] = None,
    ) -> InlineQueryAnswer:
        return to(
            InlineQueryAnswer,
            await self._request(
                "sendInlineQuery", user_id, chat_id, {"query": query, "offset": offset}
            ),
            self,
        )

    ########################### FILES ########################
    async def download(
        self,
        file_id: str,
        *,
        chunk_size: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> AsyncGenerator[bytes, None]:
        async for chunk, _ in await self._request(
            "download", file_id, {"chunkSize": chunk_size, "offset": offset}
        ):
            if chunk:
                yield chunk

    async def get_custom_emoji_stickers(self, id: str | List["str"]) -> List[Sticker]:
        return to(
            List[Sticker], await self._request("getCustomEmojiStickers", id), self
        )

    ########################### CALLBACK QUERIES ########################
    async def answer_callback_query(
        self,
        id: str,
        *,
        text: Optional[str] = None,
        alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
    ) -> None:
        await self._request(
            "answerCallbackQuery",
            id,
            {"text": text, "alert": alert, "url": url, "cacheTime": cache_time},
        )

    async def send_callback_query(
        self, chat_id: ID, message_id: int, question: CallbackQueryQuestion
    ) -> CallbackQueryAnswer:
        return to(
            CallbackQueryAnswer,
            await self._request("sendCallbackQuery", chat_id, message_id, question),
            self,
        )

    ########################### BOTS ########################
    async def get_my_commands(self) -> List[BotCommand]:
        return to(List[BotCommand], await self._request("getMyCommands"), self)

    async def get_my_description(self, *, language_code: Optional[str] = None) -> str:
        return await self._request("getMyDescription", {"languageCode": language_code})

    async def get_my_name(self, *, language_code: Optional[str] = None) -> str:
        return await self._request("getMyName", {"languageCode": language_code})

    async def get_my_short_description(
        self, *, language_code: Optional[str] = None
    ) -> str:
        return await self._request(
            "getMyShortDescription", {"languageCode": language_code}
        )

    async def set_my_commands(
        self,
        commands: List[BotCommand],
        *,
        language_code: Optional[str] = None,
        scope: Optional[BotCommandScope] = None,
    ) -> None:
        await self._request(
            "setMyCommands", commands, {"languageCode": language_code, "scope": scope}
        )

    async def set_my_description(
        self,
        *,
        description: Optional[str] = None,
        language_code: Optional[str] = None,
    ) -> None:
        await self._request(
            "setMyDescription",
            {"description": description, "languageCode": language_code},
        )

    async def set_my_name(
        self,
        *,
        name: Optional[str] = None,
        language_code: Optional[str] = None,
    ) -> None:
        await self._request("setMyName", {"name": name, "languageCode": language_code})

    async def set_my_short_description(
        self,
        *,
        short_description: Optional[str] = None,
        language_code: Optional[str] = None,
    ) -> None:
        await self._request(
            "setMyShortDescription",
            {"shortDescription": short_description, "languageCode": language_code},
        )

    async def get_business_connection(self, id: str) -> BusinessConnection:
        return to(
            BusinessConnection, await self._request("getBusinessConnection", id), self
        )

    ########################### ACCOUNT ########################
    async def get_me(self) -> User:
        return to(User, await self._request("getMe"), self)

    async def hide_username(self, id: ID, username: str) -> None:
        await self._request("hideUsername", id, username)

    async def hide_usernames(self, id: ID) -> None:
        await self._request("hideUsernames", id)

    async def reorder_usernames(self, id: ID, order: List[str]) -> bool:
        return await self._request("reorderUsernames", id, order)

    async def show_username(self, id: ID, username: str) -> None:
        await self._request("showUsername", id, username)

    ########################### CHATS ########################
    async def ban_chat_member(
        self,
        chat_id: ID,
        member_id: ID,
        *,
        until_date: Optional[datetime.datetime] = None,
        delete_messages: Optional[bool] = None,
    ) -> None:
        await self._request(
            "banChatMember",
            chat_id,
            member_id,
            {"untilDate": until_date, "deleteMessages": delete_messages},
        )

    async def unban_chat_member(self, chat_id: ID, member_id: ID) -> None:
        await self._request("unbanChatMember", chat_id, member_id)

    async def create_invite_link(
        self,
        chat_id: ID,
        *,
        title: Optional[str] = None,
        expire_at: Optional[datetime.datetime] = None,
        limits: Optional[int] = None,
        require_approval: Optional[bool] = None,
    ) -> InviteLink:
        return to(
            InviteLink,
            await self._request(
                "createInviteLink",
                chat_id,
                {
                    "title": title,
                    "expireAt": expire_at,
                    "limit": limits,
                    "requireApproval": require_approval,
                },
            ),
            self,
        )

    async def delete_chat_photo(self, chat_id: ID) -> None:
        await self._request("deleteChatPhoto", chat_id)

    async def delete_chat_sticker_set(self, chat_id: ID) -> None:
        await self._request("deleteChatStickerSet", chat_id)

    async def disable_join_requests(self, chat_id: ID) -> None:
        await self._request("disableJoinRequests", chat_id)

    async def enable_join_requests(self, chat_id: ID) -> None:
        await self._request("enableJoinRequests", chat_id)

    async def get_chat(self, chat_id: ID) -> Chat:
        return to(Chat, await self._request("getChat", chat_id), self)

    async def get_chat_administrators(self, chat_id: ID) -> List[ChatMember]:
        return to(
            List[ChatMember],
            await self._request("getChatAdministrators", chat_id),
            self,
        )

    async def get_chat_member(self, chat_id: ID, user_id: ID) -> ChatMember:
        return to(
            ChatMember, await self._request("getChatMember", chat_id, user_id), self
        )

    async def get_chats(
        self,
        *,
        from_chat_list: Optional[Literal["main", "archived"]] = None,
        after: Optional[ChatListItem] = None,
        limit: Optional[int] = None,
    ) -> List[ChatListItem]:
        return to(
            List[ChatListItem],
            await self._request(
                "getChats", {"from": from_chat_list, "after": after, "limit": limit}
            ),
            self,
        )

    async def get_created_invite_links(
        self,
        chat_id: ID,
        *,
        by: Optional[ID] = None,
        limit: Optional[int] = None,
        revoked: Optional[bool] = None,
        after_date: Optional[datetime.datetime] = None,
        after_invite_link: Optional[str] = None,
    ) -> List[InviteLink]:
        return to(
            List[InviteLink],
            await self._request(
                "getCreatedInviteLinks",
                chat_id,
                {
                    "by": by,
                    "limit": limit,
                    "revoked": revoked,
                    "afterDate": after_date,
                    "afterInviteLink": after_invite_link,
                },
            ),
            self,
        )

    async def get_history(
        self,
        chat_id: ID,
        *,
        after: Optional[Message] = None,
        limit: Optional[int] = None,
    ) -> List[Message]:
        return to(
            List[Message],
            await self._request(
                "getHistory", chat_id, {"after": after, "limit": limit}
            ),
            self,
        )

    async def get_inactive_chats(
        self,
    ) -> List[InactiveChat]:
        return to(List[InactiveChat], await self._request("getInactiveChats"), self)

    async def join_chat(self, chat_id: ID) -> None:
        await self._request("joinChat", chat_id)

    async def leave_chat(self, chat_id: ID) -> None:
        await self._request("leaveChat", chat_id)

    async def kick_chat_member(self, chat_id: ID, member_id: ID) -> None:
        await self._request("kickChatMember", chat_id, member_id)

    async def set_available_reactions(
        self,
        chat_id: ID,
        available_reactions: Union[Literal["none", "all"], List[Reaction]],
    ) -> None:
        await self._request("setAvailableReactions", chat_id, available_reactions)

    async def set_boosts_required_to_circumvent_restrictions(
        self, chat_id: ID, boosts: int
    ) -> None:
        await self._request(
            "setBoostsRequiredToCircumventRestrictions", chat_id, boosts
        )

    async def set_chat_member_rights(
        self,
        chat_id: ID,
        member_id: ID,
        *,
        rights: Optional[ChatMemberRights] = None,
        until_date: Optional[datetime.datetime] = None,
    ) -> None:
        await self._request(
            "setChatMemberRights",
            chat_id,
            member_id,
            {"rights": rights, "untilDate": until_date},
        )

    async def set_chat_photo(
        self,
        chat_id: ID,
        photo: FileSource,
        *,
        file_name: Optional[str] = None,
        mime_type: Optional[str] = None,
        chunk_size: Optional[int] = None,
    ) -> None:
        await self._request(
            "setChatPhoto",
            chat_id,
            photo,
            {"fileName": file_name, "mimeType": mime_type, "chunkSize": chunk_size},
        )

    async def set_chat_sticker_set(self, chat_id: ID, set_name: str) -> None:
        await self._request("setChatStickerSet", chat_id, set_name)

    async def approve_join_request(self, chat_id: ID, user_id: ID) -> None:
        await self._request("approveJoinRequest", chat_id, user_id)

    async def approve_join_requests(
        self, chat_id: ID, invite_link: Optional[str] = None
    ) -> None:
        await self._request("approveJoinRequests", chat_id, {"inviteLink": invite_link})

    async def decline_join_request(self, chat_id: ID, user_id: ID) -> None:
        await self._request("declineJoinRequest", chat_id, user_id)

    async def decline_join_requests(
        self, chat_id: ID, invite_link: Optional[str] = None
    ) -> None:
        await self._request("declineJoinRequests", chat_id, {"inviteLink": invite_link})

    async def add_chat_member(
        self, chat_id: ID, user_id: ID, history_limit: Optional[int] = None
    ) -> FailedInvitation:
        return to(
            FailedInvitation,
            await self._request(
                "addChatMember", chat_id, user_id, {"historyLimit": history_limit}
            ),
            self,
        )

    async def add_chat_members(
        self,
        chat_id: ID,
        user_ids: List[ID],
    ) -> List[FailedInvitation]:
        return to(
            List[FailedInvitation],
            await self._request("addChatMembers", chat_id, user_ids),
            self,
        )

    async def open_chat(
        self,
        chat_id: ID,
    ) -> None:
        await self._request("openChat", chat_id)

    async def close_chat(
        self,
        chat_id: ID,
    ) -> None:
        await self._request("closeChat", chat_id)

    async def get_chat_members(
        self, chat_id: ID, *, offset: Optional[int] = None, limit: Optional[int] = None
    ) -> List[ChatMember]:
        return to(
            List[ChatMember],
            await self._request(
                "getChatMembers", chat_id, {"offset": offset, "limit": limit}
            ),
            self,
        )


T = TypeVar("T")
HandlerCallback = Callable[[Client, T], Coroutine[Any, Any, None]]


class Handler(Generic[T]):
    def __init__(self, filter_: Callable[[Update], bool], callback: HandlerCallback[T]):
        self.filter = filter_
        self.callback = callback


AnyHandler = Handler[Any]


class NewMessageHandler(Handler[UpdateNewMessage]):
    def __init__(
        self, callback_: HandlerCallback[Any], filter_: Optional[Filter] = None
    ):
        async def callback(client: Client, update: UpdateNewMessage) -> None:
            await callback_(client, update.message)

        super().__init__(
            lambda update: (
                isinstance(update, UpdateNewMessage) and True
                if filter_ is None
                else filter_(cast(UpdateNewMessage, update).message)
            ),
            callback,
        )


class EditedMessageHandler(Handler[UpdateMessageEdited]):
    def __init__(
        self, callback_: HandlerCallback[Any], filter_: Optional[Filter] = None
    ):
        async def callback(client: Client, update: UpdateMessageEdited) -> None:
            await callback_(client, update.edited_message)

        super().__init__(
            lambda update: (
                isinstance(update, UpdateMessageEdited) and True
                if filter_ is None
                else filter_(cast(UpdateMessageEdited, update).edited_message)
            ),
            callback,
        )


class DeletedMessagesHandler(Handler[UpdateMessagesDeleted]):
    def __init__(self, callback_: HandlerCallback[UpdateMessagesDeleted]):
        async def callback(client: Client, update: UpdateMessagesDeleted) -> None:
            await callback_(client, update)

        super().__init__(
            lambda update: isinstance(update, UpdateMessagesDeleted), callback
        )


class CallbackQueryHandler(Handler[UpdateCallbackQuery]):
    def __init__(self, callback_: HandlerCallback[CallbackQuery]):
        async def callback(client: Client, update: UpdateCallbackQuery) -> None:
            await callback_(client, update.callback_query)

        super().__init__(
            lambda update: isinstance(update, UpdateCallbackQuery), callback
        )


class InlineQueryHandler(Handler[UpdateInlineQuery]):
    def __init__(self, callback_: HandlerCallback[InlineQuery]):
        async def callback(client: Client, update: UpdateInlineQuery) -> None:
            await callback_(client, update.inline_query)

        super().__init__(lambda update: isinstance(update, UpdateInlineQuery), callback)


class ChosenInlineResultHandler(Handler[UpdateChosenInlineResult]):
    def __init__(self, callback_: HandlerCallback[ChosenInlineResult]):
        async def callback(client: Client, update: UpdateChosenInlineResult) -> None:
            await callback_(client, update.chosen_inline_result)

        super().__init__(
            lambda update: isinstance(update, UpdateChosenInlineResult), callback
        )


class NewChatHandler(Handler[UpdateNewChat]):
    def __init__(self, callback_: HandlerCallback[ChatListItem]):
        async def callback(client: Client, update: UpdateNewChat) -> None:
            await callback_(client, update.new_chat)

        super().__init__(lambda update: isinstance(update, UpdateNewChat), callback)


class EditedChatHandler(Handler[UpdateEditedChat]):
    def __init__(self, callback_: HandlerCallback[ChatListItem]):
        async def callback(client: Client, update: UpdateEditedChat) -> None:
            await callback_(client, update.edited_chat)

        super().__init__(lambda update: isinstance(update, UpdateEditedChat), callback)


class DeletedChatHandler(Handler[UpdateDeletedChat]):
    def __init__(self, callback_: HandlerCallback[int]):
        async def callback(client: Client, update: UpdateDeletedChat) -> None:
            await callback_(client, update.deleted_chat.chat_id)

        super().__init__(lambda update: isinstance(update, UpdateDeletedChat), callback)


class MessageInteractionsHandler(Handler[UpdateMessageInteractions]):
    def __init__(self, callback_: HandlerCallback[MessageInteractions]):
        async def callback(client: Client, update: UpdateMessageInteractions) -> None:
            await callback_(client, update.message_interactions)

        super().__init__(
            lambda update: isinstance(update, UpdateMessageInteractions), callback
        )


class MessageReactionCountHandler(Handler[UpdateMessageReactionCount]):
    def __init__(self, callback_: HandlerCallback[MessageReactionCount]):
        async def callback(client: Client, update: UpdateMessageReactionCount) -> None:
            await callback_(client, update.message_reaction_count)

        super().__init__(
            lambda update: isinstance(update, UpdateMessageReactionCount), callback
        )


class MessageReactionsHandler(Handler[UpdateMessageReactions]):
    def __init__(self, callback_: HandlerCallback[MessageReactions]):
        async def callback(client: Client, update: UpdateMessageReactions) -> None:
            await callback_(client, update.message_reactions)

        super().__init__(
            lambda update: isinstance(update, UpdateMessageReactions), callback
        )


class ChatMemberHandler(Handler[UpdateChatMember]):
    def __init__(self, callback_: HandlerCallback[ChatMemberUpdated]):
        async def callback(client: Client, update: UpdateChatMember) -> None:
            await callback_(client, update.chat_member)

        super().__init__(lambda update: isinstance(update, UpdateChatMember), callback)


class MyChatMemberHandler(Handler[UpdateMyChatMember]):
    def __init__(self, callback_: HandlerCallback[ChatMemberUpdated]):
        async def callback(client: Client, update: UpdateMyChatMember) -> None:
            await callback_(client, update.my_chat_member)

        super().__init__(
            lambda update: isinstance(update, UpdateMyChatMember), callback
        )


class DeletedStoryHandler(Handler[UpdateDeletedStory]):
    def __init__(self, callback_: HandlerCallback[StoryReference]):
        async def callback(client: Client, update: UpdateDeletedStory) -> None:
            await callback_(client, update.deleted_story)

        super().__init__(
            lambda update: isinstance(update, UpdateDeletedStory), callback
        )


class NewStoryHandler(Handler[UpdateNewStory]):
    def __init__(self, callback_: HandlerCallback[Story]):
        async def callback(client: Client, update: UpdateNewStory) -> None:
            await callback_(client, update.story)

        super().__init__(lambda update: isinstance(update, UpdateNewStory), callback)


class BusinessConnectionHandler(Handler[UpdateBusinessConnection]):
    def __init__(self, callback_: HandlerCallback[BusinessConnection]):
        async def callback(client: Client, update: UpdateBusinessConnection) -> None:
            await callback_(client, update.business_connection)

        super().__init__(
            lambda update: isinstance(update, UpdateBusinessConnection), callback
        )


class VideoChatHandler(Handler[UpdateVideoChat]):
    def __init__(self, callback_: HandlerCallback[VideoChat]):
        async def callback(client: Client, update: UpdateVideoChat) -> None:
            await callback_(client, update.video_chat)

        super().__init__(lambda update: isinstance(update, UpdateVideoChat), callback)


class PreCheckoutQueryHandler(Handler[UpdatePreCheckoutQuery]):
    def __init__(self, callback_: HandlerCallback[PreCheckoutQuery]):
        async def callback(client: Client, update: UpdatePreCheckoutQuery) -> None:
            await callback_(client, update.pre_checkout_query)

        super().__init__(
            lambda update: isinstance(update, UpdatePreCheckoutQuery), callback
        )


class JoinRequestHandler(Handler[UpdateJoinRequest]):
    def __init__(self, callback_: HandlerCallback[JoinRequest]):
        async def callback(client: Client, update: UpdateJoinRequest) -> None:
            await callback_(client, update.join_request)

        super().__init__(lambda update: isinstance(update, UpdateJoinRequest), callback)
