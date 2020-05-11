import coloredlogs, logging, yaml
import json, time, zmq, sys, os

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

class LoadYamlConfig():

	def __init__(self, file='config.yaml'):

		self.PATH 			 = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
		self.config_file = "{}/{}".format(self.PATH, file)

		logger.info( "Loading config {}".format(self.config_file) ) 
		with open(self.config_file) as fp:
			self.config = yaml.load(fp, Loader=yaml.BaseLoader)


class ZmqReceiver(  ):


	def __init__(self, topic, host='tcp://127.0.0.1', port=5558 ):

		#####################################
		logger.info('Connecting to zmq')
		context = zmq.Context()
		self.receiver = context.socket(zmq.SUB)
		self.receiver.connect('{}:{}'.format(host,port))
		self.receiver.setsockopt_string(zmq.SUBSCRIBE, topic)
		time.sleep(0.1)


	def recv_msg( self ):

		logger.info('Awaiting message..')
		msg = self.receiver.recv()

		logger.info( "Received: {}".format( msg) ) 
		topic, msg = self.demogrify(msg.decode("utf-8"))

		return msg 


	def demogrify(self, topicmsg):
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



class ZmqSender(  ):

	#####################################
	def __init__(self, topic, host='tcp://127.0.0.1', port=5557 ):

		logger.info('ZmqSender init, connecting to zmq: {}:{} ~ {}'.format(host,port,topic))
		self.context = zmq.Context()
		self.sender = self.context.socket(zmq.PUB)
		self.sender.connect('{}:{}'.format(host, port))
		self.topic = topic
		time.sleep(0.1)

	def mogrify(self, topic, msg):
		return topic + ' ' + json.dumps(msg,  default=str)

	def send_msg( self, msg ):
		logger.info('Sending: '+str(msg))
		data = self.mogrify(self.topic, msg )
		self.sender.send_string(data)

