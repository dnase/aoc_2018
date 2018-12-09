from collections import defaultdict, deque

def cj(numplayers, total_marbles):
    marbles = deque([0])
    current_marble = 0
    players = defaultdict(int)
    player = 0
    total_marbles += 1
    for marble in range(1, total_marbles):
        if marble % 23 == 0:
            players[player] += marble
            t = ((current_marble - 7) % len(marbles))
            marbles.rotate(-t)
            players[player] += marbles.popleft()
            marbles.rotate(t - 1)
            marbles.rotate(7)
        else:
            marbles.append(marble)
            marbles.rotate(-1)
        current_marble = len(marbles) - 2
        player += 1
        player %= numplayers
    return(max(players.values()))

def part1():
    return cj(424, 71144)

def part2():
    return cj(424, 7114400)

print("P1: ", part1())
print("P2: ", part2())
