from .login import show_login
from .signup import show_signup
from .forgot_password import forgot_password as show_forgot_password
from .otp_verification import otp_verification as show_otp_verification
from .change_password import change_password as show_change_password
from .home import show_home
from .detect import show_detect
from .history import show_history
from .profile import show_profile
from .library import show_library
from .admin_dashboard import show_admin_dashboard


__all__ = [
    'show_login',
    'show_signup',
    'show_admin_dashboard'
]
