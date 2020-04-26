import coloredlogs, logging
import zmq
import telegram
from telegram.ext import Updater, CommandHandler
from telegram.utils.helpers import escape_markdown
import json  
import yaml
import sys
import os 
import coloredlogs, logging
from pprint import pprint
from .utils import DispatchUtils

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

class TGDispatcher( DispatchUtils ): 

	def __init__(self):

		self.PATH 			 = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
		self.config_file = "{}/config.yaml".format(self.PATH)
		logger = logging.getLogger(__name__)

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
					self.bot.sendPhoto(chat_id=msg['chat_id'], photo=open(msg['picture'],'rb'), caption=msg['msg'] )
				else: 
					self.bot.sendMessage(chat_id=owner_id, text=msg['msg'])