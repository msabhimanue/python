
l1=[1,1,8,4,6,5,6,5]
small=min(l1)
large=max(l1)
a=list(set(l1))
additional_l1=[10,7,9]
l1.extend(additional_l1)
print("smallest of the list is : ",small)
print("largest of the list is: ",large)
print("List without duplicate is: ",a)
print("List after appending : ",l1)
