import re

import i3pystatus
import requests
import bs4


class WeatherTemp(i3pystatus.IntervalModule):
    color_hot = "#F00000"
    color_norm = "#FF7E00"
    color_cold = "#3333F0"
    interval = 120
    settings = (
        ("color_hot", "Color when its hot"),
        ("color_norm", "Color when its norm"),
        ("color_cold", "Color when its cold")
    )

    def run(self):
        response = {'full_text': '', 'name': 'vms'}

        resp = requests.request("get", "http://www.bbc.co.uk/weather/")
        soup = bs4.BeautifulSoup(resp.content, "html.parser")
        london = soup.find(title="London")
        temp = london.find(class_="temperature-value").text[:-2]
        temp = int(temp)

        if temp > 20:
            response['color'] = self.color_hot
        elif temp > 10:
            response['color'] = self.color_norm
        else:
            response['color'] = self.color_cold

        response['full_text'] = "E:{}°C".format(temp)

        self.output = response


class WeatherRain(i3pystatus.IntervalModule):
    color_rain = "#F00000"
    color_maybe = "#3333F0"
    color_dry = "#FF7E00"
    interval = 120
    settings = (
        ("color_rain", "Color when its likely to rain"),
        ("color_maybe", "Color when its maybe going to rain"),
        ("color_dry", "Color when its not going to rain")
    )

    def run(self):
        response = {'full_text': '', 'name': 'rain'}

        resp = requests.request("get", "http://www.metoffice.gov.uk/public/weather/forecast/gcpvn15h9")
        soup = bs4.BeautifulSoup(resp.content, "html.parser")
        day = soup.find("div", {"class": "weatherDay1"})
        percs = day.find("tr", {"class": "weatherRain"})
        percs = percs.findAll('td')
        percs = [p.getText()[:-1] for p in percs]  # Cut %
        non_decimal = re.compile(r'[^\d.]+')
        percs = [non_decimal.sub('', p) for p in percs]
        percs = [int(p) for p in percs]
        rain = max(percs)

        if rain > 50:
            response['color'] = self.color_rain
        elif rain > 10:
            response['color'] = self.color_maybe
        else:
            response['color'] = self.color_dry

        response['full_text'] = "R:{}%".format(rain)

        self.output = response
