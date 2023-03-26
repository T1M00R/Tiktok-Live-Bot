from TikTokLive import TikTokLiveClient
import pygame
from TikTokLive.types.events import CommentEvent, ConnectEvent

# pygame.mixer.init()
# pygame.mixer.music.load("sounds/follow_sound.wav")

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@clickbro69420")


@client.on("follow")
async def on_follow(event):
    print(f"{event.user.uniqueId} just followed!")

    # pygame.mixer.music.play()


# Notice no decorator?
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")


# Define handling an event via a "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()