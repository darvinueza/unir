; Definimos el dominio
(define (domain trasnport)

    ; Escribimos los requerimientos del lenguaje a usar
    (:requirements :typing)

    ; Definimos el dominio
    (:types 
        truck - vehicle
        package vehicle - thing
        city thing - object
    )

    ; Definimos los predicados: 
    ;
    ; Tendremos, camion (truck), paquete (package), ciudad (city) donde se encuentra el paquete
    ; y el camión se trasladara a cada una de estas ciudades. Para indicar donde se encuentra el paquete, se udara un identificador
    ; package-in (indica en que ciudad se encuentra el paquete) y truck-in (indica en que ciudad se encuentra el camión).
    ; Para unir las ciudades, usaremos el identificador trayectoria (trajectory). Finalmente, indicamos cuando el camión está cargado o descargado
    ; load-up y load-down respectivamente.
    (:predicates ;todo: define predicates here
        (truck ?t) ; declaramos el camion como (t)
        (city ?c)  ; declaramos la ciudad como (c)
        (package ?p) ; declaramos el paquete como (p)
        (package-in ?p ?c) ; declaramos que el paquete (p) esta en la ciudad (c)
        (truck-in ?t ?c) ; declaramos que el camion (t) esta en la ciudad (c)
        (trajectory ?x ?y) ; declaramos que la trayectoria sera la union entre dos nodos
        (load-up ?p ?c); declaramos la carga del paquete (p) en el camion (c)
        (load-down ?p ?c); declaramos la descarga del paquete (p) en el camion (c)
    )

    ; Definimos las acciones:
    ;
    ; Acción: drive (Manejar el camión)
    ; Para esto se definen tres parámetros "truck", "from", "to" que permiten identificar el lugar donde se encuentra el camión
    ; Como precondiciones definimos que el camión está en la ciudad (from) desde, y que la trayectoria (trajectory), está enlazada desde (from) hasta (to)
    (:action drive
        :parameters(?truck ?from ?to) ;parametros
        :precondition (and 
            (truck ?truck) ; camion es de tipo camion
            (city ?from) ; from (desde) es de tipo ciudad
            (city ?to)   ; to (hasta) es de tipo ciudad
            (truck-in ?truck ?from) ; el camion esta en desde
            (trajectory ?from ?to) ; la trayectoria sera desde (from) hasta (to)
        )
        :effect (and 
            (not (truck-in ?truck ?from)) ; el camion ya no esta en (from) desde
            (truck-in ?truck ?to) ; el camion ahora esta en (to) hasta
        )
    )

    ; Acción: upload (subir el paquete al camión)
    ; Para esto se tiene 3 parámetros: paquete, el camión y la ciudad
    ; Como precondición declaramos a cada uno y se indica que tanto el camión como el paquete se encuentran en la ciudad.
    ; Como efectos se tiene que el paquete se carga al camión y se indica que el paquete ya no se encuentra en la ciudad.
    (:action upload
        :parameters (?package ?truck ?city) ;parametros
        :precondition (and 
            (package ?package) ;paquete es de tipo paquete
            (city ?city) ;ciudad es de tipo ciudad
            (truck ?truck) ;camion es de tipo camion
            (truck-in ?truck ?city) ;el camion esta en ciudad
            (package-in ?package ?city) ;el paquete esta en ciudad
        )
        :effect (and 
            (load-up ?package ?truck) ;paquete carga al camion
            (not (package-in ?package ?city)) ;paquete ya no esta en la ciudad
        )
    )

    ; Acción: unload (bajar el paquete del camión)
    ; Se definen 3 parámetros: paquete, el camión y la ciudad
    ; Como precondiciones declaramos a cada uno y se indica que el paquete esté cargado en el camión y que el camión se encuentre en la ciudad
    ; Como efectos se tiene que el paquete está en la ciudad y el paquete no estará en el camión
    (:action unload
        :parameters (?package ?truck ?city) ;parametros
        :precondition (and 
            (package ?package) ;paquete es de tipo paquete
            (city ?city) ;ciudad es de tipo ciudad
            (truck ?truck) ;camion es de tipo camion
            (load-up ?package ?truck) ;paquete esta en el camion
            (truck-in ?truck ?city) ;el camion esta en ciudad
        )
        :effect (and 
            (package-in ?package ?city) ;paquete esta en la ciudad
            (load-down ?package ?truck) ;paquete se descarga del camion
            (not (load-up ?package ?truck)) ;paquete no esta en el camion
        )
    )
)