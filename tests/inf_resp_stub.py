import sys

from DecenTT.IPFS.pubsub import Client

c = Client()

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

sub_1 = c.subscribe(topic="abc", callback= on_message)
sub_2 = c.subscribe(topic="def", callback= on_message)

sys.exit(0)