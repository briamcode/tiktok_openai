from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent, ConnectEvent
import re
import openai
import db

openai.api_key = " "
model_engine = "text-davinci-003"


# Función para generar una respuesta de ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Instantiate the client with the user's username
client: TikTokLiveClient = TikTokLiveClient(unique_id="@_johncito_")

# Define how you want to handle specific events via decorator
@client.on("connect")
async def on_connect(_: ConnectEvent):
    print("Connected to Room ID:", client.room_id)

# Notice no decorator?
async def on_comment(event: CommentEvent):
    prompts = "asume el rol de By Jcomunicaciones dile Hola a los usuarios solo la primera vez que hacen comentarios si han comentado no les digas hola, eres un tiktoker fanatico de la tecnologia que interactua con su publico al cual aprecia mucho por medio del chat respondiendo al comentario de este usuario :  "
    comentario = f"{event.comment}"
    #if "?" in comentario:
    #if re.search(r"\?", comentario):
    respuesta = generate_response(prompts + f"{event.user.nickname}" +  comentario)
    db.insertar_elemento(respuesta)
    

    print(f"{event.user.nickname} -> {event.comment}")

    
# Define handling an event via a "callback"
client.add_listener("comment", on_comment)

if __name__ == '__main__':

    client.run()
   


    

    
