import coloredlogs, logging
import zmq
import json  
import coloredlogs, logging
from pprint import pprint
from .utils import LoadYamlConfig, ZmqReceiver
from bfxapi.rest.bfx_rest import BfxRest
import asyncio 

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

class BFXPulse( LoadYamlConfig ): 

	def __init__(self, loop=None):

		LoadYamlConfig.__init__(self)
		
		self.z = ZmqReceiver( 'bfxpulse' )

		self.rest = BfxRest(
			API_KEY=self.config['BFX_API_KEY'], 
			API_SECRET=self.config['BFX_API_SECRET'], 
			loop=asyncio.get_event_loop() 
		)


		pprint('here')


	async def listen_zmq_commands(self): 

		#####################################
		while True:
			msg = self.z.recv_msg()

			if isinstance(msg, dict):
				resp = await self.write( msg['title'], msg['content'], msg['isPublic'], msg['isPin'], attachments=msg['attachments'])
				pprint(resp)
				pprint('got msg')


	async def write(self, title, content, isPublic=0, isPin=0, attachments=[]):
		# https://docs.bitfinex.com/reference#rest-auth-pulse-add
		endpoint = 'auth/w/pulse/add'
		payload = {
			'title': title,  # 16-120 characters
			'content': content,  # > 16 characters
			'isPublic': isPublic,  # 0 or 1
			'isPin': isPin,  # 0 or 1
			'attachments': attachments  # list of base64 strings
		}

		pprint('here')

		if len(title) < 16 or len(title) > 120:
			raise Exception("Title must be 16-120 characters (was: {length})".format(length=len(title)))

		try:
			# [ PID, MTS, None, PUID, None, TITLE, CONTENT, None, None, IS_PIN, IS_PUBLIC, None, TAGS[], ATTACHMENTS[], None, LIKES, None, None, UID_LIKED ]
			response = await self.rest.post(endpoint, payload)
		except Exception as e:
			print("pulse/write error: ", e)
			raise
		
		return response

