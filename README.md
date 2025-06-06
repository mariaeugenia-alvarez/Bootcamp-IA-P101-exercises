# Bootcamp-IA-P101-exercises
pip install -r requirements.txt


Ejercicio 1: ¿Par o impar? (if_even)
Define una función que reciba un número entero como argumento y
devuelva un valor booleano: True si el número es par y False si es
impar.


Ejercicio 2: Años humanos a años de perro (human_dog_age)
Define una función que reciba como argumento la edad de una persona
expresada en años humanos (como número real o entero). La función
debe devolver el equivalente en años de perro según el siguiente criterio:
Los primeros dos años humanos cuentan como 10.5 años de perro
cada uno.
Cada año humano adicional cuenta como 4 años de perro.
Si la edad humana es negativa, la función debe devolver un mensaje de
error apropiado.

Ejercicio 3: Vocal o consonante (vowel_or_consonant)
Define una función que reciba como argumento una única letra del
alfabeto (en minúscula) y devuelva una cadena de texto indicando si es:
Una vocal (a, e, i, o, u),
La letra “y” (que a veces se considera vocal y a veces consonante),
O una consonante.

Ejercicio 4: Nombra esa figura (figure)
Define una función que reciba como argumento un número entero
correspondiente al número de lados de una figura geométrica (entre 3 y
10, ambos inclusive). La función debe devolver el nombre
correspondiente a la figura. Si el número está fuera de ese rango, debe
devolver un mensaje de error apropiado.

Ejercicio 7: Acceso según perfil y hora (access)
Define una función que reciba dos argumentos:
una cadena de texto indicando el perfil de la persona ( "admin" ,
"usuario" o "invitado" ),
y un número entero representando la hora del día (en formato 24h, de
0 a 23).
La función debe devolver un valor booleano: True si se permite el
acceso, False en caso contrario, según las siguientes reglas:
Si el perfil es "admin" , siempre tiene acceso.
Si el perfil es "usuario" :
Tiene acceso solo si la hora está entre 8 y 20, ambos inclusive.
Si el perfil es "invitado" :
Tiene acceso solo si la hora está entre 10 y 16, ambos inclusive.
