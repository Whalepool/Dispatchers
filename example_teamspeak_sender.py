from dispatchers.utils import ZmqSender
import time

data = {     
	# specify a channel to send to  
	# 'channel_id': 123,      

	# Message to send 
	'msg': 'example_teamspeak_sender message, uid {}'.format(time.time_ns()),     
}     


z = ZmqSender( 'teamspeak' )

# Send Data
z.send_msg( data )
