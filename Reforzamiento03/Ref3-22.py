dicci6={}
num=int(input('Ingrese el número de facturas: '))
l1=[]
l2=[]
for i in range(num):
    l1.append(input('Ingrese el número de factura pendiente: '))
    l2.append(int(input('Ingrese el monto de la factura: ')))
    dicci6[l1[i]]=l2[i]
print('El diccionario de facturas pendientes es: {}.'.format(dicci6))
elec=0
while elec!=3:
    elec=int(input('Ingrese 1 si desea agregar una factura pendiente,'
               '2 si desea marcar una factura como cancelada o,'
               '3 si no tiene ninguna acción pendiente.'))
    if elec==1:
        fac=input('Ingrese el número de factura pendiente: ')
        dicci6[fac]=int(input('Ingrese el monto de la factura: '))
        print('El diccionario de facturas pendientes actualizado es: {}.'.format(dicci6))
    elif elec==2:
        fac=input('Ingrese el número de factura cancelada: ')
        del dicci6[fac]
        print('El diccionario de facturas pendientes actualizado es: {}.'.format(dicci6))
    else:
        print('El diccionario de facturas pendientes actualizado es: {}.'.format(dicci6))
        print('Gracias.')