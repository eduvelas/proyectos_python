def menu():
	#crear menu
	print """>>>****Bienvenido al comtrol de usario****<<<
	menu:
	1) **Crear cuenta** 
    2) **Iniciar sesion**  
    4) **Extra** 
    5) **Salir***"""
#control de usuario
def control():
	menu()
	opc=int(input("seleccione la opccion que desea realizar:"))
    while=(opc>0 and opc<5):
		if(opc==1):
			n=str(input("Ingrese su nombre"))
			a=input("Ingrese su apellido")
			ap=input("Ingrese su apodo o su nikname")
			c=input("Ingrese su contraseña")
			e=input("Ingrese su edad")
