history = [initial_score] * L
current = random_state()
i = 0

while not stop:
    next_state = random_neighbor(current)

    if score(next_state) <= history[i]:
        current = next_state

    history[i] = score(current)
    i = (i + 1) % L
