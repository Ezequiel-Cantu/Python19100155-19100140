from pickle import NONE

class Usuario:
    Usuario = None
    Contrasenna = None
    Rol = None
    Nombre = None
    CURP = None
    Ciudad = None

usuarioslista = []
admin = Usuario()
admin.Usuario = "admin"
admin.Contrasenna = "admin"
admin.Rol = "Administrador"
admin.Nombre = "EL ADMIN"
admin.CURP = "XXXXX0111011XXX"
admin.Ciudad = "Nuevo Laredo"
usuarioslista.append(admin)
eleccion = ""
eleccion = input("1.- Registro   2.- Inicio de sesión   3.- Salida   ")
while (eleccion != "3"):
    if (eleccion == "1"):
        usu = input("Inserte usuario: ")
        contra = input("Inserte contraseña: ")
        rol = "Cliente"
        nom = input("Inserte su nombre: ")
        curp = input("Inserte su CURP: ")
        ciud = input("Inserte su ciudad: ")
        nuevousu = Usuario()
        nuevousu.Usuario = usu
        nuevousu.Contrasenna = contra
        nuevousu.Rol = rol
        nuevousu.Nombre = nom
        nuevousu.CURP = curp
        nuevousu.Ciudad = ciud
        prueba = False
        for usuarioli in usuarioslista:
            usuario = usuarioli
            if (nuevousu.CURP == usuario.CURP):
                print("El usuario ya existe")
                prueba = False
                break
            prueba = True
        if (prueba):
            usuarioslista.append(nuevousu)
            print("Se agrego con exito el usuario")
    elif (eleccion == "2"):
        usu = input("Inserte usuario: ")
        contra = input("Inserte contraseña: ")
        prueba = False
        for usuarioli in usuarioslista:
            usuario = usuarioli
            if (usu == usuario.Usuario and contra==usuario.Contrasenna and usuario.Rol == "Administrador"):
                prueba = True
                print("Usuario: " + usuario.Usuario)
                print("Contraseña: " + usuario.Contrasenna)
                print("Rol: " + usuario.Rol)
                print("Nombre: " + usuario.Nombre)
                print("CURP: " + usuario.CURP)
                print("Ciudad: " + usuario.Ciudad)
                print()
                print()
                print("-----------------------------------------")
            elif(usu == usuario.Usuario and contra==usuario.Contrasenna):
                prueba = False
                
                print("Usuario: " + usuario.Usuario)
                print("Contraseña: " + usuario.Contrasenna)
                print("Rol: " + usuario.Rol)
                print("Nombre: " + usuario.Nombre)
                print("CURP: " + usuario.CURP)
                print("Ciudad: " + usuario.Ciudad)
        if(prueba):
            for usuariocli in usuarioslista:
                usuarios = usuariocli
                print("Usuario: " + usuarios.Usuario)
                print("Contraseña: " + usuarios.Contrasenna)
                print("Rol: " + usuarios.Rol)
                print("Nombre: " + usuarios.Nombre)
                print("CURP: " + usuarios.CURP)
                print("Ciudad: " + usuarios.Ciudad)
    else:
        print("Respuesta no valida")
    eleccion = input("1.- Registro   2.- Inicio de sesión   3.- Salida    ")
