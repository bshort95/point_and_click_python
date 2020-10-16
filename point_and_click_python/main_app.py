import pygame, sys, random
from keypad import Keypad






# init stuff
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((500,500))

# sound and music
background_music = pygame.mixer.music.load("assets/backg.mp3")
beep_sound = pygame.mixer.Sound("assets/beep.wav")
door_open_sound = pygame.mixer.Sound("assets/door_open.wav")
drawer_sound = pygame.mixer.Sound("assets/drawer.wav")
poster_sound = pygame.mixer.Sound("assets/poster.wav")
wall_breaker_sound = pygame.mixer.Sound("assets/wall_breaker.wav")
locker_sound = pygame.mixer.Sound("assets/locker.wav")
pygame.mixer.music.play(-1)

#images and clickbox being loaded into the program

# wall 1-----------------------------------------------------------

wall_1 = pygame.image.load("assets\wall1.png").convert()
wall_1_open = pygame.image.load("assets\wall1_open.png").convert()

exit_door_cb = pygame.image.load("assets\exit_door_cb.png").convert()
exit_door_cb_rect = exit_door_cb.get_rect(center = (250,250))

win_wall = pygame.image.load("assets\win_screen.png").convert()

# wall 2-----------------------------------------------------------

wall_2 = pygame.image.load("assets\wall2.png").convert()
wall_2_o = pygame.image.load("assets\wall2_open.png").convert()

door_room2 = pygame.image.load("assets\open_door.png").convert()
door_room2_rect = door_room2.get_rect(center = (200,280)) 

# wall 3-----------------------------------------------------------

wall_3 = pygame.image.load("assets\wall3.png").convert()
wall_3_o = pygame.image.load("assets\wall3_open.png").convert()

pin_pad_base = pygame.image.load("assets\pinpad_base.png").convert()

pin_pad_base1 = pygame.image.load("assets\pinpad_base_1.png").convert()
pin_pad_base2 = pygame.image.load("assets\pinpad_base_2.png").convert()
pin_pad_base3 = pygame.image.load("assets\pinpad_base_3.png").convert()
pin_pad_base4 = pygame.image.load("assets\pinpad_base_4.png").convert()

pin_pad_correct = pygame.image.load("assets\pinpad_base_correct.png").convert()
pin_pad_incorrect = pygame.image.load("assets\pinpad_base_incorrect.png").convert()

key_pad_key1 = pygame.image.load("assets\key_pad_key1.png").convert()
key_pad_key1_rect =key_pad_key1.get_rect(center = (160, 180))
key_pad_key2 = pygame.image.load("assets\key_pad_key2.png").convert()
key_pad_key2_rect =key_pad_key2.get_rect(center = (250, 180))
key_pad_key3 = pygame.image.load("assets\key_pad_key3.png").convert()
key_pad_key3_rect =key_pad_key3.get_rect(center = (340, 180))
key_pad_key4 = pygame.image.load("assets\key_pad_key4.png").convert()
key_pad_key4_rect =key_pad_key4.get_rect(center = (160,250))
key_pad_key5 = pygame.image.load("assets\key_pad_key5.png").convert()
key_pad_key5_rect =key_pad_key5.get_rect(center = (250,250))
key_pad_key6 = pygame.image.load("assets\key_pad_key6.png").convert()
key_pad_key6_rect =key_pad_key6.get_rect(center = (340,250))
key_pad_key7 = pygame.image.load("assets\key_pad_key7.png").convert()
key_pad_key7_rect =key_pad_key7.get_rect(center = (160,320))
key_pad_key8 = pygame.image.load("assets\key_pad_key8.png").convert()
key_pad_key8_rect =key_pad_key8.get_rect(center = (250,320))
key_pad_key9 = pygame.image.load("assets\key_pad_key9.png").convert()
key_pad_key9_rect =key_pad_key9.get_rect(center = (340,320))
key_pad_key0 = pygame.image.load("assets\key_pad_key0.png").convert()
key_pad_key0_rect =key_pad_key0.get_rect(center = (250,390))

key_pad_cb = pygame.image.load("assets\key_pad_click_box.png").convert()
key_pad_cb_rect = key_pad_cb.get_rect(center = (370,170))

#wall 3 camera------------------------------------------------------

camera_base = pygame.image.load("assets\camera_base.png").convert()
camera_base_full = pygame.image.load("assets\camera_base_full.png").convert()

