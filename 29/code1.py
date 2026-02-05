
    
def count_elements(lst):
        counts = {}
        for element in lst:
            if element in counts:
                counts[element] += 1
            else:
                counts[element] = 1
        return counts

def key_checks(keys):
    result = {}
    key = "b"
    for dictionary in keys:
        if key in dictionary:
        
            print("key found")
        else:
        
            print("key not found")
            
def tupletodict():
    Input = (("a", 1), ("b", 2))
    result = dict(Input)
    print(result)

def reversedlist(): 
    input = "data science is fun"
    a = input.split()
    result = a[::-1] 
    print (result)

def sumoftuples(tuples):
    result = []
    for tup in tuples:
        result.append(sum(tup))
    return result

def stringlengths(strings):
    lengths = {}
    for string in strings:
        lengths[string] = len(string)
    return lengths    

def uniquechars(string):
    unique_characters = tuple(string)
    return unique_characters

def filterevennumbers():
    numbers = [1, 2, 3, 4, 5, 6]
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    print(result)
    
def averagemarks():
    marks = [("Alice", [80, 90]), ("Bob", [70, 85, 90])]
    averages = {}
    for name , scores in marks:
        avg = sum(scores) / len(scores)
        NAME = name.lower()
        averages[NAME] = avg
    print(averages)
    
def wordfrequencies():
    text = "Python is great and Python is easy"
    words  = text.split()
    frequencies = {}
    for word in words:
        word_lower = word.lower()
        if word_lower in frequencies:
            frequencies[word_lower] += 1
        else:
            frequencies[word_lower] = 1
    print(frequencies)
    
def highestsellingproducts():
    sales = [("Pen", 10), ("Pencil", 25), ("Pen", 15)]
    total_sales = {}
    for product, quantity in sales:
        if product in total_sales:
            total_sales[product] += quantity
        else:
            total_sales[product] = quantity
    highest_selling = max(total_sales, key=total_sales.get)
    print(f"Highest selling product: {highest_selling} ")
    
def uniquevalueextraction():
    data = {"a": [1, 2, 3], "b": [3, 4], "c": [2, 5]}
    unique_values = list()
    for values in data.values():
        for value in values:
            if value not in unique_values:
                unique_values.append(value)
                reult = sorted(unique_values)
    print(reult)

def main():
        # input1 = "programming"
        # #input2 = {"a": 1, "b": 2}, 
        
        # # result = count_elements(input2)
        # #result2 = key_checks(input2)
        # #print(result2)
        # #result = sumoftuples(input1)
        # #result  = stringlengths(input1)
        # result = uniquechars(input1)
        # print(result)
    filterevennumbers()
    averagemarks()
    wordfrequencies()
    highestsellingproducts()
    uniquevalueextraction()
    
        
    
        
if __name__ == "__main__":
    main()
    #tupletodict()
    #reversedlist()