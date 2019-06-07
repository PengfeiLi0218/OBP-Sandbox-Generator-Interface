import uuid
import random
from datetime import datetime, timedelta
import re

import numpy as np

class Routing:
    def __init__(self, scheme, address):
        self.scheme = scheme
        self.address = address
        self.dict = {
            "scheme":scheme,
            "address":address,
        }


line1_list = ['No {:2d} the Road'.format(i + 1) for i in range(10)]
line2_list = ['The Place {:2d}'.format(i + 1) for i in range(7)]
line3_list = ['The {} District'.format(i + 1) for i in range(8)]
city_list = ['city{:2d}'.format(i) for i in range(20)]
county_list = ['county{:2d}'.format(i) for i in range(10)]
state_list = ['state{:2d}'.format(i) for i in range(5)]
postcode_list = [str(int(int(uuid.uuid4()) % 1e6)) for i in range(10)]
country_list = ['MX']


class Address:
    def __init__(self,
                 line1=random.choice(line1_list),
                 line2=random.choice(line2_list),
                 line3=random.choice(line3_list),
                 city=random.choice(city_list),
                 county=random.choice(county_list),
                 state=random.choice(state_list),
                 postcode=random.choice(postcode_list),
                 country_code=random.choice(country_list)
                 ):
        self.line1 = str(line1)
        self.line2 = str(line2)
        self.line3 = str(line3)
        self.city = str(city)
        self.county = str(county)
        self.state = str(state)
        self.postcode = str(postcode)
        self.country_code = str(country_code)

    def dict(self):
        return {
            "line_1":self.line1,
            "line_2":self.line2,
            "line_3":self.line3,
            "city": self.city,
            "county": self.county,
            "state": self.state,
            "post_code": self.postcode,
            "country_code": self.country_code,
        }

class Location:
    def __init__(self,
                 latitude = random.uniform(0.0, 90.0),
                 longitude = random.uniform(0.0, 360.0)
                 ):
        self.latitude = float("{:.2f}".format(latitude))
        self.longitude = float("{:.2f}".format(longitude))
    def dict(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

Meta_list = ['meta {:02}'.format(i) for i in range(10)]

open_list = ['07','08','09','10']
close_list = ['15', '16','17','18']
class Day:
    def __init__(self,
                 opening_time = random.choice(open_list),
                 closing_time = random.choice(close_list)):
        self.opening_time = opening_time+":00"
        self.closing_time = closing_time+":00"
    def dict(self):
        return {
            "opening_time" : self.opening_time,
            "closing_time" : self.closing_time,
        }

def phone_number_generation():
    p=list('0000000000')
    p[0] = str(random.randint(1,9))
    for i in [1,2,6,7,8]:
        p[i] = str(random.randint(0,9))
    for i in [3,4]:
        p[i] = str(random.randint(0,8))
    if p[3]==p[4]==0:
        p[5]=str(random.randint(1,8))
    else:
        p[5]=str(random.randint(0,8))
    n9 = range(10)
    if p[6]==p[7]==p[8]:
        n9 = (i for i in n9 if i!=p[6])
    p[9] = str(random.randint(0, 9))
    p = ''.join(p)
    return p[:3] + '-' + p[3:6] + '-' + p[6:]

def digits11():
    range_start = 10 ** (11 - 1)
    range_end = (10 ** 11) - 1
    return random.randint(range_start, range_end)

def generateIBAN(country_code):
    p = list(np.repeat('0', 20))

    for i in range(20):
        p[i] = str(random.randint(0, 9))

    p = ''.join(p)
    return country_code[:2]+p

def gen_datetime(min_year=2018, max_year=datetime.now().year):
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

def add_deltatime(current):
    return current + timedelta(minutes=random.randrange(60))

# How do people usually spend their money?  Taken from
# http://www.billshrink.com/blog/consumer-income-spending/
# The fees number is made up, but seemed appropriate.

spending_pcts = \
    { "food":          0.101,
      "utility":       0.056,
      "clothing":      0.031,
      "auto":          0.144,
      "health":        0.047,
      "entertainment": 0.044,
      "gift":         0.020,
      "education":     0.016,
      "fee":           0.026 }

spending_frequency = \
    { "food":          5,
      "utility":       0.2,
      "clothing":      1,
      "auto":          0.2,
      "health":        0.1,
      "entertainment": 1,
      "gift":         0.2,
      "education":     0.2,
      "fee":           0.5 }
# How much do people spend per transaction?  This is taken from
# the tag_summaries table in the live database.

avg_txn_amts = \
    { "auto":          -70.77*20,
      "clothing":      -58.31*20,
      "education":     -62.64*20,
      "entertainment": -30.10*20,
      "fee":           -20.95*20,
      "food":          -25.52*20,
      "gift":          -18.84*20,
      "health":        -73.05*20,
      "mortgage":      -1168.49*20,
      "rent":          -643.30*20,
      "utility":       -90.81*20 }

# For now, just throw in some merchant names for each tag. Later
# this should come from the merchant_summaries table.
# counterparty

top_merchants = \
    { "auto":          ["Chevron", "Jiffy Lube", "Union 76", "Arco", "Shell", "Pep Boys"],
      "clothing":      ["Nordstrom", "Banana Republic", "Macy's", "The Gap", "Kenneth Cole", "J. Crew"],
      "education":     ["Tuition", "Amazon.com", "Registration", "The Crucible", "Campus Books"],
      "entertainment": ["AMC Theaters", "Amazon.com", "Netflix", "iTunes Music Store", "Rhapsody", "Metreon Theaters"],
      "fee":           ["Bank Fee", "Overlimit Fee", "Late Fee", "Interest Fee", "Monthly Fee", "Annual Fee"],
      "food":          ["Safeway", "Starbucks", "In-N-Out Burger", "Trader Joe's", "Whole Foods", "Olive Garden"],
      "gift":          ["Amazon.com", "Nordstrom", "Neiman-Marcus", "Apple Store", "K&L Wines"],
      "health":        ["Dr. Phillips", "Dr. Jackson", "Walgreen's", "Wal-Mart", "Dr. Roberts", "Dr. Martins"],
      "mortgage":      ["Mortgage Payment"],
      "rent":          ["Rent Payment"],
      "utility":       ["AT&T", "Verizon", "PG&E", "Comcast", "Brinks", ""] }

tags = list(spending_pcts.keys())


lobby_default = "M-TH 8:30-3:30, F 9-5"
driveup_default = "M-Th 8:30-5:30, F-8:30-6, Sat 9-12"