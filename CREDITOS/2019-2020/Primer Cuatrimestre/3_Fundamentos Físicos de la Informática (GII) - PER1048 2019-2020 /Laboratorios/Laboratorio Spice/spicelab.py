# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# 
#  # Objetivo del laboratorio
#  El objetivo de la presenta práctica es conocer el estándar de simulación de circuitos [SPICE](http://bwrcs.eecs.berkeley.edu/Classes/IcBook/SPICE) y realizar pequeñas simulaciones en corriente continua con el mismo. SPICE es una forma elegante y sencilla de codificar circuitos eléctricos de manera que puedan ser procesados por un ordenador. Mediante un sencillo lenguaje podemos definir resistencias, fuentes de alimentación, etc., las conexiones entre ellos y los resultados que deseamos obtener.
# 
#  # El estándar SPICE
#  **SPICE** es una abreviabiación de *Simulation Program with Integrated Circtuit Emphasis*.
#  Se trata básicamente de un método estándar para describir circuitos usando texto plano en
#  lugar de una representación gráfica (o *esquemática*). A esta descripción en texto se
#  la llama también **netlist** y básicamente se corresponde con la *lista* de los componentes del circuito y cómo estos están conectados entre sí, es decir, de los nodos de unión.
#  Los ficheros netlist pueden tener extensiones `.cir`, `.net`, `.ckt`, ó `.sp` y es muy común encontrárselos con cualquiera de estas.
# 
#  Existen en el mercado muchas variantes (intérpretes) de Spice, aunque el original fue descrito
#  en la Universidad de Berkeley. En la lista de intérpretes de Spice tenemos desde esfuerzos y proyectos comerciales hasta *open source* y regidos por distintas comunidades de usuarios y programadores.
# 
# 
# > **Pregunta:** Enumera todos los intérprete de Spice que puedas encontrar. Crea una tabla en Markdown con varias columnas (para el nombre, fabricante, versión actual, licencia y alguna característica sobresaliente). Aquí tienes un ejemplo del que puedes partir y seguir completando:
# 
# **Respuesta:**
#
# | Intérprete          | Licencia   | Fabricante                   | Características                        |
# | :------------------ | :--------- | :--------------------------- | :------------------------------------- |
# | Ahkab               | GPL        | Giuseppe Venturini           | Basado en Python                       |
# | LTspice             | GPL        | Analog Devices               | App de Escritorio                      |
# | Circuit Simulator   | GPL        | Paul Falst                   | Java Script/Applets Java               |
# | QUCS                | GPL        | Stefan Jahn                  | GUI/GNU                                |
# | Xcos                | GPL        | Scilab Enterprises S.A.S     | C, C++, Java, XML, Scilab, Makefiles   |
# | Ktechlab            | GPL        | KTechLab Developers          | C++                                    |
# | Pspice              | PAGA       | Cadence                      | PSpice Designer y PSpice Designer Plus |
# 
# > **Pregunta:** ¿Qué comparación puedes efectuar entre C y Spice como estándares (lenguajes) y sus respectivas implementaciones en software? ¿Qué implementaciones reales (compiladores) del lenguaje C conoces? 
# 
# **Respuesta:**
#
# *¿Qué comparación puedes efectuar entre C y Spice como estándares (lenguajes) y sus respectivas implementaciones en software?* 
# * C es un lenguaje de programación estructurado y SPICE3, fue desarrollada en lenguaje C por Thomas Quarless.
# * Tanto C como SPICE operan en multiplataforma [Sistema Operativo: Multiplataforma].
# * Tanto C como SPICE son dos cosas muy distintas, tienen objetivos distintos: C es un lenguaje de programación con el cual puedes hacer desde módulos para Kernel como Linux hasta cryptocurrency en cambio SPICE es un estándar internacional cuyo objetivo es simular circuitos electrónicos analógicos compuestos por resistencias, condensadores, diodos, transistores, etc. 
# 
# *¿Qué implementaciones reales (compiladores) del lenguaje C conoces?*
# 
# * Kernel: Linux, Minix, Hurd, FreeBSD, OpenBSD, y Darwing.
# * Kernel de Mac OS X.
# * PostgreSQL
# * Versionado: Git, Subversion
# * Servidores Web: Apache, Nginx
# * Editores: Emacs, VIM, Geany
# * Matemáticas: R, MATLAB, Octave
# * Lenguajes de Programación: C, C++, Python, Perl, Ruby
#
#  ## Elementos de un netlist
#  Como acabamos de comentar, un netlist se corresponde con la codificación de los elementos electrónicos de un circuito y las uniones entre los mismos. Veamos con más concreción qué partes y secciones lo componen.
# 
#  ## Comentarios
# 
#  La primera línea de un netlist se corresponderá siempre con un comentario. A partir de esta línea se pueden introducir más comentarios pero tienen que ir siempre precedidos de un `*`. Ejemplo:
#  
#  ```spice
#  Mi primer circuito
#  * Otro comentario
#  * más comentarios
#  *
#  ```
# 
#  ## Dispositivos básicos de un circuito
#  Los elementos de un netlist son los mismos que encontramos en cualquier circuito eléctrico sencillo,
#  tales como resistencias, **condensadores**, **bobinas**, **interruptores**, **hilos** y **fuentes** de alimentación.
#  Para distinguir uno de otro, se reserva una letra característica: `V` para fuentes de alimentación, `R` para resistencias, `C` para condensadores y `L` para bobinas. También es posible usar estas letras en su versión en minúscula (`r`, `v`, `c`, `l`, etc.).
#  Después de esta letra característica se puede sufijar cualquier texto para diferenciar un elemento de otro (números, letras, palabras, etc.). Ejemplo:
# 
#  ```
#  * Una resistencia
#  R1
#  *  Otra resistencia
#  R2
#  * Fuente de alimentación
#  V
#  * Un condensador
#  C
#  ```
# 
#  ## Conexiones
#  A continuación de indicar el elemento eléctrico, tenemos que informar a Spice cuáles
#  son los puntos de unión tanto a un lado como al otro del elemento.
#  Así es como Spice sabe qué está conectado a qué: porque comparten un **punto**
#  (o **nodo**, aunque este término se reserva sobretodo a uniones de más de dos elementos)
#  que hemos señalizado correctamente. Para nombrar nodos, lo mejor es emplear una
#  numeración secuencial: 0...n. **La enumeración de los puntos de unión es completamente
#  a nuestro criterio**.
# 
#  ```
#  * Una resistencia
#  * entre cables 0 y 1
#  R1 0 1
#  ```
# 
#  **Sólo es necesario seguir un criterio**: en el caso de una
#  fuente de alimentación, el nodo que pondremos primero será
#  aquel que está más cerca del *borne* positivo. Ejemplo:
# 
#  ```spice
#  * Para una fuente indicamos primeramente conexión a nodo positivo.
#  v 2 3 type=vdc vdc=1
#  ```
#  
# En el *caso de LTspice* no es necesario indicar los parámetros `type=vdc` y `vdc=X`, sino que si no se especifica nada, se supone que el último valor es el del voltaje a corriente continua:
# 
# ```spice
# * Especificación de una fuente de alimentación de 10 V en corriente continua en el caso de LTspice
# v 0 1 10
# ```
# 
# Aquí tienes un ejemplo gráfico de los componentes comentados justo arriba (resistencia y voltaje):
#
# ![](https://raw.githubusercontent.com/pammacdotnet/spicelab/master/resistencia%20y%20pila%20con%20nodos.svg?sanitize=true)
# 
#  ## Unidades en SPICE
# 
#  Las unidades de las magnitudes características del circuito son siempre [unidades
#  del Sistema Internacional](https://en.wikipedia.org/wiki/SI_electromagnetism_units) y no es necesario indicarlo explícitamente en el netlist.
# 
#  La forma de especificar múltiplos de estas cantidades es añadiendo una letra.
#  Básicamente las que nos interesan y las que suelen aparecer mayoritariamente son `k` para "kilo-," `m` para "mili?" y `u` para "micro?".
# 
#  > **Pregunta:**  Crea una tabla en Markdown con todos los prefijos de múltiplos que puedas, su abreviatura y su equivalencia numérica.
#
# **Respuesta:**
#
# | Factor       | Prefijo       | Simbolo      | Factor        | Prefijo       | Simbolo      |  
# | :----------: | :----------:  | :----------: | :-----------: | :----------:  | :----------: |
# | $$10^1$$     | $$deca$$      | $$da$$       | $$10^{-1}$$   | $$deci$$      | $$d$$        |
# | $$10^2$$     | $$hecto$$     | $$h$$        | $$10^{-2}$$   | $$centi$$     | $$c$$        |
# | $$10^3$$     | $$kilo$$      | $$k$$        | $$10^{-3}$$   | $$mili$$      | $$m$$        |
# | $$10^6$$     | $$mega$$      | $$M$$        | $$10^{-6}$$   | $$micro$$     | $$µ$$        |
# | $$10^9$$     | $$giga$$      | $$G$$        | $$10^{-9}$$   | $$nano$$      | $$n$$        |
# | $$10^12$$    | $$tera$$      | $$T$$        | $$10^{-12}$$  | $$pico$$      | $$p$$        |
# | $$10^15$$    | $$peta$$      | $$P$$        | $$10^{-15}$$  | $$femto$$     | $$f$$        |
# | $$10^18$$    | $$exa$$       | $$E$$        | $$10^{-18}$$  | $$atto$$      | $$a$$        |
# | $$10^21$$    | $$zeta$$      | $$Z$$        | $$10^{-21}$$  | $$zepto$$     | $$z$$        |
# | $$10^24$$    | $$yotta$$     | $$Y$$        | $$10^{-24}$$  | $$yocto$$     | $$y$$        |
#
#  En el caso de las fuentes de alimentación hemos de especificar si se trata de corriente contínua (`vdc`) o alterna (`ac`).
# 
#  ```
#  * Una resistencia de 5 Ohmios
#  R2 1 0 5
#  * Una pila de 10 Voltios (continua)
#  V1 1 0 type=vdc vdc=10
#  * Una resistencia de 5 kΩ
#  RX 2 4 5k
#  ```
# 
#  > **Pregunta**: ¿Qué unidades del Sistema Internacional relacionadas con la asignatura –y los circuitos en general– conoces? Responde aquí mismo en una celda de Markdown con una tabla.
#
# **Respuesta:**
#
# | Magnitud                                | Unidad                         | Simbolo       |
# | --------------------------------------- | -----------------------------  | ------------- |
# | Metro                                   | Longitud                       | $$m$$         |
# | Kilogramo                               | Masa                           | $$kg$$        |
# | Segundo                                 | Tiempo                         | $$s$$         |
# | Amperio                                 | Corriente Electrica            | $$A$$         |
# | Kelvin                                  | Temperatura                    | $$K$$         |
# | Fuerza                                  | Newton                         | $$N$$         |
# | Energía, trabajo, calor                 | Julio                          | $$J$$         |
# | Potencia                                | Vatio                          | $$W$$         |
# | Carga eléctrica                         | Columbio                       | $$C$$         |
# | Potencial eléctrico, voltaje inducido   | Voltio                         | $$V$$         |
# | Resistencia eléctrica                   | Ohmio                          | $$Ω$$         |
# | Capacitancia eléctrica                  | Faradio                        | $$F$$         |
# | Área                                    | Metro cuadrado                 | $$m^2$$       |
# | Volumen                                 | Metro cúbico                   | $$m^3$$       |
# | Velocidad, rapidez                      | Metro por segundo              | $$m/s$$       |
# | Velocidad angular                       | Radián por segundo             | $$rad/s$$     |
# | Aceleración                             | Metro por segundo al cuadrado  | $$m/s^2$$     |
# | Momento de fuerza                       | Newton metro                   | $$N.m$$       |
# 
#  ## Valores iniciales
# 
#  Aparecen justo al final de la definición del componente (`ic`). Suelen aplicarse principalmente con condensadores.
# 
#  ```
#  * Una condensador inicialmente no cargado
#  c 1 0 1u ic=0
#  ```
# 
#  ## Fin del circuito
#  El fin de la descripción de un netlist se especifica mediante el
#  comando `.end`.
# 
#  ```spice
#  * Mi primer circuito
#  V 1 0 vdc=10 type=vdc
#  R 1 0 5
#  * Fin del circuito
#  .end
#  ```
# 
#  ## Comandos SPICE para circuitos en corriente continua
# 
#  Además de la descripción del circuito, hemos de indicar al intérprete de Spice qué
#  tipo de análisis queremos realizar en sobre el mismo y cómo queremos presentar
#  la salida de la simulación. Los comandos en Spice empiezan por un `.` y suelen
#  escribirse justo al final del circuito, pero antes del comando `.end`.
# 
#  ```
#   Mi primer circuito
#  * Aquí van los componentes
#  R 1 0 6k
#  ...
#  * Comandos
#  .op
#  ...
#  * Fin del circuito
#  .end
#  ```
# 
#  > **Pregunta**: Hasta lo que has visto del lenguaje Spice, ¿dentro de qué tipo o conjunto de lenguajes encajaría? 
#  * ¿Funcionales?
#  * ¿Específicos de dominio?
#  * ¿Procedurales?
#  * ¿Estructurados?
#  * ¿Orientado a Objetos? 
#  Justifica tu respuesta. 
# 
# **Respuesta:**
# *Específicos de dominio*, ya que tiene como objetivo resolver un problema en particular, y este es el de simular circuitos electrónicos analógicos compuestos por resistencias, condensadores, diodos, transistores, etc.
# 
#  Veamos los principales comandos de simulación:
# 
#  - `.op` es el comando más sencillo que podemos emplear. Devuelve el voltaje e intensidad en cada ramal y componente del circuito. Este comando no necesita parámetros.
#  - `.dc` es uy parecido al comando `.op` pero nos permite cambiar el valor del voltaje de una fuente de alimentación en pasos consecutivos entre el valor A y el valor B.
#  En el caso de que la fuente tuviera asignada ya un valor para su voltaje, este sería ignorado. Ejemplo:
# 
# 
#  ```spice
#  * Variamos el valor del voltaje
#  * de la fuente "v" de 1 a 1000
#  * en pasos de 5 voltios
#  v 1 0 type=vdc vdc=10
#  .dc v 1 start=1 stop=1000 step=20
#  v2a 2 4 type=vdc vdc=9
#  * Igual para v2a. Se ignora su voltaje de 9V
#  .dc v2a start=0 stop=10 step=2
#  ```
# 
#  - El comando `.tran` realiza un análisis en el tiempo de los parámetros del
#  circuito. Si no se emplea la directiva `uic` (*use initial conditions*) o esta es igual a cero, este análisis se realiza desde el punto estable de funcionamiento del circuito hasta un tiempo `tfinal`.
#  y en intervalos `tstep`. Si empleamos un varlor distinto para parámetro `uic`,
#  entonces se hará uso de las condiciones iniciales definidas para cada componente
#   (típicamente `ic=X` en el caso de los condensadores, que da cuenta de la carga incial que estos pudieran tener).
# 
# 
#  ```
#  * Hacemos avanzar el tiempo entre
#  * tinicial y tfinal en pasos tstep
#  .tran tstart=X tstop=Y tstep=Z uic=0/1/2/3
#  ```
# 
#  `X`, `Y` y `Z` tienen, evidentemente unidades de tiempo en el S.I. (segundos).
# 
#  > **Pregunta**: El parámetro `uic` puede tener varios valores y cada uno significa una cosa. Detállalo usando un celda Markdown y consultando la [documentación de Ahkab](https://buildmedia.readthedocs.org/media/pdf/ahkab/latest/ahkab.pdf).
# 
# | UIC   | Descripción                                                                                                                                                                                                   |
# | :---: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
# | 0     | Todos los voltajes del nodo y corrientes a través de las fuentes *v/h/e* son cero en *t=tstart*.                                                                                                              | 
# | 1     | El estado en  *'t=tstart*  es el último resultado de un análisis **OP**.                                                                                                                                      |
# | 2     | El estado en *t=tstart* es el último resultado de un análisis **OP** en el que se establecen los valores de las corrientes a través de inductores y voltajes en los condensadores especificados en su **ic**. |
# | 3     | Cargue un **ic** suministrado por el usuario. Esto requiere una directiva de **.ic** en alguna parte de la lista de red y el nombre del **ic** y **ic_label** deben coincidir.                                       | 
#
#  ## Intérprete SPICE que vamos a usar: Ahkab
#  Tras un estándar siempre hay una o varias implementaciones. Ahkab no deja de ser una implmentación más en Python del estándar Spice.
#  > **Pregunta:** Comenta las distintas implementaciones de lenguajes y estándares que conozcas. Hazlo usando una tabla en Markdown. [Aquí](https://www.markdownguide.org/extended-syntax/#tables) tienes un poco de ayuda (aunque antes ya se ha puesto el ejemplo de una tabla).
#  
#  > | Nombre  | URL                                              | Autor           | Licencia |
#  > |---------|--------------------------------------------------|-----------------|----------|
#  > | PySpice | https://github.com/FabriceSalvaire/PySpice       | Fabrice Salvaire| GNU      |
#  > | spiceypy| https://github.com/AndrewAnnex/SpiceyPy          | Andrew Annex    | MIT      |
# 
# * *spiceypy*: SpiceyPy es una envoltura de python de SPICE Toolkit. SPICE es una herramienta esencial para científicos e ingenieros por igual en el campo de la ciencia planetaria para la Geometría del Sistema Solar. Visite el sitio web de NAIF para obtener más detalles sobre SPICE.
# **IMPORTANTE:** No cuenta con una afiliació con la NASA, NAIF o JPL. El código se proporciona "tal cual", úselo bajo su propio riesgo. Sin embargo, el NAIF ahora distribuye "lecciones" de Python que usan SpiceyPy como la interfaz de Python para condimentar.
#
# * *PySpice*: PySpice es un módulo de Python que conecta Python con los simuladores de circuito Ngspice y Xyce, permite la simulación de circuitos analógicos y digitales, como la comprobación de su funcionamiento y posterior análisis y estudio.
#
# > **Pregunta:** Describe brevemente este software (creador, objetivos, versiones, licencia, características principales, dependencias, etc.).
#
# **Respuesta:**
#
# ## Introducción y Objetivo
# Ahkab es un simulador de circuitos electrónicos del tipo SPICE escrito en Python 2 y 3, el mismo es una suerte de extensión, de librería para Python. Como bien menciona el creador, ahkab surgió como un experimento o una prueba de concepto, citándolo “No tenemos expectativas de que nuestra herramienta de simulación de circuito pequeño, a veces defectuosa y de prueba de concepto, reemplace a los simuladores de circuito convencionales: son convencionales por buenas razones y merecen mucho los elogios y el dinero que pagamos. Sería tonto pensar lo contrario”, lo cual es un resumen muy claro de su punto de vista. Ahora bien, Ahkab viene a desmitificar la complejidad del análisis y simulaciones de circuitos, es una simplificación, en algún punto, que permite verificar que sucede al ejecutar las simulaciones, diseñar circuitos mas fácilmente, mas generalmente ya que esta escrito en un lenguaje mundialmente utilizado, permitiéndonos como dice el auto “ver bajo el capot” de formas tales que nos permite, por ejemplo, obtener las matrices de ecuaciones utilizadas, modificar los algoritmos que se utilizan para las simulaciones, corregirlos, modificarlos, adaptarlos, etc. Por otro lado, pone en manifiesto esos extensos documentos científicos que muchas veces carecen de implementaciones practicas por ende son una suerte de abstracción lejana de la práctica.
# ## Creador
# Ahkab (actualmente en la versión 0.18 2015) fue creado por Giuseppe Venturini[^9] un entusiasta de la electrónica y programación, Ingeniero y Licenciado y actualmente desarrollando su doctorado. A su vez, su creación tuvo contribuidores tales como Ian Daniher [^10], Rob Crowther[^11].
#
# [^9]: http://ggventurini.io/
# [^10]: https://github.com/itdaniher
# [^11]: https://github.com/weilawei
#
# ## Licencia
# GNU General Public License[^12]
#
# [^12]: https://ahkab.readthedocs.io/en/latest/misc/COPYING.html
#
# ## Versiones Disponibles
#
# Estas son las versiones “oficiales” que hay disponibles en github, los reléase notes[^13] están disponibles en la página del autor 
# *	0.18
# *	0.17
# *	0.16
# *	0.15
# *	0.14
# *	0.13
# *	0.12
# *	0.11
# *	0.10
#
# [^13]: https://github.com/ahkab/ahkab/tags
#
# ## Algunas Simulaciones Disponibles
# *	Numérica (.op - Punto de operación)
# *	Análisis transitorio (.tran)
# *	Análisis AC – Corriente Alterna
# *	Análisis PZ – Polo Cero
# *	Análisis periódico de estado estacionario
# 
# ## Dependencias
# * Algunas de sus dependencias son:
# * Dependencias Core
# * Python 2: Versiones a partir de 2.6
# * Python 3: Versiones a partir de 3.3
# * Dependencias para cálculos numéricos
# * Numpy: Versiones a partir de 1.7 
# * Scipy: Versiones a partir 0.14
# * Análisis y Simulación Simbólico
# * Sympy: Versiones a partir 0.7.6
# * Dependencias para Graficas
# * Matplotlib: Versiones a partir 1.1.1
# * Tabulate: Versiones a partir 0.7.3
# *	Dependencias para ejecución de Pruebas
# * Nose: no especificado
#
# # Trabajo práctico
# Muy bien, ahora toca definir circuitos y ejecutar simulaciones sobre los mismos gracias a Ahkab.
#
# ## Instalación de bibliotecas necesarias
#
# Si estás utilizando Anaconda, asegúrate de tener su entorno activado:
#
# ```cmd
# C:\> conda activate base (en el caso de Windows)
# ```
# ó
# 
# ```bash
# $ source /usr/local/Caskroom/miniconda/base/bin/activate (en el caso de macOS)
# ```
#
# En el caso de Windows tienes que tener en el PATH el directorio donde se encuentre el comando `conda` (visita la sección de [Environment Variables](https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10) del [Panel de Control](https://www.digitalcitizen.life/8-ways-start-control-panel-windows-10)). Si has instalado Anaconda con [esta opción](https://docs.anaconda.com/_images/win-install-options.png) marcada, ya no tienes que preocuparte por ello. 
#
# Ahora ya puedes instalar Ahkab:
# 
# ```
# (base) $ pip install ahkab
# ```
#  Como siempre, una vez instalado cualquier framework para Python, ya lo podemos utilizar, tanto desde el [REPL](https://en.wikipedia.org/wiki/Read–eval–print_loop) como desde un entorno Jupyter (Jupyter, [Jupyterlab](http://jupyterlab.readthedocs.io/en/stable/), VS Code o nteract). Recuerda que para usar el kernel Python (que viene con Anaconda) desde nteract debes seguir las instrucciones que se indican en su [documentación oficial](https://nteract.io/kernels). 
#
# %%
import pylab as plt
import ahkab

