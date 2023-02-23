import random
from helper import fetch_tracks, Playlist, change, shout


def make_squares(n: int) -> list[int]:
    """Returns a list of square numbers up to `n ** 2`."""
    squares = []
    for i in range(n):
        square = i ** 2
        squares.append(square)
    return squares


my_list_0 = [i for i in range(10)]


def change_hats(hats: list = []):
    change(hats)


def assign_if_statement(a, b):
    if a > b:
        x = 1
    else:
        x = 2
    return x


my_list_1 = [1, 2, 4]
my_list_2 = []
for i in my_list_1:
    if i != 2:
        my_list_2.append(i)
    else:
        continue


def f(a, b):
    if a > b:
        val = 42
    else:
        val = 0
    return val


hats_i_own = {}
hats_i_own["panama"] = 1
hats_i_own["baseball_cap"] = 2
hats_i_own["bowler"] = 23


def f1(a, b, c):
    if a:
        return a
    elif b:
        pass
    else:
        return c


time_of_day = "evening"
first_name = "Hasan"
last_name = "Kanmaz"
print("Good %s, %s %s" % (time_of_day, first_name, last_name))


def create_playlist(starting_tracks = []):
    tracks_all = list(fetch_tracks())
    track_list = starting_tracks
    duration_seconds_remaining = 1800

    while duration_seconds_remaining > 0:
        tracks_which_fit = []
        for track in tracks_all:
            if track.duration_seconds < duration_seconds_remaining:
                tracks_which_fit.append(track)
        if len(tracks_which_fit) == 0:
            break
        track_selected = random.choice(tracks_which_fit)
        if track_selected in track_list:
            continue
        duration_seconds_remaining = duration_seconds_remaining - track_selected.duration_seconds
        track_list.append(track_selected)

    return Playlist(track_list)


def shout_about_bowlers(hats: list[str]) -> None:
    if any(hat == "bowler" for hat in hats):
        shout("I have a bowler hat!")


# Custom Rules
class ExampleBaseClass:
    def abstract_method(self):
        raise NotImplemented


def print_sourcery_yaml():
    with open(".sourcery.yaml", "r") as f:
        print(f.read())
