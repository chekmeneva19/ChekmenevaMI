def check_winner(board, k):
    n = len(board)


    for i in range(n):
        for j in range(n - k + 1):
            if all(board[i][j + l] == "X" for l in range(k)):
                return "X"
            if all(board[j + l][i] == "X" for l in range(k)):
                return "X"
            if all(board[i][j + l] == "O" for l in range(k)):
                return "O"
            if all(board[j + l][i] == "O" for l in range(k)):
                return "O"

    for i in range(n - k + 1):
        for j in range(n - k + 1):
            if all(board[i + l][j + l] == "X" for l in range(k)):
                return "X"
            if all(board[i + l][j + l] == "O" for l in range(k)):
                return "O"
    for i in range(n - k + 1):
        for j in range(k - 1, n):
            if all(board[i + l][j - l] == "X" for l in range(k)):
                return "X"
            if all(board[i + l][j - l] == "O" for l in range(k)):
                return "O"

    return "Ничья"


board = []
k = None
for _ in range(int(input())):
    row = input().strip()
    board.append(list(row))
    if k is None:
        k = len(row)

winner = check_winner(board, k)
print(winner)
