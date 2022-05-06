; Definimos el problema
(define (problem trasnport_p1) 
; Asociamos a nuestro dominio
(:domain trasnport)
; Definimos los objetos que usaremos:
; En este caso son 3 ciudades, 1 camion y 1 paquete
(:objects 
    city1 city2 city3 city4 - city
    pos1 pos2 pos3 pos4 - location
    truck1 - truck
    pack1 - package
)

; Estado Inicial:
; Asociamos los objetos con los predicados de del dominio.
; city con city1, city3 y city4
; truck con truck1
; package con pack1
(:init
    ;inicializar donde se encuentra el camión
    (at truck1 pos3)
    ;inicializar donde se encuentra el paquete
    (at pack1 pos1)
    ;conectamos los nodos con la trayectoria
    (in-city pos1 city1)
    (in-city pos2 city1)
    (in-city pos3 city1)
    (in-city pos4 city1)
)

; Objetivo
; Declaramos el objetivo que será que el camion descargue el paquete en la ciudad destino
(:goal (and
    (at pack1 pos4)
))

)