from datetime import datetime
import pytz
from django.core.exceptions import ValidationError

def get_iran_time() -> datetime:
    """
    calculate and return the current time in Iran's timezone (Asia/Tehran)
    """
    iran_timezone = pytz.timezone('Asia/Tehran')
    return datetime.now(iran_timezone)

def get_timezone_time(*, timezone_name: str) -> datetime:
    """
    calculate and return the current time in the specified timezone
    """
    try:
        target_timezone = pytz.timezone(timezone_name)
        return datetime.now(target_timezone)
    except pytz.UnknownTimeZoneError:
        raise ValidationError(f"Timezone '{timezone_name}' is invalid.")