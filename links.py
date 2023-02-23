import os 
from telebot import *
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup 
my_secret ="5953623379:AAGfAJS7UiiMK4MEWYXyBvbWqTNZZ4Anl1Y"
bot = telebot.TeleBot(my_secret)
def cream(row_lengt):
  global row_length2 
  row_length2=row_lengt
def btn(m,bv): 
#  global sorted
 sorted=m.split()
 def srt_link(x):
  return x.startswith("https" or "www.") 
 #global get_links
 get_links= filter(srt_link,sorted)
 #global var 
 var=[]
 sar=[]
 for i,x in enumerate(get_links,start=1):
  anc=f"<a href={str(x)}> {str(i)}</a>"
  by=f"InlineKeyboardButton('{str(i) }',url='{str(x)}')"
  bytt=eval(by)
  var.append(bytt)
 # bb2=eval(anc)
  sar.append(anc) 
 #print (sar)
 global zz 
 zz=len(var)
 li =','.join(map(str,var))
 li2=' '.join(map(str,sar))
 res = [] 
 NewList= [[x] for x in var]
 list1=[]
 list2=[]
 for x in range(zz):
  if x%2==0:
   list1.append(var[x])
  else:
   list2.append(var[x])
 global list4
 list4=[]
 length1=len(list1)
 length2=len(list2)
 if length1>=length2:
  length=length1 
 else:
  length=length2 
 try:
  for i in range(length):
   list4.append([list1[i],list2[i]]) 
 except IndexError:
   list4.append([list1[i]])
 try:
  row_length=row_length2 
# print (row_length)
 except NameError:
  row_length="2"
 #except NameError:
   #row_length=1
 if row_length =="1":
  legth=NewList 
  #bot.send_message(m.chat.id," ",reply_markup=btn(m))
 else :
  legth=list4 
 mv=InlineKeyboardMarkup(legth)
 return mv 
#def html(jj):
  
