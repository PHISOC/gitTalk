from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from django.http import JsonResponse
import requests
import urllib3
import json
import math
import time
import re
import os
from bs4 import BeautifulSoup
from django.http import HttpResponse




def bodogScraper(request):
	gamesList = bodog_run_me()
	print(gamesList)
	return HttpResponse(json.dumps(gamesList),content_type = 'application/json; charset=utf8')



def bet365Scraper(request):
	gamesList = bet365_run_me()
	print(gamesList)
	return HttpResponse(gamesList)

def williamHillScraper(request):
	gamesList = run_me()
	print(gamesList)
	return HttpResponse(json.dumps(gamesList),content_type = 'application/json; charset=utf8')

def baseballSportsInteractionScraper(request):
	gamesList = si_run_me()
	print(gamesList)
	return HttpResponse(json.dumps(gamesList),content_type = 'application/json; charset=utf8')

def baseballBodogScraper(request):
	teamsList=[]
	moneyLineList = []
	gamesList = [] 
	team_id_list = []

	# GOOGLE CHROME HEADER

	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')  # Last I checked this was necessary.
	browser = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options)
	# browser = webdriver.Chrome()

	# browser = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
	# browser.get("https://mobile.bet365.com/#type=Coupon;key=16-20525425-48-1-36-0-0-0-1-0-0-4405-0-0-1-0-0-0-0-0-1096-0-0;ip=0;lng=1;anim=1")
	browser.get("https://www.888sport.com/baseball/baseball-betting.htm#/filter/baseball")

	# wait = WebDriverWait(browser,60)
	time.sleep(30)# waiting for 5 seconds before fetching the source
	src = browser.page_source
	print("HELLO")

	page = BeautifulSoup(src,"html.parser")
	
	allFields = page.findAll('div', class_='KambiBC-bet-offer__outcomes')

	teamNames = page.findAll('div', class_='KambiBC-mod-outcome__label-wrapper')

	gameOdds = page.findAll('div', class_='KambiBC-mod-outcome__odds-wrapper')
# 	# print(page)
# 	game_names= large_table.findAll('td',class_='game-name name')

# 	game_moneyline = large_table.findAll('td',class_='oddTip game-moneyline')

# 	team_names = page.findAll('td',class_='game-name name')

# 	# team_identifiers = page.findAll("div", {"id": "runnerNames"})

# 	for odd in team_names:
# 		# print(p)
# 		a= odd.text.strip("\n").split("\n\n")
# 		team_id_list.append(a[0])

# #Adds names of team for json payload identifier 

	for names in teamNames:
		# print(str(names.text))
		a = str(names.text)
		teamsList.append(a)

# #Adds moneyline of team for json payload identifier 
	for odd in gameOdds:
		print(str(odd.text))
		moneyLineList.append(str(odd.text))

	browser.close()


# 	#Finds the number of games
	game_number = int(math.ceil((len(moneyLineList)+1)/2))
	i=0
	q=0
	for i in range (0,game_number-1):
		# k = i + 1
		# gameStr = 'game'+str(k)  
		finalObj = {'game': {'team_1':teamsList[q],'odd_1':moneyLineList[q],'team_2':teamsList[q+1],'odd_2':moneyLineList[q+1]},'total':game_number,'name':'Bet888'} 
		print(finalObj)
		gamesList.append(finalObj)
		q=q+2
		# print(gameStr)
# 	print("we out here")
# 	print(gamesList)

	return HttpResponse(gamesList)



def baseballPinnacleScraper(request):
	teamsList=[]
	moneyLineList = []
	gamesList = [] 
	team_id_list = []

	# browser = webdriver.PhantomJS()

	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')  # Last I checked this was necessary.
	browser = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options)


	browser.get("https://www.pinnacle.com/en/odds/match/baseball/usa/mlb?sport=True")
	page = BeautifulSoup(browser.page_source,"html.parser")
	
	large_table = page.find('table', class_='odds-data')
	# print(page)
	game_names= large_table.findAll('td',class_='game-name name')

	game_moneyline = large_table.findAll('td',class_='oddTip game-moneyline')

	team_names = page.findAll('td',class_='game-name name')

	# team_identifiers = page.findAll("div", {"id": "runnerNames"})

	for odd in team_names:
		# print(p)
		a= odd.text.strip("\n").split("\n\n")
		team_id_list.append(a[0])

