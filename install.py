#!venv/bin/python3

from DecenTT.IPFS.config import Setup


def setup():
    nSetup = Setup()
    nSetup.install()

if __name__ == "__main__":
    setup()
    print("Restart is recommended! IPFS will start itself without any errors!")
