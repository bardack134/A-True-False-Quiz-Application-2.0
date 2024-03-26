import requests


# La URL de la API de Trivia desde donde obtendremos las preguntas
api="https://opentdb.com/api.php?amount=10"


# Los parámetros que pasaremos a la API. En este caso, estamos solicitando 10 preguntas de tipo booleano (verdadero/falso)
parameters={
    'amount': 10,
    'type':'boolean',
}

# Realizamos una solicitud GET a la API con los parámetros especificados
response=requests.get(api, params=parameters)


# Verificamos que la solicitud fue exitosa. Si hubo un error (como un error 404 o 500), esto generará una excepción
response.raise_for_status()


# Convertimos la respuesta de la API a formato JSON y obtenemos la lista de resultados, que contiene las preguntas
question_data=response.json()['results']



print(question_data)
