#coding=utf-8
#cuenta para entrar a un burger shop


#programa de password
conteo = 0
nombre = "Sean"
password = "llogomito"

usuario = input("introduce tu nombre: ")

while (nombre != usuario):
	print ("no tienes autorizacion para entrar a esta computadora")
	usuario = input("vuelve a introducir tu nombre: ")
	
con1 = input("introduce tu password: ")

while (conteo <= 5):
	if (con1 != password):
		intento = input("vuelve a introducir tu password: ")
		conteo = conteo + 1
	else:
		

#programa de pedidos
		costo = 0
		pedido = 1

		print("buenos dias que quiere pedir?")

		print("1. famous star ($90) \n2. papas grandes ($40) \n3. santa fe ($100) \n4. soda grande ($30) \n5. salir")
	
		while (pedido < 5):
			pedido = int(input("que numero vas a pedir: "))
			if (pedido == 1):
				costo = costo + 90
			elif (pedido == 2):
				costo = costo + 40
			elif(pedido  == 3):
				costo = costo + 100
			elif(pedido == 4):
				costo = costo + 30
			elif(pedido < 1):
				print("ese orden no existe")
			print("tu orden es de $%s pesos" % costo)

	
print("gracias por venir a emiliano, tomy & sean's burger shop")
