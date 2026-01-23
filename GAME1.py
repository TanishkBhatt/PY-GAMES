# ROCK PAPER SCISSOR GAME IN PYTHON
import random

print("\n------------------------------ROCK PAPER SCISSOR------------------------------\n")
print(f"COMMANDS :\n0 FOR ROCK\n1 FOR PAPER\n2 FOR SCISSOR")

moves = ["ROCK", "PAPER", 'SCISSOR']
scorecard = {"USER": 0, "COMPUTER": 0, "TIE": 0}

round_no = 1

while round_no <= 5:
    print(f"\nROUND {round_no}")
    comp_move = random.choice(moves)
    user_move = input("ENTER YOUR MOVE : ")

    if user_move in {"0", "1", "2"}:
        user_move = moves[int(user_move)]
    else:
        print("INVALID INPUT! DEFAULT MOVE : ROCK")
        user_move = "ROCK"

    print(f"YOUR MOVE : {user_move}")
    print(f"COMPUTER MOVE : {comp_move}")

    win_conditions = {
    ("ROCK", "SCISSOR"),
    ("PAPER", "ROCK"),
    ("SCISSOR", "PAPER")}

    if comp_move == user_move:
        print("OHH! THATS A TIE!")
        scorecard["TIE"] += 1

    elif (user_move, comp_move) in win_conditions:
        print("CONGRATS! YOU HAVE WON!")
        scorecard["USER"] += 1

    else:
        print("BAD LUCK! YOU HAVE LOST!")
        scorecard["COMPUTER"] += 1

    round_no += 1

print("\n------------------------------------- GAME OVER ----------------------------------")
print(f"""
FINAL SCORECARD
YOU       : {scorecard['USER']}
COMPUTER  : {scorecard['COMPUTER']}
TIE       : {scorecard['TIE']}
""")

if scorecard["USER"] > scorecard["COMPUTER"]: print("\nCONGARTS! YOU HAVE WON THE GAME!\n")
elif scorecard["USER"] < scorecard["COMPUTER"] : print("\nBAD LUCK THIS TIME! YOU HAVE LOST!\n")
else: 
    print("\nOHH! THATS A TIED GAME!\n")