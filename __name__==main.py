def calculate_arae(base, height):
    print("__name__:",__name__)
    return 1/2*(base*height)

if __name__=="__main__":
    print("I'm in area.py")
    a=calculate_arae(10,20)
    print("area:",a)