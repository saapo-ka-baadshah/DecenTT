import paho.mqtt.client

from DecenTT import Client


def sample_callback(client, userdata, msg):
    print(f"{msg} Object received : \t {msg.payload.decode()}")


if __name__ == '__main__':
    d_c = Client(
        host="172.105.247.191"
    )
    d_c.subscribe(topic="ABC", callback=sample_callback)
    d_c.subscribe(topic="secure/ABC", callback=sample_callback)

    d_c.clients[0].client.loop_forever()