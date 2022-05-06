
(define (problem logistic-ex) 

(:domain logistics)

(:objects 
    apn1 - airplane
    tru1 - truck
    obj1 - package
    aptC aptE - airport
    posA posB posD - location
    cit1 cit2 - city
)

(:init
    (at apn1 aptE)
    (at tru1 posD)
    (in-city aptC cit1)
    (in-city aptE cit2)
    (in-city posA cit1)
    (in-city posB cit1)
    (in-city posD cit1)
)

; Objetivo
; Declaramos el objetivo que será que el camion descargue el paquete en la ciudad destino
(:goal (and
    (at obj1 aptE)
))

)
