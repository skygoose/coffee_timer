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
    print(brew.get_num_pours())
    total_time: int = interval * brew.get_num_pours()
    total_minutes: int = total_time // 60
    total_seconds: int = total_time % 60
    print(brew.get_info())
    print(f"Total brew time to last pour is {total_minutes}:{total_seconds}")
    try:
        for i in range(total_time):
            minutes, seconds = divmod(i, 60)
            time.sleep(1)
            pour_num: int = i // interval + 1
            pour_to_weight: int = pour_num * brew.get_coffee_weight() * brew.get_water_ratio()[1] / brew.get_water_ratio()[0] / brew.num_pours
            timer_display:str = f"{minutes:02d}:{seconds:02d}"
            sys.stdout.write(f"\rPour #{pour_num} until {pour_to_weight}g - {timer_display}")
            sys.stdout.flush()
        print("You have finished your brew! Enjoy :)")
    except KeyboardInterrupt:
        print("\nTimer stopped.")





if __name__ == "__main__":
    # Test Brew
    brew_1 = Brew(beans="Ignis Bourbon")
    timer(brew_1)