# %% [markdown]
# También vamos a importar Sympy para hacer algún cálculo más *manual* más adelante:

# %%
import sympy.physics.units as u
from sympy.physics.units import Dimension 
from sympy import * 
from sympy.physics.units import convert_to

# %% [markdown]
#  > **Pregunta:** ¿Qué es y para qué sirve PyLab?
# 
# **Respuesta:**
# 
# De entre la infinidad de librerías que circulan por la red nos detenemos ante **PyLab** que no es una librería sino un conglomerado de varias librerías entre las que se incluyen *numpy*, *scipy*, *sympy*, *pandas*, *matplotlib*, *ipython*. Con esta suite podremos usar de manera muy parecida al interprete de Python como si de MatLab se tratara y hacer nuestros *.py* como si fueran scripts de MatLab.
#
# Creo que es interesante el uso de PyLab porque es un programa de código abierto por lo cual no dependes de caras licencias, desde el punto de vista de la eficiencia está comprobado que PyLab consigue mejores rendimientos en el calculo que MatLab en casi todas las operaciones, tiene también la ventaja de servir para Linux y para Windows y no tener que estar condenados a usar el sistema de Microsoft, además estás programando en python por tanto puedes juntar los programas de cálculo con todas las demás opciones que éste ofrece, sin olvidar que la sintaxis es la de Python conocida por su simplicidad.
#
# ## Circuitos sencillos para trabjar con la ley de Ohm:
# 
#  La *mal llamada* ley de Ohm reza que el voltaje (la *energía por unidad de carga*) que se disipa en un tramo de un circuito eléctrico es equivalente a la intensidad ($I$) de la corriente (es decir, cuántos electrones circulan por unidad de tiempo) por la resistencia del material ($R$) en el que está desplazándose dicha corriente. Matemáticamente:
# 
#  $$
#  V = I\cdot R
#  $$
# 
#  > **Pregunta:** comprueba que la ecuación anterior está ajustada a nivel dimensional, es decir, que la naturaleza de lo que está a ambos lados del signo igual es la misma. Realiza este ejercicio con LaTeX en una celda Markdown.
#
# **Respuesta:**
#
# Antes de comenzar debemos definir algunos conceptos:
# * I - La cantidad de electricidad que pasa por un conductor en un segundo se llama intensidad de la corriente y se mide en AMPERIOS (A).
# * R - La dificultad que ofrece el conductor al paso de una corriente eléctrica se llama resistencia eléctrica y semide en OHMIOS (Ω). 
# * V - A la diferencia de potencial entre dos puntos se le llama tensión o voltaje y se mide en VOLTIOS (V). 
#
# Ahora bien, la Ley de Ohm nos dice que, la intensidad es directamente proporcional a la tensión o voltaje e inversamente proporcional a la resistencia. Es decir que la intensidad crece cuando aumenta la tensión y disminuye cuando crece la resistencia.
#
### Resistencia Eléctrica en terminos de Voltaje##
# 
# Una diferencia de potencial $$\Delta V = V_b - V_a $$ mantenida a través del conductor establece un campo eléctrico E y este campo produce una corriente I que es proporcional a la diferencia de potencial.
# 
# Si el campo se considera uniforme, la diferencia de potencial $$ \Delta V $$ se puede relacionar con el campo eléctrico E de la forma: 
# $$
#  \Delta V = E l
# $$
# Por tanto, la magnitud de la densidad de corriente en el cable J se puede expresar como:
# $$
# J = \sigma E = (1/\rho)\cdot E = (1/\rho)\cdot \Delta V / l
# $$
# Puesto que J = I / A , la diferencia de potencial puede escribirse como:
# $$
# \Delta V = \rho\cdot l\cdot J = \left ( \frac{\rho \cdot l}{A} \right )\cdot I = R I
# $$
# Como se puede observar en la última fórmula, la cantidad $$R=\left ( \frac{\rho \cdot l}{A} \right )$$ se denomina resistencia R del conductor. La resistencia es la razón entre la diferencia de potencial aplicada a un conductor $$\Delta V$$ y la corriente que pasa por el mismo I :
# $$
# R = {V \over I}
# $$
# 
# Datos obtenidos de: http://wikifisica.etsit.upm.es/index.php/LA_LEY_de_OHM_y_RESISTENCIA_ELECTRICA_DEFINITIVO
# 
#  Comencemos con el circuito más sencillo posible de todos:
# 
#  ![](https://raw.githubusercontent.com/pammacdotnet/spicelab/master/primer%20circuito.svg?sanitize=true)
# 
#  Vamos a escribir su contenido (componentes o *netlist*) en disco con el nombre `circuito sencillo.sp`. Esto lo podemos lograr directamente y en tiempo real desde una celda de Jupyter gracias a los *comandos mágicos* de este entorno de programación literaria. En concreto vamos a utilizar `%%writefile` que guarda los contenidos de una celda como un fichero. 
#
# %%
get_ipython().run_cell_magic('writefile', '"circuito sencillo.sp"', '* Este es un circuito sencillo\nr1 1 0 100\nv1 0 1 type=vdc vdc=9\n.op\n.dc v1 start=0 stop=9 step=1\n.end')

