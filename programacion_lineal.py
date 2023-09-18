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
