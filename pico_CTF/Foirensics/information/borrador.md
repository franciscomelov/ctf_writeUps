## Challenge name: information

## Category: Forensics

## description
https://play.picoctf.org/practice/challenge/186
Files can always be changed in a secret way. Can you find the flag? cat.jpg

## solution
La flag esta en una imagen.
Probé diferentes comandos en la terminal
```
$ file cat.jpg # Comprueba que tipo de archivo es - .jpeg
$ exiftool cat.jpg # Da informacion sobre la imagen
$ strings cat.jpg # Muetra los caracteres que tiene la imagen
$ binwalk -Me cat.jpg # busca archivos ocultos en la imagen
$ intente abrir la imagen como archivo comprimido
```
El comando strings retorno estas dos lineas de interes (entre otros caracteres). probé con los dos pero no funcionó
```
rdf:resource='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'/>
# intenté con flag{cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9}
 id='W5M0MpCehiHzreSzNTczkc9d'?>
 # intenté con flag{W5M0MpCehiHzreSzNTczkc9d}
```
Despues de otros intentos y paginas que ponen filtros en la imagen regreé a los caracteres anteriores, 
intente decodificarlos en diferentes bases y en Base64 mostro lo siguiente
```

cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 
# Decodificando en Base64
picoCTF{the_m3tadata_1s_modified}

```
## flag
```
picoCTF{the_m3tadata_1s_modified}
```