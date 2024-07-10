"""
This is the main driver file like it is responsible for handling user input and current GameState object 
"""

import pygame as p
import ChessEngine


WIDTH = HEIGHT = 512 
DIMENSION = 8  # 8x8 chess board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animation
IMAGES = {}



def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("data/images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))



"""
The main driver which handles user input and update the graphics
"""
def main():
    p.init() #initialize pygame
    screen = p.display.set_mode((WIDTH, HEIGHT))
    p.display.set_caption('Handless Chess!')
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running= False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()
"""
Responsible for all the graphics
"""
def drawGameState(screen, gs):
    drawBoard(screen)

    drawPieces(screen, gs.board)

"""
To draw the sqaures on the board.
"""
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("light blue")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
"""
To draw the pieces on the board.
"""
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": 
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
        
if __name__ == "__main__":
    main()