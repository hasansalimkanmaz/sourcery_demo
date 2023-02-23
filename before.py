from helper import shout, InvalidCredentialsError, Scale
from typing import Any


def make_squares(n: int) -> list[int]:
    """Returns a list of square numbers up to `n ** 2`."""
    squares = []
    for i in range(n):
        square = i ** 2
        squares.append(square)
    return squares


my_list_0 = [i for i in range(10)]


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


def shout_about_bowlers(hats: list[str]) -> None:
    if any(hat == "bowler" for hat in hats):
        shout("I have a bowler hat!")


def resolve_configs(
    default_config: dict[str, Any],
    user_config: dict[str, Any],
    project_config: dict[str, Any],
):
    config = default_config.copy()
    config.update(user_config)
    config.update(project_config)
    return config


def testConnection(db, credentials):
    try:
        try:
            db.connect(credentials)
        except InvalidCredentialsError:
            return "Check your credentials"
        except ConnectionError:
            return "Error while trying to connect"
    finally:
        print("Connection attempt finished")
    return "Connection Successful"


def put_on_hat_if_needed(is_raining: bool):
    if is_raining == True:
        print("Put on hat")


DEFAULT_SPEED = 3
HORIZONTAL = True
DEFAULT_FORCE = 10
def extraction_example():
    speed_slider = Scale(
        "parent", from_=1, to=10, orient=HORIZONTAL, label="Speed"
    )
    speed_slider.pack()
    speed_slider.set(DEFAULT_SPEED)
    speed_slider.configure(background="white")

    force_slider = Scale(
        "parent", from_=1, to=10, orient=HORIZONTAL, label="Force"
    )
    force_slider.pack()
    force_slider.set(DEFAULT_FORCE)
    force_slider.configure(background="white")


# Custom Rules
class ExampleBaseClass:
    def abstract_method(self):
        raise NotImplemented


def print_sourcery_yaml():
    with open(".sourcery.yaml", "r") as f:
        print(f.read())
