from datetime import datetime

def check_and_convert_string_to_date(string, line_num):
    """
    User Story 42: Reject Illegitimate dates.
    Converts string to date.
    GEDCOM date format: dd MM YYYY
    returns: a datetime object
    """
    try:
        return datetime.strptime(string, '%d %b %Y')
    except ValueError:
        print(f'ERROR: US42, line {line_num}, Illegitimate date!')
        return None