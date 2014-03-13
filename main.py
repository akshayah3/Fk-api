__author__ = 'Akshay'

import BeautifulSoup as bs
import requests
path = 'http://www.flipkart.com'
mobiles1 = ['samsung', 'nokia', 'apple', 'lg', 'micromax', 'maxx', 'htc', 'sony']

class Flipkart:

    def __init__(self):
        pass

class mobiles:
    mobiles1 = ['samsung', 'nokia', 'apple', 'lg', 'micromax', 'maxx', 'htc', 'sony']

    def __init__(self):
        pass

    def get_mobiles(self, mobile, number = 5):
        if mobile in mobiles1:
            request = requests.get(path + '/mobiles/' + mobile +'~brand/pr?sid=tyy,4io&otracker=hp_nmenu_sub_electronics_0_' + mobile)
            request = request.text
            response = bs.BeautifulSoup(request)
            if number <= 21:
                a = response.findAll('div', {'class': 'pu-title fk-font-13'})
                print [all(str(i.text) for i in a)]
            else:



a = mobiles()
a.get_mobiles('samsung')