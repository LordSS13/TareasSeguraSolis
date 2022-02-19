from Metodos import string_work
from Metodos import num_to_str


# ############## PRUEBAS DE FUNCION string_work #####################


def test_string_alf():
    alf = "AbCdEfGhIjKlMnOpQrStUvWxYz"  # String a invertir, alfabeto completo
    assert string_work(alf) == "aBcDeFgHiJkLmNoPqRsTuVwXyZ"  # Comparación


def test_string_num():
    n = 32  # Numero random para ingresarlo como parametro
    assert string_work(n) == 4001  # Error esperado al ingresarlo


def test_string_especial():
    esp = "Hol4_AdiOS"  # String con caracteres especiales y numeros
    assert string_work(esp) == 4002  # Error esperado al ingresarlo


# ############## PRUEBAS DE FUNCION test_num #####################


def test_num():
    num = 1
    while num < 100:
        assert num_to_str(num)
        num += 1


def test_numMYR():
    num = 100  # Número mayor a 99 para ingresar como parametro
    assert num_to_str(num) == 4003  # Error esperado al ingresarlo


def test_numSTR():
    num = "hola"  # String para ingresarlo como parametro
    assert num_to_str(num) == 4004  # Error esperado
