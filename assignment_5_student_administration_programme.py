# -*- coding: utf-8 -*-
"""Assignment 5 Student Administration programme

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B67lZj5Pif_xqJBhKNdNxI_ziV4grQwY
"""

import csv

class Student:
  def __init__(self, name, age, roll_no, contact_no, email_id):
    self.name = name
    self.age = age
    self.roll_no = roll_no
    self.contact_no = contact_no
    self.email_id = email_id

  def display_details(self):
    print("Name:", self.name)
    print("Age:", self.age)
    print("Roll No:", self.roll_no)
    print("Contact No:", self.contact_no)
    print("Email ID:", self.email_id)

  def to_csv(self):
    return [self.name, self.age, self.roll_no, self.contact_no, self.email_id]


# Main Program
print("Welcome to the School Administration Program")

#Write to CSV file
with open("students.csv", "a", newline ="") as file:
  writer = csv.writer(file)

  while True:
    print("Enter the following student details(or type'quit' to exit)")
    name = input("Name: ")
    if name.lower() == "quit":
      break
    age = input("Age: ")
    roll_no = input("Roll No: ")
    contact_no = input("Contact No: ")
    email_id = input("Email ID: ")

    student = Student(name, age, roll_no, contact_no, email_id)

    print("\nStudent Details:")
    student.display_details()

    writer.writerow(student.to_csv())