## input 3 lengths to see if those three values(as sides of the tiangle) can
## make a valid triangle 
# @params a : first length
# @params b : second legnth
# @params c : third length
def valid_triangle(a,b,c):
    sides = [a,b,c]
    largest = max(sides)
    sides.remove(largest)
    if sum(sides) <= largest:
        print('The three sides do not make a valid triangle.')
    else:
        print('The three sides make a valid triangle.')
        
def main():
    print('Please input a real number each time you are prompted.')
    x = float(input('First  length: '))
    y = float(input('Second length: '))
    z = float(input('Third  length: '))
    print("")
    valid_triangle(x,y,z)

if __name__ == "__main__":
    main()