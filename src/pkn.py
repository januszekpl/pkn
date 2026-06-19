from pkn_helper import roll, wait, print_loading_dots, spell

def pkn(pkn_list : list):

    while True:
        pkn_cpu = roll(pkn_list)
        spell("\nYour choose: ")
        pkn_user = input(str())
        wait(1)

        # Validate user input
        if pkn_user not in pkn_list:
            print("Wrong input, try again [rock][paper][scissors]")
            wait(1)
            continue

        spell("Cpu choose: ", pkn_cpu)
        wait(1)
        spell("\nCalculating all possibilities")
        print_loading_dots()

        # Draw
        if pkn_user == pkn_cpu:
            spell("Draw")
            pkn_cpu = roll(pkn_list)
            continue

        # Win/Lose scenarios
        elif pkn_user == "rock":
            if pkn_cpu == "paper":
                spell("Lose")
            else: spell("Win")
        elif pkn_user == "paper":
            if pkn_cpu == "scissors":
                spell("Lose")
            else: spell("Win")
        elif pkn_user == "scissors":
            if pkn_cpu == "rock":
                spell("Lose")
            else: spell("Win")
        wait(1)
        print("")
        break