# Weather API

## Installation

Clone the repository

```bash
git clone git@github.com:AtanasKisyov/weather_api.git
pip install -r requirements.txt
```
Check the database credentials in settings.py to match your local PostgreSQL
## Usage

Register
```bash
http POST http://127.0.0.1:8000/auth/register/ username="test" password="test1234"

{
    "password": "Hidden", # Did not feel right to return hashed the password
    "username": "test"
}
```
Authorization token
```bash
http POST http://127.0.0.1:8000/auth/token/ username="test" password="test1234"

{
    "token": "14c02c2cc264ee3ea6e154778940ef560496abf0"
}
```

# Endpoints

Weather by city name
```bash
http GET http://127.0.0.1:8000/get-weather-by-city/yambol "Authorization: Token 14c02c2cc264ee3ea6e154778940ef560496abf0"

{
    "city": 3,
    "humidity": 82.0,
    "id": 9,
    "maximum_temperature": 19.99,
    "minimum_temperature": 16.14,
    "pressure": 1013.0,
    "temperature": 16.14,
    "time": "2022-05-24T09:45:08.605316+03:00",
    "wind_speed": 2.06
}
```
City information
```bash
http GET http://127.0.0.1:8000/get-city-information/yambol "Authorization: Token 14c02c2cc264ee3ea6e154778940ef560496abf0"

{
    "city_name": "yambol",
    "country_abbreviation": "BG",
    "id": 3,
    "latitude": 42.4833,
    "longitude": 26.5
}
```
Combined data
```bash
http GET http://127.0.0.1:8000/get-combined-data/yambol "Authorization: Token 14c02c2cc264ee3ea6e154778940ef560496abf0"

{
    "city": 3,
    "city_name": "yambol",
    "country_abbreviation": "BG",
    "humidity": 82.0,
    "id": 9,
    "latitude": 42.4833,
    "longitude": 26.5,
    "maximum_temperature": 19.99,
    "minimum_temperature": 16.14,
    "pressure": 1013.0,
    "temperature": 16.14,
    "time": "2022-05-24T09:45:08.605316+03:00",
    "wind_speed": 2.06
}

```
