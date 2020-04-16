

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,49.9, 45, 44.9, 40, 39.9, 2, 0]

    
def exam_grades(mark):
    if mark >= 75:
        print (str(mark)+" - first")
    elif mark >= 70 and mark < 75:
        print (str(mark)+" - Upper Second")
    elif mark >= 60 and mark < 70:
        print (str(mark)+" - Second")
    elif mark >= 50 and mark < 60:
        print (str(mark)+" - Third")
    elif mark >= 45 and mark < 50:
        print (str(mark)+" - F1 Supp")
    elif mark >= 40 and mark < 45:
        print (str(mark)+" - F2")
    elif mark < 40:
        print (str(mark)+" - F3")
    else:
        print ("ERROR")



for i in xs:
    print(str(exam_grades(i)))
