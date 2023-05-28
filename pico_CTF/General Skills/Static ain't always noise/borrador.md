## Challenge name: Static ain't always noise

## Category
Category...

## description
https://play.picoctf.org/practice/challenge/163?page=1
Can you look at the data in this binary: static? This BASH script might help!

## solution
EL reto tiene dos archivos  
un script: ltdis.sh  
un archivo static  
al abrir el archivo static con un editor exadecimal o como texto plano y buscando se puede encontrar la flag directamente sin hacer nada.
tambien podemos hacerlo ejecutando el script
```
chmod +x ltdis.sh  //para añadir permisos de ejecucion
//analizando el script podemos darnos cuenta que podemos añadir un archivo a la ejecucion , por lo que añadiremos el archivo static

./ltdis.sh static
```
al ejecutar el script se crean 2 archivos
static.ltdis.x86_64.txt y static.ltdis.srings.txt  
dentro de static.ltdis.srings.txt podremos encontrar la flag en texto plano 

## flag
```
picoCTF{d15a5m_t34s3r_f5aeda17}
```