"""Generate a banner on the GitHub commit graph"""
import subprocess
from datetime import datetime, timedelta

from txt_to_bitmap import text_to_array

# number of commits in given date to be generated
INTENSITY = 100


def first_sunday_after_date(date: str) -> datetime:
    """Return the date of the first Sunday after the given date

    :param date: Date in the format: "YYYY-MM-DD"
    :return: Date of the first Sunday after the given date
    """

    dt = datetime.strptime(date, "%Y-%m-%d")
    return dt + timedelta(days=(6 - dt.weekday()) % 7)


# # Date in the format: "2022-06-27"
# input_date = "2022-06-26"


def commit_pixel(input_date):
    """Make commits at the given date"""

    # Convert the date into git format
    dt = datetime.strptime(input_date, "%Y-%m-%d")
    git_date = dt.strftime("%a %b %d %H:%M:%S %Y %z")

    for i in range(INTENSITY):
        with open("file.txt", "a") as f:
            f.write(str(i) + "\n")

        # # Stage changes
        # subprocess.run(["git", "add", "."])

        # Make a commit with the specific date
        subprocess.run(["git", "commit", "--date", git_date, "-m", f"commit {i}", "file.txt"])


def blit_banner(banner, start_date: str):
    """Blit the banner on the given date"""
    start_date = first_sunday_after_date(start_date)

    for x in range(banner.shape[1]):
        for y in range(banner.shape[0]):
            if banner[y, x] == "X":
                date = start_date + timedelta(days=y) + timedelta(weeks=x)
                print(date)


if __name__ == "__main__":
    blit_banner(text_to_array("EMSI.ME"), "2011-01-01")