#Adds names of team for json payload identifier 
	for names in game_names:
		# print(str(names.text))
		a = str(names.text).strip('\n')
		a.rstrip()
		teamsList.append(a)

#Adds moneyline of team for json payload identifier 
	for odd in game_moneyline:
		print(str(odd.text))
		moneyLineList.append(str(odd.text).strip('\n'))


	browser.close()
	#Finds the number of games
	game_number = int(math.ceil((len(moneyLineList)+1)/2))
	i=0
	q=0
	for i in range (0,game_number-1):
		k = i + 1
		# gameStr = 'game'+str(k)  
		finalObj = {'game': {'team_1':teamsList[q],'odd_1':moneyLineList[q],'team_2':teamsList[q+1],'odd_2':moneyLineList[q+1]},'index':i,'total':game_number,'name':'Pinnacle','team_id':team_id_list[q]} 
		gamesList.append(finalObj)
		q=q+2
		# print(gameStr)
	print("we out here")
	print(gamesList)

	return HttpResponse(json.dumps(gamesList),content_type = 'application/json; charset=utf8')



# def testPinnacle (request):
# 	teamsList=[]
# 	moneyLineList = []
# 	finalList= []
# 	a = "TIMMY"
# 	gamesList = [] 
# 	team_id_list = []
# 	browser = webdriver.PhantomJS()
# 	browser.get("https://www.pinnacle.com/en/odds/match/baseball/usa/mlb?sport=True")
# 	page = BeautifulSoup(browser.page_source,"html.parser")
	

# 	team_names = page.findAll('td',class_='game-name name')

# 	for odd in team_names:
# 		print(p)
# 		a= odd.text.split("\n\n")
# 		team_id_list.append(a[0])


# 	return HttpResponse(game_names)


def test (request):
	teamsList=[]
	moneyLineList = []
	finalList= []
	a = "TIMMY"
	gamesList = [] 
	browser = webdriver.PhantomJS()
	browser.get("https://www.sportsinteraction.com/baseball/mlb-betting-lines/")
	page = BeautifulSoup(browser.page_source,"html.parser")
	

	# large_table = page.find('table', class_='odds-data')
	# game_names = page.findAll('span',class_='price wide')

	game_identifiers = page.findAll("div", {"id": "runnerNames"})
	p=0
	for odd in game_identifiers:
		print(p)
		a= odd.text.split(":")
		print(str(a[0]))
		p=p+1

	# print(game_names)

	return HttpResponse(game_identifiers)



def pinnacleScraper(request):

	teamsList=[]
	moneyLineList = []
	browser = webdriver.PhantomJS()
	browser.get("https://www.pinnacle.com/en/odds/match/basketball/usa/nba?sport=True")
	page = BeautifulSoup(browser.page_source,"html.parser")
	
	large_table = page.find('table', class_='odds-data')
	# print(page)
	print("TIMMMYYYY")
	game_names= large_table.findAll('td',class_='game-name name')

	game_moneyline = large_table.findAll('td',class_='oddTip game-moneyline')

	for names in game_names:
		teamsList.append(str(names.text))

	for odd in game_moneyline:
		print(str(odd.text))
		moneyLineList.append(str(odd.text))

	browser.close()

	resp = "TIMMY"

	return HttpResponse(game_names)



