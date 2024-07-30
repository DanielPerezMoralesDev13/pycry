# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

github_dark_colorblind: Dict[str, Any] = loads(s = """\
    # github Alacritty Colors

    # Default colors
    [colors.primary]
    background = '#0d1117'
    foreground = '#b3b1ad'

    # Normal colors
    [colors.normal]
    black   = '#484f58'
    red     = '#ff7b72'
    green   = '#3fb950'
    yellow  = '#d29922'
    blue    = '#58a6ff'
    magenta = '#bc8cff'
    cyan    = '#39c5cf'
    white   = '#b1bac4'

    # Bright colors
    [colors.bright]
    black   = '#6e7681'
    red     = '#ffa198'
    green   = '#56d364'
    yellow  = '#e3b341'
    blue    = '#79c0ff'
    magenta = '#d2a8ff'
    cyan    = '#56d4dd'
    white   = '#f0f6fc'

    [[colors.indexed_colors]]
    index = 16
    color = '#d18616'

    [[colors.indexed_colors]]
    index = 17
    color = '#ffa198'
    """
)