import random
import uuid
import re
import pandas as pd
from objects.Routing import lobby_default, driveup_default
from objects.Routing import Address, Location, Meta_list, Day, Routing, phone_number_generation


class Branch:
    def __init__(self, branch_id, bank, name,
                 address, location, meta, lobby, drive_up
                 ):
        self.id = branch_id
        self.bank = bank
        self.name = name
        self.address = address
        self.location = location
        self.meta = meta
        self.lobby = lobby
        self.drive_up = drive_up

    def dict(self):
        return {
            "id": self.id,
            "bank_id": self.bank.id,
            "name": self.name,
            "address": self.address,
            "location": self.location,
            "meta": self.meta,
            "lobby": self.lobby,
            "driveUp": self.drive_up
        }

    @staticmethod
    def Generator(bank, num):
        for i in range(num):
            branch_id = str(uuid.uuid4())
            name = "Branch {} of {}".format(i, bank.id)
            address = Address()
            location = Location()
            meta = {
                "license":{
                    "id":"PDDL",
                    "name":random.choice(Meta_list)
                }
            }

            lobby = {
                "hours":"M-TH 8:30-3:30, F 9-5"
            }

            drive_up = {
                "hours": "M-Th 8:30-5:30, F-8:30-6, Sat 9-12"
            }

            yield Branch(
                branch_id = branch_id,
                bank = bank,
                name=name,
                address=address,
                location=location,
                meta=meta,
                lobby=lobby,
                drive_up=drive_up
            )

    @staticmethod
    def generate_from_file(bank, num,  input_file = './input_file/dataset.xlsx'):
        df = pd.read_excel(input_file, sheet_name = 'branches', header=0, index_col=None)
        branch_list = []
        df = df.sample(frac=1).reset_index(drop=True)

        num = int(num)-1
        for index, row in df.loc[:num].iterrows():
        #if row['Bank_ID'] == bank.id:
            branch_id = str(uuid.uuid4())
            name = "Branch {} of {}".format(branch_id, bank.id)

            location = Location(row['latitude'], row['longitude'])
            address = Address(row['Address 1'], row['Address 2'], row['Address 3'], row['City'], row['County'], row['State'], row['Postcode'],row['Country code'])
            meta = {
                "license":{
                    "id":"PDDL",
                    "name":''
                }
            }

            lobby = {
                "hours":lobby_default
            }

            drive_up = {
                "hours": driveup_default
            }

            branch_list.append(Branch(
                branch_id = branch_id,
                bank = bank,
                name=name,
                address=address,
                location=location,
                meta=meta,
                lobby=lobby,
                drive_up=drive_up
            ))

        return branch_list


class ATM:
    def __init__(self, atm_id, bank, name,
                 address, location, meta
                 ):
        self.id = atm_id
        self.bank = bank
        self.name = name
        self.address = address
        self.location = location
        self.meta = meta

    def dict(self):
        return {
            "id": self.id,
            "bank_id": self.bank.id,
            "name": self.name,
            "address": self.address,
            "location": self.location,
            "meta": self.meta
        }

    @staticmethod
    def Generator(bank, num):
        for i in range(num):
            atm_id = str(uuid.uuid4())
            name = "ATM {} of {}".format(i, bank.id)
            address = Address()
            location = Location()
            meta = {
                "license":{
                    "id":"PDDL",
                    "name":''
                }
            }

            yield ATM(
                atm_id = atm_id,
                bank = bank,
                name=name,
                address=address,
                location=location,
                meta=meta
            )

    @staticmethod
    def generate_from_file(bank, num,  input_file = './input_file/dataset.xlsx'):
        df = pd.read_excel(input_file, sheet_name = 'atms', header=0, index_col=None)
        atm_list = []
        df = df.sample(frac=1).reset_index(drop=True)

        for row in df[:num].iterrows():
            row = row[1]
            atm_id = str(uuid.uuid4())
            name = "Branch {} of {}".format(atm_id, bank.id)

            location = Location(row['latitude'], row['longitude'])
            address = Address(row['Address 1'], row['Address 2'], row['Address 3'], row['City'], row['County'], row['State'], row['Postcode'],row['Country code'])
            meta = {
                "license":{
                    "id":"PDDL",
                    "name":''
                }
            }

            atm_list.append(ATM(
                atm_id = atm_id,
                bank = bank,
                name=name,
                address=address,
                location=location,
                meta=meta
            ))

        return atm_list