from pkn_helper import roll, wait, loading, spell, pkn_scenarios

def pkn(pkn_list : list):

    while True:
        wait(1)
        spell("Your choose: ", is_end=False)
        pkn_user = input()
        wait(1)
        # Validate user input
        if pkn_user not in pkn_list:
            spell("Wrong input, try again [rock, paper, scissors]")
            wait(1)
            continue

        pkn_cpu = roll(pkn_list)
        spell("Cpu choose: ", pkn_cpu)
        wait(1)
        spell("Calculating all possibilities ", )
        loading()

        if pkn_user == pkn_cpu:
            spell("\rDraw")
            continue
        elif pkn_scenarios()[pkn_user] == pkn_cpu:
            spell("\rWin")
        else:
            spell("\rLose")
        wait(1)
        
        break