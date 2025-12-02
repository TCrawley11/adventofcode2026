# 100 possible numbers, probably should use hashing via modulo
# answer is the amount of times the dial is pointing at zero after a move

moves = []
with open(file='input.txt', mode='r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        moves.append(line)

pos = 50 
old_pos = pos
res = 0

for i, move in enumerate(moves):
    old_pos = pos
    scale = 0

    if move.startswith('L'):
        move = int(move.strip('L'))
        pos += move * -1
        pos = pos % 100

        if pos > old_pos and pos != 0 and old_pos != 0:
            res += 1
            # print('pointed during turn + 1', '\n')
    else:
        move = int(move.strip('R'))
        pos += move
        pos = pos % 100

        if pos < old_pos and pos != 0 and old_pos != 0:
            res += 1

    if pos == 0:
        res += 1

    if move >= 101:
        # scale it if it's bigger than a hundred 
        scale = int(move/100)

    res += scale

print(res)
#print(moves)