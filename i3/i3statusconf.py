import i3pystatus
import vms
import mem

status = i3pystatus.Status(standalone=True)

color_good = "#00F000"
color_bad = "#E50000"
color_off = "#333333"

status.register("clock", format="%Y-%m-%d %H:%M:%S %z")
status.register("load", format="{avg1} {avg5} {avg15}",
                critical_color=color_bad)
status.register(mem.TempfsFree, color_up=color_good, color_down=color_off,
                color_critical=color_bad)
status.register(mem.SwapFree, color_up=color_good, color_down=color_off,
                color_critical=color_bad)
status.register(mem.MemFree, color_up=color_good, color_down=color_off,
                color_critical=color_bad)
status.register(vms, color_up=color_good, color_down=color_off)
status.register("runwatch", name="DHCP", path="/var/run/dhcpcd*.pid",
                color_up=color_good, color_down=color_off)
status.register("network", interface="eno1", format_up="E:{v4} {v6}",
                format_down="E", color_up=color_good, color_down=color_off,
                on_leftclick=None, on_rightclick=None, on_upscroll=None,
                on_downscroll=None)

status.run()
