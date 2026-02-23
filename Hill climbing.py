current = random_state()

while True:
    neighbors = problem.get_neighbors(current)
    best = min(neighbors, key=problem.evaluate)

    if problem.evaluate(best) >= problem.evaluate(current):
        break

    current = best

return current
