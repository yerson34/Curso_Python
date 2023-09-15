# 1. TIPOS DE DATOS

* *TIPOS DE DATOS PRIMITIVOS.* 

* *'a' string cadena de texto*

* *'hola' esto tambien es un string*

* *'hola soy un strig y te saludo' cadena larga*

#### OBSERVACIÓN: todo lo que este entre comillas es un string 

### un string puede estar entre comillas simples o dobles 

*  "100" Este es un tipo de dato númerico entero* 

*  "2.1" Este es un tipo de dato numerioc flotante*


*  "False" Este es un tipo de dato boleano falso* 


*  "true" Tipo de dato boleano verdadero*

## 2. variables
 
* *Es donde almacenamos nuestros tipos de datos.*

* *Esos datos pueden mutar o ccambiar o modificarse.*

* *Como creamos una variable para almacenar nuestros datos.*

* *Darle un nombre significante o realacionado al dato que estamos almacenando.*

* Indicarle a que dato esta asociado -> asignacion 

* Indicar el tipo de dato que se va a almacenar -> darle al dato a guadar.

**EJEMPLOS**

 * Primero al dato voy a pedir la edad de nadine 

     edad_nadne=18

 * El nombre de un alumno 

     nombre_alumno=edwin


## 3.Operadores 
### **Operados aritmeticos** 
* **SUMA**  (+)

* **RESTA** (-) 

* **MULTIPLICACION** (*) 

* **DIVISION** (/)

**SUMA**

**suma=45+12**

**RESTA**

**resta=34-12**

**MULIPLICACION**

**multi=3x4**

**DIVICION**

**division=2/4**

**OPERACION=(45+12+23)/4**

**OP=15+12+14+13/4**
## 4.datos estructurados

#### Listas
* Puede alamcenar distintos tipos de datos en una sola lista 
```python
     ['nombre',10,False]
     lista_amigos=['jori','edwin','adan','chinita']
```
#### Objetos
* tambien al igual que las listas almacenan distintos tipos de datos pero son un orden
* para almacenar datos en un objeto necesitamos especificar un inidce y un valor clave->valor
```python
alumno={
    'nombre':'jori'
    'edad':52',
    'sexo':'todos los dias'
```
#### Combinar ambas estructuras de datos 
 ```python
alumno={
    'nombre' : 'jori'
    'edad':30,
    'amigos':['antony','edwin','china']
'direccion': {
    'departamento':'ayacucho'
    'provincia':'lucanas'
    'distrito':'puquio'
    'jiron':'san peter'
    'numero':152 
 }
}
```
## 5. funciones

### Controles de flujos 

* solo se ejecuta si cumple o si elas condicion es verdadera podemos hacere que si condicion es false se ejecute otro codigo  
### Deciciones 

* expecifica el codigo que se ejecutara si se cumple una condicion 

```python 
if <condicion:
```
* el codigo que deseamos ejecutar si la condicxion es verdad 
```python
print ("ejecuta esto")
```
* aqui estamos fuera del if o del si este codigo siempre se ejecutara no depende.
```python
print("esto siempre ejecutara ")
```
* si queremos que se ejecute un codigo en caso sea falsa
```python 
if <condicion falsa >:
print("solo imprime si es verdad 
else :
print("solo imprime  si es falso")
```
### Ejemplo 
```python
if 15>18
print("si es verdad imprime esto ")
else:
print(" si es verdad falso imprime esto ")
```
########################################
```python
if 15*2==30
print(si es verdad imprime esto" )
else:
print(" si es falso imprime esto")
```
########################################
```python
condicion=true
if condicion:
print("si es verdad imprime esto") 
else:
print(" si es falso imprime esto")
```
### ciclos 
* Existen dos tipos 
* Cuando sabes la cantidad de veces 
* Sintaxis despues d3e la palabra reservada for deberemos crear una variable que * Almacene el numero que iremos iterando .

* Luego tendremos que interar a los elementos e iterar 
```python
VOCALES=["A","E","I","o","U"]
for i in range(i,5)
print(i)
```
* Cuando no sabemos la cantidad de veces a repetir.
