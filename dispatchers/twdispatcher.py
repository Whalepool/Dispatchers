import coloredlogs, logging
import zmq
import json  
import coloredlogs, logging
import tweepy
from pprint import pprint
from .utils import LoadYamlConfig, ZmqReceiver

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

class TWDispatcher( LoadYamlConfig ): 

	def __init__(self):

		LoadYamlConfig.__init__(self)

		auth = tweepy.OAuthHandler(self.config['TWITTER_CONSUMER_KEY'], self.config['TWITTER_CONSUMER_SECRET'])
		auth.set_access_token(self.config['TWITTER_ACCESS_TOKEN'], self.config['TWITTER_ACCESS_TOKEN_SECRET'])

		self.api = tweepy.API(auth)
		self.user = self.api.me()
		self.z = ZmqReceiver( 'twitter' )


	def listen_zmq_commands(self): 

		#####################################
		while True:
			msg = self.z.recv_msg()
			logger.info('Recieved: {}'.format(msg))

			if isinstance(msg, dict):
				if 'picture' in msg:
					out = self.api.update_with_media(msg['picture'], msg['msg'])
				else: 
					out = self.api.update_status(msg['msg'])

				pprint(out)

			
