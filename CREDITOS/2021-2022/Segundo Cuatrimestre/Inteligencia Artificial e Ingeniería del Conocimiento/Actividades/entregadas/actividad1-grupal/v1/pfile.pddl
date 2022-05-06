; Definimos el problema
(define (problem trasnport_p1) 
; Asociamos a nuestro dominio
(:domain trasnport)
; Definimos los objetos que usaremos:
; En este caso son 3 ciudades, 1 camion y 1 paquete
(:objects 
    city1
    city3
    city4
    truck1 
    pack1 
)

; Estado Inicial:
; Asociamos los objetos con los predicados de del dominio.
; city con city1, city3 y city4
; truck con truck1
; package con pack1
(:init
    ;inicializamos las ciudades
    (city city1)
    (city city3)
    (city city4)
    ;inicializamos el camión
    (truck truck1)
    ;inicializamos el paquete
    (package pack1)
    ;inicializar donde se encuentra el camión
    (truck-in truck1 city3)
    ;inicializar donde se encuentra el paquete
    (package-in pack1 city1)
    ;conectamos los nodos con la trayectoria
    (trajectory city3 city1)
    (trajectory city1 city4)
)

; Objetivo
; Declaramos el objetivo que será que el camion descargue el paquete en la ciudad destino
(:goal (and
    (package-in pack1 city4)
    (load-down pack1 truck1)
))

)
