'''This code is currently being developed and does not currently work'''

from datetime import date, time, tzinfo, timezone, datetime
import datetime
import pytz
import schedule
import time

import json
import pandas as pd
import numpy as np

import glob
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

json_file = open("config.json")

variables = json.load(json_file)
json_file.close()

path = variables["path"]

TOKEN = variables["TOKEN"]
chat_id = variables["chat_id"]

bot = telegram.Bot(TOKEN)
updater = Updater(TOKEN)


def start(update: Update, context: CallbackContext) -> None:
	context.bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)

	keyboard = [['/status', '/faces', '/RunFaceDetection']]

	reply_markup = telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
	bot.sendMessage(update.message.chat_id, text='Telegram Bot Running', reply_markup=reply_markup)



def faces(update, context):
	context.bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)

	list_of_files = glob.glob('%s/faces/*.jpg' % (path)
    	latest_file = max(list_of_files, key=os.path.getctime)

	caption = "Detected Faces {}".format(today)
	bot.send_photo(chat_id=chat_id, photo=open(latest_file, 'rb'), caption='Motion Detected')
				  
				  
				  
def facedetect(update, context):
	context.bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
	
	text = 'Running face detection script.'
				  
        bot.send_message(chat_id, text)	
				  
	os.system("%s/face.py 1" % (path))
				  

def run():
	updater = Updater(TOKEN, use_context=True)
	dispatcher = updater.dispatcher
	
	dispatcher.add_handler(CommandHandler("start", start))
	dispatcher.add_handler(CommandHandler("faces", faces))
	dispatcher.add_handler(CommandHandler("RunFaceDetection", facedetect))
	
	observer = Observer()
	pathimages = ('%s/images' % (path))

	event_handler = Handler()
	observer.schedule(event_handler, pathimages, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(1)
	except:
		observer.stop()
		print("Error")

	observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
    	list_of_files = glob.glob('%s/images/*.jpg' % (path)
    	latest_file = max(list_of_files, key=os.path.getctime)
    	print(latest_file)
    	bot.send_photo(chat_id=chat_id, photo=open(latest_file, 'rb'), caption='Motion Detected')
    	time.sleep(2)
    	
 

if __name__ == "__main__":
    run()
