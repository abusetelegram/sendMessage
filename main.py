from telethon import TelegramClient, events, sync, functions, types

# https://github.com/zhukov/webogram/blob/master/app/js/lib/config.js
api_id = 2496
api_hash = '8da85b0d5bfe62527e5b244c209159c3'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

# https://t.me/c/1138803658/15
# https://t.me/pdcn1/237
print("If you are trying to send message to private channel linked discussion, you have to join the channel first!")
channelLink = input("Please paste any link in the channel with discussion enabled (e.g. https://t.me/pdcn1/237 | https://t.me/c/1138803658/15): ")

parts = channelLink.split("/")

peer = parts[-2]
msg_id = int(parts[-1])

print("Peer: {}, MSG: {}".format(peer, msg_id))

result = client(functions.messages.GetDiscussionMessageRequest(
    peer=peer,
    msg_id=msg_id
))

assoc = result.chats[0]

print("Assoc Group info: {}[{}]".format(assoc.title, assoc.id))

client(functions.messages.SendMessageRequest(
    peer=assoc,
    message="You don't need to join group to send message in discussion, so do replies.",
    no_webpage=True,
))

print("If you are reading this line, then the message should have sent to group.")