camera_click_box = pygame.image.load("assets\camera_click_box.png").convert() 
camera_click_box_rect = camera_click_box.get_rect(center = (26,26)) 

#wall 3 poster------------------------------------------------------

poster_cb = pygame.image.load("assets\poster_click_box.png").convert()
poster_cb_rect = poster_cb.get_rect(center = (310,45))

paper_tool_cb = pygame.image.load("assets\paper_tool_click_box.png").convert()
paper_tool_cb_rect = paper_tool_cb.get_rect(center = (320, 80))




##wall 4------------------------------------------------------------

wall_4 = pygame.image.load("assets\wall4.png").convert()

drawer_empty = pygame.image.load("assets\drawer_1.png").convert()

filter_block = pygame.image.load("assets\Filter_block.png").convert()
filter_block_rect = filter_block.get_rect(center = (335,350))

click_block = pygame.image.load('assets\click_block.png').convert()
click_block_rect = click_block.get_rect(center = (250, 350))



# room 2 wall 3-----------------------------------------------------



room2_3 = pygame.image.load("assets\wall2_3.png").convert()
room2_3_open = pygame.image.load("assets\wall2_3_open.png").convert()

locker_cb = pygame.image.load("assets\lock_click_box.png").convert()
locker_cb_rect = locker_cb.get_rect(center = (300,330) )

lock_base = pygame.image.load("assets\lock.png").convert()



combo1_cb = pygame.image.load("assets\ltum1.png").convert()
combo1_cb_rect = combo1_cb.get_rect(center=(255,175))
combo2_cb = pygame.image.load("assets\ltum1.png").convert()
combo2_cb_rect = combo2_cb.get_rect(center=(255,275))
combo3_cb = pygame.image.load("assets\ltum1.png").convert()
combo3_cb_rect = combo3_cb.get_rect(center=(255,375))

tum0 = pygame.image.load("assets\ltum0.png").convert()
tum1 = pygame.image.load("assets\ltum1.png").convert()
tum2 = pygame.image.load("assets\ltum2.png").convert()
tum3 = pygame.image.load("assets\ltum3.png").convert()
tum4 = pygame.image.load("assets\ltum4.png").convert()
tum5 = pygame.image.load("assets\ltum5.png").convert()
tum6 = pygame.image.load("assets\ltum6.png").convert()
tum7 = pygame.image.load("assets\ltum7.png").convert()
tum8 = pygame.image.load("assets\ltum8.png").convert()
tum9 = pygame.image.load("assets\ltum9.png").convert()

hammer_cb = pygame.image.load("assets\hammer_block.png").convert()
hammer_cb_rect = hammer_cb.get_rect(center = (250,168))

#room 2 wall 1------------------------------------------------------

room2_1 = pygame.image.load("assets\wall2_1.png").convert()
room2_1_open = pygame.image.load("assets\wall2_1_open.png").convert()


#room 2 wall 2------------------------------------------------------

room2_2_open_bg = pygame.image.load("assets\wall2_2_open.png").convert()

break_wall_cb = pygame.image.load("assets\wallbreaker_cb.png").convert()
break_wall_cb_rect = break_wall_cb.get_rect(center = (335,205))

key_cb = pygame.image.load("assets\key_tool_cb.png").convert()
key_cb_rect = key_cb.get_rect(center = (325,205))

room2_2 = pygame.image.load("assets\wall2_2.png").convert()

#room2 wall 4-------------------------------------------------------

room2_4 = pygame.image.load("assets\wall2_4.png").convert()

door_room1 = pygame.image.load("assets\close_door.png").convert()
door_room1_rect = door_room1.get_rect(center = (285,275)) 



#tool belt----------------------------------------------------------

tool_belt = pygame.image.load("assets\Tool_bar.png").convert()

filter_tool = pygame.image.load("assets\Filter_tool.png").convert()
filter_tool_rect = filter_tool.get_rect(center = (355,465))

note_tool = pygame.image.load("assets\gnote_tool.png").convert()
note_tool_rect = note_tool.get_rect(center = (285, 465))

paper_page = pygame.image.load("assets\paper_base.png").convert()

hammer_tool = pygame.image.load("assets\hammer_tool.png").convert()
hammer_tool_rect = hammer_tool.get_rect(center = (215,465))

key_tool = pygame.image.load("assets\key_tool.png").convert()
key_tool_rect = key_tool.get_rect(center = (145,465))

