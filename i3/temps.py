import subprocess
import i3pystatus


class OnboardTemp(i3pystatus.IntervalModule):
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
        response = {'full_text': '', 'name': 'temp'}

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

        response['full_text'] = "%d°C" % temp

        self.output = response
