import requests

# URL of the prediction endpoint
PREDICT_URL = "http://localhost:8000/predict"

# Example payloads to test
test_inputs = [
        {
            "pickup_weekday": 1.0,
            "pickup_hour": 8.0,
            "work_hours": 1.0,
            "pickup_minute": 15.0,
            "passenger_count": 2.0,
            "trip_distance": 3.2,
            "trip_time": 12.5,
            "trip_speed": 15.4,
            "PULocationID": 41.0,
            "DOLocationID": 151.0,
            "RatecodeID": 1.0
        },
        {
            "pickup_weekday": 5.0,
            "pickup_hour": 18.0,
            "work_hours": 0.0,
            "pickup_minute": 45.0,
            "passenger_count": 1.0,
            "trip_distance": 7.8,
            "trip_time": 25.0,
            "trip_speed": 18.7,
            "PULocationID": 236.0,
            "DOLocationID": 162.0,
            "RatecodeID": 2.0
        },
        {
            "pickup_weekday": 2.0,
            "pickup_hour": 13.0,
            "work_hours": 5.0,
            "pickup_minute": 59.0,
            "passenger_count": 4.0,
            "trip_distance": 2.5,
            "trip_time": 1.10,
            "trip_speed": 105.0,
            "PULocationID": 1302.0,
            "DOLocationID": 408.0,
            "RatecodeID": 5.0
        }
    ]

for i, payload in enumerate(test_inputs):
    response = requests.post(PREDICT_URL, json=payload)
    print(f"Caso de prueba {i+1}: Entrada: {payload}")
    print(f"Respuesta: {response.status_code} {response.json()}\n")


    