# %% [markdown]
# Ahora vamos a leer su descripción con Ahkab, interpretar y ejecutar las simulaciones que en él estén descritas.

# %%
circuito_y_análisis = ahkab.netlist_parser.parse_circuit('circuito sencillo.sp')

# %% [markdown]
#  Separamos la información del netlist (componentes) de los análisis (uno de tipo `op` y otro de tipo `dc`):

# %%
circuito = circuito_y_análisis[0]
análisis_en_netlist = circuito_y_análisis[1]
lista_de_análisis = ahkab.netlist_parser.parse_analysis(circuito, análisis_en_netlist)
print(lista_de_análisis)

# %% [markdown]
# > **Pregunta:** ¿qué tipo de estructura de Python es `lista_de_análisis`?
#
# **Respuesta:**
# La variable **lista_de_análisis** tiene una estructura de tipo "list", la misma tiene los valores por typo **op** y **dc**, los cuales usaremos mas adelante para sacar la lista de valores que corresponda.
#
#  Las simulaciones que implican listas de datos (`.dc`, `.tran`, etc.) necesitan de un fichero temporal (`outfile`)
#  donde almacenar los resultados. Para ello tenemos que definir la propiedad `outfile`.

# %%
lista_de_análisis[1]['outfile'] = "simulación dc.tsv"

