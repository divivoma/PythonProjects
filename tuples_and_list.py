# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 10:29:42 2018

@author: Markos
"""
#tuple are immutable, t[1]=4 doesn't work
#t= (2,"mit",3) 
#print(t)
#print("len=",len(t))


def get_data(aTuple):   #Example with Tuple of Tuples !!
    """
    aTuple, tuple of tuples (int, string)
    Extracts all integers from aTuple and sets 
    them as elements in a new tuple. 
    Extracts all unique strings from from aTuple 
    and sets them as elements in a new tuple.
    Returns a tuple of the minimum integer, the
    maximum integer, and the number of unique strings
    """
    nums = ()    # empty tuple
    words = ()
    for t in aTuple:
        # concatenating with a singleton tuple
        nums = nums + (t[0],)   
        # only add words haven't added before
        if t[1] not in words:   
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)

#test = ((1,"a"),(2, "b"),(1,"a"),(7,"b"))
#
#(a, b, c) = get_data(test)
#
#print("a:",a,"b:",b,"c:",c)

# apply to any data you want!
#tswift = ((2014,"Katy"),
#          (2014, "Harry"),
#          (2012,"Jake"), 
#          (2010,"Taylor"), 
#          (2008,"Joe"))    
#(min_year, max_year, num_people) = get_data(tswift)
#print("From", min_year, "to", max_year, \
#        "Taylor Swift wrote songs about", num_people, "people!")
    

#LIST is a sorted sequence of information accessible by index. 
#   Usually contains  homogeneous type elements but can contains also mixed
#   List is MUTABLE



#########################
## EXAMPLE: aliasing
#########################
#a = 1
#b = a
#print(a)
#print(b)
#
#warm = ['red', 'yellow', 'orange']
#hot = warm
#hot.append('pink')
#print(hot)
#print(warm)

#########################
## EXAMPLE: cloning
#########################
#cool = ['blue', 'green', 'grey']
#chill = cool[:]
#chill.append('black')
#print(chill)
#print(cool)

#########################
## EXAMPLE: sorting with/without mutation
#########################
#warm = ['red', 'yellow', 'orange']
#sortedwarm = warm.sort()
#print(warm)
#print(sortedwarm) #not working!
#
#cool = ['grey', 'green', 'blue']
#sortedcool = sorted(cool) #this works instead!
#print(cool)
#print(sortedcool)

#########################
## EXAMPLE: lists of lists of lists... COOL EXAMPLE! (marco)
#########################
#warm = ['yellow', 'orange']
#hot = ['red']
#brightcolors = [warm]
#brightcolors.append(hot)
#print(brightcolors)
#hot.append('pink')  #we are modifying the hot list !
#print(hot)
#print(brightcolors) #now we get also the updated hot list too!


###############################
## EXAMPLE: mutating a list while iterating over it
###############################
def remove_dups(L1, L2):    #avoid list mutation while iterating over it !!
    for e in L1:
        if e in L2:
            L1.remove(e)
#mutating changes the list len but Python doesn’t update its internal counter
      
def remove_dups_new(L1, L2):
    L1_copy = L1[:]
    for e in L1_copy:#work instead on a copy of the list for the iteration !!
        if e in L2:
            L1.remove(e) #and remove the element from the original list

#L1 = [1, 2, 3, 4]
#L2 = [1, 2, 5, 6] 
#remove_dups(L1, L2)
#print(L1, L2)
#
#L1 = [1, 2, 3, 4]
#L2 = [1, 2, 5, 6]
#remove_dups_new(L1, L2)
#print(L1, L2)



###############################
## EXERCISE: Test yourself by predicting what the output is and 
##           what gets mutated then check with the Python Tutor
###############################
cool = ['blue', 'green']
warm = ['red', 'yellow', 'orange']
print(cool)
print(warm)

colors1 = [cool]
print(colors1)
colors1.append(warm)
print('colors1 = ', colors1)

colors2 = [['blue', 'green'],
          ['red', 'yellow', 'orange']]
print('colors2 =', colors2)

warm.remove('red') 
print('colors1 = ', colors1) #[['blue', 'green'], ['yellow', 'orange']]
print('colors2 =', colors2)

for e in colors1:
    print('e =', e) #print the 2 element of the list colors1

for e in colors1:
    if type(e) == list:
        for e1 in e:
            print(e1) #print all the elements of the list
    else:
        print(e)

flat = cool + warm #list internal concatenation
print('flat =', flat)

print(flat.sort()) #not working !! (None)
print('flat =', flat)

new_flat = sorted(flat, reverse = True)
print('flat =', flat)
print('new_flat =', new_flat)

cool[1] = 'black'
print(cool)
print(colors1)
    




