import os
import telebot

bot = telebot.TeleBot("5854556657:AAEuvckfEVkdGVOF0N22A1xpc3Kgk3fGG8M")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message,"Hello! This 🤖 Will Help To Manage Your Groups")

@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message, "https://www.youtube.com/channel/UCtsdiCF3xGQ_BdEzJKicpLQ")


bot.polling()