## wall bumpers------------------------------------------------------


wall_border_r = pygame.image.load('assets\Right_border.png').convert()
wall_border_r_rect = wall_border_r.get_rect(center = (450,350))

wall_border_l = pygame.image.load('assets\left_border.png').convert()
wall_border_l_rect = wall_border_l.get_rect(center = (50,350))

wall_border_b = pygame.image.load('assets\Bottom_border.png').convert()
wall_border_b_rect = wall_border_b.get_rect(center = (250, 50))

#---------------------------------------------------------------------

#useful variable 

wall_list = [wall_1, wall_2, wall_3, wall_4]
roomwall_list = [room2_1, room2_2, room2_3, room2_4]
tum_list = [tum0,tum1,tum2,tum3,tum4,tum5,tum6,tum7,tum8,tum9]

wall_pos = 0
option = 0
tum_pos1 = 0
tum_pos2 = 0
tum_pos3 = 0
keys_pressed = 0

game_win = False
wall_2_open = False
wall_3_open = False
wall_1_isOpen = False
room_3_2_open = False
wall2_2_isOpen = False

room_2 = False
sidetrack = False
paper_screen = False


#in room sidetracks

in_stwall3 = False
in_stwall4 = False
in_stwall3_2 = False
#items--------------------------------

#filter
grabbed_filter = False
has_filter = False

#note
grabbed_note = False
has_note = False

#hammer
grabbed_hammer = False
has_hammer = False

#key
grabbed_key = False
has_key = False


key_list = [0,0,0,0]
pin_back_list = [pin_pad_base, pin_pad_base1, pin_pad_base2, pin_pad_base3, pin_pad_base4, pin_pad_correct, pin_pad_incorrect]

# keypad function
def keypad_screen(keys_pressed):
    pin = Keypad(5,2,1,6)
    tempback = 0
    if keys_pressed == 1:
        tempback = 1   
    elif keys_pressed == 2:
        tempback = 2
    elif keys_pressed == 3:
        tempback = 3
    elif keys_pressed == 4:
        tempback = 4
        if pin.is_correct(key_list[0],key_list[1],key_list[2],key_list[3]):
            tempback = 5
        else:
            tempback = 6
    return tempback


