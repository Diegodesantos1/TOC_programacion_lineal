<h1 align="center">Programación lineal</h1>

En este [repositorio](https://github.com/Diegodesantos1/TOC_programacion_lineal) queda resuelta la práctica de programación lineal.

El pdf es el siguiente: [pdf](https://github.com/Diegodesantos1/TOC_programacion_lineal/blob/main/Programaci%C3%B3n_Lineal.pdf)

El código empleado para resolverlo es:

***
```python
# Importo la librería ortools
from ortools.linear_solver import pywraplp
# Creo el solver
solver = pywraplp.Solver('Maximize army power',
                         pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Defino las variables
espadachines = solver.IntVar(0, solver.infinity(), 'espadachines')
arqueros = solver.IntVar(0, solver.infinity(), 'arqueros')
jinetes = solver.IntVar(0, solver.infinity(), 'jinetes')

# Añado las restricciones
solver.Add(espadachines*60 + arqueros*80 + jinetes*140 <= 1200)  # Comida
solver.Add(espadachines*20 + arqueros*10 <= 800)                 # Madera
solver.Add(arqueros*40 + jinetes*100 <= 600)                 # Oro
# Máximizo la función objetivo
solver.Maximize(espadachines*70 + arqueros*95 + jinetes*230)
# Resuelvo el problema
status = solver.Solve()
# Imprimo la solución si es óptima
if status == pywraplp.Solver.OPTIMAL:
    print('================= Solución =================')
    print(
        f'Resuelto en {solver.wall_time():.2f} milisegundos en {solver.iterations()} iteraciones.')
    print(f'Poder óptimo = {solver.Objective().Value()} 💪poder')
    print('Army:')
    print(f' - 🗡️espadachines = {espadachines.solution_value()}')
    print(f' - 🏹arqueros = {arqueros.solution_value()}')
    print(f' - 🐎jinetes = {jinetes.solution_value()}')
else:
    print('El problema no tiene solución óptima.')
```

***

<h2 align="center">Resultado y conclusiones</h2>

Con todo esto he conseguido encontrar la solución óptima, siendo 6🗡️ espadachines, 0 🏹arqueros y 6 🐎jinetes otorgando 1800 💪poder.
Gracias a la librería de OR-Tools con su solucionador de problemas de optimización lineal GLOP (Paquete de optimización lineal de Google), el cual utiliza el método Simplex junto a técnicas avanzadas de optimización como el método de punto interior o método de la barrera para poder resolver este tipo de problemas


Este es el resultado final:

![image](https://github.com/Diegodesantos1/TOC_programacion_lineal/blob/main/images/solucion.jpg)
