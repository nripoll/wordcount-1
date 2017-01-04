happy = input("Enter a statement:")

words = happy.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

    
print("the word frecuency of your input is: ")
print(counts)
