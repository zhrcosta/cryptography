def str_normalize(string):
    '''
    Essa função remove de uma string qualquer caractere especial
    deixando apenas o alfabeto normal em minusculo
    '''


        # Para colocar cada caractére em letras minusculas
    string = string.lower()

        # Lista com o posicionamento dos caracteres com acento
    chr_ac = list(range(224, 228))

        # Subistitui todos os caracteres com acento por seu respectivos
    for i in chr_ac:
        string = string.replace(chr(i), "a").replace(chr(i + 8), "e").replace(chr(i + 12), "i").replace(chr(i + 18), "o").replace(
            chr(i + 25), "u")
    for i in string:
        string = string.replace("ç","c").replace("Ç","c")

        # Lista com o posicionamento dos caracteres especiais
    chr_esp = list(range(0,32))+list(range(33,65))+list(range(91,97))+list(range(123,224))

        # Remove todos os caracteres especiais
    for i in chr_esp:
        string = string.replace(chr(i),"")

        # rotorna os caracteres basicos
    return string

def polibio_alphabet(string):

        # Dicionário que será usado na substituição, de acordo com a tabela do código de polibio
    d ={"a":11,"b":12,"c":13,"d":14,"e":15,
        "f":21,"g":22,"h":23,"i":24,"j":25,
        "k":31,"l":32,"m":33,"n":34,"o":35,
        "p":41,"q":42,"r":43,"s":44,"t":45,
        "u":51,"v":52,"w":52,"x":53,"y":54,
        "z":55}

        # Cada caractere é substituido pelo respectivo numero do código de polibio
    for i in string:
        string = string.replace(i,str(d[i]))

        # Retorna a string criptografada
    return string


def normal_lphabet(lts):
    final_str = ''

    # Dicionário que será usado na substituição, de acordo com a tabela do código de polibio


    d = {'11': 'a', '12': 'b', '13': 'c', '14': 'd', '15': 'e',
         '21': 'f', '22': 'g', '23': 'h', '24': 'i', '25': 'j',
         '31': 'k', '32': 'l', '33': 'm', '34': 'n', '35': 'o',
         '41': 'p', '42': 'q', '43': 'r', '44': 's', '45': 't',
         '51': 'u', '52': 'v', '53': 'x', '54': 'y', '55': 'z'
         }

    # Cada caractere é substituido pelo respectivo numero do código de polibio
    for i in range(len(lts)):
        lts[i] = d[lts[i]]

        # Retorna a string criptografada

    for it in lts:
        final_str = final_str + it

    return final_str


def polibio_encrypt(string):
    string = str_normalize(string).split()
    final_str = ''
    for i in string:
        #print(polibio_alphabet(i), end=" ")
        final_str = final_str + polibio_alphabet(i) + str(" ")

    return final_str


def str_split(string,nm):
    string = [string[i:i+nm] for i in range(0,len(string),nm)]
    return string


def split_encrypted(string):
    lt = string.split(" ")
    if '' in lt:
        lt.remove('')
        # retorna uma lista de string
    return lt

def polibio_decrypt(string):
    spl_sentense = split_encrypted(string)
    final_sentense = ''

    for it in spl_sentense:
        str_spl = str_split(it,2)
        str_spl = normal_lphabet(str_spl)
        final_sentense = final_sentense + str_spl + " "


    return final_sentense








