class AIPlayer:
    """Logic for decisions made by a computer player."""
    
    def __init__(self, player_num):
        """Initialize a computer player.
        player_num is the computer player number from 1-6
        """
        self.name = "Computer player " + str(player_num)
        self.ward = str(player_num)
        self.budget = 10
        self.happiness = 100
        
    def add_player(self, players):
        """Adds computer player to players, if ward not assigned."""
        try:
            players[self.ward]
        except:
            players[self.ward] = self


if __name__ == "__main__":
    players = dict()
    for player_num in range(1,7):
        new_player = AIPlayer(player_num)
        new_player.add_player(players)
    print(players)
    
