from telethon import TelegramClient, events

api_id = 26113215
api_hash = "a3c58753c6bc0d05fedc8f228e54a40e"

client = TelegramClient('bot', api_id, api_hash)

source_channel = "eecav"
target_channel = "electricaempresacva"

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
    await client.send_message(target_channel, event.message)

client.start()
client.run_until_disconnected()
