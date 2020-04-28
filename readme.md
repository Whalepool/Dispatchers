### Message Dispatcherers
     
Send via ZMQ json data of anything and have it message you (or more)      
   
Supported:   
- Telegram   
- Teamspeak  
- Twitter  
   
##### Usage   
```  
# Run the zmq proxy
python zmqproxy.py

# Launch the telegram dispatcher
python tg_dispatcher.py

# Send a test to the telegram dispatcher
python example_telegram_sender.py

# ... 
# .. repeat for teamspeak / twitter dispatchers
```