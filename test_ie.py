
def run():
   print("""
   Medidor de Inteligencia Emocional
   Contesta estas 15 Afirmaciones según alguna de estas opciones
   Utilizando 1, 2, 3, 4 o 5
   1 no estás de acuerdo para nada
   2 rara vez
   3 ocasionalmente
   4 seguido
   5 muy seguido

   Empecemos""")

   A1 = int(input("No pierdo el temperamento muy facilmente. "))
   A2 = int(input("Me puedo relacionar con las emociones de los demás. "))
   A3 = int(input("La gente dice que sé escuchar a los demás. "))
   A4 = int(input("Me resulta fácil expresar mis emociones. "))
   A5 = int(input("Me puedo adaptar a mis colegas en el trabajo. "))
   A6 = int(input("Puedo dejar pasar ciertas cosas que me molestan fácilmente. "))
   A7 = int(input("No me siento molesto cuando alguien me critica. "))
   A8 = int(input("Soy muy consciente de lo que hago bien y de lo que hago mal. "))
   A9 = int(input("No evito comunicarme con las personas para ahorrarme conflictos. "))
   A10 = int(input("Disfruto organizar y gestionar eventos en mi casa o trabajo. "))
   A11 = int(input("Puedo controlar mi enojo todo el tiempo. "))
   A12 = int(input("Me siento muy mal cuando veo gente sin hogar, en la calle. "))
   A13 = int(input("No suelo cambiar muy seguido de estados de ánimo. "))
   A14 = int(input("Es fácil para mi empezar una conversación. "))
   A15 = int(input("Mis amigos pueden confiar en mi. "))

   resultado = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15

   print("""
   Ahora sumaremos el puntaje de tus 15 respuestas
   Tu resultado es """ + str(resultado) + """
   Si te dio entre 1 y 25, necesitás trabajar mucho tu inteligencia emocional.
   Entre 26 y 50 tenés una inteligencia emocional promedio, un pequeño esfuerzo de tu parte podría hacer una gran diferencia en tu vida.
   Entre 51 y 75 tenés una inteligencia emocional alta.
   """)

if __name__ == "__main__":
   run() 