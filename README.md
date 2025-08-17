## Instrucciones para instalar dependencias

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/tu-repo.git
    cd tu-repo
    ```
2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Cómo ejecutar el servidor localmente

Ejecuta el siguiente comando en la raíz del proyecto:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en [https://tareapdfastapi.onrender.com/](https://tareapdfastapi.onrender.com/).

## Cómo hacer peticiones a la API

Puedes utilizar herramientas como `curl`, [Postman](https://www.postman.com/) o [httpie](https://httpie.io/) para probar la API. 
### Ejemplo de petición POST para `/predict`

```bash
# Ejemplo 1
curl -X POST "https://tareapdfastapi.onrender.com/predict" -H "Content-Type: application/json" -d '{
    "pickup_weekday": 2,
    "pickup_hour": 0,
    "work_hours": 1.0,
    "pickup_minute": 28,
    "passenger_count": 5,
    "trip_distance": 1.2,
    "trip_time": 4.8,
    "trip_speed": 15.0,
    "PULocationID": 238,
    "DOLocationID": 239,
    "RatecodeID": 1.8
}'

# Ejemplo 2
curl -X POST "https://tareapdfastapi.onrender.com/predict" -H "Content-Type: application/json" -d '{
    "pickup_weekday": 5,
    "pickup_hour": 14,
    "work_hours": 6.5,
    "pickup_minute": 45,
    "passenger_count": 2,
    "trip_distance": 3.7,
    "trip_time": 12.3,
    "trip_speed": 18.0,
    "PULocationID": 151,
    "DOLocationID": 87,
    "RatecodeID": 1.0
}'

# Ejemplo 3
curl -X POST "https://tareapdfastapi.onrender.com/predict" -H "Content-Type: application/json" -d '{
    "pickup_weekday": 0,
    "pickup_hour": 22,
    "work_hours": 10.0,
    "pickup_minute": 5,
    "passenger_count": 1,
    "trip_distance": 8.5,
    "trip_time": 25.0,
    "trip_speed": 20.4,
    "PULocationID": 132,
    "DOLocationID": 265,
    "RatecodeID": 2.0
}'
```

#### tipos de datos para payload `/predict`

```json
{
    pickup_weekday: int,
    pickup_hour: int,
    work_hours: float,
    pickup_minute: int,
    passenger_count: int,
    trip_distance: float,
    trip_time: float,
    trip_speed: float,
    PULocationID: int,
    DOLocationID: int,
    RatecodeID: float
}
```

Consulta la documentación interactiva de la API en [https://tareapdfastapi.onrender.com/docs](https://tareapdfastapi.onrender.com/docs).
