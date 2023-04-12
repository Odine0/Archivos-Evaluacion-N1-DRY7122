acl_number = input('Introduzca el número de ALC IPv4: ')
acl_number = int(acl_number)
if acl_number >= 1 and acl_number <=99:
    print("El número de la ACL",acl_number, "corresponde a una estándar")
elif acl_number >= 100 and acl_number <=199:
    print('El número de la ACL', acl_number,'corresponde a una extendida')
else:
    print('El número de la ACL', acl_number,'no corresponde a una estándar, ni una extendida.')
