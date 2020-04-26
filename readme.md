### Message Dispatcherers
   
Send via ZMQ json data of anything and have it message you (or more)    
     
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