def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminating condition: when depth limit is reached or leaf node is reached
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')
        # Iterate over the children nodes (left and right)
        for i in range(2):
            # Recursively call minimax for the child node (switch to minimizing player)
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            # Update the best value found so far (maximize)
            best = max(best, val)
            # Update alpha (best guaranteed value for the maximizing player)
            alpha = max(alpha, best)
            # Alpha-beta pruning: stop further evaluation if beta (minimum for minimizing player) is less than or equal to alpha
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        # Iterate over the children nodes (left and right)
        for i in range(2):
            # Recursively call minimax for the child node (switch to maximizing player)
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            # Update the best value found so far (minimize)
            best = min(best, val)
            # Update beta (best guaranteed value for the minimizing player)
            beta = min(beta, best)
            # Alpha-beta pruning: stop further evaluation if beta (minimum for minimizing player) is less than or equal to alpha
            if beta <= alpha:
                break
        return best

# Driver Code
if __name__ == "__main__":
    values = [5, 6,9,1,2,0,-1]
    # Initial call to minimax function with root node (index 0), maximizing player (True), and initial alpha and beta values
    print("The optimal value is :", minimax(0, 0, True, values, float('-inf'), float('inf')))
