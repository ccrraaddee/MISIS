import requests
import telebot

bot = telebot.TeleBot('5800705162:AAEbqHDixeIFqBkSSt2cni8hlNIWSHjHAOc')

def status_check(url):
    try:
        r = requests.head(url).status_code
        if r == 200:
        	return "very cool"
        else:
        	return "not cool"
    except:
        return  "not cool"


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/checksite':
        bot.send_message(message.from_user.id, "hello enter url pls")
        bot.register_next_step_handler(message, get_status)
    else:
        bot.send_message(message.from_user.id, ' enter /checksite')

def get_status(site): 
    answer = status_check(site.text)
    bot.send_message(site.from_user.id, answer)
    bot.register_next_step_handler(site, get_status)


bot.polling(none_stop=True, interval=0)