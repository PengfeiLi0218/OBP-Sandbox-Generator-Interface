from datetime import date

from objects.Routing import *

type_list = ['10219']

income_list = np.arange(50000, 120000, 5000)

def generate_amt(base_amt):
    return random.uniform((base_amt * 0.6), (base_amt * 1.4))

def generate_transaction(account, tag, type, posted_date):
    id = str(uuid.uuid4())

    merchant = random.choice(top_merchants[tag]) if type == "DEBIT" else "Credit Card Payment"


    amount = generate_amt(avg_txn_amts[tag]) if type == "DEBIT" else generate_amt(1000)

    while abs(float(account.balance)) < amount:
        amount = generate_amt(avg_txn_amts[tag]) if type == "DEBIT" else generate_amt(float(account.balance))

    account.balance = float(account.balance) + amount

    return Transaction(
            id=id,
            this_account=account,
            other_counterparty=merchant,
            type=type,
            description="Pay to {}: {:.2f}".format(merchant, amount) if merchant!='INCOME' else "GET INCOME: {:.2f}".format(amount),
            posted=posted_date.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            completed=add_deltatime(posted_date).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            new_balance='{:.2f}'.format(account.balance),
            value='{:.2f}'.format(amount)
        )


class Transaction:
    def __init__(self, id, this_account, other_counterparty, type, description,
                 posted, completed, new_balance, value
                 ):
        self.id = id
        self.this_account = this_account
        self.other_counterparty = other_counterparty
        self.type= type
        self.description= description
        self.posted= posted
        self.completed= completed
        self.new_balance= new_balance
        self.value= value

    def dict(self):
        return {
            "id" : self.id,
            "this_account":{
                "id": self.this_account.account_id,
                "bank": self.this_account.branch.bank.id
            },
            #"counterparty":{
            #    "name": other_counterparty
            #},
            "details":{
                "type": self.type,
                "description": self.description,
                "posted": self.posted.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                "completed": self.completed.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                "new_balance": self.new_balance,
                "value": '{:.2f}'.format(self.value)
            }
        }


    @staticmethod
    def Generator(account, months):
        income = random.choice(income_list)
        take_home_pay = income * .6
        daily_income = take_home_pay / 365

        total_spending = daily_income * 30

        date_end = date.today()
        stmt = []
        accttype = random.choice(['DEBIT', 'CREDITCARD'])
        balance = generate_amt(-5000) if accttype == "CREDITCARD" else generate_amt(1000)

        account.balance = balance

        for i in range(months):
            housing_tag = random.choice(["rent", "mortgage"])

            date_end = date_end - timedelta(days= 30)
            last_housing = date_end
            transaction = generate_transaction(account, housing_tag, "DEBIT", last_housing)
            stmt.append(transaction)
            total_spending -= abs(float(transaction.value))

            for tag in tags:
                date_tmp = date_end - timedelta(days=random.randint(0, 30))
                tag_spending = total_spending * spending_pcts[tag]
                while tag_spending > 0 and total_spending > 0:
                    transaction = generate_transaction(account, tag, accttype, date_tmp)
                    stmt.append(transaction)
                    tag_spending   -= abs(float(transaction.value))
                    total_spending -= abs(float(transaction.value))

            account.balance += income

        yield stmt