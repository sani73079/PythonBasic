#tuple is same as data type but it is immutable
val = (1,2,"sandhya",4.5)
print(val[3])

val[2]="janki"
print(val) #TypeError: 'tuple' object does not support item assignment it means tuple is locked and immutable cannot modify want to change convert val into list[]
