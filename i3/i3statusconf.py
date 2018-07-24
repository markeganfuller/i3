import netifaces
import i3pystatus
import keyboardmap
import mem
import temps
import vms

status = i3pystatus.Status(standalone=True)

color_good = "#00F000"
color_ok = "#FFFFFF"
color_bad = "#E50000"
color_off = "#333333"

status.register("clock", format="%Y-%m-%d %H:%M:%S %z %s")
status.register(keyboardmap.KeyboardMap, color_good=color_ok)
status.register(temps.OnboardTemp, color_norm=color_ok)
status.register("load", format="{avg1} {avg5} {avg15}",
                critical_color=color_bad)
status.register(mem.SwapFree, color_up=color_ok, color_down=color_off,
                color_critical=color_bad)
status.register(mem.MemFree, color_up=color_ok, color_down=color_off,
                color_critical=color_bad)
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
