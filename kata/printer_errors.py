from string import ascii_lowercase
letras = ascii_lowercase[:13]

bad = 0

def printer_error(s):
    global bad
    for i in s:
        if i not in letras:
            bad += 1
    return f"{bad}/{len(s)}"