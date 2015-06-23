import psutil


class Py3status:
    """
    System status in i3bar
    """

    def free(self, json, i3status_config):
        response = {'full_text': '', 'name': 'ram'}
        total = psutil.phymem_usage().percent
        if total < 1:
            response['color'] = i3status_config['color_bad']
        elif total < 50:
            response['color'] = i3status_config['color_good']
        else:
            response['color'] = i3status_config['color_degraded']

        response['full_text'] = "M: %d%%" % total

        return (-2, response)

    def swap(self, json, i3status_config):
        response = {'full_text': '', 'name': 'swap'}
        total = psutil.swap_memory().percent
        if total < 1:
            response['color'] = i3status_config['color_bad']
        elif total < 50:
            response['color'] = i3status_config['color_good']
        else:
            response['color'] = i3status_config['color_degraded']

        response['full_text'] = "S: %d%%" % total

        return (-2, response)

    def tempfs(self, json, i3status_config):
        response = {'full_text': '', 'name': 'tempfs'}
        total = psutil.disk_usage('/home/markeganfuller/VirtualBoxVMs/').percent
        if total < 1:
            response['color'] = i3status_config['color_bad']
        elif total < 50:
            response['color'] = i3status_config['color_good']
        else:
            response['color'] = i3status_config['color_degraded']

        response['full_text'] = "T: %d%%" % total

        return (-2, response)
