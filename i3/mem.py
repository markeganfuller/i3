import i3pystatus
import psutil


class MemFree(i3pystatus.IntervalModule):
    color_up = "#00F000"
    color_critical = "#E50000"
    color_down = "#333333"
    interval = 60
    settings = (
        ("color_up", ""),
        ("color_critical", ""),
        ("color_down", "")
    )

    def run(self):
        response = {'full_text': '', 'name': 'ram'}
        total = psutil.phymem_usage().percent
        if total < 1:
            response['color'] = self.color_down
        elif total < 50:
            response['color'] = self.color_up
        else:
            response['color'] = self.color_critical

        response['full_text'] = "M: %d%%" % total
        self.output = response


class SwapFree(i3pystatus.IntervalModule):
    color_up = "#00F000"
    color_critical = "#E50000"
    color_down = "#333333"
    interval = 60
    settings = (
        ("color_up", ""),
        ("color_critical", ""),
        ("color_down", "")
    )

    def run(self):
        response = {'full_text': '', 'name': 'swap'}
        total = psutil.swap_memory().percent
        if total < 1:
            response['color'] = self.color_down
        elif total < 50:
            response['color'] = self.color_up
        else:
            response['color'] = self.critical_color

        response['full_text'] = "S: %d%%" % total
        self.output = response


class TempfsFree(i3pystatus.IntervalModule):
    color_up = "#00F000"
    color_critical = "#E50000"
    color_down = "#333333"
    interval = 60
    settings = (
        ("color_up", ""),
        ("color_critical", ""),
        ("color_down", "")
    )

    def run(self):
        response = {'full_text': '', 'name': 'tempfs'}
        total = psutil.disk_usage('/home/markeganfuller/VirtualBoxVMs/').percent
        if total < 1:
            response['color'] = self.color_down
        elif total < 50:
            response['color'] = self.color_up
        else:
            response['color'] = self.color_critical

        response['full_text'] = "T: %d%%" % total
        self.output = response
