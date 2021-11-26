
import platform
class UnsupportedPlatform(Exception):
    """
        Subjected Platform is currently not supported by the IPFS installer.
    """
    def __str__(self):
        return f"{platform.system()} is currently not supported by the IPFS installer."