def Scraper888(request):

	#Method 4 Working with Pinnacle Example:
	teamsList=[]
	moneyLineList = []
	browser = webdriver.PhantomJS()
	browser.get("https://www.888sport.com/#/filter/basketball")
	page = BeautifulSoup(browser.page_source,"html.parser")
	
	large_table = page.find('div', class_='KambiBC-collapsible-content KambiBC-mod-event-group-event-container')
	# print(page)
	print(large_table)

	print("TIMMMYYYY")
	# game_names = large_table.findAll(class_='KambiBC-bet-offer__outcomes')

	# for i in game_names:
	# 	print(i);

	# game_moneyline = large_table.findAll('td',class_='oddTip game-moneyline')

	# for names in game_names:
	# 	teamsList.append(str(names.text))

	# for odd in game_moneyline:
	# 	print(str(odd.text))
	# 	moneyLineList.append(str(odd.text))

	browser.close()

	resp = "TIMMY"


	return HttpResponse(large_table)






#WILLIAM HILL SCRAPER FUNCTIONS

def get_table(url):
    response = requests.get(url)
    # print(response.content)
    Soup = BeautifulSoup(response.content, 'html.parser')
    tables = Soup.findAll('table')
    mlbTable = ''
    for table in tables:
        if (table.findAll('tr')[0].text.replace(' ', '').replace('\n', '') == 'MLB') and ('Money Line' in table.findAll('tr')[1].text) and ('Run Line' in table.findAll('tr')[1].text) and ('Total Runs' in table.findAll('tr')[1].text):
            mlbTable = table
    if mlbTable != '':
        return mlbTable
    else:
        exit("WARNING: Table invisible")




def wh_make_json(teamList_1, teamList_2):
    date, time, team_1, winOdd_1, runPref, runOdd_1, overPref, overOdd = teamList_1
    team_2, winOdd_2, _, runOdd_2, underPref, underOdd = teamList_2
    gameJson = {
        'team_1': team_1,
        'team_2': team_2,
        'winn_odd_1': winOdd_1,
        'winn_odd_2': winOdd_2,
        'run_pref': runPref[1:],
        'run_odd_1': runOdd_1,
        'run_odd_2': runOdd_2,
        'over_pref': overPref[1:],
        'over_odd': overOdd,
        'under_pref': underPref[1:],
        'under_odd': underOdd,
        'date': date,
        'time': time
    }
    return gameJson


def add_total(data):
    new_data = []
    total = len(data)
    for item in data:
        item['total'] = total
        new_data.append(item)
    return new_data

def process_content(table):
    rows = table.findAll('tr')[2:]
    DATA = []
    index = 0
    for i in range(0, len(rows), 2):
        teamList_1 = []
        teamList_2 = []
        cols_1 = rows[i].findAll('td')
        cols_2 = rows[i + 1].findAll('td')
        for j in range(8):
            teamList_1.append(cols_1[j].text.replace('\n', '').replace('\t', '').replace(' ', ''))
            teamList_2.append(cols_2[j].text.replace('\n', '').replace('\t', '').replace(' ', ''))
        date = teamList_1[0]
        team_1 = teamList_1[2]
        if (len(date) > 0) and (date != 'Live'):
            gameJson = {
                'game': wh_make_json(teamList_1[:8], teamList_2[2:8]),
                'index': index,
                'name': 'WilliamHill',
                'team_id': re.sub('\(.*\)', '', team_1)
            }
            DATA.append(gameJson)
            index += 1
    # newDATA = add_total(DATA)
    # if len(newDATA) > 0:
    #     with open('william.json', 'w') as out:
    #         out.write(str(newDATA))
    # else:
    #     print('INFO: No games today')
    # print(DATA)

    return DATA

def run_me():
    url = 'http://sports.williamhill.com/bet/en-gb/betting/y/2/mh/Baseball.html'
    table = get_table(url)
    data = process_content(table)
    return data

#BET365 Scraper

# def bet365_run_me():
#     Bet = Bet365()
#     Bet.connect()
#     time.sleep(1)
#     Bet.link_to("Baseball")
#     Bet.go_to_lines()

#     time.sleep(5)

