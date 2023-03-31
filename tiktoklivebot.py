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
    


# Process input with count feature
def process_input(event: str):

    # Case insensitive
    event = event.lower()
    # Parse modifier if it exists
    if len(event) > 1 and event[-1].isdigit():
        modifier = int(event[-1])
        event = event[:-1]
    else:
        modifier = 1

    # Process comment and simulate a key stroke
    if event == "a":
        key = 'l'
    elif event == "b":
        key = 'k'
    elif event == "x":
        key = 's'
    elif event == "y":
        key = 'a'
    elif event == "l":
        key = 'i'
    elif event == "r":
        key = 'o'
    elif event == "up":
        key = 'w'
    elif event == "down":
        key = 's'
    elif event == "left":
        key = 'a'
    elif event == "right":
        key = 'd'
    elif event == "start":
        key = 'enter'
    elif event == "select":
        key = 'backspace'
    elif event == "skip":
        key = 'k'
        keyboard.press(key)
        time.sleep(0.2)
        keyboard.release(key)
        time.sleep(0.3)
        keyboard.press(key)
        time.sleep(0.2)
        keyboard.release(key)
        time.sleep(0.3)
        keyboard.press(key)
        time.sleep(0.2)
        keyboard.release(key)
        time.sleep(0.3)
    elif event == "spin":
        keyboard.press("w")
        time.sleep(0.2)
        keyboard.release("w")
        keyboard.press("a")
        time.sleep(0.2)
        keyboard.release("a")
        keyboard.press("s")
        time.sleep(0.2)
        keyboard.release("s")
        keyboard.press("d")
        time.sleep(0.2)
        keyboard.release("d")

        
    else:
        return  # Invalid event

    # Send key with modifier
    for _ in range(min(modifier, 9)):
        keyboard.press(key)
        time.sleep(0.2)
        keyboard.release(key)




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
