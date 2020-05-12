import configparser
import os
from munch import munchify
from .singleton import Singleton

CREDENTIAL_FILE = os.environ.get('CREDENTIAL_FILE', 'creds.cfg')
CONFIG_FILE = os.environ.get('SETUP_FILE', 'setup.cfg')


class Config(metaclass=Singleton):

    def __init__(self):
        self.creds = None
        self._read_creds()
        self.setup = None
        self._read_config()

    def _read_config(self):
        config_file = CONFIG_FILE
        if not self.setup:
            self.setup = Config._read_configfile(config_file)

    def _read_creds(self):
        creds_file = CREDENTIAL_FILE
        if not self.creds:
            self.creds = Config._read_configfile(creds_file)

    @staticmethod
    def _read_configfile(config_file: str):
        """ reads a config file and converts it into a python object """
        _config = configparser.ConfigParser(allow_no_value=False)
        _config.read(config_file)
        config = munchify(_config)
        return config
