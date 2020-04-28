from dispatchers.utils import ZmqSender
import time

data = {     
	# default no chat_id supplied will message owner 
	# 'chat_id': 34_to_chat_id_34,      

	# Message to send
	'msg': 'example_telegram_sender message, uid {}'.format(time.time_ns()),     

	# optional / control the parse mode
	# 'parse_mode': 'Markdown',    

	# optional / control if you want to enable webpage preview on any links
	# 'disable_web_page_preview': 1,      

	# optional / make the bot send a picture also 
	# 'picture': '/some/path/to/some/pic.png'     
}     


z = ZmqSender( 'telegram' )

# Send Data
z.send_msg( data )
