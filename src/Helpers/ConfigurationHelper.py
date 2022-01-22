import json

class ConfigurationHelper:
    def __init__(self, test=False):
        self.test = test
        self.config = self.GetConfiguration()

    def GetConfiguration(self):
        configurationFile = 'config.json'
        if self.test:
            configurationFile = 'configTest.json'
        with open(configurationFile) as file:
            return json.load(file)