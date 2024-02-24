import json,os
from django.core.management.base import BaseCommand
from app.models import Currency

class Command(BaseCommand):
    help = 'Import initial data for Currency model from a JSON file'

    def handle(self, *args, **options):
        file_name = 'initial_currency_data.json'
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../data', file_name)

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            codes = [entry["code"] for entry in data]
            existing = Currency.objects.filter(code__in=codes).values_list("code",flat=True)
            if len(codes) == len(existing):
                self.stdout.write(self.style.SUCCESS('Currency data is already added.'))
            else:
                for currency_data in data:
                    if currency_data["code"] in existing:
                        currency = Currency.objects.get(code=currency_data["code"])
                        currency.rate = currency_data["rate"]
                        currency.save()
                    else:
                        Currency.objects.create(**currency_data)

                self.stdout.write(self.style.SUCCESS('Successfully imported initial data'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found. Please provide the correct file path'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {str(e)}'))