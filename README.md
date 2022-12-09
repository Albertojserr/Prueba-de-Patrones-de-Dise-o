# Prueba-de-Patrones-de-Dise-o
Ejercicio 1 (2 Puntos)

El Servicio de Emergencias Sanitarias de Castilla y León, antes conocido como 061, está organizado en una jerarquía de bases. Algunas de estas bases realmente disponen de personal y ambulancias (por ejemplo la de Medina del Campo), mientras que otras son «unidades administrativas» que agrupan un conjunto de bases (por ejemplo Valladolid, que agrupa la unidad del Hospital Clínico Universitario y la de Medina del Campo entre otras).

Para cada base, interesa modelar los siguientes datos:

    Nombre de la base.
    Número de ambulancias, que en el caso de las bases compuestas es la suma de las ambulancias disponibles en las bases que las componen en ese momento.
    Tiempo medio de asistencia, que en el caso de las bases compuestas es la media de los tiempos medios de asistencia registrados en las bases que las componen en ese momento.

Elaborar un diseño que permita modelar adecuadamente esta situación, implantando completamente en python las clases que modelan las bases, sean del tipo que sean.

Ejercicio 2 (2 Puntos)

Disponemos de una clase BATERIA que modela el funcionamiento de la batería de un ordenador portátil, cuya forma corta es la siguiente:

    feature(s) from BATERIA
        Características que monitorizan el estado
            conectado: BOOLEAN
                ¿La batería está conectada?
            cargando: BOOLEAN
                ¿La batería está cargando?
            carga: INT
                En tanto por ciento
            tiempo: INT
                Minutos restantes estimados
            notifica
                Método sin código que es invocado por los métodos privados cada vez que éstos cambian el estado del objeto
    end of BATERIA

Ahora se desea elaborar dos observadores capaces de informar sobre el estado de la batería, indicando el tiempo restante o el tanto por ciento de carga respectivamente.

Elaborar un diseño adecuado a estos propósitos (se recomienda encarecidamente que este diseño esté basado en el patrón observador) Implementar completamente la clase que juega el papel del sujeto concreto en ese diseño.

Ejercicio 3(2 Puntos)

En un sistema de alarma de un edificio se consideran detectores de humo, sensores de temperatura, sensores de presión, etc. 

Todos estos elementos tienen un estado conectado/desconectado y en consecuencia se puede pasar de un estado a otro (cuando se crean, están desconectados). 

Todos ellos son capaces de proporcionar una medida (un valor REAL) y tienen un valor umbral que se fija inicialmente al crear el elemento. 

El sistema recorre en un bucle continuo todos sus elementos conectados. 

Cuando la medida de uno de ellos supera su valor umbral el sistema dispara la alarma. 

Para evitar falsas alarmas, varios elementos se pueden unir formando listas (y las a su vez en otras listas) y para este sensor complejo, la alarma sólo se dispara si el valor medio de los elementos de la lista supera el umbral definido para ese elemento compuesto. 

Diseñar una solución con las clases necesarias y sus características para este problema, implementando en python al menos todo lo relacionado con el disparo de la alarma. Recordar Pandas y Cómo convertir un Dataframe en una lista de listas por filas o columnas o viceversa
