import pygame

pygame.init()
WIDTH = 900
HEIGHT = 750

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Brookxat chess')
timer = pygame.time.Clock()
fps = 60

# game variables
white_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                   (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
black_pieces = ['rook', 'knight', 'bishop', 'king', 'queen', 'bishop', 'knight', 'rook',
                'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                   (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
captured_pieces_white = []
captured_pieces_black = []

selection = 100
valid_moves = []

#load piece images 
for i in white_pieces :
    black_piece = 'black_' + i
    white_piece = 'white_' + i
    globals()[black_piece] = pygame.image.load('assets/images/'+black_piece+'.png')
    globals()[black_piece] = pygame.transform.scale(globals()[black_piece], (80, 80))

    globals()[white_piece] = pygame.image.load('assets/images/'+white_piece+'.png')
    globals()[white_piece] = pygame.transform.scale(globals()[white_piece], (80, 80))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# draw board
def draw_board() :
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, 'light gray', [450 - (column * 150), row * 75, 75, 75])
        else:
            pygame.draw.rect(screen, 'light gray', [525 - (column * 150), row * 75, 75, 75])
        
#main game loop

run = True

while run :
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    # events handling
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :run = False
    pygame.display.flip()
pygame.quit()