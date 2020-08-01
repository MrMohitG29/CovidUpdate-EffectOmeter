from Covid19ApiWrapper import *
from urllib.request import urlopen , Request
from bs4 import BeautifulSoup



def coro():
    x = covidUpdate(BOOL_country_data=True)
    Data = x.countryData
    c = []
    si = []
    req = Request('https://www.mygov.in/covid-19' , headers = {'User-Agent' : 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage)
    l = []
    m = []
    for link in soup.find_all('div', class_ = 'views-row' ,href=False):
        for i in link.get_text().split('\n'):
            if i != '':
                m.append(i)
        l.append(m)
    l = l[1]

    j = 0
    for i in Data:
        c.append([i , Data[i]['cases'] , Data[i]['todayCases'] , Data[i]['deaths'] , Data[i]['todayDeaths'] , Data[i]['recovered'] , Data[i]['active'] , Data[i]['tests'] , Data[i]['critical']])

        if j < len(l):
            si.append([l[j] , l[j+2].split(' ')[1] , l[j+3].split(' ')[1] , l[j+4].split(' ')[1] , l[j+5].split(' ')[1]])
        j += 6

    l = [x.totalCases, x.totalDeaths, x.totalCases - x.totalDeaths - x.totalRecovered,x.totalRecovered]


    return [sorted(c, key = lambda x: x[1])[::-1],si,l]
