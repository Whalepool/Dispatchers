import coloredlogs, logging
from dispatchers import TGDispatcher
import setproctitle
from pprint import pprint

if __name__ == '__main__':

	logger = logging.getLogger(__name__)
	coloredlogs.install(level='DEBUG', logger=logger)
	
	setproctitle.setproctitle('tg_dispatcher')

	node = TGDispatcher()
	node.launch_bot() 
	node.listen_zmq_commands()
