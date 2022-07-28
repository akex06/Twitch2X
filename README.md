# Twitch2Discord
A simple script that sends messages from Twitch Channel to Discord Channel

### Prerequisites
## LINUX
* python3 pip3
  ```sh
  sudo apt install python3
  sudo apt install python3-pip
  ```
* ```sh
  pip3 install requests
  pip3 install twitchio
  ```
## WINDOWS
* python3 pip
  ```sh
  Go to https://python.org/downloads/ and install latest python version
  ```
* ```sh
  pip install requests
  pip install twitchio
  ```
## USAGE
Open `constants.py` and change the values of the variables
* ```py
    #   DISCORD

    #   CAN BE FOUND IN https://discord.com/developers
    DISCORD_TOKEN = "TOKEN"
    API_URL = "https://discord.com/api"
    #   DISCORD CHANNEL WHERE MESSAGES WILL BE SEND
    CHANNEL_ID = 000000000000000000

    #   TWITCH

    #   CAN BE GENERATED AT https://twitchtokengenerator.com/
    TWITCH_TOKEN = "TOKEN"
    #   TWITCH CHANNEL NAME
    CHANNEL = ["CHANNEL_NAME"]
  ```
