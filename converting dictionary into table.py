#program 9 anudip foundation
#convering manually input dictionary into table 
from tabulate import tabulate
table = [ #dictionary is taken inside the list because we need only values for the table , keys are not needed
    {"stdid": "std101", "stdname": "Ashish ", "standard": "10th", "age": 15, "Hindi": 67, "English": 89, "Maths": 87, "Science": 89, "Computer": 90, "Total": 422},
    {"stdid": "std102", "stdname": "Abhishek ", "standard": "10th", "age": 14, "Hindi": 85, "English": 45, "Maths": 48, "Science": 90, "Computer": 45, "Total": 313},
    {"stdid": "std103", "stdname": "Aman", "standard": "10th", "age": 15, "Hindi": 23, "English": 56, "Maths": 78, "Science": 78, "Computer": 67, "Total": 302},
    {"stdid": "std104", "stdname": "Rahul", "standard": "10th", "age": 14, "Hindi": 45, "English": 67, "Maths": 45, "Science": 45, "Computer": 56, "Total": 258},
    {"stdid": "std105", "stdname": "Ruby", "standard": "10th", "age": 13, "Hindi": 89, "English": 67, "Maths": 89, "Science": 93, "Computer": 65, "Total": 403},
    {"stdid": "std106", "stdname": "Suman", "standard": "10th", "age": 13, "Hindi": 90, "English": 46, "Maths": 67, "Science": 67, "Computer": 67, "Total": 337},
    {"stdid": "std107", "stdname": "Saurabh", "standard": "10th", "age": 15, "Hindi": 45, "English": 23, "Maths": 34, "Science": 45, "Computer": 34, "Total": 181},
    {"stdid": "std108", "stdname": "Sumit", "standard": "10th", "age": 14, "Hindi": 23, "English": 45, "Maths": 67, "Science": 78, "Computer": 90, "Total": 303},
    {"stdid": "std109", "stdname": "Kamlesh", "standard": "10th", "age": 15, "Hindi": 45, "English": 56, "Maths": 78, "Science": 99, "Computer": 67, "Total": 345},
    {"stdid": "std110", "stdname": "Rohan", "standard": "10th", "age": 15, "Hindi": 34, "English": 12, "Maths": 24, "Science": 45, "Computer": 56, "Total": 171}
]
table_data = [] #list 2
for row in table:
    table_data.append([row['stdid'], row['stdname'], row['standard'], row['age'],
                       row['Hindi'], row['English'], row['Maths'], row['Science'],
                       row['Computer'], row['Total']])
#defining header for the table
headers = ["stdid", "stdname", "standard", "age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]
#printing the table
print(tabulate(table_data, headers=headers, tablefmt="grid"))

#query_1: Students whose marks in english are greater than 50
# Filter the students based on marks in English greater than 50
filtered_students = [student for student in table if student['English'] > 50]

# Extract relevant information (stdname and age) for the filtered students
filtered_data = [[student['stdname'], student['age']] for student in filtered_students]

# Print the results using tabulate
print("Students whose marks in English are greater than 50:")
print(tabulate(filtered_data, headers=["Name", "Age"], tablefmt="grid"))

#query_2 : Display students name and age of top four scorer of maths
# Sort students based on marks in Maths (descending order)
sorted_students = sorted(table, key=lambda x: x['Maths'], reverse=True)

# Extract names and ages of the top four scorers
top_scorers = [[student['stdname'], student['age']] for student in sorted_students[:4]]

# Print the results using tabulate
print("Names and ages of the top four scorers in Maths:")
print(tabulate(top_scorers, headers=["Name", "Age"], tablefmt="grid"))
