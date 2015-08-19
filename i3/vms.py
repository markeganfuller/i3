import i3pystatus
import subprocess


class VMs(i3pystatus.IntervalModule):
    color_up = "#00F000"
    color_down = "#333333"
    interval = 120
    settings = (
        ("color_up", "Color when VMs are running"),
        ("color_down", "Color when VMs are stopped")
    )

    def run(self):
        response = {'full_text': '', 'name': 'vms'}

        num_vms = subprocess.check_output(['vboxmanage', 'list', 'runningvms'])
        num_vms = len(num_vms.splitlines())
        if num_vms > 0:
            response['color'] = self.color_up
        else:
            response['color'] = self.color_down

        response['full_text'] = "VMs: %d" % num_vms

        self.output = response
