class Player:
    """Manages all aspects related to the player of the game."""
    
    def __init__(self):
        self.name = ""
        self.ward = ""
        self.budget = 10
        self.happiness = 100
        
    def choose_ward(self, players):
        """Player chooses name and ward for game."""
        self.name = input("What is your name, council member? ")
        print()
        print("The City of Tucson has six wards:\n"
              + "   Ward 1 covers the NW part of Tucson.\n"
              + "   Ward 2 covers the NE part of Tucson.\n"
              + "   Ward 3 covers the N Central part of Tucson.\n"
              + "   Ward 4 covers the SE part of Tucson.\n"
              + "   Ward 5 covers the SW part of Tucson.\n"
              + "   Ward 6 covers the S Central part of Tucson.\n")
        valid_input = False
        while not valid_input:
            self.ward = input("Which ward would you like to represent, "
                              + self.name + "? (1-6) ")
            if 1 <= int(self.ward) <= 6:
                valid_input = True
            else:
                print("The ward number must be between 1 and 6.\n"
                      + "Please try again!")
        players[self.ward] = self
        
if __name__ == "__main__":
    test_player = Player()
    players = dict()
    test_player.choose_ward(players)
    print(players)
    