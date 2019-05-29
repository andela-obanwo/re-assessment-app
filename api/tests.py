from django.test import TestCase
from api.models import Birthday
from datetime import datetime

# Create your tests here.
class BirthdayTest(TestCase):
    def test_birthday_model_str(self):
        birthday = Birthday.objects.create(date=datetime.now())

        self.assertEqual(str(birthday), "{}:{}".format(birthday.date, birthday.celebrates))