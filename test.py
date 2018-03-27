def main():
    x=input("Please enter x:")
    y=input("Please enter y:")
    z=multiply(x,y)
    print(z)
    z=divide(x,y)
    print(z)

def multiply(x,y):
    return int(x)*int(y)


def divide(x,y):
    return float(x)/float(y)


main()
