import logic
import pygame

pygame.init()
pygame.font.init()

TILE_FONT = pygame.font.SysFont('Open Sans ExtraBold', 69)
WIDTH = 1000
HEIGHT = 1000
BACKGROUND_COLOR = (250,248,239)

clock = pygame.time.Clock()
window = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Scuffed 2048")

board = logic.initBoard(3, 3)


def DRAW_WINDOW():
    window.fill(BACKGROUND_COLOR)
    
    for i in range(0, len(board) + 1):
        pygame.draw.line(window, (0, 0, 0), (185, (i*150) + 150), ((150*len(board)) + 185, (i*150) + 150), width=8)

    for i in range(0, len(board[0]) + 1):
        pygame.draw.line(window, (0, 0, 0), ((i*150) + 185, 150), ((i*150) + 185, (150*len(board[0])) + 150), width=8)

    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            window.blit(TILE_FONT.render(str(board[i][j]), True, (0, 0, 0)), ((j*150) + 250, (i*150) + 200))

    pygame.display.flip()

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
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    score += logic.up(board)
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    score += logic.left(board)
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    score += logic.down(board)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    score += logic.right(board)

        if logic.gameOver(board):
            running = False
            return score

        DRAW_WINDOW()

if __name__ == '__main__':
    main()