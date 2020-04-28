import coloredlogs, logging
from dispatchers import TSDispatcher
import setproctitle

if __name__ == '__main__':

	logger = logging.getLogger(__name__)
	coloredlogs.install(level='DEBUG', logger=logger)
	
	setproctitle.setproctitle('ts_dispatcher')

	node = TSDispatcher()
	node.join_room() 
	node.listen_zmq_commands()







