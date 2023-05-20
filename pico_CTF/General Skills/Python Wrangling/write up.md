## Challenge name: NamePython Wrangling

## Category: General skills

## Description
https://play.picoctf.org/practice/challenge/166
Python scripts are invoked kind of like programs in the Terminal... Can you run this Python script using this password to get the flag?


## Solution  
EL reto pide descargar 3 archivos:  
ende.py  - un script en Python  
flag.txt.en - La flag, que está codificada y la decodificaremos con el archivo Python  
pw.txt  - La contraseña para poder correr el script

Para poder correr el script hay que instalar la labreria "cryptograpgy"
```
pip install cryptograpgy
```

Al correr el script nos da el siguiente mensaje
```
$ python ende.py
Usage: ende.py (-e/-d) [file]
```
Tenemos que escojer una opcion (-e/-d) y elejir un archivo [file]  
al leer el script  podemos ver que hay un mensaje de ayuda el cual obtendremos con la opcion -h
```
$ python ende.py -h
Usage: ende.py (-e/-d) [file]
Examples:
  To decrypt a file named 'pole.txt', do: '$ python ende.py -d pole.txt'
```
Aqui nos explica como usar el script, usamos -d para desencriptar y en [file] ponemos el archivo a desencriptar
```
$ python ende.py -d flag.txt.en
Please enter the password:192ee2db192ee2db192ee2db192ee2db
picoCTF{4p0110_1n_7h3_h0us3_192ee2db}
```
introducimos la contraseña de pw.txt y el script nos dará la flag desencriptada
## flag
```
picoCTF{4p0110_1n_7h3_h0us3_192ee2db}
```