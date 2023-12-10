import urllib.request 
from PIL import Image
import pandas as pd
import sqlite3 # for accessing SQL database

def clean_data():
    """
    Cleans the data from the scraper
    """
    data = sqlite3.connect("data2.db") # create/access database

    # following code will be cleaning data from the scraping
    url = "NBA_Player_Stats_2.csv"
    stats = pd.read_csv(url)
    # reads the csv file and stores it in data

    stats = stats.drop({"PF", "Age", "FGA", "GS", "G", "DRB", "3PA", "2P", "2PA", "2P%", "eFG%", "FTA", "ORB", "DRB"}, axis = 1)
    # Drops all data that won't be used for the game
    # Can always remove to add more questions and challenge to the game

    stats["Tm"] = stats["Tm"].replace({ "SEA" : "OKC", "NJN" : "BRK", "CHO" : "CHH", "NOK" : "NOP", "NOH" : "NOP", "CHA" : "CHH"})
    # renamed the teams to their current team name 
    # this was due to teams changing locations or names

    stats = stats.rename(columns = {"FT%":"FT_P", "3P%":"THRP_P","3P":"THRP", "FG%":"FG_P"})
    # renames certain columns since they contain characters that SQL query does not recognize

    stats = stats[stats['Tm'] != "TOT"]
    # removes any player that played on multiple teams in a season


    stats.to_sql("stats", data, if_exists = "replace", index = False)

    cursor = data.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")


    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
    cursor.close()
    data.close()
    return stats


def game_pics():
    """
    Downloads all needed pictures of teams and background to create the game
    """
    d = ['ATL','BOS','BRK','CHH','CHI','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP',
     'NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
    # list of all abbreviations of teams
    url = "team.csv"
    teams = pd.read_csv(url)
    # pulls the csv that contains link to image of each team
    for i in range(30):
        #iterates through each team to download and names the pictures
        urllib.request.urlretrieve(teams["team"][i], f"{d[i]}.png") 

    url1 = "https://wallpapers.com/images/hd/solid-background-zqysjfi6yvy57cc8.jpg"
    # link to image we used for background
    urllib.request.urlretrieve(url1, "background.jpg") 
    # downloads and names the background image