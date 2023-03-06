import requests
from bs4 import BeautifulSoup


webPage = 'https://www.pro-football-reference.com/boxscores/202209110crd.htm#all_pbp'
while(True):
    webPage = input('give me a link or type in anything else to make this crash and exit\n')
    page = requests.get(webPage)

    fieldPos = []
    toGo = []
    down = []
    time = []
    quarter = []
    punter = []
    awayScore = []
    homeScore =[]
    

    soup = BeautifulSoup(page.content, 'html.parser')
    divSoup = soup.find('div', {'id':"all_pbp", 'class':"table_wrapper"})
    num = 0

   # print(divSoup.prettify())
    with open('foog.txt', 'w') as f:
        f.write(divSoup.prettify())
    f.close()


    foog =  open('foog.txt', 'r')
    lines = foog.readlines()

    count = 0
    for i in lines:
        if 'punts' in i:
            quarter.append(i[(i.find("quarter") + 10)])
            num = (i.find("qtr_time_remain"))
            time.append(i[num + 40:num + 46])
            num = (i.find("yds_to_go"))
            toGo.append(i[num + 12:num+14])
            num = (i.find("location"))
            fieldPos.append(i[num+19:num+26])
            num = (i.find("data-stat=\"down\""))
            down.append(i[num+18])
            num = (i.find('.htm'))
            num2 = (i.find('punts'))
            punter.append(i[num+6:num2-5])
            num = i.find("pbp_score_aw")
            awayScore.append(i[num+15:num+17])
            num = i.find("pbp_score_hm")
            homeScore.append(i[num+15:num+17])


    for i in range(len(down)):
        time[i] = time[i].replace(">", "")
        time[i] = time[i].replace("<", "")
        time[i] = time[i].replace("/", "")

        fieldPos[i] = fieldPos[i].replace(">", "")
        fieldPos[i] = fieldPos[i].replace("<", "")
        fieldPos[i] = fieldPos[i].replace("/", "")

        toGo[i] = toGo[i].replace(">", "")
        toGo[i] = toGo[i].replace("<", "")
        toGo[i] = toGo[i].replace("/", "")

        awayScore[i] = awayScore[i].replace(">", "")
        awayScore[i] = awayScore[i].replace("<", "")
        awayScore[i] = awayScore[i].replace("/", "")

        homeScore[i] = homeScore[i].replace(">", "")
        homeScore[i] = homeScore[i].replace("<", "")
        homeScore[i] = homeScore[i].replace("/", "")

    big = 0
    
    for j in punter:
        if len(j) >= big:
            big = len(j)
        else:
            small = j

    j = 0
    
    for j in range(len(punter)):
        if len(punter[j]) < big:
            diff = big - len(punter[j])
            for k in range(diff):
                punter[j] += " "
        if len(str(toGo[j])) == 1:
            toGo[j] = str(toGo[j]) + " "
        if len(str(fieldPos[j])) == 5:
            fieldPos[j] = str(fieldPos[j]) + " "
    
    j = 0
    for j in range(len(time)):
        if len(time[j]) < 5:
            time[j] = time[j] + " "
           
    print("\nq".ljust(len(quarter[i]) + 2, ' ') + " time".ljust(2, ' ') + "    down".ljust(len(down[i]) + 2, ' ') + "   y2g".ljust(len(toGo[i]) + 2, ' ') + "    fieldPos".ljust(len(fieldPos[i]) + 2, ' ') + "   punter".ljust(big + 2, ' ') + "     score".ljust((2 *len(awayScore[i])) + 2, ' '))

    for i in range(len(quarter)):
        print(quarter[i] + "  " + time[i] + "   " + down[i] + "      " + toGo[i] +  "     " + fieldPos[i] + "     " + punter[i] + "    " + awayScore[i] + "-" + homeScore[i])
    
        
            

           
#pbpSoup = pbpSoup.find('table', {'id':"pbp"})
#pbpSoup = pbpSoup.find('tbody')
#tr_soup = pbpSoup.find('tr')
