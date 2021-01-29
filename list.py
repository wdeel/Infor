def main():

    # test cases, uncomment which one you want to run
    list1 = [7, 5, 5]
    #list1 = [3, 3, 3, 2, 2, 1]
    #list1 = [5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 2, 2, 1]

    # dictionary
    entry = { }

    # iterate through the list
    for i in list1:
        # check dictionary for key, if not there, add it and initialize 
        # value (# of occurences to 1)
        if i not in entry:
            entry[i] = 1
        # key is already there, increment # of occurences (value)
        else:
            entry[i] += 1

    print(entry)

main()