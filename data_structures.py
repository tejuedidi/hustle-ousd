# Commpnly Used Data Structures
#? Can anyone list types of data and data structures we have worked with
# * strings
# * lists
# * dictionaries
# * boolean
# * numbers (unt and float)
# * tuple
# * set


#? what are sequence types?
# * ordered collection of items of some data type/types accessed via an index
# * index is just a position, each element given an index starts at 0

hobbies = ["painting", "teaching", "crafts", 1,2,3,4,5,6,7,8,10,11,"car", "video"] # list of strings

#? indexing (pos and neg)

print(hobbies[1:8])


#? adding elements in a seq string ver
# * + or += operator
# * .join() all items in an interable and joins them into one
# * f-strings (formatted string literal)
# * split()

test = "word"


# print(test.split())
# print(test+ ' '+ hassan)


#  * 15


#? adding elements in a seq list ver
# * append 
# * extend (end of list)
# * insert (specific index)
numbs = [1,2,5,6,7]
# append 
numbs.append(9)
# print(numbs)

numbs.extend([8])
# print(numbs)

numbs.append(9)

#? removing elements in a seq ver string
#* .replace()
#* slicing [start:end:step] (del [slicing])
hassan = "idek"
# print(hassan[0:2])


#? removing elements in a seq ver list
#* .remove() removes specific element
#* .pop() remove and return element at specific index
#* clear()
ex = ["blue", "cat", "johnny", "red", "yellow"]
# ex.remove("cat")
# print(ex)

ex = ["blue", "johnny", "red", "yellow"]
# ex.remove("cat")
# print(ex)
ex.pop(1)
# print(ex)


#? dictionaries