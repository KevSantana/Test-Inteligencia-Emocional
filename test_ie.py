
import os

lang = input("""starting program....

Select Language: 
>Spanish
>Portuguese
>English

""")

resultado = 0
frases = []

if lang == "Spanish":
    with open(".//Archivos//spanish.txt","r", encoding="utf-8") as f:
        for line in f:
            frases.append(line)
elif lang == "Portuguese":
    with open(".//Archivos//portuguese.txt","r", encoding="utf-8") as f:
        for line in f:
            frases.append(line)
else:
    with open(".//Archivos//english.txt","r", encoding="utf-8") as f:
        for line in f:
            frases.append(line)


def welcome():
    if lang == "Spanish":
        print("""
Responde las siguientes afirmaciones usando: 1, 2, 3, 4 y 5.
1 no estás de acuerdo para nada
2 rara vez
3 ocasionalmente
4 seguido
5 muy seguido
""")
    elif lang == "Portuguese":
        print("""
Responda as seguintes afirmações usando: 1, 2, 3, 4 e 5.
1 você não concorda nada
2 raramente
3 ocasionalmente
4 seguidos
5 muitas vezes
""")      
    else:
        print("""
Answer the following statements using: 1, 2, 3, 4 and 5.
1 you don't agree at all
2 rarely
3 occasionally
4 often
5 very often
""")

def end(resultado):
    if lang == "Spanish":
        print("""
Felicidades Completaste el Test!            
Tu resultado del Test es """ + str(resultado) + """
Si te dio entre 1 y 25, necesitás trabajar mucho tu inteligencia emocional.
Entre 26 y 50 tenés una inteligencia emocional promedio, un pequeño esfuerzo de tu parte podría hacer una gran diferencia en tu vida.
Entre 51 y 75 tenés una inteligencia emocional alta.
""")
    elif lang == "Portuguese":
        print("""
Parabéns, você completou o teste!
O resultado do seu teste é """ + str(resultado) + """
Se ele te deu entre 1 e 25, você precisa trabalhar muito sua inteligência emocional.
Entre 26 e 50 anos você tem inteligência emocional média, um pouco de esforço de sua parte pode fazer uma grande diferença em sua vida.
Entre 51 e 75 você tem uma alta inteligência emocional.
""")
    else:
        print("""
Congratulations, you completed the test!
Your test result is """ + str(resultado) + """
If he gave you between 1 and 25, you need to work a lot on your emotional intelligence.
Between 26 and 50 you have average emotional intelligence, a little effort on your part could make a big difference in your life.
Between 51 and 75 you have a high emotional intelligence.
""")


def read():
    contador = 0
    resultado = 0

    for contador, i in enumerate(frases, start=1):
        print(contador, i + "\n")
        respuesta = (input("Opcion: "))
        assert respuesta.isnumeric() and int(respuesta) <6 and int(respuesta) >0 ,"Solo puede ingresar un número del 1 al 5"
        os.system ("cls")
        if contador < 15:
            welcome()
        resultado = (resultado + int(respuesta))
        if contador == 15:
            end(resultado)


def restart():
    inicio = input("Quieres reintentar? si/no ")
    if inicio == "si":
        run()
    else:
        print("Fin del programa")
        

def run():
    os.system ("cls")
    welcome()
    try:
        read()
        restart()
    except AssertionError:
        print("Solo puede ingresar un número del 1 al 5")
        restart()


if __name__ == '__main__':
    run()