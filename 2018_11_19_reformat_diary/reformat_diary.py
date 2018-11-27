import datetime


def entries_by_date(diary_file):
    entries = []
    cur_date, cur_entry = None, ''
    for line in diary_file:
        try:
            stripped_line = line.strip()
            parsed_date = datetime.datetime.strptime(stripped_line, '%Y-%m-%d')
            if cur_date:
                entries.append((cur_date, cur_entry.strip()))
            cur_date, cur_entry = stripped_line, ''
        except ValueError:
            cur_entry += line
    if cur_date:
        entries.append((cur_date, cur_entry.strip()))
    return entries
