import coloredlogs, logging
import zmq
import telegram
from telegram.utils.helpers import escape_markdown
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json  
import coloredlogs, logging
from pprint import pprint
from .utils import LoadYamlConfig, ZmqReceiver

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)




class TGDispatcher( LoadYamlConfig ): 

	def __init__(self):

		LoadYamlConfig.__init__(self)
		
		self.z = ZmqReceiver( 'telegram' )

	# Bot commands
	def getid(self, update, context):
		chat_id = update.message.chat.id
		update.message.reply_text(chat_id)


	def launch_bot(self):

		# Bot commands 
		self.bot = telegram.Bot(token=self.config['TG_API_KEY'])
		self.updater = Updater(bot=self.bot, use_context=True)
		self.dp = self.updater.dispatcher
		self.dp.add_handler(CommandHandler('id', self.getid))
		self.updater.start_polling()



	def listen_zmq_commands(self): 

		#####################################
		while True:
			msg = self.z.recv_msg()
			pprint(msg)
			if isinstance(msg, dict):
				if 'picture' in msg:
					self.bot.sendPhoto(chat_id=self.config['TG_OWNER_ID'], photo=open(msg['picture'],'rb'), caption=msg['msg'] )
				elif 'msg' in msg: 
					self.bot.sendMessage(chat_id=self.config['TG_OWNER_ID'], text=msg['msg'])
				else: 
					self.bot.sendMessage(chat_id=self.config['TG_OWNER_ID'], text=str(msg))