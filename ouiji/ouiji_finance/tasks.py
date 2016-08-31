from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

import socket
import requests
import pickle
import struct
import os

TCP_IP='127.0.0.1'
TCP_PORT=2004
BUFFER_SIZE=1024

api_key = 'b52f7fea9c12806f2b3353ac43a1df6f'
api_url = 'http://marketdata.websol.barchart.com/'
symbol = 'lmt'
logger = get_task_logger(__name__)
print("task is being ran")
@periodic_task(
	run_every=(crontab(minute='*/5')),
	name="task_save_latest_stock_price",
	ignore_result=True
	)
def task_save_latest_stock_price():
	"""saves the latest stock price"""
	"""send price to graphtie"""
	r = requests.get(api_url+'getQuote.json?key='+api_key+'&symbols='+symbol)
	price = r.json()['results'][0]['lastPrice']
	date = r.json()['results'][0]['tradeTimestamp']
	# listOfMetricTuples = [("lmt.stock",(date, price))]
	# payload = pickle.dumps(listOfMetricTuples, protocol=2)
	# header = struct.pack("!L", len(payload))
	# message = header + payload
	# logger.info(listOfMetricTuples)
	# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# s.connect((TCP_IP, TCP_PORT))
	# logger.info("Saved data from lmt")
	# s.send(message)
	# data = s.recv(BUFFER_SIZE)
	# s.close()
	os.system('echo "quote.lmt {0} `date +%s`" | nc  -q0 127.0.0.1 2003'.format(price))
