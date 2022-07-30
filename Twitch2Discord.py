import twitchio
import requests

from twitchio.ext import commands

from constants import(
    DISCORD_TOKEN,
    API_URL,
    CHANNEL_ID,
    
    TWITCH_TOKEN,
    CHANNEL
)

class Discord():
    def __init__(self) -> None:
        self.token = DISCORD_TOKEN
        self.api_url = API_URL
        self.channel_id = CHANNEL_ID

    async def send_message(self, message: str) -> requests.request:
        """Send a message through Discord API
        Args:
            message (str): Message to be sent to self.channel_id
        Returns:
            requests.request: Returns the request sent to Discord API
        """
        url = f"{self.api_url}/channels/{self.channel_id}/messages"
        
        headers = {
            "Authorization": f"Bot {self.token}",
            "Content-Type": "application/json"
        }

        payload = {
            "content": message
        }

        request = requests.post(
            url,
            json=payload,
            headers=headers
        )

        return request

discord = Discord()

class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            token=TWITCH_TOKEN,
            prefix="?",
            initial_channels=[CHANNEL]
        )

    async def event_ready(self):
        print(f"[   READY   ]: {self.nick}")

    async def event_message(self, message: twitchio.Message) -> None:
        message = f"[{message.author.name}]: {message.content}"

        await discord.send_message(message)

bot = Bot()
bot.run()
