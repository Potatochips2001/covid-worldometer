import requests

def cases(country_, state):
    r = requests.get('https://worldometers.info/coronavirus/{0}/{1}'.format(country_, state))
    t1 = r.text.find('<title>')
    t1 += 7
    t2 = r.text.find('</title>')
    covidCases = r.text[t1:t2]
    c1 = covidCases.find('Coronavirus: ')
    c1 += 13
    covidCases = covidCases.replace(',', '')
    covidCases = covidCases.replace(' (COVID-19 ) - Worldometer', '')
    z = r.text[t1:t2]
    z1 = int(z.find(": ")+2)
    z2 = int(z.find("and ")+4)
    z3 = int(z.find(" Deaths"))
    z4 = int(z.find(" Cases"))
    covidCases2 = z[z1:z4]
    covidDeaths = z[z2:z3]
    covidCases2 = covidCases2.replace(',', '')
    covidDeaths = covidDeaths.replace(',', '')
    lethalityRate = (int(covidDeaths) / int(covidCases2) * 100)
    lethalityRate = round(lethalityRate, 3)
    covidString = (str(covidCases) + " Lethality rate = " + str(lethalityRate) + "%")
    return covidString
def country(country_):
    r = requests.get('https://worldometers.info/coronavirus/country/{}'.format(country_))
    t1 = r.text.find('<title>')
    t1 += 7
    t2 = r.text.find('</title>')
    covidCases = r.text[t1:t2]
    c1 = covidCases.find('Coronavirus: ')
    c1 += 13
    covidCases = covidCases.replace(',', '')
    covidCases = covidCases.replace(' - Worldometer', '')
    z = r.text[t1:t2]
    z1 = int(z.find(": ")+2)
    z2 = int(z.find("and ")+4)
    z3 = int(z.find(" Deaths"))
    z4 = int(z.find(" Cases"))
    covidCases2 = z[z1:z4]
    covidDeaths = z[z2:z3]
    covidCases2 = covidCases2.replace(',', '')
    covidDeaths = covidDeaths.replace(',', '')
    lethalityRate = (int(covidDeaths) / int(covidCases2) * 100)
    lethalityRate = round(lethalityRate, 3)
    covidString = (str(covidCases) + " Lethality rate = " + str(lethalityRate) + "%")
    return covidString
