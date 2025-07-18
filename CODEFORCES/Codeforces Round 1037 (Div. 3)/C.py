from sys import stdin
import heapq

def readLine():
    return stdin.readline().strip()

def readInt():
    return int(readLine())

def readInts():
    return list(map(int, readLine().split()))

def build_heap(pq: list, h: list):
    for hi in h:
        heapq.heappush(pq, hi)

def remove_smaller_towers(pq: list, current_tower: int):
    while len(pq) > 0 and current_tower >= pq[0]:
        heapq.heappop(pq)

def play_game(pq: list, current_tower: int, max_tower: int) -> bool:
    current_time = 0
    while len(pq) > 0 and current_tower < max_tower:
        next_tower = pq[0]
        teleportation_time = next_tower - current_tower
        time_left = current_tower - current_time

        if teleportation_time <= time_left:
            current_time += teleportation_time
            current_tower = next_tower
            heapq.heappop(pq)
        else:
            return False

    return current_tower == max_tower

def main():
    t = readInt()

    for i in range(t):
        n, k = readInts()
        h = readInts()
        current_tower = h[k - 1]
        max_tower = max(h)

        pq = []
        build_heap(pq, h)
        remove_smaller_towers(pq, current_tower)
        print('YES' if play_game(pq, current_tower, max_tower) else 'NO')


if __name__ == '__main__':
    main()