# main loop
while True:
    #user input control
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:   
            x, y = event.pos
           
           #bumpers----------------------------------------------------------
           
            if wall_border_r_rect.collidepoint(x,y) and sidetrack == False:
                if wall_pos == 3:
                    wall_pos = 0
                else:
                    wall_pos = wall_pos + 1
            
            if wall_border_l_rect.collidepoint(x,y) and sidetrack == False:
                
                if  0 == wall_pos:
                    wall_pos = 3
                else:
                    wall_pos = wall_pos - 1

            if wall_border_b_rect.collidepoint(x,y) and sidetrack == True:
                sidetrack = False
                if in_stwall3 == True:
                    in_stwall3 = False
                    keys_pressed = 0
                if in_stwall4 == True:
                    in_stwall4 = False
                option = 0

            
            #wall1---------------------------------------------------------------------------------
            
            
            if exit_door_cb_rect.collidepoint(x,y) and wall_1_isOpen and wall_pos == 0 and room_2 == False:
                game_win = True
            
            #wall2---------------------------------------------------------------------------------
            
            if door_room2_rect.collidepoint(x,y) and wall_pos == 1 and wall_2_open == True:
                room_2 = True


            #wall3---------------------------------------------------------------------------------

            if key_pad_cb_rect.collidepoint(x,y) and wall_pos == 2 and room_2 == False and option == 0:
                sidetrack = True 
                option = 1
            
            if camera_click_box_rect.collidepoint(x,y) and wall_pos == 2 and room_2 == False and option == 0:
                sidetrack = True
                option = 2
            
            if poster_cb_rect.collidepoint(x,y) and wall_pos == 2 and room_2 == False and sidetrack == False and wall_3_open == False:
                wall_3_open = True
                poster_sound.play()


            #wall4--------------------------------------------------------------------------------
            
            if click_block_rect.collidepoint(x,y) and wall_pos == 3 and room_2 == False and sidetrack == False:
                sidetrack = True
                drawer_sound.play()


            #room 2 wall 1------------------------------------------------------------------------            

            #room 2 wall 2------------------------------------------------------------------------
            if break_wall_cb_rect.collidepoint(x,y) and wall_pos == 1 and room_2 and wall2_2_isOpen == False and has_hammer:
                wall2_2_isOpen = True
                wall_breaker_sound.play()

            #room 2 wall 3------------------------------------------------------------------------

            if locker_cb_rect.collidepoint(x,y) and wall_pos == 2 and room_2 and room_3_2_open == False:
                sidetrack = True
            
            #room 2 wall 4------------------------------------------------------------------------

            if door_room1_rect.collidepoint(x,y) and wall_pos == 3 and room_2:
                room_2 = False
             

            

            #pin pad-------------------------------------------------------------------------------
            
            if keys_pressed < 4:

                if key_pad_key1_rect.collidepoint(x,y) and sidetrack == True and in_stwall3 == True:    
                    key_list[keys_pressed] = 1
                    keys_pressed = keys_pressed + 1
                    beep_sound.play()
                if key_pad_key2_rect.collidepoint(x,y) and sidetrack == True and in_stwall3 == True:
                    key_list[keys_pressed] = 2
                    keys_pressed = keys_pressed + 1
                    beep_sound.play()
                if key_pad_key3_rect.collidepoint(x,y) and sidetrack == True and in_stwall3 == True:
                    key_list[keys_pressed] = 3
                    keys_pressed = keys_pressed + 1
                    beep_sound.play()
                if key_pad_key4_rect.collidepoint(x,y) and sidetrack == True and in_stwall3 == True:
                    key_list[keys_pressed] = 4
                    keys_pressed = keys_pressed + 1
                    beep_sound.play()
                if key_pad_key5_rect.collidepoint(x,y) and sidetrack == True and in_stwall3 == True:
                    key_list[keys_pressed] = 5
                    keys_pressed = keys_pressed + 1
                    beep_sound.play()
                if key_pad_key6_rect.collidepoint(x,y) and sidetrack == True and in_stwall3 == True:
                    key_list[keys_pressed] = 6
                    keys_pressed = keys_pressed + 1
                    beep_sound.play()
                if key_pad_key7_rect.collidepoint(x,y) and sidetrack == True and in_stwall3 == True:
                    key_list[keys_pressed] = 7
                    keys_pressed = keys_pressed + 1
                    beep_sound.play()
                if key_pad_key8_rect.collidepoint(x,y) and sidetrack == True and in_stwall3 == True:
                    key_list[keys_pressed] = 8
                    keys_pressed = keys_pressed + 1
                    beep_sound.play()
                if key_pad_key9_rect.collidepoint(x,y) and sidetrack == True and in_stwall3 == True:
                    key_list[keys_pressed] = 9
                    keys_pressed = keys_pressed + 1
                    beep_sound.play()
                if key_pad_key0_rect.collidepoint(x,y) and sidetrack == True and in_stwall3 == True:
                    key_list[keys_pressed] = 0
                    keys_pressed = keys_pressed + 1
                    beep_sound.play()

            ##tumblers----------------------------------------------------------------------------

            if combo1_cb_rect.collidepoint(x,y) and in_stwall3_2 and sidetrack:
                if tum_pos1 == 9:
                    tum_pos1 = 0
                else:
                    tum_pos1 = tum_pos1 + 1
            
            if combo2_cb_rect.collidepoint(x,y) and in_stwall3_2 and sidetrack:
                if tum_pos2 == 9:
                    tum_pos2 = 0
                else:
                    tum_pos2 = tum_pos2 + 1
            
            if combo3_cb_rect.collidepoint(x,y) and in_stwall3_2 and sidetrack:
                if tum_pos3 == 9:
                    tum_pos3 = 0
                else:
                    tum_pos3 = tum_pos3 + 1


            #tools------------------------------------------------------------------------------------------
            if filter_tool_rect.collidepoint(x,y) and option == 2 and in_stwall3 == True and has_filter:
                has_filter = False
            
            if filter_block_rect.collidepoint(x,y) and sidetrack == True and grabbed_filter == False and in_stwall4 == True:
                grabbed_filter = True
                has_filter = True                     

            if hammer_cb_rect.collidepoint(x,y) and room_3_2_open and grabbed_hammer == False and wall_pos == 2 and room_2:
                grabbed_hammer = True
                has_hammer = True

            if key_cb_rect.collidepoint(x,y) and wall2_2_isOpen and grabbed_key == False and wall_pos == 1 and room_2:
                grabbed_key = True
                has_key = True        

            if key_tool_rect.collidepoint(x,y) and wall_pos == 0 and room_2 == False and has_key == True:
                wall_1_isOpen = True 

            if paper_tool_cb_rect.collidepoint(x,y) and wall_pos == 2 and wall_3_open and room_2 == False:
                has_note = True
                grabbed_note = True
            
            if note_tool_rect.collidepoint(x,y) and has_note:
                if paper_screen:
                    paper_screen = False
                else:
                    paper_screen = True

    if sidetrack == False:


        if room_2 == False:
            screen.blit(wall_list[wall_pos],(0,0))   
        else:
            screen.blit(roomwall_list[wall_pos],(0,0))
        
        
        screen.blit(wall_border_r,wall_border_r_rect)
        screen.blit(wall_border_l,wall_border_l_rect)

        if wall_3_open == True and grabbed_note == False and wall_pos == 2 and room_2 == False:
            screen.blit(paper_tool_cb,paper_tool_cb_rect)
         
        if wall_pos == 2 and room_2:
            if room_3_2_open and has_hammer == False:
                    screen.blit(hammer_cb,hammer_cb_rect)

        if wall2_2_isOpen and grabbed_key == False and room_2 and wall_pos == 1:
            screen.blit(key_cb,key_cb_rect)

        if wall2_2_isOpen:
            roomwall_list[1] = room2_2_open_bg

        if room_3_2_open:
            roomwall_list[2] = room2_3_open
            
        if has_filter == False and grabbed_filter:
            roomwall_list[0] = room2_1_open

        if wall_1_isOpen:
            wall_list[0]= wall_1_open   
   
    else:
         
        if wall_pos == 2 and option == 1:
            in_stwall3 = True
            key_pos = keypad_screen(keys_pressed)
            screen.blit(pin_back_list[key_pos],(0,0))
            if key_pos == 5:
                if wall_2_open == False:
                    door_open_sound.play()
                    wall_2_open = True
                
            screen.blit(key_pad_key1,key_pad_key1_rect)
            screen.blit(key_pad_key2,key_pad_key2_rect)
            screen.blit(key_pad_key3,key_pad_key3_rect)
            screen.blit(key_pad_key4,key_pad_key4_rect)
            screen.blit(key_pad_key5,key_pad_key5_rect)
            screen.blit(key_pad_key6,key_pad_key6_rect)
            screen.blit(key_pad_key7,key_pad_key7_rect)
            screen.blit(key_pad_key8,key_pad_key8_rect)
            screen.blit(key_pad_key9,key_pad_key9_rect)
            screen.blit(key_pad_key0,key_pad_key0_rect)
            screen.blit(wall_border_b,wall_border_b_rect)    
        if wall_pos == 2 and option == 2:
            in_stwall3 = True
            if has_filter == False and grabbed_filter == True:
                screen.blit(camera_base_full,(0,0))
            else:
                screen.blit(camera_base,(0,0)) 

        if wall_pos == 3:
            in_stwall4 = True
            screen.blit(drawer_empty,(0,0))
            if grabbed_filter == False:
                screen.blit(filter_block,filter_block_rect)        
        

        if wall_pos == 2 and room_2:
            in_stwall3_2 = True
            screen.blit(lock_base,(0,0))
            screen.blit(tum_list[tum_pos1],(205,150))
            screen.blit(tum_list[tum_pos2],(205,250))
            screen.blit(tum_list[tum_pos3],(205,350))
        screen.blit(wall_border_b,wall_border_b_rect)

    if paper_screen:
        screen.blit(paper_page,(0,0))
   
    if tum_pos1 == 5 and tum_pos2 == 4 and tum_pos3 == 3:
        if room_3_2_open == False:
            room_3_2_open = True
            locker_sound.play()
                
    if wall_2_open == True:
        wall_list[1] = wall_2_o 
    

    if wall_3_open == True:
        wall_list[2] = wall_3_o


    screen.blit(tool_belt,(0,430))
   
    if has_filter == True:
        screen.blit(filter_tool,filter_tool_rect)
    if has_note == True:
        screen.blit(note_tool,note_tool_rect)
    if has_hammer == True:
        screen.blit(hammer_tool,hammer_tool_rect)
    if has_key == True:
        screen.blit(key_tool,key_tool_rect)
   
    if game_win:
        screen.blit(win_wall,(0,0))
          
    

    pygame.display.update()
