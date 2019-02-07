from string import ascii_lowercase, ascii_uppercase

def find_missing_letter(chars):
    # Checa se a string é curta demais:
    if len(chars) <= 2:
        return print("String too short. Please try again.")
    else:  
        # Checa se a entrada está em minúsculas ou maiúsculas:
        if chars[0].islower():
            letters = ascii_lowercase
        
            # Converte tudo pra caixa baixax:
            chars = chars.lower()
        elif chars[0].isupper():
            letters = ascii_uppercase
        
            # Converte tudo pra caixa alta:
            chars = chars.upper()

    



    print(chars)
find_missing_letter("abc")