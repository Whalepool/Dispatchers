import zmq, os, sys, yaml 


def main():

	PATH 			  = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
	config_file = "{}/config.yaml".format(PATH)
	with open(config_file) as fp:
		config = yaml.load(fp, Loader=yaml.BaseLoader)

	config['ZMQ_XSUB_PORT'] = int(config['ZMQ_XSUB_PORT'])
	config['ZMQ_XPUB_PORT'] = int(config['ZMQ_XPUB_PORT'])

	context = zmq.Context(1)

	print('Connecting to XSUB: {}:{}'.format(config['ZMQ_HOST'],config['ZMQ_XSUB_PORT']))
	backend = context.socket(zmq.XSUB)
	backend.bind('{}:{}'.format(config['ZMQ_HOST'],config['ZMQ_XSUB_PORT']))

	print('Connecting to XPUB: {}:{}'.format(config['ZMQ_HOST'],config['ZMQ_XPUB_PORT']))
	frontend = context.socket(zmq.XPUB)
	frontend.bind('{}:{}'.format(config['ZMQ_HOST'],config['ZMQ_XPUB_PORT']))

	print('Running..')
	zmq.device(zmq.FORWARDER, frontend, backend)

if __name__ == "__main__":
    main()


