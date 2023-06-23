import pyttsx3
import time
import tiktok
import db

def convertir_texto_a_voz(texto):
    engine = pyttsx3.init()

    # Configurar la voz de Microsoft
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)  # Utilizar la primera voz de Microsoft

    
    engine.say(texto)
    engine.runAndWait()

while True:
    elemento_extraido = db.extraer_elemento()
    if elemento_extraido == None:
        continue
    convertir_texto_a_voz(elemento_extraido)
        
    print("Procesando línea:", elemento_extraido)
            
    # Una vez que la línea ha sido procesada, no la escribimos en el archivo nuevamente,
    
#convertir_texto_a_voz(texto)
#time.sleep(1)
#convertir_texto_a_voz(tiktok.comentario)

