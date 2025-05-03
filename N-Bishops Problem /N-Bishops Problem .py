def place_bishops(n):
    
    board = [[0] * n for _ in range(n)]
    row, col = 0, 0
    placed = 0

    while placed < n:
        if row < n and col < n:
            board[row][col] = 1
            placed += 1
            row += 1
            col += 2 
        else:
            col = (col - n) + 1
            if col >= n:
                break

    return board

n = int(input())
solution = place_bishops(n)

for row in solution:
    print(" ".join(str(cell) for cell in row))
