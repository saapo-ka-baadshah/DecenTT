# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from DecenTT import Client

qos = 0
keyword = "resilient"

topic_list = [
    (f"{keyword}/test/topic1", qos),
    (f"test/topic2", qos),
    (f"test/topic3", qos),
]


def sample_callback(client, usrdata, msg):
    print(f"{type(msg.payload)}\t->\t{msg.payload.decode()}")


def main():
    client = Client(
        host="192.168.0.36",
        keyword=keyword
    )

    client.subscribe(topic=topic_list, callback=sample_callback)
    client.clients[0].client.loop_forever()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
