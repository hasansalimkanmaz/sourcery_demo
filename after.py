from helper import shout, InvalidCredentialsError, Scale
from typing import Any

def make_squares(n: int) -> list[int]:
    """Returns a list of square numbers up to `n ** 2`."""
    return [i ** 2 for i in range(n)]


my_list_0 = list(range(10))


def assign_if_statement(a, b):
    return 1 if a > b else 2


my_list_1 = [1, 2, 4]
my_list_2 = [i for i in my_list_1 if i != 2]


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


def shout_about_bowlers(hats: list[str]) -> None:
    if "bowler" in hats:
        shout("I have a bowler hat!")


def resolve_configs(
    default_config: dict[str, Any],
    user_config: dict[str, Any],
    project_config: dict[str, Any],
):
    return default_config | user_config | project_config


def testConnection(db, credentials):
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
    if is_raining:
        print("Put on hat")


DEFAULT_SPEED = 3
HORIZONTAL = True
DEFAULT_FORCE = 10
def extraction_example():
    _extracted_from_extraction_example_2("Speed", DEFAULT_SPEED)
    _extracted_from_extraction_example_2("Force", DEFAULT_FORCE)


# TODO Rename this here and in `extraction_example`
def _extracted_from_extraction_example_2(label, arg1):
    speed_slider = Scale("parent", from_=1, to=10, orient=HORIZONTAL, label=label)
    speed_slider.pack()
    speed_slider.set(arg1)
    speed_slider.configure(background="white")

# Custom Rules
class ExampleBaseClass:
    def abstract_method(self):
        raise NotImplementedError


def print_sourcery_yaml():
    with open(".sourcery.yaml") as f:
        print(f.read())
