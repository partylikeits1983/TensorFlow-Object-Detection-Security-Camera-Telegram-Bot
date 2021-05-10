from datetime import date, time, tzinfo, timezone, datetime
import datetime
import pytz
import schedule
import time

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import json
import pandas as pd
import numpy as np

import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

import glob
import os


json_file = open("config.json")
variables = json.load(json_file)
json_file.close()
TOKEN = variables["TOKEN"]
chat_id = variables["chat_id"]

path = variables["path"]


bot = telegram.Bot(TOKEN)
updater = Updater(TOKEN)

def start():
	print('hello')

def faces():
	print('faces')

def facedetect():
	print('facedt')

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
    	list_of_files = glob.glob('%s/images/*.jpg' % (path))
    	latest_file = max(list_of_files, key=os.path.getctime)
    	print(latest_file)
    	bot.send_photo(chat_id=chat_id, photo=open(latest_file, 'rb'), caption='Motion Detected')
    	time.sleep(2)


if __name__ == "__main__":
    run()
