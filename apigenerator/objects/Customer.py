import random
import uuid

from object.Routing import phone_number_generation, gen_datetime

relationship_status_list = ['Married','Divorced','Single']
employment_status_list = ['Student','Employed']
highest_education_attained_list = ['BA.','Phd.']

class Customer:
    def __init__(self, customer_number, user, mobile_phone_number,
                 face_image, date_of_birth, relationship_status,
                 dependants, dob_of_dependants, highest_education_attained,
                 employment_status, kyc_status, last_ok_date, bank, credit_rating,
                 credit_limit
                 ):
        self.customer_number=customer_number
        self.user=user
        self.mobile_phone_number=mobile_phone_number
        self.face_image=face_image
        self.date_of_birth=date_of_birth
        self.relationship_status=relationship_status
        self.dependants=dependants
        self.dob_of_dependants=dob_of_dependants
        self.highest_education_attained=highest_education_attained
        self.employment_status=employment_status
        self.kyc_status=kyc_status
        self.last_ok_date=last_ok_date
        self.bank=bank
        self.credit_rating=credit_rating
        self.credit_limit=credit_limit

    def dict(self):
        return {
            "customer_number": self.customer_number,
            "legal_name": self.user.username,
            "mobile_phone_number": self.mobile_phone_number,
            "email": self.user.email,
            "face_image": self.face_image,
            "date_of_birth": self.date_of_birth,
            "relationship_status": self.relationship_status,
            "dependants": self.dependants,
            "dob_of_dependants": self.dob_of_dependants,
            "highest_education_attained": self.highest_education_attained,
            "employment_status": self.employment_status,
            "kyc_status": self.kyc_status,
            "last_ok_date": self.last_ok_date,
            "bank_id": self.bank.id,
            "credit_rating": self.credit_rating,
            "credit_limit": self.credit_limit
        }

    @staticmethod
    def Generator(user, bank, num):
        for i in range(num):
            customer_number = str(uuid.uuid4())
            mobile_phone_number = phone_number_generation()
            face_image = {
                "url": "www.example.com",
                "date": gen_datetime().strftime("%Y-%m-%dT%H:%M:%S.000Z")
            }
            date_of_birth = gen_datetime(min_year = 1970, max_year=2001).strftime("%Y-%m-%d %H:%M:%S")
            dob_of_dependants = [
                gen_datetime().strftime("%Y-%m-%d %H:%M:%S") for _ in range(2)
            ]

            kyc_status = True
            last_ok_date = gen_datetime().strftime("%Y-%m-%dT%H:%M:%S.000Z")
            credit_rating=""
            credit_limit=""
            yield Customer(
                customer_number=customer_number,
                user=user,
                mobile_phone_number=mobile_phone_number,
                face_image=face_image,
                date_of_birth=date_of_birth,
                relationship_status=random.choice(relationship_status_list),
                dependants=random.randint(0,6),
                dob_of_dependants=dob_of_dependants,
                highest_education_attained=random.choice(highest_education_attained_list),
                employment_status=random.choice(employment_status_list),
                kyc_status=kyc_status,
                last_ok_date=last_ok_date,
                bank=bank,
                credit_rating=credit_rating,
                credit_limit=credit_limit
            )