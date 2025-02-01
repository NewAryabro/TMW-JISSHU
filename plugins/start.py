from pyrogram import Client, filters

@Client.on_message(filters.command("start"))
async def start(client, message):
    # Send a sticker (Replace with your sticker's file ID)
    await message.reply_sticker("CAACAgUAAxkBAAENrtNnnRYe5Rf20X2TGSVCgCcJPuu9TwACCRIAAodi6FRXONeJ6WO6qDYE")  # Replace with your sticker's file ID
    
    # Send a welcome message
    await message.reply_text("Hello! I am your bot. How can I assist you today?")
