
def dictdemo():
    d1 = {'a': 1, 'b': 2, 'c': 3}
    print("Dictionary d1:", d1)

    d1['d'] = 4  # Adding a new key-value pair
    print("Dictionary d1 after adding ('d', 4):", d1)
def setdemo():
    s1= {1, 2, 3, 4, 5}
    print("Set s1:", s1)

    s1.add(6)  # Adding an element to the set
    print("Set s1 after adding 6:", s1)

def main():
    # setdemo()
    dictdemo()
    
if __name__ == "__main__":
    main()

