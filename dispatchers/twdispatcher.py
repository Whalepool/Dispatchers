import coloredlogs, logging
import zmq
import json  
import yaml
import sys
import os 
import coloredlogs, logging
import tweepy
from pprint import pprint
from .utils import DispatchUtils

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

class TWDispatcher( DispatchUtils ): 

	def __init__(self):



		self.PATH 			 = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
		self.config_file = "{}/config.yaml".format(self.PATH)
		logger = logging.getLogger(__name__)

		logger.info('Running TWdispatcher  in '+self.PATH)

		logger.info( "Loading config {}".format(self.config_file) ) 
		with open(self.config_file) as fp:
			self.config = yaml.load(fp, Loader=yaml.BaseLoader)

		auth = tweepy.OAuthHandler(self.config['TWITTER_CONSUMER_KEY'], self.config['TWITTER_CONSUMER_SECRET'])
		auth.set_access_token(self.config['TWITTER_ACCESS_TOKEN'], self.config['TWITTER_ACCESS_TOKEN_SECRET'])

		self.api = tweepy.API(auth)
		self.user = self.api.me()


	def listen_zmq_commands(self): 

		#####################################
		logger.info('Connecting to zmq')
		context = zmq.Context()
		consumer_receiver = context.socket(zmq.SUB)
		consumer_receiver.connect('tcp://127.0.0.1:'+str(self.config['ZMQ_XPUB_PORT']))
		consumer_receiver.setsockopt_string(zmq.SUBSCRIBE, 'telegram')

		while True:
			msg = consumer_receiver.recv()
			topic, msg = self.demogrify(msg.decode("utf-8"))
			logger.info( "Received: {}".format( msg) ) 
			if isinstance(msg, dict):
				if 'picture' in msg:
					self.api.update_with_media(msg['picture'], msg['msg'])
				else: 
					self.api.update_status(msg['msg'])