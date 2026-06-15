from rps_helper import wait, roll

rps = ["rock","paper","scissors"]

# immersion purpose
print("ROCK PAPER SCISSORS\nLOADING THE GAME", end=" ")
for dot in range(5):
    wait(1)
    print(".", end="")
print("")
print("STARTING THE GAME")
wait(1)
 
pkn_cpu = roll(rps)

while True:
    pkn_user = input("Your choose: ")
    wait(1)
    if pkn_user in rps:
        print(f"Cpu: {pkn_cpu}")
        wait(1)
        if pkn_user == pkn_cpu:
            print("Draw")
            pkn_cpu = roll(rps)
            continue
        elif pkn_user == "rock":
            if pkn_cpu == "paper":
                print("Lose")
            else: print("Win")
        elif pkn_user == "paper":
            if pkn_cpu == "scissors":
                print("Lose")
            else: print("Win")
        elif pkn_user == "scissors":
            if pkn_cpu == "rock":
                print("Lose")
            else: print("Win")
        wait(1)
        print("Game finished.")
        break
    else: 
        print("Wrong input, try again [rock][paper][scissors]")
        continue    
