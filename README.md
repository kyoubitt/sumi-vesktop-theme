# sumi

A Vesktop / Vencord theme: ink-painting wallpaper behind neutral dark glass, white accents, two-column server list with folders.

The theme is one self-contained file. Nothing is fetched from the internet: the base CSS is vendored and both images are embedded, so it can't break when a remote host changes.

## Install

1. Copy `sumi.theme.css` into Vesktop's themes folder: `~/.config/vesktop/themes/`
2. Vesktop settings, Themes, enable **sumi**.

## What it does

- Wallpaper under translucent glass panels (server list, channel list, chat, member list, profile panel).
- Title bar, music player, menus, tooltips, popouts, modals and the composer autocomplete get a blur with a denser background so text stays readable.
- The big panels are not blurred on purpose. Blurring six full-height panels every frame made the client laggy.
- Accent is off-white. Brand-filled things like bot tags use a mid slate so white text on them stays readable.
- Round home button with a white ring.

## Fonts

It asks for **Maple Mono NF CN** first. Maple has no Unicode small capitals (the letters some servers use in channel names), so **Adwaita Mono** is next in the stack to cover them. Change `--sumi-font` in `src/sumi.tpl.css` if you want something else.

## Build from source

```
python3 src/build.py
```

This joins `src/sumi.tpl.css`, `src/naat.css` and the two images in `src/assets/` into `sumi.theme.css`. To use your own wallpaper or home icon, replace `src/assets/wallpaper.jpg` and `src/assets/home-icon.jpg` and rebuild.

## Credits

- Server list and folder layout: [NotAnotherAnimeTheme](https://github.com/puckzxz/NotAnotherAnimeTheme) by puckzxz (Unlicense). `src/naat.css` is a pinned copy of its v3 build.
- Wallpaper: found on Pinterest, artist unknown. If you know who made it, open an issue and I'll credit them.
