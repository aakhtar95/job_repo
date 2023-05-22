import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arifjobs.settings')
import django

django.setup()
from bestapp.models import Hydjobs
from faker import Faker
from random import *

fake = Faker()


def phonenumbergen():
    d1 = randint(6, 9)
    num = " " + str(d1)
    for i in range(9):
        num = num + str(randint(0, 9))
    return int(num)


def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(
            elements=('project manager', 'team leader', 'software engineer', 'associate engineer'))
        felegiblity = fake.random_element(elements=('b.tech''m.tech', 'mca', 'phd', 'mahesh sir student'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        Hydjobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, elegiblity=felegiblity,
                                      address=faddress, email=femail, phonenumber=fphonenumber)


n = int(input("enter number of records:"))
populate(n)
print(f'{n} records inserted sucessfully...')
