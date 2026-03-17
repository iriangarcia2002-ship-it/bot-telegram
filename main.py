from telethon import TelegramClient, events

# 🔑 PON TUS DATOS AQUÍ
api_id = 26113215
api_hash = "a3c58753c6bc0d05fedc8f228e54a40e"

# 👇 nombre de sesión (déjalo así)
client = TelegramClient('bot', api_id, api_hash)

# 👇 CAMBIA POR TU CANAL
CANAL = "electricaempresacva"

@client.on(events.NewMessage(chats=CANAL))
async def handler(event):
    await event.reply("Mensaje recibido 🔥")

client.start()
client.run_until_disconnected()
