import twitchio

from twitchio.ext import commands, pubsub
from tuyapy import TuyaApi
from tuyapy.devices.light import TuyaLight

from constants import(
    TWITCH_TOKEN,
    CHANNEL,

    USERNAME,
    PASSWORD,
    COUNTRY_CODE,
    APPLICATION
)

api = TuyaApi()
api.init(
    USERNAME,
    PASSWORD,
    COUNTRY_CODE,
    APPLICATION
)

light: TuyaLight = api.get_all_devices()[0]
light.turn_on()
light.set_brightness(255)

class Bot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            token=TWITCH_TOKEN,
            prefix="?",
            initial_channels=CHANNEL
        )

        self.pubsub_client = None
        self.colors = {
            "lila": (269, 100, 100),
            "cian": (174, 100, 100),
            "rosa": (300, 100, 100),
            "roja": (0, 100, 100),
            "azul": (250, 100, 100),
            "verde": (100, 100, 100),
        }

    async def event_ready(self):
        print(f"[   READY   ]: {self.nick}")

    async def event_pubsub_channel_points(self, event: pubsub.PubSubChannelPointsMessage):
        print("asd")
        title = event.reward.title
        if title.startswith("Luz"):
            color = title.split()[1]

            light.set_color(self.colors[color])




async def main():
    topics = [
        pubsub.channel_points(TWITCH_TOKEN)[545580209]
    ]

    await bot.pubsub.subscribe_topics(topics)
    await bot.connect()

if __name__ == "__main__":
    
    bot = Bot()
    bot.pubsub = pubsub.PubSubPool(bot)

    bot.loop.create_task(main())
    bot.loop.run_forever()
