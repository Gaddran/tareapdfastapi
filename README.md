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

El servidor estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Cómo hacer peticiones a la API

Puedes utilizar herramientas como `curl`, [Postman](https://www.postman.com/) o [httpie](https://httpie.io/) para probar la API. 
### Ejemplo de petición POST para `/predict`

```bash
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{
    "pickup_weekday": 2,
    "pickup_hour": 0,
    "work_hours": 1,
    "pickup_minute": 28,
    "passenger_count": 5.0,
    "trip_distance": 1.2,
    "trip_time": 4.8,
    "trip_speed": 15.0,
    "PULocationID": 238,
    "DOLocationID": 239,
    "RatecodeID": 1.0
}'
```

#### Ejemplo de payload para `/predict`

```json
{
    "pickup_weekday": 2,
    "pickup_hour": 0,
    "work_hours": 1,
    "pickup_minute": 28,
    "passenger_count": 5.0,
    "trip_distance": 1.2,
    "trip_time": 4.8,
    "trip_speed": 15.0,
    "PULocationID": 238,
    "DOLocationID": 239,
    "RatecodeID": 1.0
}

```

Consulta la documentación interactiva de la API en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Thanks

Thanks to [Harish](https://harishgarg.com) for the [inspiration to create a FastAPI quickstart for Render](https://twitter.com/harishkgarg/status/1435084018677010434) and for some sample code!