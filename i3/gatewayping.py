"""
i3pystatus Gateway Ping.

Shows average ping to gateway.
"""

import subprocess
import i3pystatus


class GatewayPing(i3pystatus.IntervalModule):
    """
    Gateway ping.

    Checks the default gateway is pinging.
    """

    # pylint: disable=too-few-public-methods

    color_bad = "#F00000"
    color_good = "#FF7E00"
    interval = 120
    settings = (
        ("color_bad", "Color when its bad"),
        ("color_good", "Color when its good"),
        ("threshold", "Max ms ping"),
    )

    def run(self):
        """Run."""
        response = {
            'full_text': '',
            'name': 'ms',
            'color': self.color_bad
        }

        try:
            command = "ip route show default | grep -v gpd | cut -d' ' -f 3"
            gateway = subprocess.check_output(command, shell=True,
                                                universal_newlines=True)
        except subprocess.CalledProcessError:
            response['full_text'] = f"GW:?"
        else:
            try:
                command = f"ping -c10 -q {gateway}"
                stats = subprocess.check_output(command, shell=True,
                                                universal_newlines=True)

                stats = stats.splitlines()
                # rtt min/avg/max/mdev = 1.405/2.246/2.584/0.322 ms
                ms = float(stats[-1].split('/')[4])
                if ms < self.threshold:
                    response['color'] = self.color_good

                response['full_text'] = f"{ms}ms"

            except subprocess.CalledProcessError:
                response['full_text'] = "?ms"

        # pylint: disable=attribute-defined-outside-init
        self.output = response
