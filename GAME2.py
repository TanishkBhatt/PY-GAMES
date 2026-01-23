# COUNTRY GUESSING GAME BY HINTS USING PYTHON
import random

countries = ["INDIA", "CHINA", "AMERICA", "AUSTRALIA", "ENGLAND", "ITALY", "PAKISTAN", "NEW ZEALAND", "SRI LANKA", "SOUTH AFRICA", "BANGLADESH", "AFGANISTAN", "BRAZIL", "FRANCE", "SPAIN", "CANADA", "ARGENTINA", "PORTUGAL", "RUSSIA", "MEXICO"]

country = random.choice(countries)

print("\n---------------------------------COUNTRY GUESSING GAME USING HINTS---------------------------------")
attempts = 1

while attempts <= 5:
    guess = input("\nENTER YOUR GUESS : ").upper()
    if guess == country:
        print(f"BRILLIANT! THATS CORRECT!\nYOU HAVE WON THE GAME IN {attempts} ATTEMPTS!\n")
        break
    else :
        hint = ""
        for i, j in zip(guess, country):
            if i == j:  hint += i
            else : hint += "_"

        hint += "_" * (len(country) - len(hint))

        
        print("NO THATS NOT CORRECT!")
        print(f"HINT : {hint}")

    attempts += 1

else:
    print(f"\nYOUR ATTEMPTS HAVE BEEN COMPLETED!")
    print(f"THE COUNTRY WAS : \'{country}\'\n")