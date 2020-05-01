### Message Dispatcherers
     
Send via ZMQ json data of anything and have it message you (or more)      
   
Supported:   
- Telegram   
- Teamspeak  
- Twitter  

##### Requirements
```
# Might need to recompile python after installing this
# recommend using pyenv 3.8.2 
sudo apt-get install libffi-dev

pip install --upgrade pip
pip install -r requirements.pip 
``` 

##### Make your config file
```
cp config.sample.yaml config.yaml

# Make sure all your config details are correct
```
   
##### Usage   
```  
# Make sure we have screen installed
# sudo apt-get install screen 

# cd into the Dispatchers folder
# execute the zmqproxy.py script inside a screen and auto detach 
screen -S zmqproxy -d -m python zmqproxy.py 


# Make sure we have tmux installed 
# sudo apt-get install tmux
# Run the telegram / teamspeak / twitter dispatchers in the tmux session
./tmux-terminal

# Detach the terminal
# crtl-b d   

# See tmux sessions 
tmux ls 

# You can also run them independently outputting to /dev/null or create service files for systemd etc.
# Personally i like them in the tmux session
```