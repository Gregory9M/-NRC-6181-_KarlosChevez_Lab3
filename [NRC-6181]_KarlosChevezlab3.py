from msilib.schema import Control
#Esto es usada para poder llevar un registro de exacto de la hora y fechade ingreso del cliente 
from calendar import c
import datetime
#Esta la clase cliente la cual contiene los diferentes objetos requeridos para la solución del problema
class datosCliente:
    def _init_(self, nombres, apellidos, edad, pais, usuario, contra):
        self.nombres=nombres
        self.apellidos=apellidos
        self.edad=edad
        self.pais=pais
        self.usuario=usuario
        self.contra=contra
    #Metodo para registrar el usuario y contraseña de la cuenta del cliente
    def registroNuevo(self, usuario, contra):
        self.usuario=usuario
        self.contra=contra


#Del mismo modo la clase datos tienda         
class datosTienda:
    def _init_(self, nombreTienda, ruc, telefono, gerente, tipoNegocio):
        self.nombreTienda=nombreTienda
        self.ruc=ruc
        self.telefono=telefono
        self.gerente=gerente
        self.tipoNegocio=tipoNegocio

    def registroTienda(self, gerente, ruc):
        self.gerente=gerente
        self.ruc=ruc


#El menú principal es lo primero que ve un usuario cuando abre la aplicación por primera vez. Es importante asegurarse de que sea fácil de navegar y tenga todas las funciones más importantes.
menuPrincipal=int(input("\n=============================== \nMENU PRINCIPAL: \n=============================== \n 1:CLIENTE \n 2:TIENDA \n 3:ADMINISTRADOR \n 4:SALIR \n=============================== \n INGRESE UNA OPCION:  "))
while menuPrincipal !=4:
    if menuPrincipal ==1:
        #Contiene enlaces a diferentes secciones del sitio web, así como algunas otras funciones, como búsqueda, inicio de sesión
        menuClientes=int(input("\n======================= \n CLIENTES: \n======================= \n 1:REGISTRARSE \n 2:INICIAR SESION \n 3:REGRESAR MENU PRINCIPAL \n======================= \n INGRESE UNA OPCION: "))
        while menuClientes !=3:
            if menuClientes ==1:
                #Los clientes son aquellos que compran los productos o servicios de una empresa, ya sea en línea o en persona.
                print ("====================================================================")
                print ("                    REGISTRO DE CLIENTES ")
                print ("====================================================================")
                nombres=str(input("INGRESE SUS DOS NOMBRES: "))
                apellidos=str(input("INGRESE SUS DOS APELLIDOS: "))
                pais=str(input("INGRESE SU NACIONALIDAD: "))
                edad=int(input("INGRES SU EDAD: "))
                if edad>=17 and edad<=65 :
                    print ("EDAD PERMITIDA")
                else:
                    print("EDAD NO PERMITIDA POR SER MENOR DE EDAD, VUELVA A INGRESAR")
                    edad=int(input("INGRESE SU EDAD: "))
                    #Validación de la edad, en caso de tener menos de 18 años
                    if edad>=17 and edad<=65 :
                        print ("EDAD PERMITIDA")
                    else:
                        print("EDAD NO PERMITIDA POR SER MENOR DE EDAD, VUELVA A INGRESAR")
                       
                usuario=str(input("REGISTRE SU USUARIO EN LA TIENDA: "))
                contra=str(input("CREE UNA CONTRASENA PARA EL CONTROL DE SU CUENTA: "))
                ##Esto sirve para poder determinar la hora y fecha del ingreso exacta de un nuevo cliente
                fecha1=datetime.datetime.now()
                fecha2=datetime.datetime.strftime(fecha1, '%b %d %Y %H:%M:%S')
                print ("====================================================================")

            if menuClientes ==2:
                #Los usuarios pueden iniciar sesión proporcionando su nombre de usuario y contraseña, o mediante la autenticación.
                print ("====================================================================")
                print ("                         INCIAR SESION ")
                print ("====================================================================")
                cliente=str(input("INGRESE SU USURIO REGISTRADO: "))
                contrasena=str(input("CONTRASEÑA: "))
                if cliente==usuario and contrasena==contra:
                    print("LOS DATOS INGRESADOS SON CORRECTOS")
                    print ("====================================================================")
                    menuClientes=int(input("\n======================= \n CLIENTES: \n======================= \n 1:REGISTRARSE \n 2:INICIAR SESION \n 3:REGRESAR MENU PRINCIPAL \n======================= \n INGRESE UNA OPCION: "))
                else:
                    print("LOS DATOS INGRESADOS SON INCORRECTOS, VUELVA A INGRESAR:")
                    print ("====================================================================")


            if menuClientes ==3:
                print ("REGRESAR AL MENU PRNCIPAL ") 
                menuPrincipal=int(input("\n=============================== \nMENU PRINCIPAL: \n=============================== \n 1:CLIENTE \n 2:TIENDA \n 3:ADMINISTRADOR \n 4:SALIR \n=============================== \n INGRESE UNA OPCION:  "))
            #En caso de que el usuario ingrese un numero incorrecto pueda volver a ingresar
            else:
                print("LA OPCION INGRESA ES INCORRECTA VUELVA A INGRESAR: ")
                menuClientes=int(input("\n======================= \n CLIENTES: \n======================= \n 1:REGISTRARSE \n 2:INICIAR SESION \n 3:REGRESAR MENU PRINCIPAL \n======================= \n INGRESE UNA OPCION: "))
