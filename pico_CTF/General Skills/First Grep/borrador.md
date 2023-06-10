## Challenge name: First Grep

## Category
Generall skills

## description  
https://play.picoctf.org/practice/challenge/85?category=5&page=2  
Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.


## solution
el reto pide descargar un archivo "file", dentro del archivo texto sin sentido
podemos abrirlo y con el buscador,  buscar la palabra "pico" y nos encontrara la bandera
pero el reto se llama "grep" por lo deberiaoms utilizar ese comando para practicar

dentro de la terinal ejecutamos el comando "grep" y nos da una ayuda de como funcion
```
$ grep
Usage: grep [OPTION]... PATTERNS [FILE]...
Try 'grep --help' for more information.
```
nos dice que ingresar un "patron-patter" y un archivo
por pattern se refiere a un texo del cual buscara coincidentcias dentro del archivo.
lo que queros buscar es "picoCTF" ya que sabemos que la flag siempre empieza de esta forma
```
$ grep flag file
```
al ejecutar lo anterior, no retorna nada, ya que flag no esta dentro del archivo.

Ahora buscaremos el texto "pico" y nos retornara las coincidencias, en este caso la flag es una sola palabra sin espacios por lo que retorna la flag completa
```
$ grep pico file
picoCTF{grep_is_good_to_find_things_5af9d829}

```


## flag
```
picoCTF{grep_is_good_to_find_things_5af9d829}
```