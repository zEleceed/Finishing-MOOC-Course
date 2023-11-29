import re


def is_dotw(my_string: str) -> bool:
    pattern = r'\b(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b'
    return re.search(pattern, my_string) is not None


def all_vowels(my_string: str) -> bool:
    pattern = r'^[aeiouAEIOU]+$'
    return re.fullmatch(pattern, my_string) is not None


def time_of_day(my_string: str) -> bool:
    pattern = r'^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$'
    return re.fullmatch(pattern, my_string) is not None
