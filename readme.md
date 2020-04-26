### Message Dispatcherers
   
Send via ZMQ json data of anything and have it message you (or more)    
     
You will need a zmq proxy setup to handle the XPUB->XSUB relay, like this..    

```python
context = zmq.Context(1)  
# Socket facing consumers
print('Conneecting to XSUB: '+"tcp://127.0.0.1:"+XSUB_PORT)
backend = context.socket(zmq.XSUB)
backend.bind("tcp://127.0.0.1:"+XSUB_PORT)

# Socket facing services
print('Conneecting to XPUB: '+"tcp://127.0.0.1:"+XPUB_PORT)
frontend = context.socket(zmq.XPUB)
frontend.bind("tcp://127.0.0.1:"+XPUB_PORT)

zmq.device(zmq.FORWARDER, frontend, backend)
```  

Sample to send to telegram
```
{     
	'chat_id': 34_to_chat_id_34,      
	'msg': 'Hey, Yo, its me!',     
	'parse_mode': 'Markdown',    
	'disable_web_page_preview': 1,      
	'picture': '/some/path/to/some/pic.png'     
}     
```  
  
Sample to send to twitter    
``` 
{
	'msg': 'Some tweet',    
	'picture': '/maybe/some/pic.png'   
}    
```   