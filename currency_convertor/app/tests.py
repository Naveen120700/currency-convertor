from django.test import TestCase

# Create your tests here.
import factory
from .models import Currency


class CurrencyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Currency

    code = factory.Sequence(lambda n: f'CUR{n:03d}')
    name = factory.Faker('currency_name')
    rate = factory.Faker('random_element', elements=[1.0, 1.2, 0.8])