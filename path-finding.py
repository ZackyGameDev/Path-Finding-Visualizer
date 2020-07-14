import pygame, random, queue

# Initializing graphics
pygame.init()
win = pygame.display.set_mode((1280, 720))
surface_size = (256, 144)
display = pygame.Surface((surface_size))
clock = pygame.time.Clock()

# Variables
running = True # Just a smol var i use to close the game
mouse_left_button_down = False
mouse_right_button_down = False
tile_size = 8 # I RECOMMEND NOT CHANGING THIS VALUE AS IM NOT SURE WHAT MIGHT END UP HAPPENNING BY DOING SO
fps = 42069 # As high as possible in the start. i dont care about consistency.
surf_x = 0
surf_y = 0
xscroll = 0
yscroll = 0
scrollsp = 2 # Set this to negative to inverse scrolling controls

# Tilemap
tilemap = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
current_tile = list()
tilemap_key_file = dict()
'''{
    'H' : pygame.image.load('sprites/wall.png'),
    'O' : pygame.image.load('sprites/player.png'),
    'X' : pygame.image.load('sprites/target.png')
}'''

def draw_map_from_array(two_dimensional_array, key_file_dict:dict, display_to_draw_to, xpos=0, ypos=0, tile_size=tile_size):
    '''
    two_dimensional_array: This is the 2D array which holds your entire map
    key_file_dict: dictionary that mentions which value in the 2D Array map corrosponds to which image to draw.
    '''
    ty = 0
    for row in two_dimensional_array:
        tx = 0
        for tile in row:
            if tile == 'H':
                pygame.draw.rect(display_to_draw_to, (255, 255, 255), pygame.Rect(
                    (tx*tile_size)+xpos,
                    (ty*tile_size)+ypos,
                    tile_size,
                    tile_size
                ))
            #if tile in key_file_dict:
                #display_to_draw_to.blit(key_file_dict[tile], ((tx*tile_size)+xpos, (ty*tile_size)+ypos))
            tx += 1
        ty += 1

def add_tile_to_tilemap(two_dimensional_array:list, value_to_insert, xpos_in_array, ypos_in_array):
    
    # Extending the Array to the point at which it can atleast hold the tile
    while len(two_dimensional_array) <= ypos_in_array:
        two_dimensional_array.append(list())
    while len(two_dimensional_array[ypos_in_array]) <= xpos_in_array:
        two_dimensional_array[ypos_in_array].append(' ')
    
    two_dimensional_array[ypos_in_array][xpos_in_array] = value_to_insert

def get_2d_array_len(array):
    xlen = 0
    for row in array:
        if len(row) > xlen: xlen = len(row)
    ylen = len(array)
    
    return (xlen, ylen)
        

# Main Graphics Loop
while running:
    clock.tick(fps)
    
    # Calculating the position of the tiles
    mx, my = pygame.mouse.get_pos()
    tx, ty = int(round((mx-surf_x)/5)), int(round((my-surf_y)/5))
    
    while tx % tile_size != 0:
        tx -= 1
    while ty % tile_size != 0:
        ty -= 1
    
    # Clearing the screen
    win.fill((0, 0, 0))
    display.fill((0, 0, 50))
    
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_left_button_down = True
            elif event.button == 3:
                mouse_right_button_down = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_left_button_down = False
            elif event.button == 3:
                mouse_right_button_down = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP : yscroll = scrollsp
            elif event.key == pygame.K_DOWN : yscroll = -scrollsp
            elif event.key == pygame.K_LEFT : xscroll = scrollsp
            elif event.key == pygame.K_RIGHT : xscroll = -scrollsp
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP : yscroll = 0
            elif event.key == pygame.K_DOWN : yscroll = 0
            elif event.key == pygame.K_LEFT : xscroll = 0
            elif event.key == pygame.K_RIGHT : xscroll = 0
    
    # Scroll
    surf_x += xscroll
    surf_y += yscroll
    
    # Acting on input
    if not tx < 1 and not ty < 1:
        if mouse_left_button_down:
            add_tile_to_tilemap(tilemap, 'H', int(round(tx/tile_size)), int(round(ty/tile_size)))
        if mouse_right_button_down:
            add_tile_to_tilemap(tilemap, ' ', int(round(tx/tile_size)), int(round(ty/tile_size)))
    
        # Drawing tile at the current position
        pygame.draw.rect(display, (250, 255, 250), pygame.Rect(
            tx,
            ty,
            tile_size,
            tile_size
        ))
    
    # Drawing the boundaries
    for line in [
        {'start':(0, 0), 'end':((get_2d_array_len(tilemap)[0])*tile_size, 0)},
        {'start':((get_2d_array_len(tilemap)[0])*tile_size, 0), 'end':((get_2d_array_len(tilemap)[0])*tile_size, (len(tilemap))*tile_size)},
        {'start':((get_2d_array_len(tilemap)[0])*tile_size, (len(tilemap))*tile_size), 'end':(0, (len(tilemap))*tile_size)},
        {'start':(0, (len(tilemap))*tile_size), 'end':(0, 0)}
    ]:
        pygame.draw.line(display, (200, 200, 200), line['start'], line['end'])
    
    # Updating the display
    draw_map_from_array(tilemap, tilemap_key_file, display)
    win.blit(pygame.transform.scale(display, (1280, 720)), (surf_x, surf_y))
    pygame.display.update()