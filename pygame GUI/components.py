# imports 
import pygame as pg # for GUI

class InputBox:
    '''
    Creates each text box for question answer.
    Handles user text input case by case.
    '''
    def __init__(self, x, y, w, h, text='', correct = False):
        self.rect = pg.Rect(x, y, w, h) # coodinates for box appearing on screen
        self.color = COLOR_INACTIVE # set color
        self.text = text # set text 
        self.txt_surface = FONT_SMALL.render(text, True, self.color) # set text surface
        self.active = False # default status is not active
        self.correct = correct # set correct flag, determines if box has accepted an answer yet
        self.x = x # x position
        self.y = y # y position

    def handle_event(self, event):
        '''
        Response if user clicks on box and enters text
        '''
        if event.type == pg.MOUSEBUTTONDOWN:
            # if the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # toggle active variable depending on correct flag
                if self.correct == False:
                    self.text = "" # reset text in box if not correct yet
                    self.active = True 
                if self.correct == True:
                    self.active = False # if answer already correct, clicking box has no effect (not active)
            else:
                self.active = False
            # change current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            
        if event.type == pg.KEYDOWN:
            # if the user presses a key
            if self.active:
                if event.key == pg.K_RETURN: # user presses enter
                    
                    if self.rect == pg.Rect(350, 150, 200, 185): # updates specific box based on coordinates
                        if np.any(b1 == self.text): # checks user's answer against list of query's correct answers
                            self.text = self.text + " is correct!" # output if user's answer matches any name in the list
                            self.correct = True  
                            self.active = False 
                        else:
                            self.text = self.text + " is incorrect." # output if user's answer does not match any name in the list
                            self.active = False
                            self.correct = True
                    if self.rect == pg.Rect(350, 350, 200, 185):
                        if np.any(b4 == self.text):
                            self.text = self.text + " is correct!"
                            self.correct = True    
                            self.active = False                            
                        else:
                            self.text = self.text + " is incorrect."
                            self.active = False
                            self.correct = True
                    if self.rect == pg.Rect(350, 550, 200, 185):
                        if np.any(b7 == self.text):
                            self.text = self.text + " is correct!"
                            self.correct = True     
                            self.active = False                            
                        else:
                            self.text = self.text + " is incorrect."    
                            self.active = False                                         
                            self.correct = True

                    if self.rect == pg.Rect(600, 150, 200, 185):
                        if np.any(b2 == self.text):
                            self.text = self.text + " is correct!"
                            self.correct = True   
                            self.active = False                            
                        else:
                            self.text = self.text + " is incorrect."
                            self.active = False
                            self.correct = True                            
                    if self.rect == pg.Rect(600, 350, 200, 185):
                        if np.any(b5 == self.text):
                            self.text = self.text + " is correct!"
                            self.correct = True
                            self.active = False                
                        else:
                            self.text = self.text + " is incorrect."
                            self.active = False 
                            self.correct = True                            
                    if self.rect == pg.Rect(600, 550, 200, 185):
                        if np.any(b8 == self.text):
                            self.text = self.text + " is correct!"
                            self.correct = True                            
                            self.active = False                            
                        else:
                            self.text = self.text + " is incorrect."    
                            self.active = False                         
                            self.correct = True                            
                    if self.rect == pg.Rect(850, 150, 200, 185):
                        if np.any(b3 == self.text):
                            self.text = self.text + " is correct!"
                            self.correct = True                   
                            self.active = False                        
                        else:
                            self.text = self.text + " is incorrect."                   
                            self.active = False                                                     
                            self.correct = True                            
                    if self.rect == pg.Rect(850, 350, 200, 185):
                        if np.any(b6 == self.text):
                            self.text = self.text + " is correct!"
                            self.correct = True                            
                            self.active = False                                                    
                        else:
                            self.text = self.text + " is incorrect."
                            self.active = False
                            self.correct = True                            
                    if self.rect == pg.Rect(850, 550, 200, 185):
                        if np.any(b9 == self.text):
                            self.text = self.text + " is correct!"
                            self.correct = True                            
                            self.active = False                            
                        else:
                            self.text = self.text + " is incorrect."
                            self.active = False   
                            self.correct = True                        
                                        
                elif event.key == pg.K_BACKSPACE: # user presses backspace
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode # user presses text keys
                    
                # re-render the text
                self.txt_surface = FONT_SMALL.render(self.text, True, self.color)
                
    def update(self):
        # update rect
        width = 200
        self.rect.w = width

    def draw(self, screen):
        # blit the text
        words = [word.split(' ') for word in self.text.splitlines()]  # 2D array where each row is a list of words
        space = FONT.size(' ')[0]  # The width of a space
        
        x = self.x
        y = self.y
        pos = (x,y)
        
        max_width = x + 185
        
        # blits text to next line if line exceeds max width
        for line in words:
            for word in line:
                word_surface = FONT.render(word, 0, COLOR_BLACK)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x
                    y += word_height  # Start on new row
                screen.blit(word_surface, (x + 5, y + 5))
                x += word_width + space
            x = pos[0]  # Reset the x
            y += word_height  # Start on new row         
        # blit the rect
        pg.draw.rect(screen, self.color, self.rect, 2)                   

class question:
    '''
    Class for each question with text and coordinates
    '''
    def __init__(self, x, y, text):
        self.color = COLOR_INACTIVE
        self.text = text
        self.x = x
        self.y = y

    def blit_text(self, screen):
        words = [word.split(' ') for word in self.text.splitlines()]  # 2D array where each row is a list of words
        space = FONT.size(' ')[0]  # The width of a space
        
        x = self.x
        y = self.y
        pos = (x,y)
        
        max_width = x + 200
                
        # blits text to next line if line exceeds max width
        for line in words:
            for word in line:
                word_surface = FONT.render(word, 0, COLOR_BLACK)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x
                    y += word_height  # Start on new row
                screen.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x
            y += word_height  # Start on new row                
        
class title:   
    '''
    Class for title with text and coordinates
    '''
    def __init__(self, x, y, text):
        self.color = COLOR_INACTIVE
        self.text = text
        self.x = x
        self.y = y
        
    def label(self, screen):
        # render text
        q = FONT_LARGE.render(self.text, False, (255,255,255))
        screen.blit(q, (self.x, self.y))    