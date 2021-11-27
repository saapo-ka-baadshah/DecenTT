from DecenTT.IPFS.pubsub import Client
import time


c = Client()


def callback(payload):
    print(payload)


sub_abc = c.subscribe(topic="abc", callback=callback)
sub_def = c.subscribe(topic="def", callback=callback)

while True:
    try:
        time.sleep(3)
        print("Thread Break")
    except KeyboardInterrupt:
        break
print("Interrupted")
sub_abc.close()
sub_def.close()
print("threads joined")



