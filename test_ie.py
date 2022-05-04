
 
def choice_option():
   Option = int(input("Opcion: "))
   if Option == 1:
      Puntaje = 1
      return Puntaje

   elif Option == 2:
      Puntaje = 2 
      return Puntaje

   elif Option == 3:
      Puntaje = 3
      return Puntaje

   elif Option == 4:
      Puntaje = 4
      return Puntaje
   
   elif Option == 5:
      Puntaje = 5
      return Puntaje

   else:
      Puntaje = 0
      return Puntaje


print("""
TEST de Inteligencia Emocional
Responde estas 15 Afirmaciones según alguna de estas opciones
Utilizando 1, 2, 3, 4 y 5.
1)no estás de acuerdo para nada
2)rara vez
3)ocasionalmente
4)seguido
5)muy seguido

Empecemos
""")

print("No pierdo el temperamento muy facilmente. ")
A1 = choice_option()
print("Me puedo relacionar con las emociones de los demás. ")
A2 = choice_option()
print("La gente dice que sé escuchar a los demás. ")
A3 = choice_option()
print("Me resulta fácil expresar mis emociones. ")
A4 = choice_option()
print("Me puedo adaptar a mis colegas en el trabajo. ")
A5 = choice_option()
print("Puedo dejar pasar ciertas cosas que me molestan fácilmente. ")
A6 = choice_option()
print("No me siento molesto cuando alguien me critica. ")
A7 = choice_option()
print("Soy muy consciente de lo que hago bien y de lo que hago mal. ")
A8 = choice_option()
print("No evito comunicarme con las personas para ahorrarme conflictos. ")
A9 = choice_option()
print("Disfruto organizar y gestionar eventos en mi casa o trabajo. ")
A10 = choice_option()
print("Me siento muy mal cuando veo gente sin hogar, en la calle. ")
A11 = choice_option()
print("Puedo controlar mi enojo todo el tiempo. ")
A12 = choice_option()
print("Mis amigos pueden confiar en mi. ")
A13 = choice_option()
print("No suelo cambiar muy seguido de estados de ánimo. ")
A14 = choice_option()
print("Es fácil para mi empezar una conversación. ")
A15 = choice_option()


resultado = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8 + A9 + A10 + A11 + A12 + A13 + A14 + A15

def run():
   print("""
   Ahora sumaremos el puntaje de tus 15 respuestas
   Tu resultado es """ + str(resultado) + """
   Si te dio entre 1 y 25, necesitás trabajar mucho tu inteligencia emocional.
   Entre 26 y 50 tenés una inteligencia emocional promedio, un pequeño esfuerzo de tu parte podría hacer una gran diferencia en tu vida.
   Entre 51 y 75 tenés una inteligencia emocional alta.
   """)


if __name__ == "__main__":
  run() 