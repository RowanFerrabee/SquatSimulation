from human import *
from read_profile import *

def main():
    rowan_profile = 'avg_male.csv'
    rowan_height = 171
    rowan_weight = 64

    squatter = read_profile(rowan_profile, rowan_height, rowan_weight)

    print(squatter)

if __name__ == '__main__':
    main()