#     Bet.process_rows()
#     DATA = []
#     index = 0
#     total = len(list(Bet.tmpJson.keys()))
#     for team_id in Bet.tmpJson.keys():
#         gameJson = {}
#         gameJson['team_id'] = team_id
#         gameJson['index'] = index
#         gameJson['total'] = total
#         gameJson['game'] = Bet.tmpJson[team_id]
#         index += 1
#         DATA.append(gameJson)
#     # with open('bet365.json', 'w') as out:
#     #     json.dump(DATA, out)
#     return DATA



# class Bet365:
#     def __init__(self):
#         self.url = ""
#         # self.options = Options()
#         # self.options.add_argument("--headless")
#         # self.geckodriver = os.path.join(os.getcwd(), 'Drivers', 'geckodriver')
#         self.driver = webdriver.PhantomJS()
#         self.tmpJson = {}

#     def connect(self):
#         self.driver.get("https://mobile.bet365.com/")
#         try:
#             WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
#                         (By.XPATH, "//div[@class='sb-SportsItem_Truncator ' and contains(text(), '%s')]" % 'Baseball')))        #     return "INFO:  Connected successfully."
#         except:
#             print("ERROR: Can't connect")

#     def link_to(self, sport):
#         try:
#             WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
#                 (By.XPATH, "//div[@class='sb-SportsItem_Truncator ' and contains(text(), '%s')]" % sport ))).click()
#             print("INFO:  Scraper linked to %s" % sport)
#         except:
#             return("ERROR:  Can't link scraper to %s.\n\tPlease check internet connection.!" % sport)


#     def go_to_lines(self):
#         WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
#             (By.CLASS_NAME, "enhancedPod")))
#         mlbBox = self.driver.find_element_by_class_name("enhancedPod")

#         WebDriverWait(mlbBox, 30).until(EC.presence_of_element_located(
#             (By.CLASS_NAME, "eventWrapper")))
#         childBox = mlbBox.find_element_by_class_name('eventWrapper')

#         childs = childBox.find_elements_by_xpath(".//*")
#         lines = childs[0]

#         try:
#             lines.click()
#             WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
#                 (By.XPATH, "//*[contains(text(), 'Game Lines')]"))).click()
#         except:
#             print("Can't open lines: Trying again.")
#             lines.click()
#             WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
#                 (By.XPATH, "//*[contains(text(), 'Game Lines')]"))).click()

#         try:
#             WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
#                 (By.CLASS_NAME, "podEventRow")))
#         except:
#             print('Data invisible. Trying to click again')
#             WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
#                 (By.XPATH, "//*[contains(text(), 'Game Lines')]"))).click()
#             WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
#                 (By.CLASS_NAME, "podEventRow")))


#     def make_json(self, tab, data_list):
#         if len(data_list) < 3:
#             return
#         team_name_1, pitcher_1, team_name_2, pitcher_2, start_time = data_list[:5]
#         if len(pitcher_1) > 3:
#             if team_name_1 not in self.tmpJson:
#                 self.tmpJson[team_name_1] = {
#                     'team_1': '%s(%s)' % (team_name_1, pitcher_1),
#                     'team_2': '%s(%s)' % (team_name_2, pitcher_2),
#                     'time': start_time
#                 }
#             if tab == 'Run Line':
#                 run_pref, run_odd_1, _, run_odd_2 = data_list[6:]
#                 self.tmpJson[team_name_1]['run_pref'] = run_pref
#                 self.tmpJson[team_name_1]['run_odd_1'] = run_odd_1
#                 self.tmpJson[team_name_1]['run_odd_2'] = run_odd_2
#             elif tab == 'Total':
#                 over_under_pref, over_odd, _, under_odd = data_list[6:]
#                 self.tmpJson[team_name_1]['over_under_pref'] = over_under_pref
#                 self.tmpJson[team_name_1]['over_odd'] = over_odd
#                 self.tmpJson[team_name_1]['under_odd'] = under_odd
#             elif tab == 'Money Line':
#                 win_odd_1, win_odd_2 = data_list[6:]
#                 self.tmpJson[team_name_1]['win_odd_1'] = win_odd_1
#                 self.tmpJson[team_name_1]['win_odd_2'] = win_odd_2
#             else:
#                 print('Something is wrong')

