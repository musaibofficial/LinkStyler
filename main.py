#import requests 
import telebot 
#url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQDGJFA3YSUBaJkF5yo0P_nzleEOqFGUYqgw&usqp=CAU'
#r=requests.get(url, allow_redirects=True)
"""open('facebook.png', 'wb').write(r.content)
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('facebook.png', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'PSquEhkKqaBjLFwGFQoFaNax'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
        f=response.content 
else:"""
  #  print("Error:", response.status_code, response.text) 
bot=telebot.TeleBot('5989308938:AAFrPoIHzm3KlIlPCsIIVQEu0uGd9RtmDb4')
@bot.message_handler(commands=['start'])
def cry(m):
  bot.reply_to(m, 'Hi Sending')
 # bot.send_photo(m.chat.id,f)
bot.infinity_polling ()

