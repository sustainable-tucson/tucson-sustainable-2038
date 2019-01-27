class Instructions:
    """Display instructions for playing the game."""
    
    def __init__(self):
        self.instructions = ("The game lasts for 20 turns.\n"
                             + "Each turn equals one year from 2019 to 2038.\n"
                             + "For each turn, you can choose from a list"
                             + " of projects.\n"
                             + "You can implement as many projects as"
                             + " your budget allows.\n"
                             + "The amount of your budget is determined each"
                             +  " year by the happiness of your constituents.\n"
                             + "(They vote for the taxes and bonds to pay for"
                             + " the projects.)\n"
                             + "The player with the happiest constituents at the"
                             + " end of the game is the winner!\n")
        
    def show_instructions(self):
        reply = input("Would you like instructions? (Y/n): ")
        print()
        if reply.lower() != 'n':
            print(self.instructions)
            
            
if __name__ == "__main__":
    instruct = Instructions()
    instruct.show_instructions()
    