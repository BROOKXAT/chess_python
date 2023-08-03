import pygame
from PIL import Image

pygame.init()
WIDTH = 900
HEIGHT = 750
font = pygame.font.SysFont('Arial', 40)
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Brookxat chess')
timer = pygame.time.Clock()
fps = 60
game_moves = []
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
    globals()[black_piece] = Image.open('assets/images/'+black_piece+'.png')
    globals()[black_piece] = globals()[black_piece].resize((60,60))
    globals()[black_piece] = pygame.image.fromstring(globals()[black_piece].tobytes(), globals()[black_piece].size, globals()[black_piece].mode)

    globals()[white_piece] = Image.open('assets/images/'+white_piece+'.png')
    globals()[white_piece] = globals()[white_piece].resize((60,60))
    globals()[white_piece] = pygame.image.fromstring(globals()[white_piece].tobytes(), globals()[white_piece].size, globals()[white_piece].mode)

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
        if black_pieces[i] == 'pawn':
            screen.blit(black_pawn, (black_locations[i][0] * 75 + 10, black_locations[i][1] * 75 + 10))
        else:
            screen.blit(black_images[index], (black_locations[i][0] * 75 + 10, black_locations[i][1] * 75 + 10))
        if turn_step >= 2:
            if selection == i:
                pygame.draw.rect(screen, 'blue', [black_locations[i][0] * 75 + 1, black_locations[i][1] * 75 + 1,
                                                 75, 75], 2)
#check if ur king is in check 
def is_check():
    pass
#check if the move doesnt put ur king in a check (illegal move)
def is_illegal(piece,move,color) :
    pass
#check valid moves for all pieces

def check_options(pieces,locations,turn):
    one_piece_moves = []
    all_moves = []
    for i,j in enumerate(pieces) :
        location = locations[i]
        piece = pieces[i]
        
        if piece == "pawn" : 
            
            one_piece_moves = check_pawn(location,turn)
        if piece == "rook" :
            
            one_piece_moves = check_rook(location,turn)
        if piece == "knight" : one_piece_moves = check_knight(location,turn)
        if piece == "bishop" : one_piece_moves = check_bishop(location,turn)
        if piece == "queen" : one_piece_moves = check_queen(location,turn)
        if piece == "king" : one_piece_moves = check_king(location,turn)
        all_moves.append(one_piece_moves)
    return all_moves
#check moves for each piece .
def check_pawn(position,color) :
    moves = []
    if color == "white" :
        # moving 1 square
        if (position[0],position[1]+1) not in white_locations and (position[0],position[1]+1) not in black_locations and position[1]<7 :
            moves.append((position[0],position[1]+1))
        # moving 2 squares
        if  (position[0],position[1]+1) not in white_locations and (position[0],position[1]+2) not in white_locations and (position[0],position[1]+2) not in black_locations and position[1] == 1 :
            moves.append((position[0],position[1]+2))
        # capture on the right
        if (position[0]+1,position[1]+1) in black_locations :
            moves.append((position[0]+1,position[1]+1))
        # capture on the left
        if (position[0]-1,position[1]+1) in black_locations :
            moves.append((position[0]-1,position[1]+1))
        #en passant
        if position[1] == 4 : 
            print("here")
            player,moved_piece,move = game_moves[-1]
            if moved_piece == "pawn" :
                
                print("here 1")
                start_pos,end_pos = move
                print(game_moves)
                if start_pos[1] == 6 and end_pos[1] == 4 and (end_pos[0] == position[0]+1 or end_pos[0] == position[0]-1) :
                    print("here 2")
                    moves.append((end_pos[0],5))

    
    if color == "black" :
        # moving one square
        if (position[0],position[1]-1) not in white_locations and (position[0],position[1]-1) not in black_locations and position[1] > 0 :
            moves.append((position[0],position[1]-1))
        #moving 2 square
        if (position[0],position[1]-2) not in white_locations and (position[0],position[1]-2) not in black_locations and position[1] == 6 :
            moves.append((position[0],position[1]-2))
        #capture on the right
        if (position[0]+1,position[1]-1) in white_locations :
            moves.append((position[0]+1,position[1]-1))
        if (position[0]-1,position[1]-1) in white_locations :
            moves.append((position[0]-1,position[1]-1))
        #en passant
        if position[1] == 3 : 
            player,moved_piece,move = game_moves[-1]
            if moved_piece == "pawn" :
                
                start_pos,end_pos = move
                if start_pos[1] == 1 and end_pos[1] == 3 and (end_pos[0] == position[0]+1 or end_pos[0] == position[0]-1) :
                    moves.append((end_pos[0],2))
    return moves
