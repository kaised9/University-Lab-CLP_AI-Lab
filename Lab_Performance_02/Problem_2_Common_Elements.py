list_1=[1,2,3,4,5,6]
list_2=[1,4,5,6,7,8,9]

setNo_1=set(list_1)
setNo_2=set(list_2)

find_common_elements=setNo_1.intersection(setNo_2)
find_common_elements_list=list(find_common_elements)

print("Common Elements Are : ",find_common_elements_list)
