import os
from enum import Enum


class Season(Enum):
  SPRING = 1
  SUMMER = 2
  AUTUMN = 3
  WINTER = 4
  
  def __str__(self):
    return self.name
  
  def __repr__(self):
    return f"{self.name} ({self.value})"


if __name__ == "__main__":
  print(f"os.path is \n\t{'\n\t'.join(os.path.defpath.split(':'))}")
  print()
  print("repr of Spring?: " + repr(Season.SPRING))
  print()
