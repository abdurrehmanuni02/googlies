
import random

WINNING_CONDITIONS = [

    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]


def printBoard(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if (i != 2):
            print("-" * 9)


def agentMove(board, player):
    playerPossibleWins = []
    agentPossibleWins = []
    for condition in WINNING_CONDITIONS:
        playerCount = 0
        agentCount = 0
        playerEmpty = None
        agentEmpty = None
        for pos in condition:
            if board[pos[0]][pos[1]] == player:
                playerCount += 1
            elif board[pos[0]][pos[1]] == ' ':
                playerEmpty = pos
            else:
                agentCount += 1
        if playerCount == 2 and playerEmpty:
            playerPossibleWins.append(playerEmpty)
        if agentCount == 2 and playerEmpty:
            agentPossibleWins.append(playerEmpty)

    print("Player Possible Wins:", playerPossibleWins)
    print("Agent Possible Wins:", agentPossibleWins)

    if playerPossibleWins:
        row, col = playerPossibleWins[0]
    elif agentPossibleWins:
        row, col = agentPossibleWins[0]
    else:
        row, col = random.choice(movesLeft)

    board[row][col] = player
    movesLeft.remove((row, col))
    agentMoves.append((row, col))


def isWinner(board, player):
    for condition in WINNING_CONDITIONS:
        if all(board[row][col] == player for row, col in condition):
            return True
    return False


def isFull(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


board = [[' ' for _ in range(3)] for _ in range(3)]
player = ['X', 'O']
movesLeft = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
playerMoves = []
agentMoves = []
currentPlayer = random.choice(player)
printBoard(board)
while True:

    if (currentPlayer == 'X'):
        row = int(input("Enter Row : "))
        col = int(input("Enter Column : "))
        if (row > 2 or col > 2):
            print("Illegal Move")
            continue
        if (board[row][col] == ' '):
            board[row][col] = currentPlayer
            movesLeft.remove((row, col))
            playerMoves.append((row, col))
        else:
            print("Illegal Move")
            continue
    elif (currentPlayer == 'O'):
        agentMove(board, currentPlayer)
    printBoard(board)
    if (isWinner(board, currentPlayer)):
        print("Player ", currentPlayer, " is the Winner !");
        break;
    elif (isFull(board)):
        print("Its a draw!")
        break;
    else:
        currentPlayer = 'X' if currentPlayer == 'O' else 'O'
        print("Player Moves : ", playerMoves)
        print("Agent Moves : ", agentMoves)
        print("Move Left : ", movesLeft)