; Definimos el dominio
(define (domain trasnport)

    ; Escribimos los requerimientos del lenguaje a usar
    (:requirements :typing)

    ; Definimos el dominio
    (:types 
        truck - vehicle
        package vehicle - thing
        city location thing - object
    )

    ; Definimos los predicados: 
    (:predicates ;todo: define predicates here
        (in-city ?p - location ?c - city) ; se lo ve como la ciudad a donde se movera el paquete
        (at ?obj - thing ?c - location) ;paquete, vehiculo en ciudad
        (in ?p - package ?t - truck) ; paquete en el vehiculo
    )

    ; Definimos las acciones:
    ;
    ; Acción: drive (Manejar el camión)
    ; Para esto se definen cuatro parámetros "truck" (vehicle), "from" (desde donde), "to" (hasta donde) y "c" (ciudad) que permiten identificar el lugar donde se encuentra el camión
    ; Como precondiciones definimos que el camión está en la ciudad (from) desde, y que la trayectoria (trajectory), está enlazada desde (from) hasta (to)
    (:action drive
        :parameters(?truck - vehicle ?from ?to - location ?c - city) ;parametros
        :precondition (and 
            (at ?truck ?from) ; paquete en el camión desde
            (in-city ?from ?c) ; la trayectoria sera desde que ciudad
            (in-city ?to ?c) ; la trayectoria sera hasta que ciudad
        )
        :effect (and 
            (not (at ?truck ?from)) ; el camion ya no esta en (from) desde
            (at ?truck ?to) ;  el camion ahora esta en (to) hasta
        )
    )

    ; Acción: load (subir el paquete al camión)
    ; Para esto se tiene 3 parámetros: t (vehicle), package (paquete), y l (ciudad o sitio)
    ; Como precondición declaramos a cada uno y se indica que tanto el camión como el paquete se encuentran en la ciudad.
    ; Como efectos se tiene que el paquete se carga al camión y se indica que el paquete ya no se encuentra en la ciudad.
    (:action load
        :parameters (?t - vehicle ?p - package ?l - location) ;parametros
        :precondition (and 
            (at ?p ?l) ; paquete ensta en el sitio (ciudad)
            (at ?t ?l) ; camion esta en el sitio (ciudad)
        )
        :effect (and 
            (not (at ?p ?l)) ;paquete ya no esta en el sitio (ciudad)
            (in ?p ?t) ;paquete carga al camion
        )
    )

    ; Acción: unload (bajar el paquete del camión)
    ; Para esto se tiene 3 parámetros: t (vehicle), p (paquete), y l (ciudad o sitio)
    ; Como precondiciones declaramos a cada uno y se indica que el camion se encuentre en la ciudad y el paquete esté cargado en el camión
    ; Como efectos se tiene que el paquete no está en el camion y el paquete no estará en la ciudad
    (:action unload
        :parameters (?t - vehicle ?p - package ?l - location) ;parametros
        :precondition (and 
            (at ?t ?l) ;el camion esta en ciudad
            (in ?p ?t) ;paquete esta en el camion
        )
        :effect (and 
            (not (in ?p ?t)) ;paquete no esta en el camion
            (at ?p ?l) ;paquete esta en la ciudad
            
        )
    )
)