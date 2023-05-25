encoded_char = ord("扽") #primer caracter encriptado
known_letter = "b" # letra conocida que se pudo desencriptar

unknown_char = chr(encoded_char - (ord(known_letter) << 8))
#esta parte es lo inver del algoritmo original chr((ord(flag[i]) << 8) + ord(flag[i + 1]))

print(unknown_char)
# retorna }