from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10
import logging
logging.getLogger('sqlalchemy.engine').setLevel(logging.ERROR)


if __name__ == "__main__":
    print(1,'_'* 180)
    select_1()
    print(2,'_'* 180)
    select_2(subject_name='Math')
    print(3,'_'* 180)
    select_3('Chemistry')
    print(4,'_'* 180)
    select_4('Biology')
    print(5,'_'* 180)
    select_5('Амалія Стельмах')
    print(6,'_'* 180)
    select_6('GroupB')
    print(7,'_'* 180)
    select_7('GroupB', 'Math')
    print(8,'_'* 180)
    select_8(teacher_name='Мілена Ейбоженко')
    print(9,'_'* 180)
    select_9(student_name='Богуслав Романенко')
    print(10,'_'* 180)
    select_10(student_name='Богуслав Романенко', teacher_name='Амалія Стельмах')