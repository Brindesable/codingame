import sys
import math

# Quick sort algorithm from :
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html
def quickSort(list):
    quickSortHelper(list,0,len(list)-1)

def quickSortHelper(list,first,last):
    if first<last:
        splitpoint = partition(list,first,last)
        quickSortHelper(list,first,splitpoint-1)
        quickSortHelper(list,splitpoint+1,last)


def partition(list, first, last):
    pivotvalue = list[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and list[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while list[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
           temp = list[leftmark]
           list[leftmark] = list[rightmark]
           list[rightmark] = temp

    temp = list[first]
    list[first] = list[rightmark]
    list[rightmark] = temp


    return rightmark

# Here the budget of each Ood
budgets = []
# Here wha will have each Ood to pay
contributions = []

n = int(raw_input())
total = int(raw_input())
for i in xrange(n):
    b = int(raw_input())
    budgets.append(b)

# We sort the budgets
quickSort(budgets)

# We calculate a mean amount of money each Ood has to pay
mean = int(total/n)
for budget in budgets:
    contribution = 0
    if budget >= mean:
        contribution = mean
    else:
        contribution = budget

    contributions.append(contribution)

    # Because some hasn't enough money, we recalculate the mean each time
    total -= contribution
    n -= 1
    if n > 0:
        mean = total/n

# If there isn't enough money t pay
if total > 0:
    print "IMPOSSIBLE"
else :
    for contribution in contributions:
        print contribution