# SLOTING MACHINE BETTING GAME
import random

def slotMatrix(betAmount: float) -> tuple[list[list], int]:
    marks = ["A", "B", "C"]
    matrix = [[0, 0, 0], 
              [0, 0, 0], 
              [0, 0, 0]]
    winnings = 0

    for i in range(3):
        for j in range(3):
            item = random.choice(marks)
            matrix[i][j] = item
    
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2]:
            winnings += 1
        if matrix[0][i] == matrix[1][i] == matrix[2][i]:
            winnings += 1

    profitAmount = (winnings + 0.5) * betAmount
    return matrix, winnings, profitAmount

print("\nSLOTING MACHINE BETTING GAME!\n")

betAmount = float(input("ENTER YOU BETTING AMOUNT : $"))
res = slotMatrix(betAmount)

print("\nSLOT MATRIX :")
for row in res[0]:
    print(row)

print(f"\nTOTAL WINNINGS : {res[1]}")
print(f"TOTAL PROFIT : {res[2] - betAmount}")
print(f"FINAL AMOUNT RECIEVED : {res[2]}\n")