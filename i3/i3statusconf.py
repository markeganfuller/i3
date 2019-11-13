"""py3status config."""

import netifaces
import i3pystatus

import keyboardmap
import vms

status = i3pystatus.Status(standalone=True)

color_good = "#00F000"
color_ok = "#FFFFFF"
color_bad = "#E50000"
color_off = "#333333"

status.register("clock", format="%Y-%m-%d %H:%M:%S %z %s")
status.register(keyboardmap.KeyboardMap, color_good=color_ok, map="gb")
status.register("temp", format="{Package_id_0}°C", hints={"markup": "pango"},
                lm_sensors_enabled=True, color=color_ok, alert_color=color_bad,
                alert_temp=60)
status.register('battery', format='{status}{percentage_design:.0f}%{glyph}',
                alert=True, alert_percentage=15,
                status={
                    'DPL': 'X',
                    'CHR': 'C',
                    'DIS': 'D',
                    'FULL': 'F',
                })

status.register("load", format="{avg1} {avg5} {avg15}",
                critical_color=color_bad)
status.register("swap", format="S:{percent_used:.0f}%", round_size=0,
                warn_color=color_bad, alert_color=color_bad, color=color_ok)
status.register("mem", format="M:{percent_used_mem:.0f}%", round_size=0,
                warn_color=color_bad, alert_color=color_bad, color=color_ok)

status.register(vms.VMs, color_up=color_good, color_down=color_off)

if "tun0" in netifaces.interfaces():
    status.register("network", interface="tun0", format_up="V:{v4}",
                    format_down="V", color_up=color_ok, color_down=color_off,
                    on_leftclick=None, on_rightclick=None, on_upscroll=None,
                    on_downscroll=None, unknown_up=True)

status.register("network", interface="net0", format_up="E:{v4}",
                format_down="E", color_up=color_ok, color_down=color_off,
                on_leftclick=None, on_rightclick=None, on_upscroll=None,
                on_downscroll=None)

if "wnet0" in netifaces.interfaces():
    status.register("network", interface="wnet0", format_up="W:{v4}",
                    format_down="W", color_up=color_ok, color_down=color_off,
                    on_leftclick=None, on_rightclick=None, on_upscroll=None,
                    on_downscroll=None)

status.run()
