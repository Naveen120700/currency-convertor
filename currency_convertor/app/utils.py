import httpx
from .models import Currency
from django.conf import settings
def get_exchange_rates():
    try:
        with httpx.Client() as client:
            # response = client.get(, params={"access_key": settings.EXCHANGE_API_SECRET})
            response = client.get(f"{settings.EXCHANGE_API_URL}{settings.BASE_CURRENCY}")
            return response.json()
    except Exception as e:
        return dict

def get_conversion(source,target,amount):
    return amount * (target.rate / source.rate)

def get_last_updated(code=None):
    try:
        if code:
            last_modified = Currency.objects.get(code=code).last_modified
            return last_modified.strftime("%d-%m-%y %H:%M:%S")
        return Currency.objects.all().values(Currency.objects.all().values("code","name","last-modified"))
    except:
        return None

