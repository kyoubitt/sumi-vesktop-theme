"""Builds sumi.theme.css: template + vendored NAAT base + both images embedded as data URIs."""
import base64
import pathlib

src = pathlib.Path(__file__).resolve().parent


def b64(name):
    return base64.b64encode((src / "assets" / name).read_bytes()).decode()


css = (src / "sumi.tpl.css").read_text()
css = css.replace("__NAAT__", (src / "naat.css").read_text())
css = css.replace("__HOME__", "data:image/jpeg;base64," + b64("home-icon.jpg"))
css = css.replace("__WALL__", "data:image/jpeg;base64," + b64("wallpaper.jpg"))

out = src.parent / "sumi.theme.css"
out.write_text(css)
print(f"{len(css)} bytes -> {out}")
