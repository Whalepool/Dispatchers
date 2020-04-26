import coloredlogs, logging
import dispatchers
import setproctitle

if __name__ == '__main__':

	logger = logging.getLogger(__name__)
	coloredlogs.install(level='DEBUG', logger=logger)
	
	setproctitle.setproctitle('tg_dispatcher')

	node = dispatchers.TGDispatcher()
	node.launch_bot() 
	node.listen_zmq_commands()