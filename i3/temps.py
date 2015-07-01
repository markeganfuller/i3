import subprocess
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
        soup = bs4.BeautifulSoup(resp.content)
        london = soup.find(title="London")
        temp = london.find(class_="temperature-value").text[:-2]
        temp = int(temp)

        if temp > 20:
            response['color'] = self.color_hot
        elif temp > 10:
            response['color'] = self.color_norm
        else:
            response['color'] = self.color_cold

        response['full_text'] = "E:%d°C" % temp

        self.output = response


class OnboardTemp(i3pystatus.IntervalModule):
    color_hot = "#F00000"
    color_norm = "#FF7E00"
    color_cold = "#3333F0"
    settings = (
        ("color_hot", "Color when its hot"),
        ("color_norm", "Color when its norm"),
        ("color_cold", "Color when its cold")
    )

    def run(self):
        response = {'full_text': '', 'name': 'vms'}

        output = subprocess.check_output(["acpi", "-t"],
                                         universal_newlines=True)
        output = output.splitlines()
        output = [temp.split(' ')[3] for temp in output]
        output = [float(temp) for temp in output]
        temp = max(output)

        if temp > 30:
            response['color'] = self.color_hot
        elif temp > 10:
            response['color'] = self.color_norm
        else:
            response['color'] = self.color_cold

        response['full_text'] = "I:%d°C" % temp

        self.output = response
