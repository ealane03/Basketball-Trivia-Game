import pandas as pd # for storing data in pandas dataframe
import sqlite3 # for accessing SQL database
import numpy as np 
import random
from random import randint # random for randomizing questions


def query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1,team2, pos, mvp):
    '''
    SQL query function pulling stats.
    
    Will be used to check for players who meet the given criteria
    
    parameters:
    players, position, teams, points, assists, blocks, steals, rebounds, three point percentage, three point, free throw percentage, mvp
   
    outputs:
    table (pandas dataframe): dataframe with queried data
    '''
    
    cmd = \
    f"""SELECT S.PLAYER, S.POS, S.TM, S.FG, S.FG_P, S.THRP, S.THRP_P, S.FT, 
        S.FT_P, S.PTS, S.AST, S.BLK, S.STL, S.TRB, S.TOV, S.SEASON, S.MVP
    FROM stats S 
    WHERE S.PTS >= {points} AND S.AST >= {assists} AND S.BLK >= {blocks} AND S.STL >= {steals} AND S.TRB >= {rebounds} AND 
          S.PTS <= {points_} AND S.AST <= {assists_} AND S.BLK <= {blocks_} AND S.STL <= {steals_} AND S.TRB <= {rebounds_} AND
          S.THRP >= {thr_pt} AND S.THRP_P >= {thr_pt_pct} AND S.FT_P >= {ft_pct}  AND S.MVP == {mvp}
    """
    # the following command takes the data from stats and checks to see which players meet the given stats
    data = sqlite3.connect("data.db")
    # opens up data
    table = pd.read_sql_query(cmd, data)
    # will return a table of players that meet the stats
    
    # the following code is used to check for teams
    # this is only done since SQL can't match strings
    if team1 and team2 != None:
        # if the question asks for two teams
        table1 = table[table['Tm']==f"{team1}"]
        # returns players who played for team1
        table2 = table[table['Tm']==f"{team2}"]
        # returns players who player for team2
        frames = [table1,table2]
        table = pd.merge(table1,table2,how="inner",on="Player")
        # merges the two tables on players who have played for both teams
        table=table.drop_duplicates()
        # drops any duplicates
    elif team1 != None:
        # if only one team is asked
        table= table[table['Tm']==f"{team1}"]
    elif team2 != None:
        # if only one team is asked
        table= table[table['Tm']==f"{team2}"]
    
    # the following is used to check for positions
    if pos != None:
        table= table[table['Pos']==f"{pos}"]
        # returns players who play at the specified position
    data.close()
    #closes data
    
    return table # return pandas dataframe



def random_var():
    """
    Chooses random numbers for questions
    Some are integers and others are percentages depending on the question
    Also chooses more than or less than for certain questions
    """
    
    # the following uses random package to randomly generate numbers and choices
    points_rand = randint(7,15)
    assists_rand = randint(1,5)
    blocks_rand = round(random.uniform(0.1,1), 1)
    steals_rand = round(random.uniform(0.1,1.5), 1)
    rebounds_rand = round(random.uniform(0.1,6), 1)
    thr_pt_rand = randint(1,5)
    thr_pt_pct_rand = round(random.uniform(0.2,0.5), 3)
    ft_pct_rand = round(random.uniform(0.4,0.9), 3)
    hol_points = random.choice([True, False])
    hol_assists = random.choice([True, False])
    hol_blocks = random.choice([True, False])
    hol_steals = random.choice([True, False])
    hol_rebounds = random.choice([True, False])
    globals().update(locals())
    #updates the variables so they can be accessed by other classes ad functions
    
