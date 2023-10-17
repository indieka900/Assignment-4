
# collecting marks from user
chemistry = int(input("Enter the chemistry marks: "))
maths = int(input("Enter the maths marks: "))
physics = int(input("Enter the physics marks: "))
geography = int(input("Enter the geography marks: "))

#function for grading
def grade(average):
    if (average < 31):
        print(f"Your Grade D : {average}")
    elif (average >=  31 and average < 51):
        print(f"Your Grade is C : {average}")
    elif (average >=  51 and average < 71):
        print(f"Your Grade is B : {average}")
    else:
        print(f"Your Grade is A : {average}")
        
    #grade(50.19) should be graded as C
        
# validating the marks before grading (0-100)
if(chemistry >= 0 and chemistry <=100):
    if(maths >= 0 and maths <=100):
        if(physics >= 0 and physics <=100):
            if(geography >= 0 and geography <=100):
                average = (chemistry+maths+physics+geography)/4
                grade(average)
            else:
                print(f"unrecognized/Invalid geography marks {geography}")
        else:
            print(f"unrecognized/Invalid physics marks {physics}")
    else:
        print(f"unrecognized/Invalid maths marks {maths}")
else:
    print(f"unrecognized/Invalid chemistry marks {chemistry}")
