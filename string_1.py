def target(str):

    string = str
    shortest_str = string[0]

    for i in string:
        if (len(i) < len(shortest_str)):
                shortest_str = i

    string.remove(shortest_str)

    # comparing shorest string 
    for j in range(len(string)):
        temp = ''
        for i in range(len(shortest_str)):
            if (shortest_str[i] == string[j][i]):
                temp += shortest_str[i]

        shortest_str = temp
    
    print(temp)


string =['light','live','liver']
target(string)
