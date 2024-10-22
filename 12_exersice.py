# Multiple Inheritance
# Real Life Example :
#
# Create multiple inheritance on teacher,student and youtuber.
# Q. if we have created teacher and now one student joins master degree with becoming teacher then what??
#
# Ans :  just make subclass from  teacher so that student will become teacher
# Now student is teacher as well as youtuber then what???
# -just use multiple inheritance for these three relations

class teacher:
    def teacher_action(self):
        print('i can teach')

class student:
    def student_action(self):
        print('i can code')

class youtuber:
    def youtuber_action(self):
        print('i can code and teach')

class person(teacher,student,youtuber):
    pass

coder =person()
coder.teacher_action()
coder.student_action()
coder.youtuber_action()