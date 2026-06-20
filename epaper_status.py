import os
import time
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from waveshare_epd import epd2in13_V4

WIDTH = 250
HEIGHT = 122
REFRESH_SECONDS = 60

# Change this if needed:
# 0 = normal, 180 = upside-down fix
ROTATION = 180

def cmd(command):
    try:
        return os.popen(command).read().strip()
    except Exception:
        return ""

def font(size, bold=False):
    base = "/usr/share/fonts/truetype/dejavu"
    path = f"{base}/DejaVuSans-Bold.ttf" if bold else f"{base}/DejaVuSans.ttf"
    if Path(path).exists():
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

TITLE = font(18, True)
LABEL = font(12, True)
TEXT = font(12)
SMALL = font(10)
SMILE = font(42, True)

def get_ip():
    return cmd("hostname -I | awk '{print $1}'") or "No IP"

def wifi_ok():
    return get_ip() != "No IP"

def ups_ok():
    return cmd("systemctl is-active x120x_upsd") == "active"

def ssd_ok():
    root = cmd("findmnt -n -o SOURCE /")
    return "nvme" in root

def all_systems_ok():
    return wifi_ok() and ups_ok() and ssd_ok()

def temp():
    t = cmd("vcgencmd measure_temp")
    return t.replace("temp=", "") if "temp=" in t else "N/A"

def ram():
    return cmd("free -h | awk '/Mem:/ {print $3 \"/\" $2}'") or "N/A"

def disk():
    return cmd("df -h / | awk 'NR==2 {print $3 \"/\" $2}'") or "N/A"

def row(draw, y, label, value):
    draw.text((8, y), label, font=LABEL, fill=0)
    draw.text((58, y), value, font=TEXT, fill=0)

def status_text(ok):
    return "OK" if ok else "FAIL"

def build_image():
    img = Image.new("1", (WIDTH, HEIGHT), 255)
    draw = ImageDraw.Draw(img)

    # Outer border
    draw.rectangle((0, 0, WIDTH - 1, HEIGHT - 1), outline=0, width=1)

    # Header
    draw.text((8, 4), "MAEHARA LAB", font=TITLE, fill=0)
    draw.line((0, 27, WIDTH, 27), fill=0, width=1)

    # Main stats left side
    row(draw, 34, "TEMP", temp())
    row(draw, 50, "RAM", ram())
    row(draw, 66, "DISK", disk())
    row(draw, 82, "IP", get_ip())

    # Right-side status face
    face = ":)" if all_systems_ok() else ":("
    draw.text((176, 38), face, font=SMILE, fill=0)

    # Bottom system status bar
    draw.line((0, 100, WIDTH, 100), fill=0, width=1)

    wifi = status_text(wifi_ok())
    ups = status_text(ups_ok())
    ssd = status_text(ssd_ok())

    draw.text((8, 105), f"WIFI {wifi}", font=SMALL, fill=0)
    draw.text((85, 105), f"UPS {ups}", font=SMALL, fill=0)
    draw.text((158, 105), f"SSD {ssd}", font=SMALL, fill=0)

    if ROTATION in [90, 180, 270]:
        img = img.rotate(ROTATION, expand=False)

    return img

def main():
    epd = epd2in13_V4.EPD()
    epd.init()
    epd.Clear(0xFF)

    try:
        while True:
            image = build_image()
            epd.displayPartial(epd.getbuffer(image))
            time.sleep(REFRESH_SECONDS)
    except KeyboardInterrupt:
        pass
    finally:
        epd.sleep()

if __name__ == "__main__":
    main()
