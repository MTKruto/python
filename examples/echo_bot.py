import asyncio

from mtkruto import Client, filters
from mtkruto.types import Message, MessageText

bot_token = "4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc"
client = Client(f"http://localhost:8000/bot{bot_token}")


@client.on_new_message(filters.text)
async def handle_text_message(_client: Client, message: MessageText) -> None:
    await message.reply(message.text)


@client.on_new_message(~filters.text)
async def handle_non_text_message(_client: Client, message: Message) -> None:
    await message.reply("Say what")


async def main() -> None:
    me = await client.get_me()
    print("Running as", me.username)
    await client.start()


asyncio.get_event_loop().run_until_complete(main())
