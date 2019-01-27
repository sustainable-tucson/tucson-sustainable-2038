import introduction
import instructions
import player
import aiplayer
import projects
import climateevents

class TucsonSustainable2038Game:
    """The manager for the Tucson Sustainable 2038 game."""
    
    def __init__(self):
        self.players = dict()
    
    def play_game(self):
        intro = introduction.Introduction()
        intro.show_intro()
        instruct = instructions.Instructions()
        instruct.show_instructions()
        human = player.Player()
        human.choose_ward(self.players)
        for player_num in range(1,7):
            ai_player = aiplayer.AIPlayer(player_num)
            ai_player.add_player(self.players)
        print(self.players)
    
    
if __name__ == "__main__":
    game = TucsonSustainable2038Game()
    game.play_game()