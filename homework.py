# 1.Reverse the order of the items in an array.
# Example:
#   a = [1, 2, 3, 4, 5]
#   Result:
#   a = [5, 4, 3, 2, 1]

def reverseFunction(aList):
    return aList.reverse()

a=[1,2,3,4,5]

reverseFunction(a)
print(a)

# 2. Get the number of occurrences of var b in array a.
#   Example:
#   a = [1, 1, 2, 2, 2, 2, 3, 3, 3]
#   b = 2
#   Result:
#   4

def occurencesNr(aList,elem):
    return aList.count(elem)

b = [1,1,2,2,2,2,3,3,3]
c = 3

d = occurencesNr(b,c)
print(d)


# 3. Given a sentence as string, count the number of words in it.
#   Example:
#   a = 'ana are mere si nu are pere'
#   Result:
#   7

def wordsCounter(aString):
    return len(aString.split())

string = 'ana are mere si nu are pere'
ret = wordsCounter(string)
print(ret)