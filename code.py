import os
import time as t

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def solicitar_id(id):
    entrada = id.upper()
    if (len(entrada) < 11 or len(entrada) > 11):
        return ""
    else:
        return entrada

def troca_letra(l: str) -> int:
    mapa = {
        'A': 6,
        'B': 3,
        'C': 0,
        'D': 9,
        'E': 1,
        'F': 2
    }
    return mapa.get(l.upper(), '5')

def troca_simbolo(s: str) -> str:
    mapa = {
        'A': '(',
        'B': '&',
        'C': '@',
        'D': '%',
        'E': '$',
        'F': '='
    }
    return mapa.get(s, '?')

def troca_numero(n: int) -> chr:
    mapa = {
        0: 'P',
        1: 'J',
        2: 'D',
        3: 'H',
        4: 'U',
        5: 'W',
        6: 'V',
        7: 'B',
        8: 'Y',
        9: 'Q'
    }
    return mapa.get(n, 'Z')


def case1(id_input):
    contra_senha = []

    for char in id_input:
        if char.isdigit():
            number = int(char)
            new_number = number * 7
            contra_senha.append(str(new_number)[-1])
        else:
            contra_senha.append(char)

    clear_terminal()
    print("Contra Senha:", ''.join(contra_senha))
    return ''.join(contra_senha)

def case2(id_input):
    contra_senha = []

    for char in id_input:
        if char.isdigit():
            new_char = troca_numero(int(char))
            contra_senha.append(str(new_char[-1]))
        else:
            contra_senha.append(char)

    clear_terminal()
    print("Contra Senha:", ''.join(contra_senha))
    return ''.join(contra_senha)

def case3(id_input):
    id_invert = id_input[::-1]
    contra_senha = []

    for char in id_invert:
        if char.isdigit():
            number = int(char)
            new_number = number * 2
            contra_senha.append(str(new_number)[-1])
        else:
            new_letter = chr(ord('Z') - (ord(char) - ord('A')))
            contra_senha.append(new_letter)

    clear_terminal()
    print("Contra Senha:", ''.join(contra_senha))
    return ''.join(contra_senha)

def case4(passwordId: str) -> str:
    final_password = []

    for char in passwordId:
        if not char.isdigit():
            new_letter = troca_simbolo(char)
            final_password.append(new_letter)
        else:
            digit = int(char)
            new_number = digit * 2 if digit <= 4 else digit * 4
            final_password.append(troca_numero(new_number % 10))

    clear_terminal()
    print("Contra senha:", ''.join(final_password))
    return ''.join(final_password)

def case5(id_input):
    password_new_id = id_input[::-1]
    contra_senha = []

    for char in password_new_id:
        if char.isdigit():
            number = int(char)
            new_number = number * 3
            contra_senha.append(str(new_number)[-1])
        else:
            new_letter = chr(ord('Z') - (ord(char) - ord('A')))
            contra_senha.append(new_letter)

    clear_terminal()
    print("Contra Senha:", ''.join(contra_senha))
    return ''.join(contra_senha)


def main (id):
        id_input = solicitar_id(id)
        if (len(id_input) < 2):
            return "error"
        else:
            selector = id_input[-1]
            id_input = id_input[:-1]
            
            try:
                int(selector)
            except:
                return "error_int"
                

            if selector == '1' or selector == '2':
                senha = case1(id_input)
            elif selector == '3' or selector == '4':
                senha = case2(id_input)
            elif selector == '5' or selector == '6':
                senha = case3(id_input)
            elif selector == '7' or selector == '8':
                senha = case4(id_input)
            elif selector == '9' or selector == '0':
                senha = case5(id_input)

            return senha