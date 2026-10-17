# Este programa tiene como objetivo lavar la ropa de la semana.

print ("Bienvenido, este programa te guiará para lavar la ropa")
print ("¿Tienes ropa por lavar?")
ropa_sucia = input("para que sea valida la respuesta solo escribe 's' para si o 'n' para no:")

if ropa_sucia == "s":
    print("""Toma la ropa del cesto
    hecho la ropa a la lavadora
    enciendo la lavadora
    saco la ropa de la lavadora""")
    ropa ="sucia"
    while ropa == "sucia":
        ropa_limpia= input("la ropa esta limpia? s o n")
        if ropa_limpia == "s":
            print("tender la ropa")
            print("esperar que seque")
            ropa_mojada = "mojada"
            ropa_seca = input("la ropa está seca? s o n")
            if ropa_seca == "s":
                    print("doblar la ropa")
                    print("organizar todo para salir")
                    ropa="limpia"
            else:
                 print("esperar a que seque")
                    
        else:
            print("tomar esa ropa que no quedo limpia")
            print("volver a lavar")
    print("salir al trabajo")
    print("fin")
else:
    print("felicidades, tienes la ropa limpia")
    print("fin")