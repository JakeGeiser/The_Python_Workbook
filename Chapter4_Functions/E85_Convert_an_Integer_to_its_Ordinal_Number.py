
# make_ordinal is taken form Florian Brucker
# https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement

## Returns the numeric ordianl number (1st,2nd,3rd, etc)
# @param n : the integer you want the ordinal number of
def make_ordinal(n):
    '''
    Convert an integer into its ordinal representation::

    make_ordinal(0)   => '0th'
    make_ordinal(3)   => '3rd'
    make_ordinal(122) => '122nd'
    make_ordinal(213) => '213th'
    '''
    n = int(n)
    suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    return str(n) + suffix

# main function to run through the first 100 integers
def main():
    for num in range(1,101):
        print(make_ordinal(num))
if __name__ == "__main__":
    main()