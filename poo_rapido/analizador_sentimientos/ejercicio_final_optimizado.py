#ejercicio final mal hecho o hecho a lo criollo
#NO ESTÁ FINALIZADO. SALTEAR

import openai

#configuro la key
openai.api_key="" #COMPLETAR CON LA KEY DE LA API DE CHATGPT PARA QUE FUNCIONE

#creo una variable para asignar como rol de sistema
system_rol= '''Simula que sos un analizador de sentimientos.
                Yo te digo como me siento y vos me respondes con al menos 1 caracter y máximo 4 caracteres.
                SOLO RESPUESTAS NUMÉRICAS (float e int) donde -1 es negatividad máxima, 0 es neutral, y 1 positividad máxima'''

#creo una lista con un diccionario que es lo que debe recibir chat-gpt
#los roles se determinan por system, assistant y user (toda la info está en la documentación de chatgpt)
mensajes=[{"role": "system", "content": system_rol}]

class Sentimiento():
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
    
    def __str__(self):
        return "\x1b[1;{}m{}\x1b[0;37m".format(self.color,self.nombre) #el str de Sentimiento devuelve el cambio de color mas el se


class AnalizadorDeSentimientos:
    def __init__(self, rangos):
        self.rangos=rangos
    def analizar_sentimientos(self, polaridad):
        for rango, sentimiento in self.rangos:
            if rango[0] < polaridad <= rango[1]:
                return sentimiento
        return Sentimiento("MUY negativo!", "31")

rangos=[
    ((-0.6, -0.3), Sentimiento("Negativo", "31"))
]
        
        
        # if polaridad > -0.8 and polaridad<=-0.3:
        #     #el código cambia el color del texto consola a rojo
        #     return "\x1b[1;32m" +"Negativo" +"\x1b[0;37m" #al final lo vuelvo a blanco
        # elif polaridad >-0.3 and polaridad <-0.1:
        #     return "\x1b[1;32m" +"Algo Negativo" +"\x1b[0;37m"
        # elif polaridad >=-0.1 and polaridad <=0.1:
        #     return "\x1b[1;32m" +"Neutral" +"\x1b[0;37m"
        # elif polaridad >0.1 and polaridad <0.4:
        #     return "\x1b[1;32m" +"Algo Positivo" +"\x1b[0;37m"
        # elif polaridad >=0.4 and polaridad <0.9:
        #     return "\x1b[1;32m" +"Positivo" +"\x1b[0;37m"
        # elif polaridad >=0.9:
        #     return "\x1b[1;32m" +"MUY Positivo!" +"\x1b[0;37m"
        # else:
        #     return "\x1b[1;32m" +"MUY Negativo!" +"\x1b[0;37m"

analizadorSentimientos=AnalizadorDeSentimientos(rangos[0])


while True:
    user_prompt=input("\x1b[1;33m" +"\n Decime algo: " +"\x1b[0;37m")
    mensajes.append([{"role": "user", "content": user_prompt}])
    
    completion= openai.chat.completions.create(
        model= "gpt-3.5-turbo",
        messages= mensajes,
        max_tokens = 8
    )

    #aca añadimos su respuesta por si el usuario debiera resolver algo.
    respuesta= completion.choices[0].message["content"] #respuesta de chatgpt
    mensajes.append([{"role":"assistant", "content":respuesta}])

    polaridad=analizadorSentimientos.analizar_sentimientos(float(respuesta))
    print(polaridad)