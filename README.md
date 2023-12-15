# __Basketball-Trivia-Game__

## DESCRIPTION
Welcome to our project! Our project is going to be a game called Basketball Trivia! Basketball Trivia is a great game where you can put your knowledge of the National Basketball Association (NBA) to the test. The way this game works is the player is going to be presented with a 3x3 grid with prompts/descriptions of either teams or statistics displayed on the horizontal and vertical sides of the grid. The goal of the game is to come up with a player name that corresponds to the descriptions on both the horizontal and vertical axes. 

## INSTRUCTIONS:
To run the game yourself, first clone this repository on your local computer using the following line:  
`git clone https://github.com/ealane03/Basketball-Trivia-Game.git && cd Basketball-Trivia-Game`

To install the package requirements on your local computer, use the following line:  
`conda create --name NEWENV --file requirements.txt`

To run the game, download `demo.ipynb` and run all cells.

## PROJECT TECHNICAL OVERVIEW

### Scraper
To start off we need to get the meat of our game: the statistics. To do that, we are going to webscrape the basketball-reference website. The basketball-reference website contains all the statistics we need in our project and more including the teams that the player has played for and their career averages in points, rebounds, assists, steals, blocks, shot percentages, etc. We are first going to start by creating our spider with the base website being the homepage of the basketball reference website. We can then create our first parsing function which serves the purpose of navigating from the home page of basketball-reference (as seen above) to the players page. This function does not output anything. Instead it ends by calling the next function. Upon the first parsing function finishing, the second parsing function will be called. This function starts at the players page on the basketball-reference website and collects the link of all the pages showing lists of letters of the alphabet in correspondence to the player's last name. Similar to the first function, this parsing function does not return an output, but instead calls our next parsing function. Our next parsing function starts on the page of the letters corresponding to the letter of the last name of each nba player. It then collects the links of the pages to each of the individual player's pages. Similarly to the previous two functions, the function does not have an output, and instead calls the next and final parsing function. For our final parsing function, we start on the individual player's pages. The function then serves to fetch the different statistics that we are interested in using. 
### Query
With all the data in the database cleaned, we can write SQL commands to filter for players that fit the criteria the user enters into the query. For all inputs that are integers or floats, the SQL command can easily handle math symbols like greater and less than. However, for strings like team or position, the command cannot filter the way we want it to and thus we created a separate code. After the command has handled the other inputs, we can then manually match for players depending on whether one or two teams are inputted. Using several if commands to handle all possible scenarios, we can filter properly for players and return a table of players and their stats who met the criteria.
### PyGame GUI
We'll create a GUI using `Pygame`. We make a 3x3 grid where each grid box accepts a user's input. Each input will be an answer to the question generated by the prompt on the left side of the grid and along the top of the grid. Our query code will have already run and generated 6 questions to create a 3x3 matrix of answers in the form of lists of player names. The user's answer will be checked against all names in the list and depending on correctness, there will be an output either 'correct' or 'incorrect'. Once the user has answered all 9 questions, the game will end and prompt the user to exit the game. 

## HOW TO PLAY
The goal of the game is to fill out all 9 squares with names of the players which entail to the descriptions that the game provides. Once the game has started you are able to click each square and enter the names of the players that you have a knowledge of. Once you are finished typing out the name, be sure to hit the enter key and the game will display a message of whether or not you were able to get the correct answer. Once you have completed answering all 9 squares of the grid, you are going to be prompted with an option to exit the game, by pressing X. 

![image](https://github.com/ealane03/Basketball-Trivia-Game/assets/146393991/f0735f5d-9536-402f-90cf-1a81b0f692db)

![image](https://github.com/ealane03/Basketball-Trivia-Game/assets/146393991/5794999c-adc4-4200-94c6-3af7c475a4e0)

## DATASET SOURCE
As our scraper faced difficulties scraping a complete dataset due to 403 errors and bot defenses, we used this dataset to simulate a .csv file outputted by our scraper: https://data.world/etocco/nba-player-stats (NBA player stats per game from the 1997-98 season through 2021-22 season)

## SCOPE, LIMITATIONS,  FINAL DISCUSSION
Our game successfully functions if given a completed dataset. However, we faced challenges scraping public websites and resorted to using a .csv file on the internet of NBA player data. The game in its current state only runs for one round before requring a reset and relies on exact spelling, punctuation, and capitalization of player names. Additional functionality to the game can be added, such as a recursive restart fuction, hint option, suggested text prompting, time limit, or the addition of different gamemodes implementing a score system. We were inspired to make this game by the popular online basketball trivia game [Immaculate Grid]([https://website-name.com](https://www.immaculategrid.com/basketball/mens)).

A group of people that can potentially benefit from Basketball Trivia is the NBA fanbase. This game is created as something that can be fun and enjoyable with a bit of competition to test your knowledge of the NBA with your friends. A group of people that might be harmed by this product is people that have been affected by these NBA players. Some of the NBA players, in the past or present, have been involved in particular scandals that could be offensive to some people.

## REFERENCES AND ACKNOWLEDGEMENTS: 
Basketball Reference: https://www.basketball-reference.com/  
Immaculate Grid: https://www.immaculategrid.com/basketball/mens

