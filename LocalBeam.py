states = [random_state() for _ in range(k)]

while True:
    all_neighbors = []

    for s in states:
        all_neighbors.extend(problem.get_neighbors(s))

    states = best_k(all_neighbors)
