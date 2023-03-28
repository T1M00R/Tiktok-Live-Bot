from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent, LikeEvent, JoinEvent, DisconnectEvent, FollowEvent
import keyboard
import time



# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@clickbro69420")

#"@i_haskill"
#"@clickbro69420"

# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

# @client.on("like")
# async def on_like(event: LikeEvent):
#     print(f"@{event.user.unique_id} liked the stream!")

@client.on("follow")
async def on_follow(event: FollowEvent):
    print(f"{event.user.uniqueId} just followed!")




# On comment , check input and simulate appropriate key stroke
@client.on("comment")
async def on_comment(event: CommentEvent):
    process_input(event.comment)
    print(f"{event.user.nickname} -> {event.comment}")
    


# Switch case to process inputs
def process_input(event: str):
    # Process comment and simulate a key stroke
    if event == "a":
        keyboard.press('l')
        time.sleep(0.1)
        keyboard.release('l')
    elif event == "b":
        keyboard.press('k')
        time.sleep(0.1)
        keyboard.release('k')
    elif event == "x":
        keyboard.press('s')
        time.sleep(0.1)
        keyboard.release('s')
    elif event == "y":
        keyboard.press('a')
        time.sleep(0.1)
        keyboard.release('a')
    elif event == "l":
        keyboard.press('i')
        time.sleep(0.1)
        keyboard.release('i')
    elif event == "r":
        keyboard.press('o')
        time.sleep(0.1)
        keyboard.release('o')
    elif event == "up":
        keyboard.press('w')
        time.sleep(0.1)
        keyboard.release('w')
    elif event == "down":
        keyboard.press('s')
        time.sleep(0.1)
        keyboard.release('s')
    elif event == "left":
        keyboard.press('a')
        time.sleep(0.1)
        keyboard.release('a')
    elif event == "right":
        keyboard.press('d')
        time.sleep(0.1)
        keyboard.release('d')
    elif event == "start":
        keyboard.press('enter')
        time.sleep(0.1)
        keyboard.release('enter')
    elif event == "select":
        keyboard.press('backspace')
        time.sleep(0.1)
        keyboard.release('backspace')
    # print("Input processed: " + comment)



# @client.on("join")
# async def on_join(event: JoinEvent):
#     print(f"@{event.user.unique_id} joined the stream!")



@client.on("disconnect")
async def on_disconnect(event: DisconnectEvent):
    print("Disconnected")
    



# Define handling an event via a "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()