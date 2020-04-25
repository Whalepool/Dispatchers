from pprint import pprint
import zmq
import telegram
import sys
import os 
import json  
import yaml
import coloredlogs, logging
import setproctitle
from telegram.ext import Updater, CommandHandler
from telegram.utils.helpers import escape_markdown



class TGDispatcher(): 

	def __init__(self):

		self.PATH 			 = os.path.dirname(os.path.abspath(__file__))
		self.config_file = "{}/config.yaml".format(self.PATH)

		logger.info('Running TGdispatcher  in '+self.PATH)

		logger.info( "Loading config {}".format(self.config_file) ) 
		with open(self.config_file) as fp:
			self.config = yaml.load(fp, Loader=yaml.BaseLoader)


	def launch_bot(self):

		# Bot commands
		def getid(bot, update):
			pprint(update.message.chat.__dict__, indent=4)
			reply = "{} :: {}".format( update.message.chat.first_name, update.message.chat.id)
			update.message.reply_text( reply )


		def subprocess_command(bot, update):
			pprint(update.message.chat.__dict__, indent=4)
			return 'setup if you want' 
			# pipe = Popen(['my_subprocess_script.sh'], stdout=PIPE, shell=True)
			# text = pipe.communicate()[0]
			# pprint(text.decode("utf-8") )
			# update.message.reply_text(text.decode("utf-8") )


		# Bot commands 
		self.bot = telegram.Bot(token=self.config['TG_API_KEY'])
		updater = Updater(bot=self.bot, use_context=True)
		dp = updater.dispatcher
		dp.add_handler(CommandHandler('id', getid))
		dp.add_handler(CommandHandler('subprocess_command', subprocess_command))
		updater.start_polling()



	def listen_zmq_commands(self): 


		def demogrify(topicmsg):
			""" Inverse of mogrify() """
			json0 = topicmsg.find('[')
			json1 = topicmsg.find('{')

			start = json0
			if (json1 > 0):
				if (json0 > 0):
					if (json1 < json0):
						start = json1
				else:
					start = json1

			topic = topicmsg[0:start].strip()
			msg = json.loads(topicmsg[start:])

			return topic, msg 	#


		#####################################
		logger.info('Connecting to zmq')
		context = zmq.Context()
		consumer_receiver = context.socket(zmq.SUB)
		consumer_receiver.connect('tcp://127.0.0.1:'+str(self.config['ZMQ_XPUB_PORT']))
		consumer_receiver.setsockopt_string(zmq.SUBSCRIBE, 'telegram')

		while True:
			msg = consumer_receiver.recv()
			topic, msg = demogrify(msg.decode("utf-8"))
			logger.info( "Received: {}".format( msg) ) 
			if isinstance(msg, dict):
				if 'picture' in msg:
					self.bot.sendPhoto(chat_id=msg['chat_id'], photo=open(msg['picture'],'rb'), caption=msg['msg'] )
				else: 
					self.bot.sendMessage(chat_id=owner_id, text=msg['msg'])



if __name__ == '__main__':

	logger = logging.getLogger(__name__)
	coloredlogs.install(level='DEBUG', logger=logger)
	
	setproctitle.setproctitle('tgdispatcher')

	node = TGDispatcher()
	node.launch_bot() 
	node.listen_zmq_commands()

	pprint('hello')
	exit()



