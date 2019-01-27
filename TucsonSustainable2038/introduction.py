class Introduction:
    """Print the introduction to the Tucson Sustainable 2038 Game."""
    
    def __init__(self):
        """Initialize the game introduction strings."""
        self.first_paragraph = ("Tucson is a unique place to live.\n"
                                + "The beautiful, yet fragile Sonoran Desert"
                                + " is unlike any other in the world.\n"
                                + "Climate change poses many challenges to"
                                + " life in Tucson:\n"
                                + "* Water shortages.\n"
                                + "* Food shortages.\n"
                                + "* Extreme heat events.\n"
                                + "* Floods.\n"
                                + "* Habitat loss.\n")
        self.second_paragraph = ("As a member of the Tucson City Council,"
                                 + " can you invest in a sustainable future?\n"
                                 + "Your constituents will be unhappy about"
                                 + " how much they pay in taxes.\n"
                                 + "But they will also be unhappy about"
                                 + " crises that could have been avoided.\n"
                                 + "You will need to find a balance.\n"
                                 + "Good luck, council member!\n")
        
    def show_intro(self):
        print(self.first_paragraph)
        print(self.second_paragraph)


if __name__ == "__main__":
    intro = Introduction()
    intro.show_intro()