# %% [markdown]
#  > **Pregunta:** escribe el código Python necesario para identificar qué análisis de `lista_de_análisis`
#  son de tipo `dc` ó `tran` y sólo añadir la propiedad `outfile` en estos casos.
# Aquí tenéis un post de Stackoverflow con algo de [ayuda](https://stackoverflow.com/questions/49194107/how-to-find-index-of-a-dictionary-key-value-within-a-list-python).
#  Un poco más de ayuda: el siguiente código (sí, una única línea) devuelve el índice de la simulación que es de tipo `dc`. Para simplificar un poco el ejercicio, suponed que, como máximo, habrá un análisis de tipo `tran` y/o `dc`.

# %%
for element in lista_de_análisis:
    elementValues = element.values()
    if "tran" in elementValues and "outfile" not in elementValues: 
        element['outfile'] = "C:\simulación tran.tsv"
    elif "dc" in elementValues and "outfile" not in elementValues:
        element['outfile'] = "C:\simulación dc.tsv"

# %% [markdown]
# Una vez que ya hemos separado netlists de simulaciones, ahora ejecutamos las segundas (¡todas a la vez!) gracias al método `.run` de Ahkab: 

# %%
resultados = ahkab.run(circuito, lista_de_análisis)

# %% [markdown]
# ### Resultados de la simulación `.dc`
# Imprimimos información sobre la simulación de tipo `.dc`:

