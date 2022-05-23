"""py3status config."""

import netifaces
import i3pystatus
import i3pystatus.temp
import i3pystatus.updates.pacman

import gatewayping
import keyboardmap
import vms

status = i3pystatus.Status(standalone=True)

color_good = "#00F000"  # Green
color_ok = "#FFFFFF"  # White
color_warn = "#FF7C00"  # Amber
color_bad = "#E50000"  # Red
color_off = "#333333"  # Grey

status.register("clock", format="%a %Y-%m-%d %H:%M:%S %z %s")

status.register(keyboardmap.KeyboardMap, color_good=color_ok, map="gb")

if i3pystatus.temp.get_sensors():
    status.register(
        "temp",
        format="{Package_id_0}°C",
        hints={"markup": "pango"},
        lm_sensors_enabled=True,
        color=color_ok,
        alert_color=color_bad,
        alert_temp=60
    )
else:
    status.register(
        "text",
        text="??°C",
        color=color_off
    )

status.register(
    'battery',
    format='{status}{percentage_design:.0f}%{glyph}',
    not_present_text="B",
    color=color_ok,
    full_color=color_good,
    charging_color=color_warn,
    critical_color=color_bad,
    not_present_color=color_off,
    alert=True,
    alert_percentage=15,
    status={
        'DPL': 'X',
        'CHR': 'C',
        'DIS': 'D',
        'FULL': 'F',
    }
)

status.register(
    "load",
    format="{avg1} {avg5} {avg15}",
    critical_color=color_bad
)

status.register(
    "swap",
    format="S:{percent_used:.0f}%",
    round_size=0,
    warn_color=color_bad,
    alert_color=color_bad,
    color=color_ok
)

status.register(
    "mem",
    format="M:{percent_used_mem:.0f}%",
    round_size=0,
    warn_color=color_warn,
    alert_color=color_bad,
    color=color_ok
)

status.register(
    vms.VMs,
    color_up=color_good,
    color_down=color_off
)

status.register(
    "pulseaudio",
    format="A:{volume}%",
    format_muted="A:XX%",
    on_upscroll=None,
    on_downscroll=None,
    on_doubleleftclick=None
)

status.register(
    "updates",
    format="U:{count}",
    color=color_bad,
    color_no_updates=color_off,
    format_no_updates="U",
    format_working="U:-",
    backends=[i3pystatus.updates.pacman.Pacman()]
)

status.register(
    "network",
    interface="tun0",
    format_up="V:{v4}",
    format_down="V",
    color_up=color_ok,
    color_down=color_off,
    on_leftclick=None,
    on_rightclick=None,
    on_upscroll=None,
    on_downscroll=None,
    unknown_up=True
)

status.register(
    "network",
    interface="wnet0",
    format_up="W:{v4}",
    format_down="W",
    color_up=color_ok,
    color_down=color_off,
    on_leftclick=None,
    on_rightclick=None,
    on_upscroll=None,
    on_downscroll=None
)

status.register(
    "network",
    interface="net0",
    format_up="E:{v4}",
    format_down="E",
    color_up=color_ok,
    color_down=color_off,
    on_leftclick=None,
    on_rightclick=None,
    on_upscroll=None,
    on_downscroll=None
)

status.register(
    "network",
    interface="usbnet0",
    format_up="U:{v4}",
    format_down="U",
    color_up=color_ok,
    color_down=color_off,
    on_leftclick=None,
    on_rightclick=None,
    on_upscroll=None,
    on_downscroll=None
)


status.register(
    gatewayping.GatewayPing,
    threshold=20,
    color_good=color_off,
    color_bad=color_bad
)

status.register(
    "timewarrior",
    format="{tags} {duration}",
    enable_stop=False,
    enable_continue=False
)

status.register(
    "spotify",
    player="spotifyd",
    format="{title} : {artist} {status}",
    status={
        'pause': '⏸︎',
        'play': '▶',
        'stop': '⏹︎',
    },
    color=color_off,
    on_leftclick=None,
    on_middleclick=None,
    on_rightclick=None,
    on_upscroll=None,
    on_downscroll=None,
    interval=20,
)

status.run()
