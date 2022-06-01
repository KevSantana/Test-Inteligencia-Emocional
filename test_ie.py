import os


def restart():
    inicio = input("Quieres reintentar? si/no ")
    if inicio == "si" or "SI" or "Si":
        run()
    else:
        print("Fin del programa")


def bienvenido():
    print("""
Bienvenido al Test de Inteligencia Emocional
Responde las siguientes afirmaciones usando: 1, 2, 3, 4 y 5.
1)no estás de acuerdo para nada
2)rara vez
3)ocasionalmente
4)seguido
5)muy seguido

Empecemos
""")


def read():
    frases = []
    contador = 0
    resultado = 0
    with open("C:\\Users\\Kevin\\Desktop\\Projectos\\Test_ie\\Archivos\\afirmaciones.txt","r", encoding="utf-8") as f:
        for line in f:
            frases.append(line)
    for i in frases:
        contador += 1
        print(i + "\n")
        respuesta = (input("Opcion: "))
        assert respuesta.isnumeric() and int(respuesta) <6 and int(respuesta) >0 ,"Solo puede ingresar un número del 1 al 5"
        os.system ("cls")
        if contador < 15:
            bienvenido()
        resultado = (resultado + int(respuesta))
        if contador == 15:
            print("""
Felicidades Completaste el Test!            
Tu resultado del Test es """ + str(resultado) + """
Si te dio entre 1 y 25, necesitás trabajar mucho tu inteligencia emocional.
Entre 26 y 50 tenés una inteligencia emocional promedio, un pequeño esfuerzo de tu parte podría hacer una gran diferencia en tu vida.
Entre 51 y 75 tenés una inteligencia emocional alta.
""")
        

def run():
    os.system ("cls")
    bienvenido()
    try:
        read()
        restart()
    except AssertionError:
        print("Solo puede ingresar un número del 1 al 5")
        restart()


if __name__ == '__main__':
    run()