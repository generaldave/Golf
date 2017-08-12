################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# App class: App initializer                                                   #
#                                                                              #
# Created on 2016-12-29                                                        #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              IMPORT STATEMENTS                               #
#                                                                              #
################################################################################

from   .Constants import *   # Constants file
import pygame                # For GUI

################################################################################
#                                                                              #
#                                   APP CLASS                                  #
#                                                                              #
################################################################################

class App(object):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, appDirectory: str) -> None:
        self.appDirectory = appDirectory

        # Set up GUI
        self.setupGUI()

        # Run app
        self.runApp()

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Mehtod sets up GUI
    def setupGUI(self) -> None:
        # Screen attributes
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RESOLUTION)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()      # For frames per second
        self.mouse = pygame.mouse.get_pos()   # For mouse position

        self.background = pygame.image.load(self.appDirectory + "/images/golf2.png")
        self.test_card = pygame.image.load(self.appDirectory + "/images/joker.png")
        self.joker2 = pygame.image.load(self.appDirectory + "/images/joker2.png")
        self.back_vertical = pygame.image.load(self.appDirectory + "/images/back_vertical.png")
        self.back_horizontal = pygame.image.load(self.appDirectory + "/images/back_horizontal.png")
    # Method runs app
    def runApp(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                
                # Handle quit event
                if event.type == pygame.QUIT:
                    running = False

            self.screen.blit(self.background, ORIGIN)

            # Player 1
            self.screen.blit(self.back_horizontal, (20, 90))
            self.screen.blit(self.back_horizontal, (155, 90))
            self.screen.blit(self.test_card, (20, 190))
            self.screen.blit(self.test_card, (155, 190))
            self.screen.blit(self.back_horizontal, (20, 290))
            self.screen.blit(self.back_horizontal, (155, 290))

            # Player 2
            self.screen.blit(self.back_horizontal, (520, 90))
            self.screen.blit(self.back_horizontal, (655, 90))
            self.screen.blit(self.test_card, (520, 190))
            self.screen.blit(self.test_card, (655, 190))
            self.screen.blit(self.back_horizontal, (520, 290))
            self.screen.blit(self.back_horizontal, (655, 290))

            # Middle Cards
            self.screen.blit(self.joker2, (307, 180))
            self.screen.blit(self.back_vertical, (402, 180))

            # Update Screen
            pygame.display.update()
            self.clock.tick(FPS)            

        # Close app cleanly
        pygame.quit()
