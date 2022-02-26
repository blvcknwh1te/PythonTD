import pygame
from os import path
from Anims import background,button_images,button_images_activated,button_images_clicked,\
    background_blocked,background_tutorial, clouds,towers,sky,saveBox,bg_save_mask,button_play_blocked

from Anims import background_save as bg_save
from settings import HS_FILE

pygame.font.init()

#x,y,item_name,item_color,item_color_active,number,surface

item_color=(255,140,0)
item_color_active=(220,20,60)

font_Save=pygame.font.SysFont('Century Gothic',45)
font_SaveBox=pygame.font.SysFont('Century Gothic',80)

class Menu:


    def __init__(self,surface):
        self.surface=surface
        self.bg=background
        self.button_images=button_images
        self.button_images_active=button_images_activated
        self.button_images_clicked=button_images_clicked
        self.realButtonImage=button_images
        self.mouseX=0
        self.mouseY=0
        self.game_started=False
        self.isTutorial=False
        self.game_finished=False
        self.cloudsX=40
        self.cloudsY=280
        self.clouds=clouds
        self.sky=sky
        self.towers=towers
        self.animCount=0
        self.isSaveMenu=False
        self.dir = path.dirname(__file__)


        self.isStartGame=True
        self.isSaveBox = False
        self.save_slot = 0
        self.nicknames = ["Empty", "Empty", "Empty", "Empty", "Empty"]
        self.nickname = ""
        self.scores = [0, 0, 0, 0, 0]
        self.score = 0
        self.color1=(30,30,30)

        self.input_text = font_SaveBox.render("", True, self.color1)
        self.text=""
        self.text_c=0
        i=0
        def return_empty():
            self.nicknames = ["Empty", "Empty", "Empty", "Empty", "Empty"]
            self.nickname = ""
            self.scores = [0, 0, 0, 0, 0]
            self.score = 0

            print("Highscores file ERROR.")

        with open(path.join(self.dir, HS_FILE), 'r') as f:

            counter1=0

            try:
                for line in f:
                    char_i = line.find(":")
                    if ":" in line:
                        counter1+=line.count(":")
                    end_i = line.find("\n")
                    self.nicknames[i] = line[0:char_i]
                    self.scores[i] = int(line[char_i + 1:end_i])

                    if self.nicknames[i].upper()=="empty".upper() and self.scores[i]!=0:
                        return_empty()
                        print(self.scores[i])
                    if len(str(self.scores[i]))>=9 or len(self.nicknames[i])>12\
                        or len(self.nicknames[i])==0:
                        return_empty()

                    i+=1
                if counter1!=5:
                    return_empty()
            except:
                return_empty()


    def draw(self):
        if self.game_finished:
            self.surface.blit(background_blocked,(0,0))
            self.surface.blit(self.bg, (0, 0))
            pass


        ###################################
        if self.isSaveBox:#######IF SAVEBOX
            self.surface.blit(self.bg, (0, 0))

            text_back = font_Save.render('Back', True, self.color1)
            text_delete = font_Save.render('Delete', True, self.color1)
            self.surface.blit(text_back, (745, 895))
            self.surface.blit(text_delete, (495, 895))
            x = 472
            y = 112
            yl = 127
            yd = 24

            for i in range(5):
                nick = font_Save.render(self.nicknames[i], True, (50, 50, 50))
                self.surface.blit(nick, (x + 15, 10 + y + i * (yl + yd)))

            self.surface.blit(bg_save_mask,(0,0))
            self.surface.blit(saveBox,(225,350))
            self.surface.blit(self.input_text, (270, 400))

            return
        ##############################

        if not self.isTutorial and not self.game_finished and not self.isSaveMenu: ###IF IS NOT TUTORIAL
            x=500
            y=220

            if self.animCount+1>=140:#Animating background
                self.animCount=0
                self.cloudsX=40
            self.surface.blit(self.sky,(0,0))
            self.surface.blit(self.clouds, (self.cloudsX, self.cloudsY))
            self.surface.blit(self.clouds, (self.cloudsX+1400, self.cloudsY))
            self.surface.blit(self.towers, (0, 0))  # Static background
            self.animCount+=1
            self.cloudsX-=10


            for image in range(len(self.button_images)):
                mouseOnButton=self.mouseX > x and self.mouseX < x + 400 \
                        and self.mouseY>y and self.mouseY<y+90

                if pygame.mouse.get_pressed()[0] and mouseOnButton:#Button clicked
                        self.realButtonImage=self.button_images_clicked[image]
                        self.surface.blit(self.realButtonImage, (x, y))
                else:
                    if mouseOnButton: ##MOUSE ON BUTTON
                        self.realButtonImage=self.button_images_active[image]
                    else:##BUTTON STATIC
                        self.realButtonImage=self.button_images[image]
                    self.surface.blit(self.realButtonImage, (x, y))


                print("IMAGE:",image)
                print("IS STARTGame",self.isStartGame)
                if image==0 and self.isStartGame: ##IF PLAY IS BLOCKED ( START GAME)
                    print("true")
                    self.realButtonImage = button_play_blocked
                    self.surface.blit(self.realButtonImage, (x, y))
                if mouseOnButton:
                    self.button_index=image+1
                else:
                    self.button_index=0

                y += 150
        else:#IF TUTORIAL IS CLICKED
            if self.isTutorial:
                self.surface.blit(self.bg, (0, 0))

            ###IF SAVE_MENU IS CLICKED
            if self.isSaveMenu:
                self.surface.blit(self.bg, (0, 0))
                text_back = font_Save.render('Back', True, (30,30,30))
                text_delete=font_Save.render('Delete', True, (30,30,30))
                self.surface.blit(text_back,(745,895))
                self.surface.blit(text_delete,(495,895))
                x = 472
                y = 112
                yl = 127
                xl = 456
                yd=24

                bx = 712
                by = 896
                bxl = 216
                byl = 959
                for i in range(5):
                    nick = font_Save.render(self.nicknames[i], True, (50, 80, 50))
                    score = font_Save.render("Level "+str(self.scores[i]), True, (50, 50, 95))
                    self.surface.blit(nick, (x+15,10+y+i*(yl+yd)))
                    self.surface.blit(score,(x+15,65+y+i*(yl+yd)))





    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                self.mouseX = event.pos[0]
                self.mouseY = event.pos[1]

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouseX = event.pos[0]
                self.mouseY = event.pos[1]

                print(self.text)

                if event.button==1 and not self.isSaveBox:#Left click
                    x = 500
                    y = 220
                    if self.game_finished:
                        x = 315
                        y = 290



                        mouseOnButton = self.mouseX > x and self.mouseX < x + 768 \
                                        and self.mouseY > y and self.mouseY < y + 464
                        if mouseOnButton:
                            pygame.quit()

                    if not self.isTutorial and not self.isSaveMenu:
                        for image in range(len(self.button_images)):
                            mouseOnButton = self.mouseX > x and self.mouseX < x + 400 \
                                            and self.mouseY > y and self.mouseY < y + 90
                            if mouseOnButton:
                                if image==0 and not self.isStartGame: ###BUTTON 1 //PLAY GAME
                                    self.game_started=True
                                    self.bg=background_blocked
                                    return False

                                elif image==1: ###BUTTON2 //SAVE_LOAD
                                    self.isSaveMenu=True
                                    self.bg=bg_save

                                elif image==2:###BUTTON3 //TUTORIAL
                                    self.isTutorial=True
                                    self.bg=background_tutorial
                                    ...

                                elif image==3:###BUTTON4 //EXIT
                                    pygame.quit()
                            y += 150
                    else:
                        if self.isTutorial:
                            x=7
                            y=5
                            mouseOnButton = self.mouseX > x and self.mouseX < x + 240 \
                                            and self.mouseY > y and self.mouseY < y + 115
                            if mouseOnButton:
                                self.isTutorial=False
                                self.bg=background


                        elif self.isSaveMenu:
                            x=472
                            y=112
                            yl=127
                            xl=456
                            yd=24

                            bx=712
                            by=896
                            bxl=216
                            byl=63
                            mouseOnButton = self.mouseX > bx and self.mouseX < bx + bxl \
                                            and self.mouseY > by and self.mouseY < by + byl


                            ###IF BACK_BUTTON IS CLICKED
                            if mouseOnButton and not self.isStartGame:
                                self.isSaveMenu=False
                                self.bg=background

                            for i in range(5):
                                mouseOnButton =  self.isMouseOnButton(x,y,xl,yl)
                                y+=yl+yd
                                if mouseOnButton:
                                    if self.nicknames[i] == "Empty":
                                        self.isSaveBox = True
                                        self.save_slot = i

                                        if self.nicknames:
                                            print(self.nicknames[self.save_slot])

                                    else:
                                        self.save_slot = i
                                        self.isSaveMenu = False
                                        self.isStartGame=False
                                       # return False

                elif self.isSaveBox:
                    x1 = 225
                    y1 = 350
                    mouseOnBox = self.mouseX > x1 and self.mouseX < x1 + 1050 \
                                 and self.mouseY > y1 and self.mouseY < y1 + 1050

                    if not mouseOnBox:
                        self.isSaveBox = False
                        self.text = ""
                        self.text_c = 0
                        self.input_text = font_SaveBox.render(self.text, True, self.color1)



            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.game_finished:
                        pygame.quit()
                    if self.game_started :
                        return False
                    if self.isTutorial:
                        self.isTutorial = False
                        self.bg = background

                    elif self.isSaveMenu:
                        if not self.isSaveBox:
                            self.isSaveMenu=False
                            self.bg=background



                if self.isSaveBox:

                    if event.key==pygame.K_RETURN:
                        self.isSaveBox = False
                        if any(c.isalnum() for c in self.text) and \
                                (self.text!="Empty" and self.text!="empty"):
                            self.nicknames[self.save_slot]=self.text
                            self.scores[self.save_slot]=self.score
                            self.nickname=self.text
                            self.text=""
                            self.text_c=0
                            self.isSaveMenu=False
                            self.isStartGame=False

                            with open(path.join(self.dir, HS_FILE), 'w') as f:
                                for i in range(5):
                                    f.write(str(self.nicknames[i]) + ":" + str(self.scores[i]) + "\n")


                            #return False

                        else:
                            self.isSaveBox=True


                    elif event.key == pygame.K_BACKSPACE:
                        self.text=self.text[:-1]
                        if self.text_c>0:
                            self.text_c-=1
                            print(self.text_c)


                    elif event.key == pygame.K_ESCAPE:
                        self.isSaveBox=False
                        self.text=""
                        self.text_c=0
                    else:
                        if self.text_c<12 and event.unicode!=":":
                            self.text+=event.unicode
                            print("key down "+event.unicode)


                            if str.isalnum(event.unicode):
                                self.text_c+=1
                                print(self.text_c)

                    self.input_text = font_SaveBox.render(self.text, True, self.color1)


        return True

    def isMouseOnButton(self,x,y,xl,yl,yd=0):
        return self.mouseX > x and self.mouseX < x + xl \
                and self.mouseY > y and self.mouseY < y + yl

