import re
from datetime import datetime

def validate_field(value, field_type):
    if field_type == "email":
        # Проверка на email
        return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", value)
    elif field_type == "phone":
        # Проверка на телефон в формате +7 xxx xxx xx xx
        return re.match(r"^\+7 \d{3} \d{3} \d{2} \d{2}$", value)
    elif field_type == "date":
        # Проверка на дату в формате DD.MM.YYYY или YYYY-MM-DD
        try:
            datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError:
            try:
                datetime.strptime(value, "%d.%m.%Y")
                return True
            except ValueError:
                return False
    elif field_type == "text":
        # Проверка на текст
        return isinstance(value, str)
    return False

def detect_field_type(value):
    if validate_field(value, "email"):
        return "email"
    elif validate_field(value, "phone"):
        return "phone"
    elif validate_field(value, "date"):
        return "date"
    return "text"  # Если ничего не подошло
