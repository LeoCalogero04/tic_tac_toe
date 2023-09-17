import pygame
import time

def identify_region(screen_width,screen_height): #returns region mouse is pressed in
    
    mouse=pygame.mouse.get_pressed() # [left mouse state, middle button state, right mouse button state]
    if mouse[0]==True:
        position=pygame.mouse.get_pos()  #(x,y)
        if position[0] < screen_width/3 and position[0]>0: 
            if position[1] < screen_height/3:  #if height is less then 1/3 of screen
                return 1
            elif position [1] < screen_height*2/3: #if height less then 2/3 and greater then 1/3
                return 2
            else:  #only option left is to be within bottom right
                return 3
            

        elif position[0] < screen_width*2/3:  #within middle of screen
            if position[1] < screen_height/3 and position[1]>0:
                return 4
            elif position [1] < screen_height*2/3:
                return 5
            else:
                return 6
        else: #within right column of screen
            if position[1] < screen_height/3 and position[1]>0:
                return 7
            elif position [1] < screen_height*2/3:
                return 8
            else:
                return 9

def check_win(territory): #return True if won, false if not
    if 1 in territory:
        if 4 in territory and 7 in territory:
            return True
        elif 2 in territory and 3 in territory:
            return True
        elif 5 in territory and 9 in territory:
            return True
    elif 5 in territory:
        if 2 in territory and 8 in territory:
            return True
        elif 3 in territory and 7 in territory:
            return True
        elif 4 in territory and 6 in territory:
            return True
    elif 9 in territory:
        if 3 in territory and 6 in territory:
            return True
        elif 7 in territory and 8 in territory:
            return True
    else:
        return False
def draw_grid(screen_width,screen_height):
    for i in range(1,3): #draw vertical lines
        pygame.draw.line(screen,(225,225,225),(screen_width/3*i,0),(screen_width/3*i,screen_height),5)
    for j in range(1,3):
        pygame.draw.line(screen,(225,225,225),(0,screen_height/3*j),(screen_width,screen_height/3*j),5)

def draw_circle(center):
    pygame.draw.circle(screen,(200,0,0),center,50,5)
def region_center(region,screen_width,screen_height):
    if region == 1:
        center= [screen_width/6,screen_height/6]
    elif region == 2:
        center=[screen_width/6,screen_height/2]
    elif region == 3:
        center=[screen_width/6,screen_height*5/6]
    elif region == 4:
        center= [screen_width/2,screen_height/6]
    elif region == 5:
        center= [screen_width/2,screen_height/2]
    elif region == 6:
        center=[screen_width/2,screen_height*5/6]
    elif region == 7:
        center= [screen_width*5/6,screen_height/6]
    elif region == 8:
        center= [screen_width*5/6,screen_height/2]
    else:
        center=[screen_width*5/6,screen_height*5/6]

    return center

def draw_x(center,screen_width,screen_height):
    top_left= (center[0]-1/12*screen_width,center[1]+1/12*screen_height)
    bottom_right= (center[0]+1/12*screen_width,center[1]-1/12*screen_height)
    bottom_left=(center[0]-1/12*screen_width,center[1]-1/12*screen_height)
    top_right=(center[0]+1/12*screen_width,center[1]+1/12*screen_height)

    pygame.draw.line(screen,(0,0,255),top_left,bottom_right,5)
    pygame.draw.line(screen,(0,0,255),bottom_left,top_right,5)

def draw_text(text,font,color,x,y):
    img= font.render(text,True,color)
    screen.blit(img,(x,y))

pygame.init()
screen_width=800
screen_height=600
sum=1
screen=pygame.display.set_mode((screen_width,screen_height))
run=True
player1=[]
player2=[]
win=False
winner=''
while run:
    if win==True:
            for event in pygame.event.get():  
                if event.type== pygame.QUIT:
                    run=False
            screen.fill((0,0,0))
            text_font=pygame.font.SysFont("Arial",60)
            draw_text(winner + ' wins!',text_font,(255,255,255),screen_width/3,screen_height/2)
            pygame.display.update()
    
    else:
        if sum >= 10 and win!= True:
            for event in pygame.event.get():  
                if event.type== pygame.QUIT:
                    run=False
            screen.fill((0,0,0))
            text_font=pygame.font.SysFont("Arial",60)
            draw_text('Tie game!',text_font,(255,255,255),screen_width/3,screen_height/2)
            

        else:

            for event in pygame.event.get():  #end game if x is clicked
                if event.type== pygame.QUIT:
                    run=False

            draw_grid(screen_width,screen_height)

    
            mouse=pygame.mouse.get_pressed()
            if mouse[0] == True: 
            
                region= identify_region(screen_width,screen_height)
                center= region_center(region,screen_width,screen_height)
                if sum%2 != 0 and region not in (player2 or player1):
                    draw_circle(center)
                    player1.append(region)
                    sum+=1
                    if sum > 4:
                        if check_win(player1) == True:
                            winner += 'Player1'
                            win=True
                elif sum%2 == 0 and region not in (player1 or player2):

                    draw_x(center,screen_width,screen_height)
                    player2.append(region)
                    sum+=1
                    if sum > 4:
                        if check_win(player2)== True:
                            winner+='Player2'
                            win=True

                time.sleep(0.25)

        pygame.display.update()
    




        

    
    





