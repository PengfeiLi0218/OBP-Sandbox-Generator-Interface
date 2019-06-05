import random

from object.Routing import *


class Counterparty:
    def __init__(self, account, name, description,
                 is_beneficiary,
                 bespoke,corporate_location,more_info,open_corporates_URL,
                 image_URL,physical_location,alias,URL
                 ):
        self.account = account
        self.name = name
        self.description = description
        self.is_beneficiary= is_beneficiary
        self.bespoke= bespoke
        self.corporate_location =corporate_location
        self.more_info = more_info
        self.open_corporates_URL = open_corporates_URL
        self.image_URL = image_URL
        self.physical_location = physical_location
        self.alias = alias
        self.URL = URL

        self.dict = {
            "name": name,
            "description": description,
            "other_account_routing_scheme": account.account_routing[0].scheme,
            "other_account_routing_address": account.account_routing[0].address,
            "other_account_secondary_routing_scheme": "IBAN",
            "other_account_secondary_routing_address": account.iban,
            "other_bank_routing_scheme": account.branch.bank.bank_routing.scheme,
            "other_bank_routing_address": account.branch.bank.bank_routing.address,
            "other_branch_routing_scheme": account.branch.branch_routing.scheme,
            "other_branch_routing_address": account.branch.branch_routing.address,
            "is_beneficiary": is_beneficiary,
            "bespoke": bespoke,
            "corporate_location": corporate_location,
            "more_info":more_info,
            "open_corporates_URL":open_corporates_URL,
            "image_URL":image_URL,
            "physical_location":physical_location,
            "alias":alias,
            "URL":URL
        }

    @staticmethod
    def Generator(account):
        name = account.user.username
        description= 'Account description: {}'.format(account.account_id)
        is_beneficiary = True if random.uniform(0,1) > 0.5 else False
        bespoke = [{
            "key":"englishName",
            "value":"english Name"
        }]
        corporate_location = Location()
        more_info="{}:{}".format(name, description)
        open_corporates_URL="String"
        image_URL="String"
        physical_location = Location()
        alias="String"
        URL="String"

        yield Counterparty(account, name, description, is_beneficiary, bespoke,corporate_location,
                           more_info,open_corporates_URL,image_URL,physical_location,alias,URL)
