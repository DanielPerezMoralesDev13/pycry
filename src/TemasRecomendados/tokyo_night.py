# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/DanielPerezMoralesDev13
# Email: danielperezdev@proton.me

from typing import Dict, Any
from toml import loads

tokyo_night: Dict[str, Any] = loads(s = """\
    # Colors (Tokyo Night)
    # Source https//github.com/zatchheems/tokyo-night-alacritty-theme

    # Default colors
    [colors.primary]
    background = '#1a1b26'
    foreground = '#a9b1d6'

    # Normal colors
    [colors.normal]
    black   = '#32344a'
    red     = '#f7768e'
    green   = '#9ece6a'
    yellow  = '#e0af68'
    blue    = '#7aa2f7'
    magenta = '#ad8ee6'
    cyan    = '#449dab'
    white   = '#787c99'

    # Bright colors
    [colors.bright]
    black   = '#444b6a'
    red     = '#ff7a93'
    green   = '#b9f27c'
    yellow  = '#ff9e64'
    blue    = '#7da6ff'
    magenta = '#bb9af7'
    cyan    = '#0db9d7'
    white   = '#acb0d0'
    """
)