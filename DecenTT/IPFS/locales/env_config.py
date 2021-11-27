import os
from DecenTT.IPFS.locales.IPFSLocalesExceptions import *


def onLoadEnv():
    import dotenv
    dotenv.load_dotenv()


def getBootstrapNodes() -> list:
    import re
    onLoadEnv()

    pat = re.compile("BOOTSTRAP")
    bs_keys = list(filter(pat.match, list(os.environ)))

    nodes = list()
    try:
        for i, key in enumerate(bs_keys):
            nodes.append(os.environ[key])
    except Exception as e:
        raise BootstrapNodeError(error=e)

    return nodes

def getIPFSHost() -> str:
    onLoadEnv()
    return os.environ["DEFAULT_HOST"]

