"""i3pystatus Docker running container count."""
import subprocess
import i3pystatus


class Docker(i3pystatus.IntervalModule):
    """Docker running container count."""

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
        response = {'full_text': '', 'name': 'docker'}

        num_containers = self.get_running_docker_containers()
        if num_containers > 0:
            response['color'] = self.color_up
            response['full_text'] = "DK: %d" % num_containers
        else:
            response['color'] = self.color_down
            response['full_text'] = "DK"

        # pylint: disable=attribute-defined-outside-init
        self.output = response

    @staticmethod
    def get_running_docker_containers():
        """Get count of running Docker containers."""
        num_containers = subprocess.check_output(['docker', 'ps', '-q'])
        num_containers = len(num_containers.splitlines())
        return num_containers
