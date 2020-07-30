"""
Creada en la decada de los 50 por Richard Bellman. Como necesitaba financiamiento del Gobierno para continuar con sus investigaciones,
le coloco un nombre llamativo para que su propuesta al Gobierno fuera aceptada, por eso lo llamó Programación dinámica.

La programación dinámica no esta relacionada con el nombre, pero si es una técnica poderosa para la optimización de cierto tipo de problemas.

Aquellos problemas que puede dar solucion son:

1.- Subestructura óptima: La solución optima global se puede encontrar al combinar soluciones optimas de subproblemas locales.
2.- Problemas empalmados: Una solución optima que involucra resolver el mismo problema en varias ocaciones.

Memoization (Memorización)

Es una técnica para guardar computos previos y evitar realizarlos nuevamente.
Normalmente se utiliza un diccionario, donde las consultas se puedern hacer en O(1).
Intercambia tiempo por espacio.
"""