import psutil


class Py3status:
    """
    System status in i3bar
    """

    def free(self, json, i3status_config):
        response = {'full_text': '', 'name': 'free'}
        total = psutil.phymem_usage().percent
        if total < 50:
            response['color'] = i3status_config['color_good']
        elif total < 70:
            response['color'] = i3status_config['color_degraded']
        else:
            response['color'] = i3status_config['color_bad']

        response['full_text'] = "M: %d%%" % total

        return (-1, response)
