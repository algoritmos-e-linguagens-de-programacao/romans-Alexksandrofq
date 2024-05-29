def int_to_roman(num):
    # Implemente sua função aqui
   
    if not 1 <= num <= 3999:
        return
    valores = (1000, 'M'), (500, 'D'), (100, 'C'), (50, 'L'), (10, 'X'), (5, 'V'), (1, 'I')
    resultado = ''

    for valor, romano in valores:
        while num >= valor:
            resultado += romano 
            num -=valor

print (int_to_roman(num))


def roman_to_int(s):
    # Implemente sua função aqui
    pass
