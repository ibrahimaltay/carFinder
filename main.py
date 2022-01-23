import time
from src.PageObjects import SahibindenPageObject
from src.Helpers import ConfigurationHelper

config = ConfigurationHelper.ConfigurationHelper(test=True).config

for url in config['searchUrl']:
    sah = SahibindenPageObject.Sahibinden(config['searchUrl'][0])
    time.sleep(5)
    sah.ParseListings()
    sah.DisposeDriver()

