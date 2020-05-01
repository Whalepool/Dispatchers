### Message Dispatcherers
     
Send via ZMQ json data of anything and have it message you (or more)      
   
Supported:   
- Telegram   
- Teamspeak  
- Twitter  

##### Requirements
```bash
# Might need to recompile python after installing this
# recommend using pyenv 3.8.2 
sudo apt-get install libffi-dev

pip install --upgrade pip
pip install -r requirements.pip 
``` 

##### Make your config file
```bash
# Make sure all your config details are correct
cp config.sample.yaml config.yaml

# Asssuming using zsh make sure locale is set right 
echo 'export LANG=en_US.utf8' >> ~/.zshrc
```
   
##### Usage   
```bash
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