current = random_state()
T = initial_temperature

while T > 0:
    next_state = random_neighbor(current)

    if better(next_state, current):
        current = next_state
    else:
        accept with probability based on T

    decrease T
