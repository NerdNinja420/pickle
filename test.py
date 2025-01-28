import pygame


font = [font for font in pygame.font.get_fonts() if font == "jetbrainsmononlnfsemibold"]
print(True if "☹" in font else False)
