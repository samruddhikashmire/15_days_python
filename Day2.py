'''Question 1: 
Write a Python function that takes a list of numbers as input and returns a new list containing only the even numbers.
Test your function with a sample list and ensure it handles various cases gracefully.'''

def even_nums(lis):
    res=[]
    for i in lis:
        if(i%2==0):
            res.append(i)
    return res
 sample = [22,53,45,62,2,7,23,98,52,68]
result = even_nums(sample)
print("Original List: " ,sample)
if(len(result)==0):
    print("There are no even Numbers in the list ")
else:
       print("Even Numbers:" ,result)


# Question 2
'''Create a Python program that reads a text file named "input.txt," counts the occurrences of each word, and then writes the word count to a new file named "output.txt." 
Ensure the program handles file not found and other potential errors.'''

try:
    ifile = open("input.txt" , 'r')
    data = ifile.read()
        
    count={}
    words = data.split()
    for i in words:
        count[i] = count.get(i,0)+1
        
        
    ofile = open("output.txt", 'w')
    for i, c in count.items():
        ofile.write(f"{i}: {c}\n")
        
    except FileNotFoundError:
    print("File not find")
finally:
    ifile.close()
    ofile.close()
