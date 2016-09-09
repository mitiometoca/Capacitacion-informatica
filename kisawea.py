#coding=utf-8
nombre = input("Dime tu nombre: ")
edad = int(input("dime tu edad wey: ")) 
nombre2 = input("dime tu nombre tambien wey: ")
edad2 = int(input("y tu edad es?... "))
if (edad>edad2):
	print ("%s, eres mayor que %s" % (nombre , nombre2))
	 
elif (edad<edad2):
	print ("%s, eres mayor que %s" % (nombre2 , nombre))

else:
	print ("%s y %s tienen la misma edad" % (nombre , nombre2))
