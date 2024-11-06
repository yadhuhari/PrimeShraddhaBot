#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
import random

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = caption,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'Developers', url="https://t.me/CrazyBotsz"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode=enums.ParseMode.HTML)
            LOGGER(__name__).error(e)
        return
    await bot.reply_photo(
        chat_id=update.chat.id,
        photo=random.choice(PICS),
        caption=f"""<b> Hᴇʏ ᴛʜᴇʀᴇ {update.from_user.mention} 👋,

Mʏ Nᴀᴍᴇ Is Sʜʀᴀᴅᴅʜᴀ Kᴀᴘᴏᴏʀ ✨

I Aᴍ ᴀ Mᴏᴠɪᴇ Pʀᴏᴠɪᴅɪɴɢ Mᴀᴄʜɪɴᴇ Fᴏʀ Pʀɪᴍᴇ Mᴏᴠɪᴇᴢ Gʀᴏᴜᴘs, Oɴʟʏ Aᴜᴛʜᴏʀɪᴢᴇᴅ Aᴅᴍɪɴs Cᴀɴ Usᴇ Mᴇ Sᴏ Dᴏɴ'ᴛ Wᴀsᴛᴇ Yᴏᴜʀ Tɪᴍᴇ 😁

◈ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ :- @PrimeXLinkzz </b>""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ ✨", url="t.me/PrimeXLinkzz"),
            ],[
            InlineKeyboardButton("Hᴇʟᴘ ⚙️", callback_data="help"),
            InlineKeyboardButton("Aʙᴏᴜᴛ 🤠", callback_data="about"),
            ],[
            InlineKeyboardButton("Dᴇᴠᴇʟᴏᴘᴇʀ 💀", url="t.me/YourPrimeTG")
            ]]
            )
        )
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Hᴏᴍᴇ 🏡', callback_data='start'),
        InlineKeyboardButton('Aʙᴏᴜᴛ 🤠', callback_data='about')
    ],[
        InlineKeyboardButton('Cʟᴏsᴇ ⛔', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.reply_photo(
        chat_id=update.chat.id,
        photo=random.choice(PICS),
        caption=f"""<b> Hᴇʏ {update.from_user.mention} 👋,
        
 Sᴇᴇ Yᴏᴜ Iɴ Gʀᴏᴜᴘ കുട്ടാ..😁 </b>""",
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Hᴏᴍᴇ 🏡', callback_data='start'),
        InlineKeyboardButton('Cʟᴏsᴇ ⛔', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.reply_photo(
        chat_id=update.chat.id,
        photo=random.choice(PICS),
        caption=f"""<b> Hᴇʏ {update.from_user.mention} 👋,
         
✯ Mʏ Nᴀᴍᴇ : [Sʜʀᴀᴅᴅʜᴀ Kᴀᴘᴏᴏʀ](t.me/PrimeShraddhaBot)
✯ Dᴇᴠᴇʟᴏᴘᴇʀ : [𓊈𒆜 𝙼𝚛.ᴘʀɪᴍᴇ 𝚃𝙶 𒆜𓊉](t.me/YourPrimeTG)
✯ Lᴀɴɢᴜᴀɢᴇ : [Pʏᴛʜᴏɴ 3.13.0](www.python.org)
✯ Lɪʙʀᴀʀʏ : [Pʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org/)
✯ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ : [Pʀɪᴍᴇ Lɪɴᴋᴢᴢ ✨](t.me/PrimeXLinkzz)
✯ Sᴇʀᴠᴇʀ : Sᴏᴍᴇᴡʜᴇʀᴇ
✯ Dᴀᴛᴀʙᴀsᴇ : [Mᴏɴɢᴏ DB](www.mongodb.com) </b>""",
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
        reply_to_message_id=update.id
    )
