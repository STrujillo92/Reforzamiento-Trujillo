
def funcionADecoradora(funcionB):

    def funcionC(*args, **kwargs):
        print('Está por ejecutarse la función.')
        resultado=funcionB(*args, **kwargs)
        print('La función ha sido ejecutada correctamente.')
        return resultado
    return funcionC


@funcionADecoradora
def multiplica(*args,**kwargs):
    multi=1
    for arg in args:
        multi=multi*arg
    for value in kwargs.values():
        multi=multi*value
    print(multi)


multiplica(1,2,3,num=4,num1=5,num2=6)