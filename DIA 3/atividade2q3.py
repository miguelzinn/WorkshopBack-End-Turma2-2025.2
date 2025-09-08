'''
# 1 
def somar(a, b):
    return a + b

resultado = somar(10, "5")
print(resultado)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
O erro ocorre pois não é possivel fazer a soma de uma variável do tipo "int"  com outra do tipo "str" 
'''
''' #2/3 '''
def somar(a,b):
    try:
        return a + b
    
    except TypeError:

        a_int = int(a)
        b_int = int(b)
        return a_int + b_int
    
resultado = somar(10,"5")
print(resultado)