# %%
print(resultados['dc'])

# %% [markdown]
#  Veamos qué variables podemos dibujar para el caso del análisis `dc`.

# %%
print(resultados['dc'].keys())

# %% [markdown]
# Y ahora graficamos el resultado del análisis anterior. Concretamente vamos a representar el voltaje en el borne 1 (`V1`) con respecto a la intensidad del circuito (`I(V1)`).

# %%
figura = plt.figure()
plt.title("Prueba DC")
plt.ylabel('Intensidad (A)')
plt.xlabel('Voltaje (V)')
plt.plot(resultados['dc']['V1'], resultados['dc']['I(V1)'], label="Voltaje (V1)")
print(resultados['op'])

# %% [markdown]
# > **Pregunta:** comenta la gráfica anterior… ¿qué estamos viendo exactamente? Etiqueta los ejes de la misma convenientemente. Así como ningún número puede *viajar* solo sin hacer referencia a su naturaleza, ninguna gráfica puede estar sin sus ejes convenientemente etiquetados. Algo de [ayuda](https://matplotlib.org/3.1.0/gallery/pyplots/fig_axes_labels_simple.html). ¿Qué biblioteca estamos usando para graficar? Una [pista](https://matplotlib.org).
#
# **Respuesta:**
#
# Estamos viendo la evolucion o los valores de potencial en los dos bornes o puntos de conexiòn cuando el circuito llega al punto de estabilizaciòn o equilibrio siendo estos puntos: V0 y V1. Es decir, se ve graficamente como se inicia en un valor de voltaje existente pero el mismo disminuye al pasar por la resistencia, en otras palabras podriamos decir que la resistencia le "quita" potencial al circuito.
# La Libreria que estamos usando se llama matplotlib, una suerte librería de trazado utilizada para gráficos 2D en Python, es muy flexible y tiene muchos valores predeterminados incorporados que ayuda enormemente a la hora de realizar graficas en python cuya referencia puede encontrarse en (https://matplotlib.org/).
# Resultados de la simulación .op El método .results nos devuelve un diccionario con los resultados de la simulación.

