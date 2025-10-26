def luvut(lista):
    return(lista)
def poista_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]

lista = luvut([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print ("Alkuperäinen lista: ", lista)

print ("Parilliset luvut:", poista_parittomat(lista))

