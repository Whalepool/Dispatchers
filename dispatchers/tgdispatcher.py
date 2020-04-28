import coloredlogs, logging
import zmq
import telegram
from telegram.ext import Updater, CommandHandler
from telegram.utils.helpers import escape_markdown
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
		while True:
			msg = self.z.recv_msg()
			pprint(msg)
			if isinstance(msg, dict):
				if 'picture' in msg:
					self.bot.sendPhoto(chat_id=msg['chat_id'], photo=open(msg['picture'],'rb'), caption=msg['msg'] )
				elif 'msg' in msg: 
					self.bot.sendMessage(chat_id=self.config['TG_OWNER_ID'], text=msg['msg'])
				else: 
					self.bot.sendMessage(chat_id=self.config['TG_OWNER_ID'], text=str(msg))