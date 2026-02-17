import pandas as pd
import numpy as np

def ip_as_list():

    student_data = []

    name = input("Enter Student's Name: ")
    student_data.append(name)

    classs = input("Enter Student's Class: ")
    student_data.append(classs)
    
    subj_count = int(input("How many subjects ? "))
    for i in range(subj_count):
        mark = int(input(f"Enter mark for Subject {i+1}: "))
        student_data.append(mark)
    result = input("Enter Student's Result: ")
    student_data.append(result)

    index_labels = ["Name", "Class"]
    for i in range(subj_count):
        index_labels.append(f"Subject{i+1}")
    index_labels.append("Result")

    student_series = pd.Series(student_data, index=index_labels)
    print(student_series)



def ip_as_dictionary():

    student_data = {}

    name = input("Enter Student's Name: ")
    student_data["Name"] = name

    classs = input("Enter Student's Class: ")
    student_data["Class"] = classs

    subj_count = int(input("How many subjects ? "))
    for i in range(subj_count):
        mark = int(input(f"Enter mark for Subject {i+1}: "))
        student_data[f"Subject {i+1}"] = mark

    result = input("Enter Student's Result: ")
    student_data["Result"] = result

    print(student_data)

    student_series = pd.Series(student_data)
    print(student_series)



def ip_as_numpyarray():

    # numpyarrays go with only one datatype and typically int.
    # so taking ip as list and converting the end list to numpyarray makes even the integer datatypes to be as strings.
    # thus, losing the numeric features of numpyarrays

    name = input("Enter Student's Name: ")
    classs = input("Enter Student's Class: ")

    subj_count = int(input("How many subjects ? "))
    marks = []
    for i in range(subj_count):
        mark = int(input(f"Enter mark for Subject {i+1}: "))
        marks.append(mark)
    marks_array = np.array(marks)
    
    result = input("Enter Student's Result: ")

    data = [name, classs]
    data.extend(marks_array)
    data.append(result)

    index_labels = ["Name", "Class"]
    for i in range(subj_count):
        index_labels.append(f"Subject{i+1}")
    index_labels.append("Result")

    student_series = pd.Series(data, index=index_labels)
    print(student_series)



def dataframe_for_whole_class_and_statistics():
    
    students = []

    count = int(input("How many students ? "))
    for i in range(count):

        print(f"Enter data for Student {i + 1}")

        student = {}

        student["Name"] = input("Enter student's name: ") 
        student["Class"] = input("Enter student's class: ") 

        subject_count = int(input("How many subjects ? "))
        for i in range(subject_count):
            mark = int(input(f"Enter mark for subject {i+1}: "))
            student[f"Subject {i+1}"] = mark

        student["Result"] = input("Enter student's result: ") 
        students.append(student)


    students_dataframe = pd.DataFrame(students)
    print(students_dataframe)



    # Statistics


    subject_columns = [col for col in students_dataframe.columns if "Subject" in col]

    highest_score = students_dataframe[subject_columns].max()
    average_marks = students_dataframe[subject_columns].mean()
    percentile = students_dataframe[subject_columns].quantile(0.9)

    print(f"Highest Scores in each Subject:\n {highest_score}")
    print()
    print(f"Average Marks for each Subject:\n {average_marks}")
    print()
    print(f"Percentile for each Subject:\n {percentile}")
    print()

    # axis = 1 means across columns row wise
    # axis = 0 means down the row in a column
    students_dataframe["Average"] = students_dataframe[subject_columns].mean(axis=1) 

    def assign_grades(avg):
        return round(avg/10)

    students_dataframe["Grade"] = students_dataframe["Average"].apply(assign_grades)

    print("\nFinal DataFrame with Grades:")
    print(students_dataframe)


ip_as_dictionary()