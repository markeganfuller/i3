"""
i3pystatus Keyboard map.

Displays current keyboard map.
"""

import subprocess
import i3pystatus


class KeyboardMap(i3pystatus.IntervalModule):
    """Keyboard map."""

    # pylint: disable=too-few-public-methods

    color_bad = "#F00000"
    color_good = "#FF7E00"
    interval = 120
    settings = (
        ("color_bad", "Color when its bad"),
        ("color_good", "Color when its good"),
    )

    def run(self):
        """Run."""
        response = {'full_text': '', 'name': 'kbm'}

        command = "setxkbmap -query | awk '/layout/{print $2}'"
        kbm = subprocess.check_output(command, shell=True,
                                      universal_newlines=True)
        kbm = kbm.strip()
        if kbm != "gb":
            response['color'] = self.color_bad
        else:
            response['color'] = self.color_good

        kbm = kbm.upper()
        response['full_text'] = "{}".format(kbm)

        # pylint: disable=attribute-defined-outside-init
        self.output = response
