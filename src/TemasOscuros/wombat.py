# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

wombat: Dict[str, Any] = loads(s = """\
    # Colors (Wombat)

    # Default colors
    [colors.primary]
    background = '#1f1f1f'
    foreground = '#e5e1d8'

    # Normal colors
    [colors.normal]
    black   = '#000000'
    red     = '#f7786d'
    green   = '#bde97c'
    yellow  = '#efdfac'
    blue    = '#6ebaf8'
    magenta = '#ef88ff'
    cyan    = '#90fdf8'
    white   = '#e5e1d8'

    # Bright colors
    [colors.bright]
    black   = '#b4b4b4'
    red     = '#f99f92'
    green   = '#e3f7a1'
    yellow  = '#f2e9bf'
    blue    = '#b3d2ff'
    magenta = '#e5bdff'
    cyan    = '#c2fefa'
    white   = '#ffffff'
    """
)