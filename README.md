# currency-convertor

## Intial Project setup

1. **Traverse through the project directory**
   ```bash
   cd currency_conversion
   ```
## Run the project
1. **Start the project in docker**
   ```bash
   docker-compose up -d --build   
   ```
2. **Stop the project in docker**
   ```bash
   docker-compose down   
   ```

## Intial Migrations 
A migration script is present in the app/migrations 0001_intial.py, that helps in creating data after intialising the model.

## Endpoints

1. **Api to convert currency**
   ```commandline
   http://localhost:8000/api/v1/convert_currency?source={source-currency-code}&target={source-currency-code}&amount={amount}
   ```
   example: http://localhost:8000/api/v1/convert_currency?source=USD&target=INR&amount=1000
   source-currrency-code refers to code of the source currency
   target-currrency-code refers to code of the target currency
   amount refers to the amount that needs to be calculated

2. **Api to get last updated date of a currency**
   ```commandline
   http://localhost:8000/api/v1/last_updated/{currency-code}
   ```
   example: http://localhost:8000/api/v1/last_updated/{currency-code}
   currrency-code refers to code of the source currency


3. **Api to update the exchange rates**
   ```commandline
   http://localhost:8000/api/v1/update_exchange_rates
   ```
   example: http://localhost:8000/api/v1/update_exchange_rates