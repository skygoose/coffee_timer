"""
Class for each brew.
"""
from typing import Optional, Tuple
class Brew:
    # Class attributes
    brew_type: str = "v60"
    coffee_weight: int = 15
    water_ratio: Tuple[int, int] = (1, 15)
    num_pours: int = 5

    # Constructor
    def __init__(
                self, 
                beans: str,
                brew_type: Optional[str] = None,
                coffee_weight: Optional[int] = None, 
                water_ratio: Optional[Tuple[int, int]] = None, 
                num_pours: Optional[int] = None,
            ):
            self.beans = beans
            if brew_type is not None:
                self.brew_type = brew_type
            if coffee_weight is not None:
                 self.coffee_weight = coffee_weight
            if water_ratio is not None:
                self.water_ratio = water_ratio
            if num_pours is not None:
                self.num_pours = num_pours
                 
    # Getter method
    def get_info(self):
        return (
             f"Brewing a {self.brew_type} with {str(self.coffee_weight)}g of {self.beans} "
             f"coffee in a {self.water_ratio[0]}:{self.water_ratio[1]} ratio, "
             f"doing {self.num_pours} pours."
             )

    def get_brew_type(self):
         return self.brew_type
    
    def get_coffee_weight(self):
         return self.coffee_weight
    
    def get_beans(self):
         return self.beans
    
    def get_water_ratio(self):
         return self.water_ratio
    
    def get_num_pours(self):
         return self.num_pours
    
    
    
if __name__ == "__main__":
    # Test code for random brew
    brew_1 = Brew(brew_type = "v60", beans="Ignis Bourbon", coffee_weight=15, water_ratio=(1, 15))
    print(brew_1.get_info())

    # brew_2 = brew(beans="Ignis Bourbon")
    # print(brew_2.get_info())
