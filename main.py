
#import ast
import os
#import json
import telebot 
from text import *
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from links import *
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
state_storage = StateMemoryStorage()
my_secret="5953623379:AAGfAJS7UiiMK4MEWYXyBvbWqTNZZ4Anl1Y"
bot = telebot.TeleBot(my_secret,state_storage=state_storage)

class MyStates(StatesGroup):
  title = State() 
  user_id = State()
def gen_markup():
  buttons = [[InlineKeyboardButton('Featured Channel ®️', url='https://t.me/DevSavior')],
             [InlineKeyboardButton('Lets Start ➡️', callback_data='start')]]
  m = InlineKeyboardMarkup(buttons)
  return m
def gen_markup2():
  buttons = [[InlineKeyboardButton('⚙️Setting⚙️', callback_data='setting')],
[InlineKeyboardButton('Set Title ✍️',callback_data='title')],            [InlineKeyboardButton('Send Links 🔗', callback_data='links')]]
  m = InlineKeyboardMarkup(buttons)
  return m
def gen_markup3():
  buttons = [[InlineKeyboardButton('HTML Links', callback_data='0')],
             [
               InlineKeyboardButton('1 In Row', callback_data='1'),
               InlineKeyboardButton('2 In Row', callback_data='2')
             ], [InlineKeyboardButton('🔙Back🔙 ', callback_data='back')]]
  m = InlineKeyboardMarkup(buttons)
  return m
def gen_markup4():
  buttons = [[InlineKeyboardButton('HTML Links ', callback_data='0')],
             [
               InlineKeyboardButton('1 In Row✅', callback_data='1'),
               InlineKeyboardButton('2 In Row', callback_data='2')
             ], [InlineKeyboardButton('Back', callback_data='back')]]
  m = InlineKeyboardMarkup(buttons)
  return m


def gen_markup5():
  buttons = [[InlineKeyboardButton('HTML Links', callback_data='0')],
             [
               InlineKeyboardButton('1 In Row', callback_data='1'),
               InlineKeyboardButton('2 In Row✅', callback_data='2')
             ], [InlineKeyboardButton('Back', callback_data='back')]]
  m = InlineKeyboardMarkup(buttons)
  return m


def set_title(m, jj):
 bot.set_state(m, MyStates.title)
 with bot.retrieve_data(m) as data:
   data['title'] =title
   data['id'] = ide
def gen_markup6():
  buttons = [[InlineKeyboardButton('HTML Links 🔜', callback_data='0')],
             [
               InlineKeyboardButton('1 In Row', callback_data='1'),
               InlineKeyboardButton('2 In Row', callback_data='2')
             ], [InlineKeyboardButton('Back', callback_data='back')]]
  m = InlineKeyboardMarkup(buttons)
  return m


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  # print (call)
  if call.data == "start": 
   #text2=" I am Not Complicated 😀 \n👉To Begin With \n •Give A title To Your Links using Title Button \n•Default Setting Is Set To (1 button in row )You Can Change It In Settings \n •You Can Forward Any Link and I will Convert It Into Button"
   bot.edit_message_text(message_id=v.id,
chat_id=call.from_user.id,text=setting, reply_markup=gen_markup2())
  elif call.data =="No":
    bot.send_message(v.chat.id, "Answer Is No")
  elif call.data == "links":
    bot.edit_message_text(message_id=v.id,
                          chat_id=call.from_user.id,
                          text=links_txt)
    
  elif call.data == 'setting':
    bot.edit_message_text(message_id=v.id,
                          chat_id=v.chat.id,
                          text=row_num,
                          reply_markup=gen_markup3())
  elif call.data == 'back':
    jj = call.data
    #snd_cl(call.from_user.id, jj)
    bot.edit_message_text(message_id=v.id,
                          chat_id=v.chat.id,
                          text=setting,
                          reply_markup=gen_markup2())

  elif call.data == '1':
    jj = call.data
   # snd_cl(call.from_user.id, jj)
   # print(jj)
    cream(jj)
    bot.edit_message_reply_markup(message_id=v.id,
                                  chat_id=v.chat.id,
                                  reply_markup=gen_markup4())
  elif call.data == '2':
    jj = call.data
   # snd_cl(call.from_user.id, jj)
    cream(jj)
    #  snd_cl(call)

    bot.edit_message_reply_markup(message_id=v.id,
                                  chat_id=v.chat.id,
                                  reply_markup=gen_markup5())
  elif call.data == '0':
    jj = call.data
    bot.answer_callback_query(call.id,show_alert=True,text="Not Supporred Yet")   
  
    bot.edit_message_reply_markup(message_id=v.id,
                                  chat_id=v.chat.id,
                                  reply_markup=gen_markup6()) 



  elif call.data=='title':  
    bot.set_state(call.from_user.id,MyStates.user_id,call.from_user.id) 
    bot.send_message (call.from_user.id, "💡 Send Title For Your Message In One Line")
   
@bot.message_handler(state=MyStates.user_id)
def name_get(message):
    """
    State 1. Will process when user's state is MyStates.name.
    """ 
    bot.reply_to(message, "Title Added")
    bot.send_message(message.chat.id, links_txt)
    bot.set_state(message.from_user.id, MyStates.title, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['title'] = message.text 
        htitle=message.text
     
#print (MyStates)


@bot.message_handler(commands=['start','help'])
def reply(m):
  try:
   user_name= m.from_user.first_name+" "+m.from_user.last_name 
  except TypeError:
    user_name=m.from_user.first_name 
  except TypeError:
    user_name=m.from_user.last_name 
  except TypeError:
    user_name="user"
  #print (user_name) 
  message="👋 Hey There<b> "+user_name+" !\n •) Welcome To Link Styler Bot 🎉</b>\n •) I Can Convert Links Into Button \n •) I Was Specially Designed For The Channel That Share Episode Wise Serials, Dramas, Or Web Series \n •) Want to give your channel a fresh look with some customized links and buttons?⤵️"
  bot.delete_message(message_id=m.id,chat_id=m.chat.id)
  global v 
  v = bot.send_message(m.chat.id,message, reply_markup=gen_markup(),parse_mode='Html') 
  bot.delete_state(m.from_user.id, m.chat.id)




# print (v)
@bot.message_handler(content_types=['photo','text'])
def vvv(m): 
   
  if m.photo==None:
    text=m.text 
    try:
     with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
      bv=data['title'] 
    except :
      bv="Here Are Your Links"
     #print (bv)
    bot.send_message (m.chat.id,text=bv,reply_markup=btn(text,bv))
  else :
    photo_id=m.json['photo'][0]['file_id'] 
    try:
     with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
      bv=data['title'] 
    except: 
      bv="Here Are Your Pinks"
    text=m.caption 
    bot.send_photo(m.chat.id,photo=photo_id,caption=bv,reply_markup=btn(text, bv)) 

bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
bot.infinity_polling(skip_pending=True)

