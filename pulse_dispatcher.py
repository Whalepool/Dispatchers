import coloredlogs, logging
import dispatchers
import setproctitle
import asyncio 

if __name__ == '__main__':

	logger = logging.getLogger(__name__)
	coloredlogs.install(level='DEBUG', logger=logger)
	
	setproctitle.setproctitle('bfxpulse')

	async def run():
		node = dispatchers.BFXPulse()
		await node.listen_zmq_commands()

	asyncio.run(run())
