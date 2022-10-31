'''
Dynamic leave application --> Name,class,section,school,classteacher name,date,subject,date of leave,reason

'''
date=str(input("enter the date: "))
place=str(input("enter the place: "))
student_name=str(input("enter the name of the student: "))
class_name=str(input("enter the class: "))
section=str(input("enter the section: "))
school_name=str(input("enter the school name: "))
classteacher_name=str(input("enter the classteacher name: "))
subject=str(input("enter the subject: "))
date_of_leave=(input("enter the date of leave: "))
reason=(input("enter your reason: "))
permission_letter=f'''


from
        {student_name},
        {class_name},
        {section},
        {place}.

 to

        {classteacher_name},   
        {class_name},
        {section},
        {school_name},
        {place}.

Respected Sir/madam,
    sub:
                   i am {name}. Studying in {class_name} section {section}. Am not able to attend the class tommorow due to {reason}.
I request to grant me a leave on {date_of_leave}. I will come back to the class from very next day.
                   i hoping for you to give me the permission for this leave.

                                                                             thanking you sir.

                                                                                               your's faithfully
                                                                                               {student_name}.

'''
print(permission_letter)