def check_rook(position, color):
    moves = []
    if color == "white" :
        enemy = black_locations
        friend = white_locations
    else :
        enemy = white_locations
        friend = black_locations
    for i in range(4) :
        path = True
        chain = 1
        # vertical movement
        if i == 0 :
            x = 0
            y = 1
        if i == 1 :
            x = 0
            y = -1
        # horizontal movement
        if i == 2 :
            x = 1 
            y = 0
        if i == 3 :
            x = -1
            y = 0
        
        while path :

            if (position[0] + chain*x, position[1]+ chain*y) not in friend and 0<= position[0]+chain*x <8 and 0 <= position[1]+ chain*y < 8 :
                moves.append((position[0] + chain*x, position[1]+ chain*y))
                if (position[0] + chain*x, position[1]+ chain*y) in enemy:
                    path = False
                chain += 1
            else : path = False
    return moves

        


def check_knight(position , color):
    moves = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in friends_list and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves.append(target)
    return moves

def check_bishop(position , color) :
    moves = []
    if color == 'white':
        enemies_list = black_locations
        friends_list = white_locations
    else:
        friends_list = black_locations
        enemies_list = white_locations
    for i in range(4) :
        if i == 0 :
            x,y = 1,1
        if i == 1 :
            x,y = 1,-1
        if i == 2 :
            x,y = -1,1
        if  i == 3 :
            x,y = -1,-1
        path = True
        chain = 1
        while path :
            if (position[0]+chain*x,position[1]+chain*y) not in friends_list and  0 <= position[0]+chain*x < 8 and 0 <= position[1]+chain*y< 8 :
                moves.append((position[0]+chain*x,position[1]+chain*y))
                if (position[0]+chain*x,position[1]+chain*y) in enemies_list : path = False
                chain += 1
            else : path = False
    return moves
def check_queen(position , color) :
    return check_bishop(position,color)+check_rook(position,color)
    
def check_king(position , color):
    moves = []
    if color == 'white':
        friends_list = white_locations
    else:
        friends_list = black_locations
    targets = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for i in targets :
        if (position[0]+i[0],position[1]+i[1]) not in friends_list and 0 <= position[0]+i[0] < 8 and 0 <= position[1]+i[1] < 8 :
            moves.append((position[0]+i[0],position[1]+i[1]) )
    return moves

        
# check balid moves for seleced piece
def check_valid_moves():
    if turn_step < 2:
        options_list = white_options
    else:
        options_list = black_options
    valid_options = options_list[selection]
    return valid_options       

# draw valid moves on screen
def draw_valid(moves):
    if turn_step < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(moves)):
        pygame.draw.circle(screen, color, (moves[i][0] * 75 + 37.5, moves[i][1] * 75 + 37.5), 5)

#main game loop

run = True
black_options = check_options(black_pieces, black_locations, 'black')
white_options = check_options(white_pieces, white_locations, 'white')

while run :
    timer.tick(fps)
    screen.fill('dark gray')
    draw_board()
    draw_pieces()
    if selection != 100:
        valid_moves = check_valid_moves()
        draw_valid(valid_moves)
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
                    #to keep track of the move played in thee game (player,the moved piece, (from , to))
                    game_moves.append(("white",white_pieces[selection],(white_locations[selection],click_cords)))
                    white_locations[selection] = click_cords
                    en_passant_capture = (click_cords[0], click_cords[1] - 1)
                    # en passant carture
                    if white_pieces[selection] == "pawn" and en_passant_capture in black_locations and click_cords not in black_locations:
                        taken_black_piece = black_locations.index(en_passant_capture)
                        captured_pieces_white.append(black_pieces[taken_black_piece])
                        black_pieces.pop(taken_black_piece)
                        black_locations.pop(taken_black_piece)
                    if click_cords in black_locations  :
                        taken_black_piece = black_locations.index(click_cords)
                        captured_pieces_white.append(black_pieces[taken_black_piece])
                        black_pieces.pop(taken_black_piece)
                        black_locations.pop(taken_black_piece)
                
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            
            #black turn 
            if turn_step > 1 :
                if click_cords in black_locations :
                    selection = black_locations.index(click_cords)
                    if turn_step == 2 : turn_step = 3
                if click_cords in valid_moves and selection != 100 :
                    game_moves.append(("black",black_pieces[selection],(black_locations[selection],click_cords)))
                    black_locations[selection] = click_cords 
                    en_passant_capture = (click_cords[0], click_cords[1] + 1)
                    # en passant carture
                    if black_pieces[selection] == "pawn" and en_passant_capture in white_locations and click_cords not in white_locations:
                        taken_white_piece = white_locations.index(en_passant_capture)
                        captured_pieces_black.append(white_pieces[taken_white_piece])
                        white_pieces.pop(taken_white_piece)
                        white_locations.pop(taken_white_piece)
                    if click_cords in white_locations :
                        taken_white_piece = white_locations.index(click_cords)
                        captured_pieces_black.append(white_pieces[taken_white_piece])
                        white_pieces.pop(taken_white_piece)
                        white_locations.pop(taken_white_piece)
                    black_options = check_options(black_pieces, black_locations, 'black')
                    white_options = check_options(white_pieces, white_locations, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
            
    
    




                        


    pygame.display.flip()
pygame.quit()