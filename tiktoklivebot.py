from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, LikeEvent, JoinEvent, DisconnectEvent, FollowEvent
import keyboard



# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@i_haskill")

#"@clickbro69420"

# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

@client.on("like")
async def on_like(event: LikeEvent):
    print(f"@{event.user.unique_id} liked the stream!")

@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"{event.user.uniqueId} just followed!")




# On comment , check input and simulate appropriate key stroke
@client.on("comment")
async def on_comment(event: CommentEvent):
    # Press and release the 'a' key
    keyboard.press_and_release('a')
    print(f"{event.user.nickname} -> {event.comment}")


    # if {event.comment} == "a":
    #     print(f"{event.user.nickname} -> User pressed A")
    # elif {event.comment} == "b":
    #     print(f"{event.user.nickname} -> User pressed B")
    # elif {event.comment} == "up":
    #     print(f"{event.user.nickname} -> User pressed Up")
    # elif {event.comment} == "down":
    #     print(f"{event.user.nickname} -> User pressed Down")
    # elif {event.comment} == "left":
    #     print(f"{event.user.nickname} -> User pressed Left")
    # elif {event.comment} == "right":
    #     print(f"{event.user.nickname} -> User pressed Right")
    
#comment = {event.comment}
# Switch case to process inputs
    
        


@client.on("join")
async def on_join(event: JoinEvent):
    print(f"@{event.user.unique_id} joined the stream!")



@client.on("disconnect")
async def on_disconnect(event: DisconnectEvent):
    print("Disconnected")
    



# Define handling an event via a "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()