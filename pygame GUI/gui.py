class run_main:
    '''
    Runs game with main function.
    '''
    def run():
        '''
        Runs full game.
        '''
        pg.init() # initialize game
        screen = pg.display.set_mode((1400, 800)) # render screen
        COLOR_INACTIVE = pg.Color('lightskyblue3') # set color for inactive status
        COLOR_ACTIVE = pg.Color('dodgerblue2') # set color for active status
        COLOR_BLACK = pg.Color('black') # set black color
        FONT = pg.font.Font(None, 35) # question font size
        FONT_SMALL = pg.font.Font(None, 28) # small font size
        FONT_LARGE = pg.font.Font(None, 50) # large font size
        globals().update(locals())

        if __name__ == '__main__':
            main()
            pg.quit()

    def main():
        '''
        Runs game query, creates 9 input boxes, 6 questions, and reruns code if gameover.
        '''
        bg = pg.image.load("background.jpg") # background
        clock = pg.time.Clock()

        # create answer boxes, 3x3 grid
        input_box1 = InputBox(350, 150, 185, 185)
        input_box4 = InputBox(600, 150, 185, 185)
        input_box7 = InputBox(850, 150, 185, 185)

        input_box2 = InputBox(350, 350, 185, 185)
        input_box5 = InputBox(600, 350, 185, 185)
        input_box8 = InputBox(850, 350, 185, 185)

        input_box3 = InputBox(350, 550, 185, 185)
        input_box6 = InputBox(600, 550, 185, 185)
        input_box9 = InputBox(850, 550, 185, 185)

        input_boxes = [input_box1, input_box2, input_box3,
                       input_box4, input_box5, input_box6,
                       input_box7, input_box8, input_box9]

        # run query to create game (modify once classes are created)
        create_game()

        # create 4 questions
        Q1 = question(600, 100, q1)
        Q2 = question(850, 100, q2)
        Q3 = question(150, 350, q3)
        Q4 = question(150, 550, q4)

        questions = [Q1, Q2, Q3, Q4]

        # create 2 team questions
        team1 = pg.image.load(team1_q)
        team2 = pg.image.load(team2_q)

        done = False
        finished = False    

        # loop game until all all questions have been answered 
        while not done:
            for event in pg.event.get():

                if event.type == pg.QUIT: # exit game
                    done = True

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_r and finished: # restart game
                        main()
                    if event.key == pg.K_x and finished: # exit game
                        done = True

                # handle user input in box   
                for box in input_boxes:
                    box.handle_event(event) 

                # fill background
                screen.fill((30, 30, 30))

                # blit backgound image
                screen.blit(bg, (0, 0))

                # blit team questions
                screen.blit(team2, (375, 40))
                screen.blit(team1, (155, 180))

                # output text for each box
                for box in input_boxes:
                    box.draw(screen)

                # update each box
                for box in input_boxes:
                    box.update()

                # blit questions
                for q in questions:
                    q.blit_text(screen)                      

                # display title
                t = title(595, 40, "Hoops Trivia")
                t.label(screen)

                # game finished when all boxes have accepted answer, present option to restart game
                if input_box1.correct & input_box2.correct & input_box3.correct & input_box4.correct & input_box5.correct & input_box6.correct & input_box7.correct &    input_box8.correct & input_box9.correct:
                    finished = True
                if finished:  
                    # restart option
                    gameover = FONT.render("Press R to Restart or X to Exit", False, (255, 255, 255))
                    rect = gameover.get_rect()
                    rect.center = screen.get_rect().center
                    screen.blit(gameover, rect)

                pg.display.flip() # updates screen
                clock.tick(30) # at most 30 FPS