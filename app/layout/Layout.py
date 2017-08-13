################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# Layout class: Card Layout                                                    #
#                                                                              #
# Created on 2017-8-12                                                         #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              IMPORT STATEMENTS                               #
#                                                                              #
################################################################################

import pygame # For GUI

################################################################################
#                                                                              #
#                                 LAYOUT CLASS                                 #
#                                                                              #
################################################################################

class Layout(object):
    screenHint = "screen object"

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, appDirectory: str, screen : screenHint) -> None:
        self.image_directory = appDirectory + "/images/"
        self.screen = screen
        self.card_back = pygame.image.load(self.image_directory + "back.png")
        self.setupGUI()

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Mehtod sets up GUI
    def setupGUI(self) -> None:
        self.rotated = pygame.transform.rotate(self.card_back, -90)
        # Player 1
        self.screen.blit(self.rotated, (20, 90))
        self.screen.blit(self.rotated, (155, 90))
        self.screen.blit(self.rotated, (20, 190))
        self.screen.blit(self.rotated, (155, 190))
        self.screen.blit(self.rotated, (20, 290))
        self.screen.blit(self.rotated, (155, 290))

        # Player 2
        self.screen.blit(self.rotated, (520, 90))
        self.screen.blit(self.rotated, (655, 90))
        self.screen.blit(self.rotated, (520, 190))
        self.screen.blit(self.rotated, (655, 190))
        self.screen.blit(self.rotated, (520, 290))
        self.screen.blit(self.rotated, (655, 290))

        # Middle Cards
        self.screen.blit(self.card_back, (307, 180))
        self.screen.blit(self.card_back, (402, 180))

    # Method updates game layout
    def update(self) -> None:
        self.setupGUI()
