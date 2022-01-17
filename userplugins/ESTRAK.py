import requests,telebot

token = '{BOT_TOKEN}'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        ch = 'MAMO246@'
        idd = message.chat.id
        join = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{ch}&user_id={idd}").text
        if '"status":"left"' in join:
            bot.send_message(message.chat.id, f'''
🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- @{ch}

‼️| اشترك ثم ارسل /start
'''
        else:
            bot.send_message(message.chat.id,"اهلا")

bot.polling()
