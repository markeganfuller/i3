"""
i3pystatus Virtualbox VMs count.

Displays number of Vbox VMs running.
"""
import subprocess
import i3pystatus


class VMs(i3pystatus.IntervalModule):
    """Virtualbox VMs count."""

    # pylint: disable=too-few-public-methods

    color_up = "#00F000"
    color_down = "#333333"
    interval = 120
    settings = (
        ("color_up", "Color when VMs are running"),
        ("color_down", "Color when VMs are stopped")
    )

    def run(self):
        """Run."""
        response = {'full_text': '', 'name': 'vms'}

        num_vms = self.get_virtualbox_vms() + self.get_libvirt_vms()
        if num_vms > 0:
            response['color'] = self.color_up
            response['full_text'] = "VM: %d" % num_vms
        else:
            response['color'] = self.color_down
            response['full_text'] = "VM"

        # pylint: disable=attribute-defined-outside-init
        self.output = response

    @staticmethod
    def get_virtualbox_vms():
        """Get count of Virtualbox VMs."""
        num_vms = subprocess.check_output(['vboxmanage', 'list', 'runningvms'])
        num_vms = len(num_vms.splitlines())
        return num_vms

    @staticmethod
    def get_libvirt_vms():
        """Get count of libvirt VMs."""
        num_vms = subprocess.check_output(['virsh', '-q', '-c', 'qemu:///system', 'list'])
        num_vms = len(num_vms.splitlines())
        return num_vms
