import pygame

pygame.init()
WIDTH = 900
HEIGHT = 750
font = pygame.font.SysFont('Arial', 40)
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

turn_step = 0
selection = 100
valid_moves = []

#load piece images 
for i in white_pieces :
    black_piece = 'black_' + i
    white_piece = 'white_' + i
    globals()[black_piece] = pygame.image.load('assets/images/'+black_piece+'.png')
    globals()[black_piece] = pygame.transform.scale(globals()[black_piece], (60, 60))

    globals()[white_piece] = pygame.image.load('assets/images/'+white_piece+'.png')
    globals()[white_piece] = pygame.transform.scale(globals()[white_piece], (60, 60))

white_images = [white_pawn, white_queen, white_king, white_knight, white_rook, white_bishop]
black_images = [black_pawn, black_queen, black_king, black_knight, black_rook, black_bishop]
piece_list = ['pawn', 'queen', 'king', 'knight', 'rook', 'bishop']

# draw board
def draw_board() :
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen, '#5E1914', [450 - (column * 150), row * 75, 75, 75])
        else:
            pygame.draw.rect(screen, '#5E1914', [525 - (column * 150), row * 75, 75, 75])
        pygame.draw.rect(screen, 'gray', [0, 600, WIDTH, 150])
        pygame.draw.rect(screen, 'red', [0, 600, WIDTH, 150], 5)
        pygame.draw.rect(screen, 'red', [600, 0, 300, HEIGHT], 5)
        status_text = ['White: Select a Piece to Move!', 'White: Select a Destination!',
                       'Black: Select a Piece to Move!', 'Black: Select a Destination!']
        screen.blit(font.render(status_text[turn_step],True,'black'),(20,650))
        for i in range(9):
            pygame.draw.line(screen, 'black', (0, 75 * i), (600, 75 * i), 2)
            pygame.draw.line(screen, 'black', (75 * i, 0), (75 * i, 600), 2)
        screen.blit(font.render('FORFEIT', True, 'black'), (810, 830))
    
def draw_pieces():
    for i in range(len(white_pieces)):
        index = piece_list.index(white_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(white_pawn, (white_locations[i][0] * 75 + 10, white_locations[i][1] * 75 + 10))
        else:
            screen.blit(white_images[index], (white_locations[i][0] * 75 + 10, white_locations[i][1] * 75 + 10))
        if turn_step < 2:
            if selection == i:
                pygame.draw.rect(screen, 'green', [white_locations[i][0] * 75 + 1, white_locations[i][1] * 75 + 1,
                                                 75, 75], 2)
    for i in range(len(black_pieces)):
        index = piece_list.index(black_pieces[i])
        if white_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 75 + 10, black_locations[i][1] * 75 + 10))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 75 + 10, black_locations[i][1] * 75 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 75 + 1, black_locations[i][1] * 75 + 1,
                                                 75, 75], 2)

#check valid moves for all pieces
def check_option():
    pass

#main game loop

run = True

while run :
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    # events handling
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
            x_click = event.pos[0]//75
            y_click = event.pos[1]//75
            click_cords = (x_click,y_click)
            #white turn 
            if turn_step <= 1 :
                if click_cords in white_locations :
                    selection = white_locations.index(click_cords)
                    if turn_step == 0 : turn_step = 1
                if click_cords in valid_moves and selection != 100 :
                    white_locations[selection] = click_cords 
                    if click_cords in black_locations :
                        taken_black_piece = black_locations.index(click_cords)
                        captured_pieces_white.append(black_piece[taken_black_piece])
                        black_piece.pop(taken_black_piece)
                        black_piece.pop(taken_black_piece)
            
            #black turn 
            if turn_step > 1 :
                if click_cords in black_locations :
                    selection = black_locations.index(click_cords)
                    if turn_step == 2 : turn_step = 3
                if click_cords in valid_moves and selection != 100 :
                    black_locations[selection] = click_cords 
                    if click_cords in white_locations :
                        taken_white_piece = white_locations.index(click_cords)
                        captured_pieces_black.append(white_piece[taken_white_piece])
                        white_piece.pop(taken_white_piece)
                        white_piece.pop(taken_white_piece)
                        



                        


    pygame.display.flip()
pygame.quit()