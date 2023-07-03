import openai
from pydantic import BaseModel
# Importamos la biblioteca openai para interactuar con OpenAI GPT-3
# Importamos BaseModel de pydantic para definir el esquema del objeto Document

# Definimos una clase Document que hereda de BaseModel y tiene un atributo prompt de tipo string


class Document(BaseModel):
    prompt: str = ''


def inference(prompt: str) -> list:
    # Definimos la función de inferencia que toma una cadena prompt como entrada y devuelve una lista

    print('[PROCESANDO KARI Ponte Pilas]'.center(40, '-'))
    # Imprimo un mensaje de inicio de procesamiento

    openai.organization = 'org-FlF7DjfN8kf6smfJafiv4p82'
    openai.api_key = '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'
    # Configuramos la organización y la clave de API de OpenAI

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Eres un calculador matemático" "Elige un numero y dame el resultado el "
                                          "factorial" "y si texto da un mensaje de error"},
            {"role": "user", "content": prompt}
        ]
    )
    # Creamos una conversación con el modelo de lenguaje gpt-3.5-turbo de OpenAI
    # Enviamos un mensaje de sistema que indica que queremos invertir la palabra
    # Y enviamos el mensaje del usuario con la palabra a invertir

    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    # Obtenemos el contenido del mensaje de respuesta del modelo y el número total de tokens utilizados en la inferencia

    print('[Finalizo el proceso KARI >>]'.center(40, '-'))
    # Imprimo un mensaje de finalización del procesamiento

    return [content, total_tokens]
    # Devolvemos el contenido del mensaje de respuesta y el número total de tokens utilizados en forma de lista
