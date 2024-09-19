def funcionADecoradora(funcionB):

    def funcionC(*args,**kwargs):
        print('La cantidad de argumentos que tiene la función es')
        resultado=funcionB(*args,**kwargs)
        print('La función decoradora terminó de ejecutarse correctamente.')
        return resultado
    return funcionC


@funcionADecoradora
def elem(*args,**kwargs):
    cont=0
    for arg in args:
        cont=cont+1
    for key in kwargs:
        cont=cont+1
    print(cont)

elem(4,1,10,num1=2,num2=50,num3=64)