from E85_Convert_an_Integer_to_its_Ordinal_Number import make_ordinal

    ## verse() function returns the verse for a given day in 12 days of christmas
    # @param day : the day you want the verse for. From 1 to 12
def verse(day):
    day = day-1
    days = [
        'And a partridge in a pear tree',
        'Two turtle doves',
        'Three French hens',
        'Four calling birds',
        'Five gold rings',
        'Six geese a laying',
        'Seven swans a swimming',
        'Eight maids a milking',
        'Nine ladies dancing',
        'Ten lords a leaping',
        'Eleven pipers piping',
        '12 drummers drumming',
    ]
    return(days[day])
    

def main():
    # For loop to construct the song
    for n in range(1,12+1):
        print(f"On the {make_ordinal(n)} day of Christmas \n My true love gave to me")
        for i in range(1,n+1):
            print(verse(n+1-i))
        print('\n')
if __name__ == "__main__":
    main()
