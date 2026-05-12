

# Builds the starting position's gamestate
gamestate = {}

for i1 in range(1, 9):
    gamestate[i1] = {}
    for i2 in range(1, 9):
        gamestate[i1][i2] = None

print(gamestate)