#     def process_rows(self):
#         rows = self.driver.find_elements_by_class_name('podEventRow')
#         # rows = self.driver.findAll('div', class_='podEventRow')
#         flag = (len(rows) / 3) - 1
#         tabs = ['Run Line', 'Total', 'Money Line']
#         tab = 0
#         i = 0
#         while i <= len(rows) - 1:
#             row = rows[i]
#             if 'OTB' in row.text:
#                 print('WARNING: OTB')
#             else:
#                 pass
#                 self.make_json(tabs[tab], row.text.split('\n'))
#             if i == flag:
#                 tab += 1
#                 self.change_to(tabs[tab])
#                 flag *= 2
#             i += 1

#     def change_to(self, type):

#         tab = self.driver.find_element_by_xpath("//div[@class='enhancedTab' and contains(text(), '%s')]" % type)
#         tab.click()
#         time.sleep(1)
#         print('Changed to %s' % type)


#BODOG STUFF STARTS HERE


def get_data_from_bodog():
    url = 'https://www.bodog.eu/sports/baseball/mlb/game-lines-market-group'
    headers = {'Content-type': 'application/x-www-form-urlencoded',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8',
               'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return response.text



def get_json_from_content(html):
    marketJsonSearch = re.search("var swc_market_lists = (.*?)</script>", html)
    print("DICKKK")
    print(marketJsonSearch)
    marketJson = json.loads(marketJsonSearch.group(1))
    return marketJson['items'][0]['itemList']['items']


def make_game_json(game):
    gameJson = {}
    team_name_1 = game['competitors'][0]['description']
    team_name_2 = game['competitors'][1]['description']
    if 'opponentAName' in game:
        pitcher_1 = game['opponentAName']
    else:
        pitcher_1 = 'N/A'

    if 'opponentBName' in game:
        pitcher_2 = game['opponentBName']
    else:
        pitcher_2 = 'N/A'
    gameJson['team_id'] = team_name_1
    gameJson['name'] = 'Bodog'
    gameJson['game'] = {}
    gameJson['game']['team_1'] = '%s(%s)' % (team_name_1, pitcher_1)
    gameJson['game']['team_2'] = '%s(%s)' % (team_name_2, pitcher_2)
    for market in game['displayGroups'][0]['itemList']:
        marketType = market['description']
        if marketType == 'Moneyline':
            if 'price' in market['outcomes'][0]:
                win_odd_1 = market['outcomes'][0]['price']['decimal']
                win_odd_2 = market['outcomes'][1]['price']['decimal']
                gameJson['game']['win_odd_1'] = win_odd_1
                gameJson['game']['win_odd_2'] = win_odd_2
        elif marketType == 'Runline':
            if 'price' in market['outcomes'][0]:
                run_pref = market['outcomes'][0]['price']['handicap']
                run_odd_1 = market['outcomes'][0]['price']['decimal']
                run_odd_2 = market['outcomes'][1]['price']['decimal']
                gameJson['game']['run_pref'] = run_pref
                gameJson['game']['run_odd_1'] = run_odd_1
                gameJson['game']['run_odd_2'] = run_odd_2
        elif marketType == 'Total':
            if 'price' in market['outcomes'][0]:
                over_under_pref = market['outcomes'][0]['price']['handicap']
                over_odd = market['outcomes'][0]['price']['decimal']
                under_odd = market['outcomes'][1]['price']['decimal']
                gameJson['game']['over_under_pref'] = over_under_pref
                gameJson['game']['over_odd'] = over_odd
                gameJson['game']['under_odd'] = under_odd
    return gameJson


def bodog_run_me():

    bodogJson = get_json_from_content(get_data_from_bodog())
    DATA = []
    index = 0
    for game in bodogJson:
        game_json = make_game_json(game)
        if 'win_odd_1' in game_json['game']:
            game_json['index'] = index
            DATA.append(game_json)
            index += 1
        time.sleep(0.3)
    total = len(DATA)
    for game in DATA:
        game['total'] = total
    # with open('bodogv2.json', 'w') as out:
    #     json.dump(DATA, out)
    return DATA


#SPORTS INTERACTION SCRAPER------------------------------------------------------------------------------------------


def si_get_page_source(url):
    headers = {'Content-type': 'application/x-www-form-urlencoded',
               'Accept': 'text/plain',
               'Content-Encoding': 'utf-8',
               'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return response.text


def si_get_game_lines(html):
    Soup = BeautifulSoup(html, 'html.parser')
    gameLines = Soup.findAll('div', {'class': 'game'})
    total = len(gameLines)
    if total > 0:
        date = gameLines[0].find('span', {'class': 'date'})
        DATA = []
        for index in range(len(gameLines)):
            gameJson = si_make_json(gameLines[index], index, total, date)
            DATA.append(gameJson)
    return DATA


def si_make_json(game, index, totalNum, date):
    home, away = game.find('div', {'id': 'runnerNames'}).findAll('li')
    print("TESSSSST---------------")
    print(home)
    print("AWAAAY----------")
    print(away)
    # print(game.findAll('div', {'class': 'betTypeContent'}))
    runLine, moneyLine, total = game.findAll('div', {'class': 'betTypeContent'})
    run_pref = runLine.find('span', {'class': 'handicap'})
    # print("DICKLE")
    # print(run_pref.text)
    run_odd_1, run_odd_2 = runLine.findAll('span', {'class': 'price'})
    win_odd_1, win_odd_2 = moneyLine.findAll('span', {'class': 'price'})
    over_under_pref = total.find('span', {'class': 'handicap'})
    over_odd, under_odd = total.findAll('span', {'class': 'price'})
    startTime = game.find('span', {'class': 'time'})
    gameJson = {}
    gameJson['index'] = index
    gameJson['total'] = totalNum
    gameJson['date'] = date.text.replace('\t', '').replace('\n', '')
    gameJson['name'] = 'SportsInteraction'
    gameJson['team_id'] = home.text.replace('\t', '').replace('\n', '').split(':')[0].replace('\r', '')
    gameJson['game'] = {}
    gameJson['game']['time'] = startTime.text.replace('\t', '').replace('\n', '').replace('\r', '')
    gameJson['game']['team_1'] = home.text.replace('\t', '').replace('\n', '').replace('\r', '')
    gameJson['game']['team_2'] = away.text.replace('\t', '').replace('\n', '').replace('\r', '')
    if run_pref is None:
         gameJson['game']['run_pref'] = "N/A"
    else:
        gameJson['game']['run_pref'] = run_pref.text.replace('\t', '').replace('\n', '').replace(' ', '').replace('-', '').replace('\r', '')
    gameJson['game']['run_odd_1'] = run_odd_1.text.replace('\t', '').replace('\n', '')
    gameJson['game']['run_odd_2'] = run_odd_2.text.replace('\t', '').replace('\n', '')
    gameJson['game']['win_odd_1'] = win_odd_1.text.replace('\t', '').replace('\n', '')
    gameJson['game']['win_odd_2'] = win_odd_2.text.replace('\t', '').replace('\n', '')
    if over_under_pref is None:
        gameJson['game']['over_under_pref'] = "N/A"
    else:
        gameJson['game']['over_under_pref'] = over_under_pref.text.replace('\t', '').replace('\n', '').replace(' ', '').replace('+', '').replace('\r', '')

    gameJson['game']['over_odd'] = over_odd.text.replace('\t', '').replace('\n', '')
    gameJson['game']['under_odd'] = under_odd.text.replace('\t', '').replace('\n', '')
    
    return gameJson

def si_run_me():
    url = 'https://www.sportsinteraction.com/baseball/mlb-betting-lines/'
    url2= 'https://www.sportsinteraction.com/baseball/national-league-betting-lines/'
    html = si_get_page_source(url)
    DATA = si_get_game_lines(html)
    html2 = si_get_page_source(url2)
    DATA2 = si_get_game_lines(html2) 
    DATA3 = DATA + DATA2
    return DATA3