#program 11 anudip foundation
# Example of a list representing tabular data
from tabulate import tabulate
student = [
    ["stdid","stdname","standard","age","Hindi","English","Maths","Science","Computer","Total"],
    ["std101","Ashish ","10th",15,67,89,87,89,90,422],
    ["std102","Abhishek ","10th",14,85,45,48,90,45,313],
    ["std103","Aman","10th",15,23,56,78,78,67,302],
    ["std104","Rahul","10th",14,45,67,45,45,56,258],
    ["std105","Ruby","10th",13,89,67,89,93,65,403],
    ["std106","Suman","10th",13,90,46,67,67,67,337],
    ["std107","Saurabh","10th",15,45,23,34,45,34,181],
    ["std108","Sumit","10th",14,23,45,67,78,90,303],
    ["std109","Kamlesh","10th",15,45,56,78,99,67,345],
    ["std110","Rohan","10th",15,34,12,24,45,56,171]
]
def print_table(student): 
     for row in student:
        print("| {:<10} | {:<10} | {:<10} | {:<5} | {:<5} | {:<10} | {:<5} | {:<10} | {:<10} | {:<5} |".format(*row))
def query_1(student):
    print("\nQuery 1: Names of students whose marks in English are greater than 50")
    for row in student[1:]:  
        if row[6] > 50:  
            print(row[1])
def query_2(student):
    print("\nQuery 2: Names and ages of the top four scorers in Maths")
    sorted_table = sorted(student[1:],  reverse=True)  
    for row in sorted_table[:4]:
        print(f"{row[1]:<10} | Age: {row[3]:<7} |")
def query_3(student):
    print("\nQuery 3: Names,id nd ages student who are bottom three scorer in computer")
    sorted_table = sorted(student[1:],  reverse=True)  
    for row in sorted_table[:3]:
        print(f"{row[1]:<10} | Age: {row[3]:<7} |")
    
print_table(student)
query_1(student)
query_2(student)
query_3(student)
