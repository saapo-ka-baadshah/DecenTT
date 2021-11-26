import subprocess
from DecenTT.IPFS.locales.bootstrap import BStrapper


class Daemon:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self.daemon = self.__start_daemon(**self._kwargs)

    def __start_daemon(self, pubsub=True, **kwargs):
        if not pubsub:
            return subprocess.Popen(["ipfs", "daemon"], **kwargs)
        return subprocess.Popen(["ipfs", "daemon", "--enable-pubsub-experiment"], **kwargs)

    def stop(self):
        self.daemon.kill()
        _sd_process = subprocess.Popen(["ipfs", "shutdown"])

    def reload(self):
        self.stop()
        self.daemon = self.__start_daemon(**self._kwargs)


class Client:
    def __init__(self) -> None:
        pass

    def init(self) -> None:
        pass

    def publish(self):
        pass

    def subscribe(self):
        pass