class all_question:
    """
    Class that contains almost all possible questions that will be asked
    Applies randomly generated numbers from the random_var function into the query
    Returns the question in question form
    """
    
    def points():
        if hol_points == True:
            # if it is chosen as more than
            global points
            points = points_rand
            # takes the randomized points number and will apply it into the query 
            question = f"> {points} points in a season"
            # asks the question
        else:
            # if it is chosen as less than
            global points_
            points_ = points_rand
            # takes the randomized points number and will apply it into the query
            question = f"< {points_} points in a season"
            # asks the question
        return question
    def assists():
        if hol_assists == True:
            # if it is chosen as more than
            global assists
            assists = assists_rand
            # takes the randomized assists number and will apply it into the query 
            question = f"> {assists} assists in a season"
            # asks the question
        else:
            # if it is chosen as less than
            global assists_
            assists_ = assists_rand
            # takes the randomized assists number and will apply it into the query
            question = f"< {assists_} assists in a season" 
            # asks the question
        return question
    def blocks():
        if hol_blocks == True:
            # if it is chosen as more than
            global blocks
            blocks = blocks_rand
            # takes the randomized blocks number and will apply it into the query
            question = f"> {blocks} blocks in a season"
            # asks the question
        else:
            # if it is chosen as less than
            global blocks_
            blocks_ = blocks_rand
            # takes the randomized blocks number and will apply it into the query
            question = f"< {blocks_} blocks in a season"
            # asks the question
        return question
    def steals():
        if hol_steals == True:
            # if it is chosen as more than
            global steals
            steals = steals_rand
            # takes the randomized steals number and will apply it into the query
            question = f"> {steals} steals in a season"
            # asks the question
        else:
            # if it is chosen as less than
            global steals_
            steals_ = steals_rand
            # takes the randomized steals number and will apply it into the query
            question = f"< {steals_} steals in a season"
            # asks the question
        return question
    def rebounds():
        if hol_rebounds == True:
            # if it is chosen as more than
            global rebounds
            rebounds = rebounds_rand
            # takes the randomized rebounds number and will apply it into the query
            question = f"> {rebounds} rebounds in a season"
            # asks the question
        else:
            # if it is chosen as less than
            global rebounds_
            rebounds_ = rebounds_rand
            # takes the randomized rebounds number and will apply it into the query
            question = f"< {rebounds_} rebounds in a season"
            # asks the question
        return question
    def three_point():
        global thr_pt
        thr_pt = thr_pt_rand
        # takes the randomized three point number and will apply it into the query
        question = f"> {thr_pt} 3-pointers in a season"
        # asks the question
        return question
    def three_point_perc():
        global thr_pt_pct
        thr_pt_pct = thr_pt_pct_rand
        # takes the randomized three point percentage and will apply it into the query
        question = f"> {round(thr_pt_pct*100)}% 3-point in a season"
        # asks the question
        return question
    def free_throw_perc():
        global ft_pct
        ft_pct = ft_pct_rand
        # takes the randomized free throw percentage and will apply it into the query
        question = f"> {ft_pct} free throw % in a season"
        # asks the question
        return question
    def mvp():
        # mvp question is defined but not used for our game to make it more challenging
        global mvp
        mvp = random.choice([True, False])
        if mvp == True:
            question = "Was an MVP"
        else:
            question = "Was never an MVP"
        # asks the question
        return question
        
        
def rand_question():
    """
    First randomly chooses which teams will be asked
    Also randomly chooses a position but is not used for our game but can be
    Then randomly chooses which questions to ask
    Question asking teams are hard coded to be asked every time to be more challenging
    """
    team_choice=list(base["Tm"].unique())
    # makes a list of all teams
    team_q1 = random.sample(team_choice,2)
    #randomly chooses two different teams from list
    global team1_q, team2_q
    team1_q = f"{team_q1[0]}.png"
    team2_q = f"{team_q1[1]}.png"
    pos_choice=list(base["Pos"].unique())
    # makes a list of positions
    pos1 = random.choice(pos_choice)
    # randomly chooses a position from the list
    pos_q = f"Played {pos1}"
    # returns position in question form
    
    random_var()
    # calls the random_var function to generate random numbers for the questions
    list_of_question=[all_question.points,all_question.assists,all_question.three_point,all_question.three_point_perc,
              all_question.steals,all_question.blocks,all_question.rebounds,all_question.free_throw_perc]   
    # list of all possible questions that is used for our game excluding teams and positions
    loq = random.sample(list_of_question,k=4)
    # randomly chooses four different questions to ask
    qr1=loq[0]
    # runs the first question
    qr2=loq[1]
    # runs the second question
    qr3=loq[2]
    # runs the third question
    qr4=loq[3]
    # runs the fourth question
    globals().update(locals())

def default():
    """
    Resets all variables in query to default so all players are included
    """
    points=0
    assists = 0
    blocks = 0
    steals = 0
    rebounds = 0
    points_ = 100 
    assists_ = 100
    blocks_ = 100 
    steals_ = 100 
    rebounds_ = 100 
    thr_pt = 0
    thr_pt_pct = 0 
    ft_pct = 0 
    team1 = None
    team2 = None
    pos = None
    mvp = False
    base = query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1,team2, pos, mvp)
    # contains the table of all players
    globals().update(locals()) 
    
    
    

