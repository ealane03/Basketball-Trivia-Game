# to run 
# scrapy crawl team_spider -o team.csv

import scrapy
from scrapy.http.request import Request
import string
USER_AGENT='hoops-cool-project (https://www.sportslogos.net/teams/list_by_league/6/National_Basketball_Association/NBA/logos)'
class TeamSpider(scrapy.Spider):
    name = 'team1_spider'
    
    start_urls = ["https://www.sportslogos.net/teams/list_by_league/6/National_Basketball_Association/NBA/logos"]
    def parse(self, response):
        '''
        Hardcode from initial homepage to players page.
        Call parse_players function on players page.
        
        No output. 
        '''
        team_logo = response.css("div.section[id=team] ul.logoWall img::attr(src)").extract()
        for i in range(30):
            yield {"team":team_logo[i]} # callback next function
