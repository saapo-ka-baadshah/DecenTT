import os
from DecenTT.IPFS.locales.IPFSLocalesExceptions import *


def onLoadBootstrapList():
    import dotenv
    dotenv.load_dotenv()


def getBootstrapNodes() -> list:
    import re
    onLoadBootstrapList()

    pat = re.compile("BOOTSTRAP")
    bs_keys = list(filter(pat.match, list(os.environ)))

    nodes = list()
    try:
        for i, key in enumerate(bs_keys):
            nodes.append(os.environ[key])
    except Exception as e:
        raise BootstrapNodeError(error=e)

    return nodes
