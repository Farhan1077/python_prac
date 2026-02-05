
def dictdemo():
    d1 = {'a': 1, 'b': 2, 'c': 3}
    print("Dictionary d1:", d1)

    d1['d'] = 4  # Adding a new key-value pair
    print("Dictionary d1 after adding ('d', 4):", d1)
    
    # iterating through the dictionary
    for key, value in d1.items():
        print(f"Key: {key}, Value: {value}")
        
    # updating a value
    d1['a'] = 10
    print("Dictionary d1 after updating 'a':", d1)
    
    #deleting a key-value pair
    del d1['b']
    print("Dictionary d1 after deleting 'b':", d1)
def setdemo():
    s1= {1, 2, 3, 4, 5}
    print("Set s1:", s1)

    s1.add(6)  # Adding an element to the set
    print("Set s1 after adding 6:", s1)
    
    # iterating through the set
    for item in s1:
        print(f"Set item: {item}")

def main():
    # setdemo()
    dictdemo()
    
if __name__ == "__main__":
    main()

