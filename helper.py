from dataclasses import dataclass
import typing


@dataclass
class Track:
    title: str
    artist: str
    duration_seconds: int


@dataclass
class Playlist:
    tracks: typing.List[Track]


def fetch_tracks() -> typing.Iterator[Track]:
    yield Track(title="", artist="", duration_seconds=3)

def change(hat: list):
    assert hat


def shout(message: str):
    print(message)