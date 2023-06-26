"""Generate a banner on the GitHub commit graph"""
import subprocess
from datetime import datetime, timedelta

import pytz
from tqdm import tqdm

from txt_to_bitmap import text_to_array

# number of commits in given date to be generated
INTENSITY = 1


def first_sunday_after_date(date: str) -> datetime:
    """Return the date of the first Sunday after the given date

    :param date: Date in the format: "YYYY-MM-DD"
    :return: Date of the first Sunday after the given date
    """

    dt = datetime.strptime(date, "%Y-%m-%d")
    sunday = dt + timedelta(days=(6 - dt.weekday()) % 7)
    tz = pytz.timezone("America/Los_Angeles")
    return tz.localize(sunday)


def commit_pixel(input_date: datetime):
    """Make commits at the given date"""

    # Convert the date into git format
    git_date = input_date.strftime("%a %b %d %H:%M:%S %Y %z")

    for i in range(INTENSITY):
        with open("file.txt", "a") as f:
            f.write(str(i) + "\n")

        # Stage changes
        subprocess.run(["git", "add", "."], stdout=subprocess.PIPE)

        # Make a commit with the specific date
        subprocess.run(
            ["git", "commit", "--date", git_date, "-m", f"commit {i}"], stdout=subprocess.PIPE
        )


def blit_banner(banner, start_date: str):
    """Blit the banner on the given date"""
    start_date = first_sunday_after_date(start_date)

    for x in tqdm(range(banner.shape[1]), desc="Blitting banner"):
        for y in range(banner.shape[0]):
            if banner[y, x] == "X":
                date = start_date + timedelta(days=y) + timedelta(weeks=x)
                commit_pixel(date)


if __name__ == "__main__":
    blit_banner(text_to_array("EMSI.ME"), "2013-02-17")