# %% [markdown]
#  ### Resultados de la simulación `.op` 
#  El método `.results` nos devuelve un diccionario con los resultados de la simulación.
#
# %%
print(resultados['op'].results)

# %% [markdown]
#  > **Pregunta:** justifica el sencillo resultado anterior (análisis `op`). Repite el cálculo con Sympy, atendiendo con mimo a las unidades y al formateo de los resultados (tal y como hemos visto en muchos otros notebooks en clase).
#
# **Respuesta:**
#
# Como vemos si analizamos el circuito y realizamos el calculo con Sympy, aplicando la falsamente llamada Ley de Ohm, podemos verificar que la intensidad de corriente por su resistencia coincide con el voltaje del circuito siendo este 9V segun la definicion del mismo. 
# 
# %%
r1 = 100*u.ohms
print("Ohm(R1): 100")
print("I(V1):" + str(resultados['op']['I(V1)'][0][0]))
intensidad_ahkab = resultados['op']['I(V1)'][0][0]*u.ampere
print('Aplicamos la falsamente Ley de Ohm: V = I * R')
v1 = convert_to(intensidad_ahkab*r1, [u.volt])
pprint(v1)
# %% [markdown]
#  ## Análisis de circuito con resistencias en serie
# %% [markdown]
# Vamos a resolver (en punto de operación) el siguiente circuito:
# 
# ![](https://raw.githubusercontent.com/pammacdotnet/spicelab/master/resistencias%20en%20serie.svg?sanitize=true)
# 
# Al igual que antes, grabamos el netlist en disco desde Jupyter gracias a la *palabra mágica* [`%writefile`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#cellmagic-writefile). 

# %%
get_ipython().run_cell_magic('writefile', '"resistencias en serie.net"', '* circuito con tres resistencias en serie\nv1 1 0 type=vdc vdc=9\nR1 0 2 3k\nR2 2 3 10k  \nR3 3 1 5k\n* análisis del circuito\n.op\n.end')

# %%
circuito_y_análisis = ahkab.netlist_parser.parse_circuit('resistencias en serie.net')
circuito = circuito_y_análisis[0]       
análisis_en_netlist = circuito_y_análisis[1]
lista_de_análisis = ahkab.netlist_parser.parse_analysis(circuito, análisis_en_netlist)
resultados = ahkab.run(circuito, lista_de_análisis)

# %% [markdown]
# Imprimos los resultados del análisis `.op`:

# %%
print(resultados['op'])

