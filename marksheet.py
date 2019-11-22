name = input("Enter a Name")
print(name)
sub1 = int(input("Enter marks of English"))
sub2 = int(input("Enter marks of Physices"))
sub3 = int(input("Enter marks of Biology"))
sub4 = int(input("Enter marks of Chemistry"))
sub5 = int(input("Enter marks of Computer"))

total = (sub1+sub2+sub3+sub4+sub5)
print(total)

total = (sub1+sub2+sub3+sub4+sub5)/5
print(total)
if total>=80 :
     print("Grade A+")
elif total>=70 <=80 :
     print("Grade A")
elif total>=60 <=70 :
     print("Grade B")
elif total>=50 <=60 :
     print("Grade C")
else :
     print("You Are Fail")







