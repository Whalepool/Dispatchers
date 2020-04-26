import coloredlogs, logging
import dispatchers
import setproctitle

if __name__ == '__main__':

	logger = logging.getLogger(__name__)
	coloredlogs.install(level='DEBUG', logger=logger)
	
	setproctitle.setproctitle('tw_dispatcher')

	node = dispatchers.TWDispatcher()
	node.listen_zmq_commands()
