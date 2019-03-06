list_x = [1,2,4]
list_y = [1,3,4]
value_x = 0
value_y = 0
mergedtwosortlisted = []
while value_x<len(list_y) or value_y < len(list_y):
    if value_x<len(list_x) and list_x[value_x]<=list_y[value_y]:
        mergedtwosortlisted.append(list_x[value_x])
        value_x +=1
    elif value_y<len(list_y):
        mergedtwosortlisted.append(list_y[value_y])
        value_y +=1
print mergedtwosortlisteds
