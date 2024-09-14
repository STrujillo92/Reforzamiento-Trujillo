dicci = {}


class Contacto:
    # constructor
    def __init__(self, nom, tel, email, dni):
        self.nom = nom
        self.tel = tel
        self.email = email
        self.dni = dni

    # metodos
    def anadir_contacto(self):
        l1 = []
        l1.append(self.nom)
        l1.append(self.tel)
        l1.append(self.email)
        l1.append(self.dni)
        dicci[self.dni] = l1
        print('El contacto con dni {} ha sido añadido.'.format(self.dni))

    def mostrar_contactos(self):
        print('La agenda contiene los siguientes contactos: {}.'.format(dicci))

    def buscar_cont(self):
        if self.dni in dicci:
            print('Los datos del contacto con dni {} son: {}.'.format(self.dni, dicci[self.dni]))
        else:
            print('El contacto con dni {} no existe.'.format(self.dni))


pers1 = Contacto('Samantha', 4709177, 'abc@gmail.com', 70477228)
pers1.anadir_contacto()
pers2 = Contacto('Francesco', 4701892, 'xyz@gmail.com', 70955611)
pers2.anadir_contacto()
pers3 = Contacto('Giovanna', 4701883, 'abc@yahoo.es', 40056871)
pers3.anadir_contacto()
pers4 = Contacto('Lucy', 4701415, 'xyz@yahoo.es', 47612378)
pers4.anadir_contacto()
pers1.mostrar_contactos()
pers5 = Contacto('Henry', 4701873, 'abc@yahoo.com', 40057823)
pers1.buscar_cont()
pers2.buscar_cont()
pers3.buscar_cont()
pers4.buscar_cont()
pers5.buscar_cont()
