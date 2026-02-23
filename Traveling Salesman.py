def tour_cost(tour, cities):
    total = 0
    for i in range(len(tour)):
        j = (i + 1) % len(tour)
        total += distance(cities[tour[i]], cities[tour[j]])
    return total
