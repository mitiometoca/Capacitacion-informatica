#coding=utf-8
#programa que pida una contrasena y rechase al usuario
#despues de cinco intentos

import time

password = "overwaifu"
correcto = 0
intentos = 1

print("bienvenido al centro educativo patria.")


while (correcto==0) & (intentos<=4):
	intento = input("introduce tu contrasena:")
	if intento==password:
		correcto=1
		print("tu contrasena es correcta")
	else:
		time.sleep(5)
		print("la contrasenas incorrecta")
		intentos=intentos+1	
		if intentos>4: 	
			print("has introducido demasiadas contrasenas") 
