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

You can also run `./tmux-terminal.sh` to load up a 3 pane tmux session of the 3 dispatchers