import coloredlogs, logging
import json  

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', logger=logger)

class DispatchUtils(): 

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