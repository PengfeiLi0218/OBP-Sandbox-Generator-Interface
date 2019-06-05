import random
import uuid
import pandas as pd

category_list = ["Mortgage", "Account","Credit Card","Loan","Savings","Overdraft"]
family_list = ["Mortgage", "Service","Credit Card","Loan","Credit","Loan"]
super_family_list =["Lending", "Service","Lending","Lending","Credit","Lending"]

product_list = list(zip(category_list, family_list, super_family_list))
class Product:
    def __init__(self, bank, code, name, category, family, super_family,
                 more_info_url, meta
                 ):
        self.bank = bank
        self.code = code
        self.name = name
        self.category = category
        self.family =family
        self.super_family = super_family
        self.more_info_url = more_info_url
        self.meta = meta

    def dict(self):
        return {
            "bank_id":self.bank.id,
            "code":self.code,
            "name":self.name,
            "category":self.category,
            "family":self.family,
            "super_family":self.super_family,
            "more_info_url":self.more_info_url,
            "meta":self.meta
        }

    @staticmethod
    def Generator(bank,  num):
        for i in range(num):
            code = str(uuid.uuid4())
            name = "PRODUCT{}{:2d}".format(code[:4], num)
            category, family, super_family = random.choice(product_list)

            yield Product(
                bank=bank,
                code=code,
                name=name,
                category=category,
                family=family,
                super_family=super_family,
                more_info_url="",
                meta={
                    "license":{
                        "id": "copyright",
                        "name": "Copyright"
                    }
                }
            )

    @staticmethod
    def generate_from_file(bank, num,  input_file = './input_file/dataset.xlsx'):
        df = pd.read_excel(input_file, sheet_name = 'products', header=0, index_col=None)
        atm_list = []
        df = df.sample(frac=1).reset_index(drop=True)

        num = int(num)-1
        for index, row in df.loc[:num].iterrows():
            #row = row[1]
            code = str(uuid.uuid4())
            name = row['Product']

            category = row['Category']
            family = row['Family']
            super_family = row['Super-Family']
            more_info = row['More info']

            atm_list.append(Product(
                bank=bank,
                code=code,
                name=name,
                category=category,
                family=family,
                super_family=super_family,
                more_info_url=more_info,
                meta={
                    "license":{
                        "id": "copyright",
                        "name": "Copyright"
                    }
                }
            ))

        return atm_list