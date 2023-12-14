# to run player data
# scrapy crawl hoops_spider -o NBA_Player_Stats_2.csv

# to run team logo scraper
# scrapy crawl team_spider -o team.csv


import scrapy
from scrapy.http.request import Request
import string
USER_AGENT='hoops-cool-project (https://www.basketball-reference.com/players/a/abdelal01.html)'
class HoopsSpider(scrapy.Spider):
    name = 'hoops_spider'
    
    start_urls = ["https://www.basketball-reference.com"]
    def parse(self, response):
        '''
        Hardcode from initial homepage to players page.
        Call parse_players function on players page.
        
        No output. 
        '''
        players_url = response.url + "/players/" # use to navigate to players page
        yield scrapy.Request(players_url, callback = self.parse_players) # callback next function
        
    def parse_players(self,response):
        '''
        Begin at players page, collect links to pages showing lists of all nba players by letter of last name
        For each group of players, call next function.
        
        No output.
        '''
        prefix = "https://www.basketball-reference.com/players/"
        suffix = list(string.ascii_lowercase) 
        # used to go through entire alphabet to extract all players
        for a in suffix:
            alph_url = prefix + a + "/"
            # results in url to basketball reference page that is sorted by alphabet
            yield scrapy.Request(alph_url, callback = self.parse_player_by_alph) # callback next function for each player list    
    def parse_player_by_alph(self,response):
        """
        Begin at player page by alphabet, collects links to players pages
        Will call next function to scrape player page
        
        No output
        """
        prefix = "https://www.basketball-reference.com"
        player_suffix = response.css("th.left a::attr(href)").getall()
        # link to player player info page
        for suffix in player_suffix:
            # iterates through each player page
            player_url = prefix + suffix
            yield scrapy.Request(player_url, callback = self.parse_player_stats)      
            
    def parse_player_stats(self,response):
        """
        Starting at a specific player page, collects all needed data from table
        Outputs a table that contains all data
        """
        for i in range(0,22):
            # iterates through the entire table
            if response.css(f"tr.full_table th.left:nth-of-type({i}) a::text").get() == "":
                # used if players didn't play for 22 years to prevent blanks when scraping
                break
            else:
                # scrapes all data individually
                yield{
                "Season":response.css(f"tr.full_table th.left:nth-of-type({i}) a::text").get(), #years
                "Tms":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.left[data-stat=team_id] a::text").get(), #teams
                "Pos":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.center[data-stat=pos]::text").get(), #pos
                "G":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=g]::text").get(), #
                "GS":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=gs]::text").get(), #
                "MP":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=mp_per_g]::text").get(), #
                "FG":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=fg_per_g]::text").get(), #
                "FGA":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=fga_per_g]::text").get(), #
                "FG%":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=fg_pct]::text").get(), #
                "3P":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=fg3_per_g]::text").get(), #
                "3PA":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=fg3a_per_g]::text").get(), #
                "3P%":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=fg3_pct]::text").get(), #
                "2P":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=fg2_per_g]::text").get(), #
                "2PA":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=fg2a_per_g]::text").get(), #
                "2P%":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=fg2_pct]::text").get(), #
                "eFG%":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=efg_pct]::text").get(), #
                "FT":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=ft_per_g]::text").get(), #
                "FTA":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=fta_per_g]::text").get(), #
                "FT%":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=ft_pct]::text").get(), #
                "ORB":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=orb_per_g]::text").get(), #
                "DRB":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=drb_per_g]::text").get(), #
                "TRB":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=trb_per_g]::text").get(), #
                "AST":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=ast_per_g]::text").get(), #
                "STL":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=stl_per_g]::text").get(), #
                "BLK":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=blk_per_g]::text").get(), #
                "TOV":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=tov_per_g]::text").get(), #
                "PF":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=pf_per_g]::text").get(), #
                "PTS":response.css(f"#per_game tbody tr.full_table:nth-of-type({i}) td.right[data-stat=pts_per_g]::text").get() #
                }

class TeamSpider(scrapy.Spider):
    name = 'team_spider'
    
    start_urls = ["https://www.sportslogos.net/teams/list_by_league/6/National_Basketball_Association/NBA/logos"]
    def parse(self, response):
        '''
        Extracts the link to the logo of each image
        Returns a dictionary containing a list of all teams in alphabetical order
        '''
        team_logo = response.css("div.section[id=team] ul.logoWall img::attr(src)").extract()
        # extracts the logos link
        for i in range(30):
            yield {"team":team_logo[i]} # callback next function
