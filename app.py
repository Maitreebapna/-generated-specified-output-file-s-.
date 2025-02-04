
import sys
import pandas as pd
import matplotlib.pyplot as plt
from jinja2 import Template
import csv 

with open('data.csv',newline ='') as csvfile:
    reader = csv.reader(csvfile)

student_course=[]
Course_data=[]
course_marks=[]

input_list=sys.argv

#read the arguments 
#1) -s then calculate the render
#2) -c then calculate the render
#3) something wrong 

#app.py -s 1002

total=0
if len(input_list) > 1 and input_list[1]=='-s':
    with open('data.csv', "r", newline="") as csvfile:
        reader = csv.reader(csvfile)  # Create CSV reader
        for row in reader:  # Iterate inside the 'with' block
            print(row)  # Process each row safely'''for row in reader:
        '''if input_list[2] in row[0]:
            total+=int(row[2].strip())
            student_course.append(row)'''

if student_course==[]:
    data=''' <h1>Wrong Input</h1>
        <p> Something Went Wrong</p>'''
    File=open('output.html','w')
    File.write(data)
    File.close()   

else:
    text='''<h1> Student Details</h1>
        <table>
            <tr>
                <th> Student ID</th>
                <th> Course ID</th>
                <th> Marks</th>
            </tr>
            {% for student in student_course%}
            <tr>
                <td>{{student[0].strip()}}</td>
                <td>{{student[1].strip()}}</td>
                <td>{{student[2].strip()}}</td>
            </tr>    
            {%endfor%}         
            <tr>
                <td colspan ="2"> Total Marks </td>
                <td> {{total}} </td>
            </tr>
        </table>  '''
    temp=Template(text) 
    output1=temp.render(total=total,student_course=student_course)
    File=open('output.html','w')
    File.write(output1)
    File.close()

    if len(input_list) > 1:
        if input_list[1] == 'c':
            course_marks.append #print("Processing")

    '''for row in render:
            if input_list[2] in row[1]:
    '''

    if course_marks ==[]:
        data=''' <h1> Wrong Inputs</h1>
        <p>Something Went Wrong</p>'''
        File=open('output.html','w')
        File.write(data)
        File.close()

    else:
        Average_Marks=sum(course_marks)/len(course_marks)
        Max_Marks=max(course_marks)    

        Course_data 
        '''
        <h1>Course Details</h1>
        <table border='2>
            <tr>
                <th> Average Marks</th>
                <th>Maximum Marks</th>
            </tr>
            <tr>
                <td> {{Average_Marks}} </td>
                <td> {{Max_Marks}} </td>
            </tr>
        </table>
        <img src ="hist.png">'''

        temp=Template(Course_data)
        output=temp.render(Average_Marks=Average_Marks,Max_Marks=Max_Marks)

        x=course_marks
        plt.hist(x)
        plt.savefig('hist.png')

        File=open('output.html','w')
        File.write(output)
        File.close()

             
 

