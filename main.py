import time

from DecenTT.IPFS import Daemon
from DecenTT import Client

def sample_callback(client, userdata, msg):
    print(msg)

if __name__ == '__main__':
    d_c = Client(
        host="172.105.247.191"
    )
    d_c.publish(topic="secure/ABC", payload="HelloWorld")



