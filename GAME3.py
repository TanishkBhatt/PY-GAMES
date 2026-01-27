# SLOTING MACHINE BETTING GAME
import random
import time

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
rounds = int(input("ENTER THE NUMBEROF ROUNDS YOU WANNA PLAY : "))

total_winnings = 0

for i in range(rounds):
    res = slotMatrix(betAmount / rounds)

    print("\nSLOT MATRIX :")
    for row in res[0]:
        print(row)

    print(f"\nTOTAL WINNINGS : {res[1]}")
    print(f"TOTAL PROFIT (THIS ROUND): {res[2] - (betAmount/rounds)}")
    print(f"FINAL AMOUNT RECIEVED : {res[2]}\n") 

    total_winnings += res[2]
    time.sleep(2)

print(f"\nYOUR TOTAL WINNINGS AFTER {rounds} ROUNDS ON ${betAmount} IS ${total_winnings}")
print(f"THATS {((total_winnings - betAmount) / betAmount) * 100}% PROFIT!\n") 
