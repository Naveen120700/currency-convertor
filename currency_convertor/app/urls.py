from django.urls import path
from .views import UpdateExchangeRates, LastUpdated, ConvertCurrency

urlpatterns = [
    path('update_exchange_rates', UpdateExchangeRates.as_view(), name='update_exchange_rates'),
    path('last_updated/<str:code>', LastUpdated.as_view(), name='last_update'),
    path('convert_currency', ConvertCurrency.as_view(), name='convert_currency'),
]