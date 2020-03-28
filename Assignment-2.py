#!/usr/bin/env python
# coding: utf-8

# Assignment -2

# 1.1
# Write a Python Program to implement your own myreduce() function which works exactly like
# Python's built-in function reduce()

# In[3]:


# python code to demonstrate working of reduce() 

# importing functools for reduce() 
import functools 

# initializing list 
lis = [ 1 , 3, 5, 6, 2, ] 

# using reduce to compute sum of list 
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(lambda a,b : a+b,lis)) 

# using reduce to compute maximum element from list 
print ("The maximum element of the list is : ",end="") 
print (functools.reduce(lambda a,b : a if a > b else b,lis)) 


# In[6]:


# Reduce will produce a single result
def myreduce(anyfunc, sequence):

 # Get first item in sequence and assign to result
  result = sequence[0]
 # iterate over remaining items in sequence and apply reduction function 
  for item in sequence[1:]:
   result = anyfunc(result, item)

  return result

# test myreduce function
def sum(x,y): return x + y

print ("Sum on list [1,2,3] using custom reduce function "   + str(myreduce(sum, [1,2,3])) )


# Write a Python program to implement your own myfilter() function which works exactly like
# Python's built-in function filter()

# In[7]:


# function that filters vowels 
def fun(variable): 
	letters = ['a', 'e', 'i', 'o', 'u'] 
	if (variable in letters): 
		return True
	else: 
		return False


# sequence 
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 

# using filter function 
filtered = filter(fun, sequence) 

print('The filtered letters are:') 
for s in filtered: 
	print(s) 


# In[8]:


# Custom filter function 
def myfilter(anyfunc, sequence):

 # Initialize empty list
 result = []
 # iterate over sequence of items in sequence and apply filter function
 for item in sequence:
  if anyfunc(item):
   result.append(item)

 # return funal output
 return result
# test myfilter function
def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True
print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))


# 2.
# Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[10]:


########
word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ("ACADGILD => " + str(alphabet_list))

#########
# Compress above for loop into a single list comprehension using technique [i <Upper for condition> <lower for condition>]
input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))

#########
# Compress above for loop into a single list comprehension using technique [i <Upper for condition> <lower for condition>]
input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print("['x','y','z'] => " +   str(result))

#########
input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))

#########
input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))

#########
input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# 3.
# Implement a function longestWord() that takes a list of words and returns the longest one.

# In[17]:


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["CHIRU", "Chiranjeevi", "Chiranjeevi Elaboina"]))


# 1.1
# Write a Python Program(with class concepts) to find the area of the triangle using the below
# formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

# 1.2
# Write a function filter_long_words() that takes a list of words and an integer n and returns the list
# of words that are longer than n.

# In[20]:


def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(3, "The quick brown fox jumps over the lazy dog"))


# 2.1
# Write a Python program using function concept that maps list of words into a list of integers
# representing the lengths of the corresponding words .
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# In[21]:


listOfWords = ['wordOne','wordTwo','wordThree','wordFour','wordFive']
 
listOfInts = []
 
for i in range(len(listOfWords)):
    listOfInts.append(len(listOfWords[i]))
 
print ("List of words:"+str(listOfWords))    
print ("List of wordlength:"+str(listOfInts))


# 2.2
# Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is
# a vowel, False otherwise.

# In[30]:


def is_vowel(char):
    all_vowels = 'aeiou''AEIOU'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))


# In[23]:





# In[ ]:




