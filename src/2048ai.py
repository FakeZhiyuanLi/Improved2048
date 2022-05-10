import logic
import pygame
import copy
import random

pygame.init()
pygame.font.init()

TILE_FONT = pygame.font.SysFont('Open Sans ExtraBold', 69)
WIDTH = 1000
HEIGHT = 1000
BACKGROUND_COLOR = (250,248,239)

clock = pygame.time.Clock()
window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Scuffed 2048")

board = logic.initBoard(4, 4)

def findMove(board):
    dummy_board = copy.deepcopy(board)
    max_score = 0
    # 0=up, 1=right, 2=down, 3=left
    direction = random.randint(0, 3)

    # up
    temp_score = logic.up(dummy_board)
    
    if temp_score > max_score:
        max_score = temp_score
        direction = 0

    dummy_board = copy.deepcopy(board)

    # right
    temp_score = logic.right(dummy_board)
    
    if temp_score > max_score:
        max_score = temp_score
        direction = 1

    dummy_board = copy.deepcopy(board)

    # down
    temp_score = logic.down(dummy_board)
    
    if temp_score > max_score:
        max_score = temp_score
        direction = 2

    dummy_board = copy.deepcopy(board)

    # left
    temp_score = logic.left(dummy_board)
    
    if temp_score > max_score:
        max_score = temp_score
        direction = 3

    return direction

    



def DRAW_WINDOW():
    window.fill(BACKGROUND_COLOR)
    
    for i in range(0, len(board) + 1):
        pygame.draw.line(window, (0, 0, 0), (185, (i*150) + 150), (785, (i*150) + 150), width=8)

    for i in range(0, len(board[0]) + 1):
        pygame.draw.line(window, (0, 0, 0), ((i*150) + 185, 150), ((i*150) + 185, 750), width=8)

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            window.blit(TILE_FONT.render(str(board[j][i]), True, (0, 0, 0)), ((i*150) + 250, (j*150) + 200))

    pygame.display.update()

def main():
    running = True

    logic.addTile(board)
    logic.addTile(board)
    
    score = 0

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return score

        if logic.gameOver(board):
            running = False
            return score

        direction = findMove(board)

        if direction == 0:
            score += logic.up(board)
        elif direction == 1:
            score += logic.right(board)
        elif direction == 2:
            score += logic.down(board)
        elif direction == 3:
            score += logic.left(board)
    

        DRAW_WINDOW()

if __name__ == '__main__':
    print(main())