class Game:
    """
    Matches the question to each square following row and column
    Runs the question and imports the stats into the query
    Makes a list of all possible players who fit the requirements
    """
    # all squares follow the same comment structure
    def r1c1():
        global b1
        # makes the variable that will contain all possible answers for the square global
        team1=team_q1[0]
        # takes the first randomized team
        team2=team_q1[1]
        # takes the second randomized team
        a = query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1, team2, pos, mvp)
        # runs the questions through the query
        b1=a['Player'].unique()
        # generates a list of the players who match the criteria
        default()
        # sets query to default for next question
        return team1_q,team2_q
        # asks the question that will be visible in the game
    def r1c2():
        global b2,q3
        # makes variable that contains all answers and also the question that is asked global
        team1=team_q1[0]
        # takes the first randomized team
        q3=qr3()
        # runs the third randomized question
        a = query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1, team2, pos, mvp)
        # runs the questions through the query
        b2=a['Player'].unique()
        # generates a list of the players who match the criteria
        default()
        # sets query to default for next question
        return team1_q,q3
        # asks the question that will be visible in the game
    def r1c3():
        global b3,q4
        # makes variable that contains all answers and also the question that is asked global
        team1=team_q1[0]
        # takes the first randomized team
        q4=qr4()
        # runs the fourth randomized question
        a = query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1, team2, pos, mvp)
        # runs the questions through the query
        b3=a['Player'].unique()
        # generates a list of the players who match the criteria
        default()
        # sets query to default for next question
        return team1_q,q4
        # asks the question that will be visible in the game
    def r2c1():
        global b4,q1
        # makes variable that contains all answers and also the question that is asked global
        q1=qr1()
        # runs the first randomized question
        team2=team_q1[1]
        # takes the second randomized team
        a = query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1, team2, pos, mvp)
        # runs the questions through the query
        b4=a['Player'].unique()
        # generates a list of the players who match the criteria
        default()
        # sets query to default for next question
        return q1,team2_q
        # asks the question that will be visible in the game
    def r2c2():
        global b5,q1,q3
        # makes variable that contains all answers and also the question that is asked global
        q1=qr1()
        # runs the first randomized question
        q3=qr3()
        # runs the third randomized question
        a = query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1, team2, pos, mvp)
        # runs the questions through the query
        b5=a['Player'].unique()
        # generates a list of the players who match the criteria
        default()
        # sets query to default for next question
        return q1,q3
        # asks the question that will be visible in the game
    def r2c3():
        global b6,q1,q4
        # makes variable that contains all answers and also the question that is asked global
        q1=qr1()
        # runs the first randomized question
        q4=qr4()
        # runs the fourth question
        a = query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1, team2, pos, mvp)
        # runs the questions through the query
        b6=a['Player'].unique()
        # generates a list of the players who match the criteria
        default()
        # sets query to default for next question
        return q1,q4
        # asks the question that will be visible in the game
    def r3c1():
        global b7,q2
        # makes variable that contains all answers and also the question that is asked global
        q2=qr2()
        # runs the second randomized question
        team2=team_q1[1]
        # takes the second randomized team
        a = query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1, team2, pos, mvp)
        # runs the questions through the query
        b7=a['Player'].unique()
        # generates a list of the players who match the criteria
        default()
        # sets query to default for next question
        return q2,team2_q
        # asks the question that will be visible in the game
    def r3c2():
        global b8,q2,q3
        # makes variable that contains all answers and also the question that is asked global
        q2=qr2()
        # runs the second randomized question
        q3=qr3()
        # runs the third randomized question
        a = query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1, team2, pos, mvp)
        # runs the questions through the query
        b8=a['Player'].unique()
        # generates a list of the players who match the criteria
        default()
        # sets query to default for next question
        return q2,q3
        # asks the question that will be visible in the game
    def r3c3():
        global b9,q2,q4
        # makes variable that contains all answers and also the question that is asked global
        q2=qr2()
        # runs the second randomized question
        q4=qr4()
        # runs the fourth randomized question
        a = query_stats(points, assists, blocks, steals, rebounds, points_, assists_, blocks_, steals_, rebounds_, thr_pt_pct, thr_pt, ft_pct, team1, team2, pos, mvp)
        # runs the questions through the query
        b9=a['Player'].unique()
        # generates a list of the players who match the criteria
        default()
        # sets query to default for next question
        return q2,q4
        # asks the question that will be visible in the game
    
    
def create_game():
    """
    Function that will create a new game when ran
    Also checks to make sure that each question has answers
    """
    default()
    # sets all stats to default
    rand_question()
    # runs function to generate the randomized questions
    f=Game.r1c1(),Game.r1c2(),Game.r1c3(),Game.r2c1(),Game.r2c2(),Game.r2c3(),Game.r3c1(),Game.r3c2(),Game.r3c3()
    # runs all squares in gmae to compile a list of all players who match criteria
    min_ans = 5
    # the minimum amount of players the twp questions can have
    max_ans = 800
    # the max amount of players the questions can have to make it more challenging
    ans_len = (min_ans < len(list(b1)) < max_ans and min_ans < len(list(b2)) < max_ans and min_ans < len(list(b3)) < max_ans
               and min_ans < len(list(b4)) < max_ans and min_ans < len(list(b5)) < max_ans and min_ans < len(list(b6)) < max_ans 
               and min_ans < len(list(b7)) < max_ans and min_ans < len(list(b8)) < max_ans and min_ans < len(list(b9)) < max_ans)
    # checks the length of each answer to make sure they are within the boundaries
    if None in (qr1(),qr2(),qr3(),qr4()):
        # checks to see if there no question is asked due to randomly choosing
        print ("None")
        # used to let user know the game is invalid
        return create_game()
        # runs the create_game function to get a new game
    if  ans_len == True:
        # if the game meets all the conditions
        print("valid game")
        # lets user know the game can be played
        return f
        # outputs the game
    else:
        print("invalid and retried")
        # lets the user know the game cannot be played
        random_var()
        # randomizes the variables for questions
        return create_game()
        #creates a new game with new questions and variables