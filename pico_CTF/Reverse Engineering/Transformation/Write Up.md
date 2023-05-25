## Challenge name: Transformation

## Category: Reverse Engineering

## description
https://play.picoctf.org/practice/challenge/104?page=1
I wonder what this really is... enc ```''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])```

## solution
La descripcion tiene unalgoritmo de codificacion o decodificacion y dentro del aerchivo "enc" una serie de caracteres (parece coreano o japones) 
use el algoritmo con los caracteres
```
flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"
result = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
print(result)
```
Pero solo obtuve un error : ValueError: chr() arg not in range(0x110000)

Analizando el algoritmo se ocupa la funcion chr(), el cual acepta un numero y retorna un caracter, y ord() que acepta un caracter y retorna un numero.
al parecer el algoritmo le da un numero a chr() fuera de su rango.

Llegue a la conclucion de que los caracteres era la flag encriptada, y se uso el algoritmo para encriptarla. por lo que habria que hacer que algoritmo haga lo contrario, por lo que cambie sus signos
```
''.join([chr((ord(flag[i]) >> 8) - ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```
siguie marcando error.
ya que el ciclo for va de 2 en dos.
tambien eliminé esta parte, solo por prueba y error: - ord(flag[i + 1])
este fue el resultado final
```
flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"

result = ''.join([chr((ord(flag[i]) >> 8) ) for i in range(0, len(flag), 1)])
print(result)
# Retorno: "pcCF1_isis3do__549b"
```
"pcCF1_isis3do__549b" parece mas una flag tiene "_" y al inicio lo que parece ser "picoCTF"
llegue a la conclucion que obtuve la bandera con caracteres faltantes
```
pcCF1_isis3do__549b
p*c*C*F*1*_*i*s*i*s*3*d*o*_*_*5*4*9*b*  
falta caracteres pero si añado los que se que lleva la flag, esta comienza a tomar forma  
los * es donde faltan caracteres  
picoCTF{1_*i*s*i*s*3*d*o*_*_*5*4*9*b}
```
Ya que se sabe que el algoritmo se uso para encriptar la flag, le pase al algoritmo la parte de la flag que conoszo y que siempre es igual y reto los primero cuatro caracteres que vienen en el archivo "enc"
```
flag = "picoCTF{"
result = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
灩捯䍔䙻
```
Hasta ahora se puede deducir, al algorimo le pase 8 caracteres y retorno 4, se ocupan 2 caracteres por caracter encriptado

por lo que de cada ceracter encriptado tendre que obtener 2 desencriptados
Teniendo los siguientes datos
flag encriptada:
灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽

parte que se pudo desencriptar, invirtiendo los operadores del algoritmos:
pcCF1_isis3do__549b

```
flag = "pi"
result = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
灩
```
"pi" retorna "灩", por lo que tengo que determinar como obter "pi" del caracter "灩"
hice el siguiente codigo
```
encoded_char = ord("灩") #primer caracter encriptado
known_letter = "p" # letra conocida que se pudo desencriptar

unknown_char = chr(encoded_char - (ord(known_letter) << 8))
#esta parte es lo inver del algoritmo original chr((ord(flag[i]) << 8) + ord(flag[i + 1]))

print(unknown_char)
# retorna i
```
hare una prueba mas con los ultimos caracteres
encoded_char = ord("扽") #primer caracter encriptado
known_letter = "b" # letra conocida que se pudo desencriptar


```
encoded_char = ord("扽") #primer caracter encriptado
known_letter = "b" # letra conocida que se pudo desencriptar

unknown_char = chr(encoded_char - (ord(known_letter) << 8))
#esta parte es lo inver del algoritmo original chr((ord(flag[i]) << 8) + ord(flag[i + 1]))

print(unknown_char)
# retorna } y se que "}" es el ultimo caracter de cualquier flag
```
Ahora solo tengo que hacer lo mismo para cada caracter de mi flag parcialmente descriptada y caracteres encriptados
por lo que hice el siguiente ciclo for

```
encoded ="灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽"
partial_flag= "pcCF1_isis3do__549b"
original_flag=""
for i in range(0, len(encoded)):
    encoded_char = ord(encoded[i])
    known_letter = partial_flag[i]

    first_char = known_letter
    second_char = chr(encoded_char - (ord(known_letter) << 8))
    original_flag += first_char + second_char

print(original_flag)

# retorna picoCTF{16_bits_inst34d_of_8_75d4898b}
```
Esto tomara cada caracter encriptado y la parte que se pudo desencriptar y retornará el cracter faltante  
灩 p -> haran "pi"  
捯 c -> harán "co"  
䍔 C -> harán "CT"  
....

## flag
```
picoCTF{16_bits_inst34d_of_8_75d4898b}
```