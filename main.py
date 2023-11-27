import pygame, sys
from classes.player import Player
from classes.gui import GUI
from classes.plant.plant import Plant

#COSTINANTS
WIDTH = 800
HIGH = 600

if __name__ == "__main__":
    gui = GUI(
        width=WIDTH, 
        height=HIGH
    )

    gui.run_game()
