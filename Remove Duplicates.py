def removeDuplicates(listofElements):
    List = []

    for elem in listofElements:
        if elem not in List:
            List.append(elem)
    return List
 
def main():

    listOfNums = [0,0,1,1,1,2,2,3,3,4,5,5,7]
    listOfNums = removeDuplicates(listOfNums)
    print("List with elements : ", listOfNums)

if __name__ == '__main__':
    main()

