# components/__init__.py
from .header import show_header
from .navigation import show_bottom_nav
from .footer import show_footer
from .styles import apply_custom_styles, show_splash_screen

__all__ = [
    'show_header',
    'show_bottom_nav',
    'show_footer',
    'apply_custom_styles',
    'show_splash_screen'
]
