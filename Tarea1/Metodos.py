# //////////////////////////////Primer función/////////////////////////////////


def string_work(s):
    if isinstance(s, int):  # Verifica que la variable de entrada no sea numero
        return(4001)
    elif s.isalpha():  # .isalpha() verifica que sean unicamente letras.
        return(s.swapcase())  # .swapcase() invierte todos los digitos.
    else:  # Si el string tiene caracteres especiales o numeros, da error.
        return(4002)

# /////////////////////////////Segunda función/////////////////////////////////


def num_to_str(num):
    numero = str(num)  # Se cambia la variable tipo int a str.
    if numero.isnumeric():  # Identifica si el valor de entrada es un número.
        nam = int(numero)   # Se cambia la variable tipo str a int.
        if nam > 99:  # Identifica si el valor se encuentra dentro del rango.
            return(4003)
        elif nam == 0:  # Identifica si el valor de entrada es 0.
            return ('cero')
        else:
            to_str = ''  # Se define la variable de salida tipo str.
            # Unidades y decenas como las posibles combinaciones.
            unidades = [' ', 'uno', 'dos', 'tres', 'cuatro', 'cinco',
                        'seis', 'siete', 'ocho', 'nueve']
            decenas = [' ', 'dieci', 'veinti', 'treinta_y_', ' cuarenta_y_',
                       'cincuenta_y_', 'sesenta_y_', 'setenta_y_',
                       'ochenta_y_', 'noventa_y_']
            # Se establece para que la longitud del valor siempre sea 2.
            numero = '0' * (2-len(str(numero))) + str(numero)
            # Se definen los números a retornar en la salida.
            unidad = int(numero[-1])
            decena = int(numero[-2])
            # Se ordenan las decenas y unidaddes sin espacios extra.
            to_str = '{}{}'.format(decenas[decena], unidades[unidad]).strip()
            # Para los casos especiales se replantean las salidas respectivas.
            to_str = to_str.replace('dieciuno', 'once')
            to_str = to_str.replace('diecidos', 'doce')
            to_str = to_str.replace('diecitres', 'trece')
            to_str = to_str.replace('diecicuatro', 'catorce')
            to_str = to_str.replace('diecicinco', 'quince')
            if to_str.endswith('dieci'):
                to_str = to_str.replace('dieci', 'diez')
            elif to_str.endswith('veinti'):
                to_str = to_str.replace('veinti', 'veinte')
            elif to_str.endswith('_y_'):  # Los terminados en (y) se cortan.
                to_str = to_str[:-3]
            return to_str  # Retorna el número en palabras.
    else:
        return(4004)


# ############################## CÓDIGOS DE ERROR ##########################
# Error 4001: Función string_work recibió un número
# Error 4002: Función string_work recibió un string con números
#     ó caracteres especiales
# Error 4003: Función num_to_str recibió un número mayor a 99
# Error 4004: Función num_to_str recibió una entrada distinta a un número
