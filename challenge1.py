def getMinimumNumberOfMoves(A):
    N = len(A)

    total_bricks = sum(A)

    # Check if total is divisible by the number of boxes
    if total_bricks % N != 0:
        return -1

    # Calculate the target number of bricks in each box
    target = total_bricks // N

    # Calculate the total number of moves
    moves = 0
    accumulated_difference = 0

    for i in range(N):
        difference = A[i] - target
        accumulated_difference += difference
        moves += abs(accumulated_difference)

    return moves

result = getMinimumNumberOfMoves([11, 10, 8, 12, 8, 10, 11])
print(result) 
