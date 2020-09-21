print("""
----------------------------------------------------------
|                                                        |
| Student Information and Exams Information and Average  |
|                                                        |
----------------------------------------------------------
""")

print("""
----------------------------------------------------------
|            Student Information Login Panel             |
----------------------------------------------------------
""")
name=input("Please Enter Student Name: ")
surname=input("Please Enter Student Surname: ")
idnumber=int(input("Please Enter Student ID Number: "))
print("""
----------------------------------------------------------
|         Student Exams Information Login Panel          |
----------------------------------------------------------
""")
exam1=float(input("Please Enter First Exam Point:"))
exam2=float(input("Please Enter Second Exam Point:"))
exam3=float(input("Please Enter Third Exam Point:"))
average=(exam1+exam2+exam3)/3
result = "Point: {}/{}"
try:
    if average >=0 and average<30:
        result=result.format(average,"FF")
    elif average >=30 and average<40:
        result=result.format(average,"DD")
    elif average >=40 and average<70:
        result=result.format(average,"CC")
    elif average >=70 and average<85:
        result=result.format(average,"BB")
    elif average >=85 and average<100:
        result=result.format(average,"AA")
    else:
        pass
except ValueError as error:
    print("Incorrect Data Entry")

print(f"""
----------------------------------------------------------
|                 Student İnformations                   |
----------------------------------------------------------
  Student Name   : {name}                                
  Student Surname: {surname}                             
  Studen Id      : {idnumber}                            
----------------------------------------------------------
|            Exams İnformation  and Average              |
----------------------------------------------------------
  First Exam Point : {exam1}                                
  Second Exam Point: {exam2}                                
  Third Exam Point : {exam3}                                
  Average          : {result}                   
----------------------------------------------------------
""")


        

