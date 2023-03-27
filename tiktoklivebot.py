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
    
    process_input(event.comment)
    print(f"{event.user.nickname} -> {event.comment}")


    
# Switch case to process inputs
def process_input(comment):
    # Process comment and simulate a key stroke
    if(comment == "a"):
        keyboard.press_and_release('x')
    elif(comment == "b"):
        keyboard.press_and_release('z')
    elif(comment == "x"):
        keyboard.press_and_release('s')
    elif(comment == "y"):
        keyboard.press_and_release('a')
    elif(comment == "l"):
        keyboard.press_and_release('q')
    elif(comment == "r"):
        keyboard.press_and_release('w')
    elif(comment == "up"):
        keyboard.press_and_release('up')
    elif(comment == "down"):
        keyboard.press_and_release('down')
    elif(comment == "left"):
        keyboard.press_and_release('left')
    elif(comment == "right"):
        keyboard.press_and_release('right')
    elif(comment == "start"):
        keyboard.press_and_release('enter')
    elif(comment == "select"):
        keyboard.press_and_release('right shift')
    print("Input processed: " + comment)



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