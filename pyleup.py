#!/usr/bin/python3
from datetime import datetime, timedelta


def gen_date_coordinates(origin_date, message_template):
    lines = message_template.split("\n")

    # Nuke the first & last line
    del lines[0]
    del lines[len(lines) - 1]

    dates = []

    for row_index, line in enumerate(lines):
        cells = line.split("|")
        del cells[0]
        del cells[len(cells) - 1]

        for column_index, cell in enumerate(cells):
            if cells[column_index] == "X":
                dates.append(origin_date + (timedelta(row_index + (7 * column_index))))

        [print(f'git commit --allow-empty --date="{date.isoformat()}" -m "YOLO mode active. See https://github.com/jonathancone/pyleup."') for date in dates]
    return


# Change this to the message you would like to display:
message_template = """
| | | | |X| | | | | |X| | | |X|X|X| | | |X|X|X|X|X|X|X| |X| | | | | |X| |X|X|X|X|X|X|X| |X|X|X|X|X| | |
| | | | |X| | | | | |X| | |X| | | |X| | |X| | | | | | | |X| | | |X|X| | |X| | | | | | | |X| | | | | |X|
| | | | |X| | | | | |X| |X| | | | | |X| |X| | | | | | | |X| | |X| | | | |X| | | | | | | |X| | | | | |X|
| | | | |X|X|X|X|X|X|X| |X|X|X|X|X|X|X| |X| | | | | | | |X|X|X| | | | | |X|X|X|X|X|X|X| |X|X|X|X|X|X| |
| | | | |X| | | | | |X| |X| | | | | |X| |X| | | | | | | |X| | |X|X| | | |X| | | | | | | |X| | | |X| | |
| | | | |X| | | | | |X| |X| | | | | |X| |X| | | | | | | |X| | | | |X| | |X| | | | | | | |X| | | | |X| |
| | | | |X| | | | | |X| |X| | | | | |X| |X|X|X|X|X|X|X| |X| | | | | |X| |X|X|X|X|X|X|X| |X| | | | | |X|
"""

run_date = datetime.today()

# We want the origin coordinate to start on Sunday
day_of_week_differential = 6 - run_date.weekday()

# The date that represents 0,0 origin in the grid
origin_date = run_date - timedelta(day_of_week_differential + 364)

gen_date_coordinates(origin_date, message_template)

# git commit --date="10 day ago" -m "Your commit message"
