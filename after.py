import random
from helper import fetch_tracks, Playlist, change


def make_squares(n: int) -> list[int]:
    """Returns a list of square numbers up to `n ** 2`."""
    return [i ** 2 for i in range(n)]


my_list_0 = list(range(10))


def change_hats(hats=None):
    if hats is None:
        hats = []
    change(hats)


def assign_if_statement(a, b):
    return 1 if a > b else 2


my_list_1 = [1, 2, 4]
my_list_2 = [i for i in my_list_1 if i != 2]


def f(a, b):
    return 42 if a > b else 0


hats_i_own = {"panama": 1, "baseball_cap": 2, "bowler": 23}


def f1(a, b, c):
    if a:
        return a
    elif not b:
        return c


time_of_day = "evening"
first_name = "Hasan"
last_name = "Kanmaz"
print(f"Good {time_of_day}, {first_name} {last_name}")


def create_playlist(starting_tracks=None):
    if starting_tracks is None:
        starting_tracks = []
    tracks_all = list(fetch_tracks())
    track_list = starting_tracks
    duration_seconds_remaining = 1800

    while duration_seconds_remaining > 0:
        tracks_which_fit = [
            track
            for track in tracks_all
            if track.duration_seconds < duration_seconds_remaining
        ]
        if not tracks_which_fit:
            break
        track_selected = random.choice(tracks_which_fit)
        if track_selected in track_list:
            continue
        duration_seconds_remaining -= track_selected.duration_seconds
        track_list.append(track_selected)

    return Playlist(track_list)


# Custom Rules
class ExampleBaseClass:
    def abstract_method(self):
        raise NotImplementedError


def print_sourcery_yaml():
    with open(".sourcery.yaml") as f:
        print(f.read())
