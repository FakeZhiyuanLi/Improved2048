import logic
import pygame

pygame.init()
pygame.font.init()

TILE_FONT = pygame.font.SysFont('Open Sans ExtraBold', 40)
WIDTH = 1000
HEIGHT = 1000
BACKGROUND_COLOR = (250,248,239)

clock = pygame.time.Clock()
window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Scuffed 2048")

board = logic.initBoard(4, 4)

def DRAW_WINDOW():
    window.fill(BACKGROUND_COLOR)

    pygame.display.update()

def main():
    running = True

    logic.addTile(board)
    logic.addTile(board)
    
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    logic.up(board)
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    logic.left(board)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    logic.down(board)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    logic.right(board)
        for row in board:
            print(row)
        print()
        DRAW_WINDOW()

if __name__ == '__main__':
    main()