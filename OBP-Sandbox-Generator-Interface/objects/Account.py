import random
import uuid
from datetime import timedelta

from objects.Routing import digits11, Routing, generateIBAN, top_merchants, avg_txn_amts, add_deltatime, spending_frequency
from objects.Transaction import Transaction, generate_amt

type_list = ["CURRENT", "SAVING"]
currency_list = ["GBP"]

def getTransactionNum(frequency):
    if frequency<1:
        if random.random()>frequency:
            return 1
        else:
            return 0
    else:
        frequency_min = int(frequency*0.8) if int(frequency*0.8)>1 else 1
        return random.randint(frequency_min, int(frequency*1.2))

class Account:
    def __init__(self, account_id, branch, user, label, number, type, balance, account_routing, iban):
        self.account_id = account_id
        self.branch = branch
        self.user = user
        self.label = label
        self.number = number
        self.type = type
        self.balance = balance
        self.account_routing = account_routing
        self.iban = iban

    def dict(self):
        return {
            "id":self.account_id,
            "bank":self.branch.bank.id,
            "label":self.label,
            "number":self.number,
            "type":self.type,
            "balance":{
                "currency":self.balance['currency'],
                "amount":'{:.2f}'.format(self.balance['amount'])
            },
            "IBAN":self.iban,
            "owners":[elem.username for elem in self.user],
            "generate_public_view":False,
            "generate_accountants_view":True,
            "generate_auditors_view":True
        }

    def set_behavior(self, income, spending_frequency = spending_frequency, housing_type = None):
        self.income = income
        self.spending_frequency = spending_frequency
        self.housing_type = housing_type

    def generateTransaction(self, start_date):
        transaction_list = []
        self.balance['amount'] = float(self.balance['amount'])

        transaction_list.append(Transaction(
            id=str(uuid.uuid4()),
            this_account=self,
            other_counterparty='INCOME',
            type='INCOME',
            description="GET INCOME: {:.2f}".format(self.income),
            posted=start_date,
            completed=add_deltatime(start_date),
            new_balance=self.balance['amount'],
            value=self.income
        ))

        if self.type != 'SAVING':
            for spending, frequency in spending_frequency.items():
                transaction_num = getTransactionNum(frequency)
                merchant = random.choice(top_merchants[spending])

                for i in range(transaction_num):
                    amount = float('{:.2f}'.format(generate_amt(avg_txn_amts[spending])))

                    posted_date = start_date + timedelta(days=random.randint(0, 30))

                    transaction_list.append(Transaction(
                        id=str(uuid.uuid4()),
                        this_account=self,
                        other_counterparty=merchant,
                        type=spending,
                        description="Pay to {}: {:.2f}".format(merchant, amount),
                        posted=posted_date,
                        completed=add_deltatime(posted_date),
                        new_balance=self.balance['amount'],
                        value=amount
                    ))

            if self.housing_type is not None:
                list = [(type, value) for type, value in self.housing_type.items()]
                type, value = list[0]

                transaction_list.append(Transaction(
                    id=str(uuid.uuid4()),
                    this_account=self,
                    other_counterparty=type,
                    type=type,
                    description="Pay to {}: {:.2f}".format(type, value),
                    posted=start_date,
                    completed=add_deltatime(start_date),
                    new_balance=self.balance['amount'],
                    value=value
                ))

        transaction_list.sort(key=lambda x: x.posted)
        balance = self.balance['amount']
        for trans in transaction_list:
            balance = balance + trans.value
            trans.new_balance = '{:.2f}'.format(balance)

        self.balance = {
            "currency":self.balance['currency'],
            "amount":balance
        }
        return transaction_list


    @staticmethod
    def Generator(num, branch, user):
        for i in range(num):
            account_id = str(uuid.uuid4())
            label = "{} {}".format(user.username, branch.name)
            number = str(digits11())
            type = random.choice(type_list)
            balance= {
                "currency":random.choice(currency_list),
                "amount":'{}{:.2f}'.format(random.randint(0,100000), random.random())
            }
            account_routing = Routing(
                scheme="OBP",
                address=account_id
            ),
            iban = generateIBAN(branch.address.country_code.upper())
            yield Account(
                account_id=account_id,
                branch=branch,
                user=[user],
                label=label,
                number=number,
                type=type,
                balance=balance,
                account_routing=account_routing,
                iban=iban
            )
