# Recorrido hacia adelante
def buscar_multiplo_Av(x, fin, max_actual=None):
    if x > fin:
        return max_actual
    if x % 3 == 0:
        if max_actual is None:
            max_actual = x
        else:
            max_actual = max(max_actual, x)
    return buscar_multiplo_Av(x + 1, fin, max_actual)
# Recorrido hacia atrás
def buscar_multiplo_Re(x, fin, min_actual=None):
    if x < fin:
        return min_actual
    
    if x % 3 == 0:
        # para qedarse con el menor 
        if min_actual is None:
            min_actual = x
        else:
            min_actual = min(min_actual, x)            
    return buscar_multiplo_Re(x - 1, fin, min_actual)

inicio = int(input("Ingrese número de inicio: "))
fin = int(input("Ingrese número de fin: "))

if inicio <= fin:
    resultado = buscar_multiplo_Av(inicio, fin)
    print("Resultado máximo múltiplo de 3:", resultado)
else:
    resultado = buscar_multiplo_Re(inicio, fin)
    print("Resultado mínimo múltiplo de 3:", resultado)
