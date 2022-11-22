# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import telebot
from telebot import types

bot = telebot.TeleBot('5800705162:AAEbqHDixeIFqBkSSt2cni8hlNIWSHjHAOc')
expr = ''
numbers = types.InlineKeyboardMarkup()
numbers.row(
    types.InlineKeyboardButton(text = '(', callback_data='('),
    types.InlineKeyboardButton(text = ')', callback_data=')'),
    types.InlineKeyboardButton(text = '<-', callback_data='<-'))
numbers.row(
    types.InlineKeyboardButton(text = '7', callback_data='7'),
    types.InlineKeyboardButton(text = '8', callback_data='8'),
    types.InlineKeyboardButton(text = '9', callback_data='9'),
    types.InlineKeyboardButton(text = '/', callback_data='/'))
numbers.row(
    types.InlineKeyboardButton(text = '4', callback_data='4'),
    types.InlineKeyboardButton(text = '5', callback_data='5'),
    types.InlineKeyboardButton(text = '6', callback_data='6'),
    types.InlineKeyboardButton(text = '*', callback_data='*')
)
numbers.row(
    types.InlineKeyboardButton(text = '1', callback_data='1'),
    types.InlineKeyboardButton(text = '2', callback_data='2'),
    types.InlineKeyboardButton(text = '3', callback_data='3'),
    types.InlineKeyboardButton(text = '-', callback_data='-')
)
numbers.row(
    types.InlineKeyboardButton(text = '0', callback_data='0'),
    types.InlineKeyboardButton(text = '.', callback_data='.'),
    types.InlineKeyboardButton(text = '=', callback_data='='),
    types.InlineKeyboardButton(text = '+', callback_data='+')
)
@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id, 'Write a mathematical expression')


@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text == '/help':
        bot.send_message(message.from_user.id, f'Привет! \nНапиши мне какое-нибудь математическое выражение через /calc, '
                                               f'и я дам тебе ответ')

    elif message.text == '/calc':
        global expr
        try:
            bot.send_message(message.from_user.id, text=expr, reply_markup=numbers)
        except:
            bot.send_message(message.from_user.id, text='0', reply_markup=numbers)

    else:
        bot.send_message(message.chat.id, f'Попробуй еще раз через /calc')


@bot.callback_query_handler(func=lambda call: True)
def analizer(query):
    global expr
    data = query.data
    if data == '<-':
        expr = ''
    elif data == '=':
        try:
            expr = str(eval(expr))
        except:
            expr = 'Error'
    else:
        expr+=data
    if expr == '':
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text = '0', reply_markup=numbers)
    else:
        bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text=expr, reply_markup=numbers)

bot.polling(none_stop=True, interval=0)