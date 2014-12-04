import subprocess


class Py3status:
    """
    System status in i3bar
    """
    def vms(self, json, i3status_config):
        response = {'full_text': '', 'name': 'vms'}

        num_vms = subprocess.check_output(['vboxmanage', 'list', 'runningvms'])
        num_vms = len(num_vms.splitlines())
        if num_vms > 0:
            response['color'] = i3status_config['color_good']
        else:
            response['color'] = i3status_config['color_bad']

        response['full_text'] = "VMs: %d" % num_vms

        return (-2, response)
