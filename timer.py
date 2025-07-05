"""
Timer program for brewing coffee!
"""
import time
from typing import Optional
from src.brew import Brew

def timer(
        brew: Brew,
        interval: Optional[int] = 45
    ):
    human_readable_time = time.ctime()
    print(brew_1.get_info())
    print(f"Time: {human_readable_time}")




if __name__ == "__main__":
    brew_1 = Brew(beans="Ignis Bourbon")
    timer(brew_1)

