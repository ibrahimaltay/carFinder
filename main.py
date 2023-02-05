import time
from src.PageObjects import SahibindenPageObject
from src.Helpers import ConfigurationHelper

config = ConfigurationHelper.ConfigurationHelper(test=True).config

sah = SahibindenPageObject.Sahibinden(config['searchUrl'])
listing_type = config['listingType']
# time.sleep(300)
sah.ParseListings(listing_type)
sah.DisposeDriver()