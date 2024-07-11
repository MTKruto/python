import datetime
from typing import List, Literal, Optional, Union

from ._client import Client
from .types import (
    ID,
    ChatAction,
    ChatMember,
    ChatMemberRights,
    FileSource,
    InlineQueryResult,
    InlineQueryResultButton,
    InputMedia,
    InviteLink,
    LinkPreview,
    Message,
    MessageAnimation,
    MessageAudio,
    MessageContact,
    MessageDice,
    MessageDocument,
    MessageEntity,
    MessageLocation,
    MessagePhoto,
    MessagePoll,
    MessageSticker,
    MessageText,
    MessageVenue,
    MessageVideo,
    MessageVideoNote,
    MessageVoice,
    ParseMode,
    Poll,
    Reaction,
    ReplyMarkup,
    ReplyQuote,
    ReplyToMessage,
    SelfDestructOption,
)
from .types import CallbackQuery as _CallbackQuery_
from .types import InlineQuery as _InlineQuery_
from .types import User as _User_
from .types import _ChatPBase as _ChatPBase_
from .types import _MessageBase as _MessageBase_


class User(_User_):
    _client: Client

    # extend User

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

    # endextend


class _ChatPBase(_ChatPBase_):
    _client: Client

    # extend _ChatPBase

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

    # endextend


class InlineQuery(_InlineQuery_):
    _client: Client

    # extend InlineQuery
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

    # endextend


class CallbackQuery(_CallbackQuery_):
    _client: Client

    # extend CallbackQuery
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

    # endextend


class _MessageBase(_MessageBase_):
    _client: Client

    # extend _MessageBase

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

    # endextend
