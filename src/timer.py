"""
Timer program for brewing coffee!
"""
import time
import sys
from typing import Optional
from src.brew import Brew

def timer(
        brew: Brew,
        interval: Optional[int] = 45
    ):
    total_time: int = interval * brew.get_num_pours()
    print(brew_1.get_info())
    print(f"Total seconds is {total_time}")

    try:
        for i in range(total_time):
            minutes = i // 60
            seconds = i % 60
            time.sleep(1)
            if i % interval == 0:
                pour_num: int = i // interval + 1
                sys.stdout.write(f" Time to do pour #{pour_num}")
            timer_display:str = f"{minutes:02d}:{seconds:02d}"
            sys.stdout.write(f"\rTime elapsed: {timer_display}")
    except KeyboardInterrupt:
        print("\nTimer stopped.")





if __name__ == "__main__":
    brew_1 = Brew(beans="Ignis Bourbon")
    timer(brew_1)

