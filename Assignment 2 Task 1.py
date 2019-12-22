data_structure = int(input("Enter Data Structure Marks :- "))
c = int(input("Enter C Language Marks :- "))
java = int(input("Enter Java Marks :- "))
python = int(input("Enter Python Marks :- "))
algorithm = int(input("Enter Algorithm Marks :- "))

total = data_structure + c + java + python + algorithm
average = data_structure + c + java + python + algorithm/5
if(average >= 80 and average <=100):
    grade = "A Grade"

if(average >= 60 and average < 80):
    grade = "B Grade"

if(average >= 50 and average < 60):
    grade = "C Grade"

if(average >= 40 and average < 50):
    grade = "D Grade"

else:
    grade = "Fail"
    
print("======================================="
      "  ||   SUBJECTS    ||     MARKS   ||  "
      "    DATA STRUCTURE       ",data_structure,
      "      C LANGUAGE         ",c,
      "         JAVA            ",java,
      "        PYTHON           ",python,
      "      ALGORITHM          ",algorithm,
      "========================================"
      "TOTAL MARKS              ",total,
      "GRADE                    ",grade)

