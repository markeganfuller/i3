import i3pystatus
import subprocess


class TmuxS(i3pystatus.IntervalModule):
    color_down = "#333333"
    interval = 120
    settings = (
        ("color_up", "Color when Tmux sessions are running"),
        ("color_down", "Color when Tmux sessions are stopped")
    )

    def run(self):
        response = {'full_text': '', 'name': 'tmuxs'}

        num_sessions = subprocess.check_output(['tmux', 'list-sessions'])
        num_sessions = len(num_sessions.splitlines())
        if num_sessions < 1:
            response['color'] = self.color_down

        response['full_text'] = "TMUXs: %d" % num_sessions

        self.output = response
