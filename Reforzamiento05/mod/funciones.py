
def verificar(x):
    res=False
    if len(x)>=7:
        if len(x)<=12:
            if x.isalnum()==True:
                res=True
            else:
                print('El nombre del usuario puede contener solo letras y números.')
        else:
            print('El nombre de usuario no puede contener más de 12 caracteres.')
    else:
        print('El nombre de usuario debe contener al menos 7 caracteres.')
    return res