# %% [markdown]
# Los cantidades `V1`, `V2` y `V3` hacen referencia a los distintos valores del potencial que se ha perdido en cada uno de los bornes que has elegido para describir el netlist (`1`, `2`, etc.). Por ejemplo, podemos calcular el *potencial consumido* por la resistencia `R1` y verás que coincide con el del punto `V2` devuelto por Ahkab. 

# %%
r1 = 3E3*u.ohms
r2 = 10E3*u.ohms
r3 = 5E3*u.ohms
intensidad_ahkab = resultados['op']['I(V1)'][0][0]*u.ampere
v2r1 = convert_to(intensidad_ahkab*r1, [u.volt])
v3r2 = convert_to(intensidad_ahkab*(r2), [u.volt])
v4r3 = convert_to(intensidad_ahkab*(r3), [u.volt])
pprint(v2r1)
pprint(v3r2)
pprint(v4r3)

# %% [markdown]
#  > **Pregunta**: reproduce el resto de los valores anteriores de manera *manual* mediante Sympy (es decir, aplicando la ley de Ohm, pero con tun *toque computacional*). Te pongo aquí un ejemplo del que puedes partir… En él sólo calculo la corriente que circula por el circuito (sí, justo la que antes Ahkab ha devuelto de manera automática). Para ello necesito previamente computar la resistencia total (`r_total`). Faltarían el resto de resultados y convertirlos a unidades más *vistosas* (mediante la orden `convert_to` y `.n()`).
#
#
# %%
v1 = 9*u.volts
r1 = 3E3*u.ohms
r2 = 10E3*u.ohms
r3 = 5E3*u.ohms
r_total = r1 + r2 + r3

# **Respuesta:**

# %%
intensidad = u.Quantity('i')
intensidad.set_dimension(u.current)

ley_ohm = Eq(v1, intensidad*r_total)

solucion_para_intensidad = solve(ley_ohm, intensidad)

iv1 = convert_to(solucion_para_intensidad[0], [u.ampere]).n(2)

intensidad_ahkab = resultados['op']['I(V1)'][0][0]*u.ampere

vv2 = convert_to(intensidad_ahkab*r1, [u.volt])
vv3 = convert_to(intensidad_ahkab*(r1 + r2), [u.volt])
vv4 = convert_to(intensidad_ahkab*r_total, [u.volt])

print('Resistencia Total del Circuito: ' + str(r_total))
print('V(V0) - Carece de Sentido realizar un calculo ya que es igual al voltaje de la fuente porque no existe ningun componente mas que la propia perdida (fuga) del material del cableado: ' + str(v1))
print('V(V1):' + str(vv2))
print('V(V2):' + str(vv3))
print('V(V4):' + str(vv4))
pprint('I(V1):' + str(iv1))

# %% [markdown]
# > **Pregunta**: Demuestra que se cumple la Ley de Kirchhoff de la energía en un circuito, es decir, que la suma de la energía suministrada por las fuentes (pilas) es igual a la consumida por las resistencias. Realiza la operación con Sympy.
# 
# 
# $$
# \sum_i^N V_{\text{fuentes}} = \sum_j^M V_{\text{consumido en resistencias}}
# $$
# 
# Ten en cuenta que en este caso sólo hay una fuente.

# %%
v2r1 = convert_to(intensidad_ahkab*r1, [u.volt])
v3r2 = convert_to(intensidad_ahkab*(r2), [u.volt])
v4r3 = convert_to(intensidad_ahkab*(r3), [u.volt])
print('Si sumamos las energias consumidas por cada una de las resistencias, siendo estas v2R1, v3R2, V4R3, tenemos:'+ str(v2r1 + v3r2 + v4r3))
print('Siendo el voltaje de la fuente de alimentacion V1 igual a:' + str(v1))
print('Se comprueba que la suma de las corrientes entrantes es igual a la suma de las corrientes consumidas por las resistencias.')

# %% [markdown]
# ## Análisis `.op` de circuitos con resistencias en paralelo
# 
# Vamos a complicar un poco el trabajo añadiendo elementos en paralelo.
# 
#  > **Pregunta**: realiza los análisis `.op` de los siguientes circuitos.
#  Para ello crea un netlist separado para cada uno donde queden correctamente descritos
#  junto con la simulación (`.op`). Comenta los resultados que devuelve Ahkab (no imprimas los resultados de las simulaciones *sin más*).
# 
#  ![](https://raw.githubusercontent.com/pammacdotnet/spicelab/master/resistencias%20en%20paralelo.svg?sanitize=true)
# 
#  Aquí tienes el análisis del primer circuito, para que sirva de ejemplo:
#
# **Respuesta:**
#
# %%
get_ipython().run_cell_magic('writefile', '"resistencias en paralelo 1.cir"', '* resistencias en paralelo\nvdd 0 1 vdc=12 type=vdc\nr2 1 2 1k\nr3 2 3 220\nr4 3 0 1.5k\nr5 2 0 470\n.op\n.end')

# %%
circuito_y_análisis = ahkab.netlist_parser.parse_circuit('resistencias en paralelo 1.cir')
circuito = circuito_y_análisis[0]       
análisis_en_netlist = circuito_y_análisis[1]
lista_de_análisis = ahkab.netlist_parser.parse_analysis(circuito, análisis_en_netlist)
resultados = ahkab.run(circuito, lista_de_análisis)

# %% [markdown]
# Imprimimos los resultados del análisis `.op`. Como puedes comprobar, Ahkab sólo reporta la intensidad de corriente en las ramas en las que hay una pila (en este caso, la rama donde está la pila `VDD`).

# %%
print(resultados['op'])

# %%
get_ipython().run_cell_magic('writefile', '"resistencias en paralelo 2.cir"', '* resistencias en paralelo 2\nvdd1 1 0 vdc=9 type=vdc\nvdd2 4 0 vdc=1.5 type=vdc\nr1 1 2 47\nr2 2 3 220\nr3 2 4 180\nr4 3 5 1k\nr5 5 0 560\n.op\n.end')

