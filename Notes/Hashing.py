# to apan ek array banaenge of some size N with all element as zero jisme hum index ko as element represnt kar rahe honge and 
# occurence ko index se compare kakre us index mein +1 kar denge

# Problem 1 -> Count the Occurence of elements

n=int(input("Enter the size of your Array : "))
Array=[]*n
for i in range(n):
  element=int(input(f"Enter {i+1}th Element: "))
  Array.append(element)

##preCompute
hash=[0]*13
for i in range(n):
  hash[Array[i]]+=1

q=int(input("Enter no of elements you want to Search : "))
while q>0 :
  number=int(input("Enter a number : "))
  print(hash[number])
  q-=1

  # Problem 2 -> Count the Occurence of Character

str = input("Enter your String : ")

# Create a hash table to store character frequencies
hash_table = {}

# Precompute character frequencies
for char in str:
    hash_table[char] = hash_table.get(char, 0) + 1

#freq_dict.get(char, 0): This part safely retrieves the value for the key char. 
# If the key char exists in the dictionary, its value is returned. Otherwise, 
# the default value 0 is returned.

p = int(input("Enter no of Char you want to Search : "))
while p > 0:
    c = input("Enter a char : ")
    print(hash_table.get(c, 0))  # Get frequency, default to 0 if not found
    p -= 1
    
# Which element has the highest Freq
# highest and lowest freq of element

n=int(input("Enter the size of your Array : "))
Array1=[]*n
for i in range(n):
  element=int(input(f"Enter {i+1}th Element: "))
  Array1.append(element)

hash_table={}

highest_freq=0
max_element=0
for high in Array1:
    hash_table[high] = hash_table.get(high, 0) + 1

for num , freq in hash_table.items():
    if freq>highest_freq:
        highest_freq=freq
        max_element=num

print(max_element)