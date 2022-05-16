def second_highest(students):

    grades = [stu[1] for stu in students]
    grades = sorted(set(grades))
    second = grades[-2]
    sec_students = [gra[0] for gra in students if gra[1] == second]
    for stu in sec_students:
        print(stu) 

students =[["jerry",88],["jerry",88],["jerry",88],["jerk",85],["smith",87],["jimmy",38],["poll",66],["ilea",87],["ken",44],["bull",22],["ilea",87],["ilea",87]]
second_highest(students)