"""Generate a banner on the GitHub commit graph"""
import subprocess
from datetime import datetime, timedelta

import pytz
import typer as typer
from tqdm import tqdm

from txt_to_bitmap import text_to_array

app = typer.Typer(add_completion=False)


def first_sunday_after_date(date: str) -> datetime:
    """Return the date of the first Sunday after the given date

    :param date: Date in the format: "YYYY-MM-DD"
    :return: Date of the first Sunday after the given date
    """

    dt = datetime.strptime(date, "%Y-%m-%d")
    sunday = dt + timedelta(days=(6 - dt.weekday()) % 7)
    tz = pytz.timezone("America/Los_Angeles")
    return tz.localize(sunday)


def commit_pixel(input_date: datetime, intensity: int, x: int, y: int):
    """Make commits at the given date"""

    # Convert the date into git format
    git_date = input_date.strftime("%a %b %d %H:%M:%S %Y %z")

    for i in range(intensity):
        # Make a commit with the specific date
        subprocess.run(
            [
                "git",
                "commit",
                "--date",
                git_date,
                "--allow-empty",
                "-m",
                f"pixel x:{x}, y:{y}, commit:{i}",
            ],
            stdout=subprocess.PIPE,
        )


def blit_banner(banner, start_date: str, intensity: int):
    """Blit the banner on the given date"""
    start_date = first_sunday_after_date(start_date)

    for x in tqdm(range(banner.shape[1]), desc="Blitting banner"):
        for y in range(banner.shape[0]):
            if banner[y, x] == "X":
                date = start_date + timedelta(days=y) + timedelta(weeks=x)
                commit_pixel(date, intensity, x, y)


@app.command()
def main(
    banner_text: str = typer.Option("EMSI.ME", help="Text to be displayed on the commit graph."),
    date: str = typer.Option(
        "2013-02-17", help="Date from which the banner should start in the format: 'YYYY-MM-DD'"
    ),
    intensity: int = typer.Option(1, help="Number of commits per day"),
):
    """Generate a banner on the GitHub commit graph"""
    blit_banner(text_to_array(banner_text), date, intensity)


if __name__ == "__main__":
    app()
