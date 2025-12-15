import heapq

def min_cost_to_connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)

    total_cost = 0

    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        cost = first + second
        total_cost += cost

        heapq.heappush(cable_lengths, cost)

    return total_cost

if __name__ == "__main__":
    cable_lengths = [5, 3, 8, 6]
    min_cost = min_cost_to_connect_cables(cable_lengths)
    print("Мінімальні витрати на об'єднання кабелів:", min_cost)