#==================================================================================================================================================================================================================================================================================
    if menuPrincipal ==2:
       # print ("TIENDA ")
        #Contiene enlaces a diferentes secciones del sitio web, así como algunas otras funciones, como búsqueda, inicio de sesión
        menuTienda=int(input("\n======================= \n TIENDAS: \n======================= \n 1:REGISTRO DE TIENDAS \n 2:INICIAR SESION \n 3:REGRESAR MENU PRINCIPAL \n======================= \n INGRESE UNA OPCION: "))
        while menuTienda!=3:
            if menuTienda==1:
                #El registro de una tienda es un proceso que los comerciantes pueden usar para registrar su negocio con el gobierno.
                print ("====================================================================")
                print ("                  REGISTRO DE NEGOCIOS NUEVOS ")
                print ("====================================================================")
                nombreTienda=str(input("INGRESE EL NOMBRE DE SU NEGOCIO: "))
                ruc=str(input("INGRESE EL RUC DEL NEGOCIO: "))
                telefono=int(input("INGRESE EL NUMERO DE TELEFONO DEL NEGOCIO: "))
                gerente=str(input("INGRESE EL NOMBRE Y APELLIDO DEL GERENTE: "))
                #INGRESA EL TIPO DE NEGOCIO EJ. BAZAR, TIENDA, CYBER, RESTAURANTE, ETC.
                tipoNegocio=str(input("INGRESE EL TIPO DE NEGOCIO QUE VA REGISTAR: "))
                #Esto sirve para poder determinar la hora y fecha del ingreso exacta de la nueva tienda
                fecha3=datetime.datetime.now()
                fecha4=datetime.datetime.strftime(fecha3, '%b %d %Y %H:%M:%S')
                print ("====================================================================")
                menuTienda=int(input("\n======================= \n TIENDAS: \n======================= \n 1:REGISTRO DE TIENDAS \n 2:INICIAR SESION \n 3:REGRESAR MENU PRINCIPAL \n======================= \n INGRESE UNA OPCION: "))
           
           
            if menuTienda==2:
                #Los tenderos pueden iniciar sesión proporcionando su nombre de usuario y contraseña.
                print ("====================================================================")
                print ("                         INCIAR SESION ")
                print ("====================================================================")
                tendero=str(input("INGRESE EL NOMBRE DE SU NEGOCIO: "))
                passw=str(input("LA CONTRASENA ES SU NUMERO RUC: "))
                if tendero==nombreTienda and passw==ruc:
                    print("LOS DATOS INGRESADOS SON CORRECTOS")
                    print ("====================================================================") 
                    menuTienda=int(input("\n======================= \n TIENDAS: \n======================= \n 1:REGISTRO DE TIENDAS \n 2:INICIAR SESION \n 3:REGRESAR MENU PRINCIPAL \n======================= \n INGRESE UNA OPCION: "))
                else:
                    print("LOS DATOS INGRESADOS SON INCORRECTOS, VUELVA A INGRESAR:")
                    print ("====================================================================")
            
            if menuTienda ==3:
                print ("REGRESAR AL MENU PRNCIPAL ")
                menuPrincipal=int(input("\n=============================== \nMENU PRINCIPAL: \n=============================== \n 1:CLIENTE \n 2:TIENDA \n 3:ADMINISTRADOR \n 4:SALIR \n=============================== \n INGRESE UNA OPCION:  "))
            #En caso de que el usuario ingrese un numero incorrecto pueda volver a ingresar
            else:
                print("LA OPCION INGRESA ES INCORRECTA VUELVA A INGRESAR: ")
    
    
    if menuPrincipal ==3:
        print ("ADMINISTRADOR ")
        #El menú administrativo brinda las opciones del historial de los nuevos clientes registrados, y tambien de las nuevas tiendas registradas.
        menuAdmin=int(input("\n======================================== \n TIENDAS: \n======================================== \n 1:HISTORIAL DE CLIENTES INGRESADOS \n 2:HISTORILA DE NEGOCIOS REGISTRADOS \n 3:REGRESAR MENU PRINCIPAL \n===================================== \n INGRESE UNA OPCION: "))
        while menuAdmin!=3:
            if menuAdmin==1:
                #Historial de los nuevos clientes
                m=datosCliente(nombres, apellidos, edad, pais, usuario, contra)
                print ("====================================================================")
                print ("            HISTORIAL DE CLIENTES INGRESADOS")
                print ("====================================================================")
                print("USURIO RESGISTRADO POR EL CLIENTE: ",m.usuario)
                print("CONTRASENA CREADA POR EL USUARIO: ",m.contra)
                print("NOMBRES Y APELLIDOS DEL USUARIO: ",m.nombres+" " ,m.apellidos)
                print("EDAD DEL USUARIO: ",m.edad)
                print("NACIONALIDAD DEL USUARIO: ",m.pais) 
                print ("FECHA DE REGISTRO DEL CLIENTE: "+fecha2)
                print ("====================================================================")
                menuAdmin=int(input("\n======================================== \n TIENDAS: \n======================================== \n 1:HISTORIAL DE CLIENTES INGRESADOS \n 2:HISTORILA DE NEGOCIOS REGISTRADOS \n 3:REGRESAR MENU PRINCIPAL \n===================================== \n INGRESE UNA OPCION: "))
           
           
           
            #Historial de los nuevos negocios registrados
            if menuAdmin==2:
                g=datosTienda(nombreTienda, ruc, telefono, gerente, tipoNegocio)
                print ("====================================================================")
                print ("            HISTORIAL DE NEGOCIOS REGISTRADOS")
                print ("====================================================================")
                print("NOMBRE DEL NEGOCIO: ",g.nombreTienda)
                print("RUC DEL NEGOCIO: ",g.ruc)
                print("TELEFONO DE CONTACTO: " ,g.telefono)
                print("NOMBRE DEL GERENTE DEL NEGOCIO: ",g.gerente)
                print("TIPO DE NEGOCIO: ",g.tipoNegocio) 
                print ("FECHA DE REGISTRO DEL CLIENTE "+str(fecha3))
                print("====================================================================")
            menuAdmin=int(input("\n======================================== \n TIENDAS: \n======================================== \n 1:HISTORIAL DE CLIENTES INGRESADOS \n 2:HISTORILA DE NEGOCIOS REGISTRADOS \n 3:REGRESAR MENU PRINCIPAL \n===================================== \n INGRESE UNA OPCION: "))
            
            if menuAdmin==3:
                print ("REGRESAR AL MENU PRNCIPAL ")
                menuPrincipal=int(input("\n=============================== \nMENU PRINCIPAL: \n=============================== \n 1:CLIENTE \n 2:TIENDA \n 3:ADMINISTRADOR \n 4:SALIR \n=============================== \n INGRESE UNA OPCION:  "))
            else:
                print("LA OPCION INGRESA ES INCORRECTA VUELVA A INGRESAR: ")
    if menuPrincipal ==4:
        print ("GRACIAS POR SU VISITA VUELVA PRONTO")
        menuPrincipal=int(input("\n=============================== \nMENU PRINCIPAL: \n=============================== \n 1:CLIENTE \n 2:TIENDA \n 3:ADMINISTRADOR \n 4:SALIR \n=============================== \n INGRESE UNA OPCION:  "))

    else:
        #En caso de que el usuario ingrese un numero incorrecto pueda volver a ingresar
        print("LA OPCION INGRESA ES INCORRECTA VUELVA A INGRESAR: ")