# %%
circuito_y_análisis_3 = ahkab.netlist_parser.parse_circuit('resistencias en paralelo 3.cir')
circuito_3 = circuito_y_análisis_3[0]       
análisis_en_netlist_3 = circuito_y_análisis_3[1]
lista_de_análisis_3 = ahkab.netlist_parser.parse_analysis(circuito_3, análisis_en_netlist_3)
resultados_3 = ahkab.run(circuito_3, lista_de_análisis_3)

# %%
print(resultados_3['op'])

# %% [markdown]
# > **Pregunta:** inserta dos *pilas virtuales* de 0 voltios en el resto de ramas del circuito (`Vdummy1` en la rama donde está `R5` y `Vdummy2` en la rama donde está `R3` y `R4`) para que Ahkab nos imprima también la corriente en las mismas. Es muy parecido al tercer circuito que tienes que resolver, donde `V1`, `V2` y `V3` tienen cero voltios. Estas *pilas nulas* son, a todos los efectos, *simples cables*. Una vez que ya tienes las corrientes en todas las ramas, comprueba que se cumple la Ley de Kirchhoff para las corrientes:
# 
# $$
# I_{\text{entrante}} = \sum_i^{N} I_{\text{salientes}}
# $$
# 
# Repite lo mismo para los otros dos circuitos. Realiza además los cálculos con Sympy (recalcula los mismos voltajes que devuelve Ahkab a partir de la corriente que sí te devuelve la simulación) y cuidando de no olvidar las unidades. Recuerda que el objeto `resultados` alberga toda la información que necesitas de manera indexada. Ya han aparecido un ejemplo más arriba. Es decir: no *copies* los números *a mano*, trabaja de manera informáticamente elegante (usando la variable `resultados`). 
# %% [markdown]
#  # Circuitos en DC que evolucionan con el tiempo
# %% [markdown]
#  ## Carga de un condensador
#  Vamos a ver qué le pasa a un circuito de corriente continua cuando tiene un condensador
#  en serie.
# 
#  ![](https://raw.githubusercontent.com/pammacdotnet/spicelab/master/condensador%20en%20continua.svg?sanitize=true)
# 
#  Al igual que antes, primero guardamos el circuito en un netlist externo:
# %%
get_ipython().run_cell_magic('writefile', '"condensador en continua.ckt"', '* Carga condensador\nv1 0 1 type=vdc vdc=6\nr1 1 2 1k\nc1 2 0 1m ic=0\n.op\n.tran tstep=0.1 tstop=8 uic=0\n.end')

# %% [markdown]
# > **Pregunta:** ¿qué significa el parámetro `ic=0`? ¿qué perseguimos con un análisis de tipo `.tran`?
# 
# Leamos el circuito:
# %%
circuito_y_análisis = ahkab.netlist_parser.parse_circuit("condensador en continua.ckt")

# %% [markdown]
#  Separamos el netlist de los análisis y asignamos un fichero de almacenamiento de datos (`outfile`):

# %%
circuito = circuito_y_análisis[0]
análisis_en_netlist = circuito_y_análisis[1]
lista_de_análisis = ahkab.netlist_parser.parse_analysis(circuito, análisis_en_netlist)
lista_de_análisis[1]['outfile'] = "simulación tran.tsv"

# %% [markdown]
#  Ejecutamos la simulación:

# %%
resultados = ahkab.run(circuito, lista_de_análisis)
print('Anàlsis OP.')
print(resultados['op'])

print('Anàlsis Tran.')
print(resultados['tran'])

# %% [markdown]
#  Dibujamos la gráfica de carga del condensador con el tiempo, centrándonos en la intensidad que circula por la pila. 

# %%
figura = plt.figure()
plt.title("Carga de un condensador")
plt.ylabel('Corriente de Carga (V)')
plt.xlabel('Tiempo (T)')
plt.plot(resultados['tran']['T'], resultados['tran']['I(V1)'], label="Una etiqueta")

figura_v1 = plt.figure()
plt.title("Gráfica con el voltaje en el borne V1")
plt.ylabel('Voltaje (V)')
plt.xlabel('Tiempo (T)')
plt.plot(resultados['tran']['T'], resultados['tran']['V1'], label="Una etiqueta")

figura_v2 = plt.figure()
plt.title("Gráfica con el voltaje en el borne V2")
plt.ylabel('Voltaje (V)')
plt.xlabel('Tiempo (T)')
plt.plot(resultados['tran']['T'], resultados['tran']['V2'], label="Una etiqueta")

# %% [markdown]
# > **Pregunta:** Etiqueta los ejes convenientemente y comenta la gráfica. Dibuja otra gráfica con el voltaje en el borne `V1`. ¿Por qué son *opuestas*? ¿Qué le ocurre al voltaje a medida que evoluciona el circuito en el tiempo? Dibuja las gráficas en un formato estándar de representación vectorial (SVG, por ejemplo). Algo de ayuda [aquí](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html#IPython.display.set_matplotlib_formats). ¿Qué valores devuelve el análisis de tipo `.op`? Justifícalo.
# %% [markdown]
# ## Carrera de condensadores
# 
# Ahora tenemos un circuito con dos condensadores en paralelo: 
# 
# ![](https://raw.githubusercontent.com/pammacdotnet/spicelab/master/condensadores%20en%20paralelo.svg?sanitize=true)
# 
# > **Pregunta:** Crea el netlist de este circuito e identifica qué condensador se satura primero. Dibuja la evolución de la intensidad en ambas ramas de manera simultánea. [Aquí](https://matplotlib.org/gallery/api/two_scales.html) tienes un ejemplo de cómo se hace esto en Matplotlib. Recuerda que para que Ahkab nos devuelva la corriente en una rama, debe de estar presente una pila. Si es necesario, inserta pilas virtuales de valor nulo (cero voltios), tal y como hemos comentado antes. Grafica también los voltajes (en otra gráfica, pero que aparezcan juntos). 