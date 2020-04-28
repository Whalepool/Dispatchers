import coloredlogs, logging
import zmq
import json  
import coloredlogs, logging
import ts3
from ts3.escape import TS3Escape
import string
import random
from pprint import pprint
from .utils import LoadYamlConfig, ZmqReceiver 
import time 
import threading
import signal

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)


class TSDispatcher( LoadYamlConfig ):

	def __init__(self):

		LoadYamlConfig.__init__(self)

		self.z = ZmqReceiver( 'teamspeak' )

		logger.info( "Connecting to teamspeak" ) 
		self.ts3conn =  ts3.query.TS3Connection(
				self.config['TS_SERVER_IP'], self.config['TS_SERVER_PORT']
		)

		# Catch crtl+c
		signal.signal(signal.SIGINT, self.handle_crtl_c)

	def handle_crtl_c(self, sig, frame):
		logger.error('Closing connection & quitting')
		self.ts3conn.quit()
		sys.exit(0)


	def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))


	def join_room(self, room_id=None):

		if room_id == None:
			room_id = self.config['TS_PRIMARY_ROOM_ID']
		
		try:
			logger.info( "Logging in to teamspeak" ) 
			self.ts3conn.login(
			client_login_name=self.config['TS_API_USERNAME'],
			client_login_password=self.config['TS_API_PASSWORD']
			)
		except ts3.query.TS3QueryError as err:
			logger.error("Login failed:", err.resp.error["msg"])
			exit(1)

		logger.info("..connected")
		self.ts3conn.use(sid=self.config['TS_SERVER_ID'])
		self.ts3conn.clientupdate(client_nickname=self.config['TS_BOT_USERNAME']+self.id_generator(6))

		resp = self.ts3conn.whoami()
		client_id=resp[0]['client_id']
		self.ts3conn.clientmove(cid=room_id, clid=client_id)


		def run_keep_alive(s):

			while True:
				time.sleep(60)
				logger.info('ts keep alive ping')
				s.ts3conn.send_keepalive()

		threading.Thread(target=run_keep_alive, args=[self], daemon=True).start()


	def listen_zmq_commands(self): 

		#####################################
		while True:
			msg = self.z.recv_msg()
			logger.info('Recieved: {}'.format(msg))

			if 'msg' in msg:
				self.ts3conn.sendtextmessage(targetmode=2, target=1, msg=msg['msg'])
			else:
				logger.error('Missing message field')


