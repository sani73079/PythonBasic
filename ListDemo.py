#         0 1   2       3  4
values = [1,2,"sandhya",4,5]
#negative-5 -4 -3      -2 -1
#list is datatype that allows  multiple  values and can be diffrent  data types
print(values[1])
print(values[-1])
print(values[1:3]) #[2, 'sandhya']
#insert
values.insert(3,"shetty")
print(values)  #[1, 2, 'sandhya', 'shetty', 4, 5]

#Append
values.append("end")
print(values) #[1, 2, 'sandhya', 'shetty', 4, 5, 'end']

#Update
values[3]= "janki"
print(values)  #[1, 2, 'sandhya', 'janki', 4, 5, 'end']

#delete
del values[1]
print(values) #[1, 'sandhya', 'janki', 4, 5, 'end']


