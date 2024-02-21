from django.shortcuts import render

# Create your views here.
# app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Currency
from .serializers import CurrencySerializer
from .utils import get_exchange_rates,get_conversion,get_last_updated

class UpdateExchangeRates(APIView):
    permission_classes = []
    def get(self, request):
        # Update exchange rates in the database
        try:
            rates = get_exchange_rates()
            if rates["result"]=="success":
                for code, rate in rates['rates'].items():
                    try:
                        currency = Currency.objects.get(code=code)
                        currency.rate = rate
                        currency.save()
                    except:
                        pass
                return Response({"status":True,"msg": "Exchange rates updated successfully."})
            return Response({"status": False, "msg": "Exchange rates could not get updated, Please try again."})
        except:
            return Response({"status": False, "msg": "Exchange rates could not get updated, Please try again."})

class LastUpdated(APIView):
    def get(self, request, code):
        last_updated = get_last_updated(code)
        if not last_updated:
            return Response({
                "status": False,
                "msg": "Please provide valid code.",
                "data": []
            }
            )
        return Response({
                "status": True,
                "msg": "OK",
                "data": last_updated
            }
        )

class ConvertCurrency(APIView):
    def get(self, request):
        try:
            source = request.query_params.get("source")
            target = request.query_params.get("target")
            amount = request.query_params.get("amount")
            if not source or not target or not amount:
                return Response(
                    {
                        "status": False,
                        "msg": "Please provide valid input.",
                        "data": []
                    }
                )
            amount = int(amount)
            source_object = Currency.objects.get(code=source)
            target_object = Currency.objects.get(code=target)
            conversion_result = get_conversion(source_object,target_object,amount)
            return Response({
                "status": True,
                "msg": "OK",
                "data": conversion_result
            })
        except Exception as e:
            return Response(
                {
                    "status":False,
                    "msg":"Something went wrong, Please try again.",
                    "data": []
                }
            )
        except Currency.DoesNotExist as e:
            return Response(
                {
                    "status": False,
                    "msg": "Please provide valid source, target code.",
                    "data": []
                }
            )
