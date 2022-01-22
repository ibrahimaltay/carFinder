import time
from src.PageObjects import SahibindenPageObject
from src.Helpers import ConfigurationHelper

config = ConfigurationHelper.ConfigurationHelper(test=True).config

sah = SahibindenPageObject.Sahibinden(config['searchUrl'])
sah.ParseListings()
