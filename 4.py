# Excersize 4
#Create a program that reads the length and width of a farmer’s field from the user in
#feet. Display the area of the field in acres.

length = float(input('Enter the field length in feet: '))
width = float(input('Enter the field width in feet: '))
sfPerAcre = 43560
area = str(((length * width)/sfPerAcre))
print('The field is ' + area + ' acres')