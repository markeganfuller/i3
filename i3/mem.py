"""
i3pystatus Memory display.

Displays memory and swap usage.
"""

import psutil
import i3pystatus


class MemFree(i3pystatus.IntervalModule):
    """Display memory usage."""

    # pylint: disable=too-few-public-methods

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
        """Run."""
        response = {'full_text': '', 'name': 'ram'}
        total = psutil.virtual_memory().percent
        if total < 1:
            response['color'] = self.color_down
        elif total < 50:
            response['color'] = self.color_up
        else:
            response['color'] = self.color_critical

        response['full_text'] = "M:%d%%" % total
        # pylint: disable=attribute-defined-outside-init
        self.output = response


class SwapFree(i3pystatus.IntervalModule):
    """Display swap usage."""

    # pylint: disable=too-few-public-methods

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
        """Run."""
        response = {'full_text': '', 'name': 'swap'}
        total = psutil.swap_memory().percent
        if total < 1:
            response['color'] = self.color_down
        elif total < 50:
            response['color'] = self.color_up
        else:
            response['color'] = self.color_critical

        response['full_text'] = "S:%d%%" % total
        # pylint: disable=attribute-defined-outside-init
        self.output = response
