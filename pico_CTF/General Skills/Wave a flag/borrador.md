## Challenge name: Wave a flag

## Category
General Skills

## description
https://play.picoctf.org/practice/challenge/170
Can you invoke help flags for a tool or binary? This program has extraordinarily helpful information...

## solution
primero descargamos el archivo "warm", con el siguiente comando
```
wget <link del archivo >
```
si lo intentamos ejecutar obtendremos el siguiente error
```
$ ./warm
./warm: Permission denied
```
para poder ejecutar el archivo y pedir ayuda hay que cambiar los permisos del archivo 
con el siguiente comando le damos permisos de ejecución
```
chmod +x warm
```
Ahora si podremos ejecutar
```
$ ./warm       
Hello user! Pass me a -h to learn what I can do!
```
EL mismo programa nos dice que podemos pasarle la opcion -h
```
./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
```
Tambien es posible abrir el archivo "warm" desde visual studio code y buscar la palabra "pico" para encontrar la flag


## flag
```
picoCTF{b1scu1ts_4nd_gr4vy_616f7182}
```