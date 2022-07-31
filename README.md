### Prerequisites

  ```sh
  WINDOWS:
    - Install python from https://python.org/downloads/
    - pip install requirements.txt
  
  Linux (Debian):
    - sudo apt install python3
    - sudo apt install python3-pip
    - pip3 install requirements.txt
  ```

# Twitch2X
Python scripts for connecting Twitch to other stuff

# Twitch2Discord
A simple script that sends messages from Twitch Channel to Discord Channel

# Twitch2Light
A simple script that uses channel point redeems for lighting up a smart lighbulb (needs to be compatible with Tuya or Smart Life app)

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
  TWITCH_TOKEN = "TWITCH_TOKEN"
  #   TWITCH CHANNEL NAME
  CHANNEL = ["CHANNEL_NAME"]

  #   LIGHTBULB
  #   SMART LIFE / Tuya

  USERNAME = "email"
  PASSWORD = "password"
  COUNTRY_CODE = "1"
  # "tuya" or "smart_life"
  APPLICATION = "smart_life"
  ```
