class Event:
    def __init__(self,title,date,capacity):#كيف ال date string ولما ادخله بكون عدد وايش علامة worning اللي ظاهرتلي
        self.__title = title
        self.__date = date
        self.__capacity = capacity
    def get_title(self):
        return self.__title
    def get_date(self):
        return self.__date
    def get_capacity(self):
        return self.__capacity
    def set_capacity(self,capacity): # for all parameters set ?
        if capacity >0 :
            self.__capacity = capacity
            return True
        else:
            return False
    def reduce_capacity(self):
        if self.__capacity <=0:
            raise ValueError("Capacity can't be less than 0")
        else:
            self.__capacity = self.__capacity - 1
    def increase_capacity(self):
        self.__capacity += 1
    def setname(self,name):
        self.__name = name
    def setdate(self,date):
        self.__date = date
    def __str__(self):
        return "title:"+self.__title+"\n date:"+self.__date+"\ncapacity:"+str(self.__capacity)


class Student:
    def __init__(self,name,student_id):
        self.__name = name
        self.__student_id = student_id
        self.__registered_events = []
    def get_name(self):
        return self.__name
    def get_student_id(self):
        return self.__student_id
    def get_registered_events(self):
        return self.__registered_events
    def set_name(self,name):
        self.__name = name    #the same point
    def set_student_id(self,student_id):
        self.__student_id = student_id

    def registered_events(self, event_titles):
            if len(self.__registered_events) <=3:#==or not     #*******لازم نحط جيت سيت
                self.__registered_events.append(event_titles)
            else:
                print("Cannot register more than 3 events")
    def remove_registered_events(self,event_titles):
        if event_titles in self.__registered_events:
            self.__registered_events.remove(event_titles)

    def __str__(self):
        return " name:"+self.__name+"\n student_id:"+self.__student_id+"\n registered_events:"+str(self.__registered_events)
class  Club:
    def __init__(self,club_name):
        self.__club_name = club_name
        self.__events = []
        self.__students = []
    def getClubName(self):
        return self.__club_name
    def setClubName(self,club_name):#use getters setters for list
        self.__club_name = club_name
    def addEvent(self,event):
        self.__events.append(event)
    def enrollStudent(self,student):
        self.__students.append(student)
#the main code is right?
club=Club("AI club")
print("="*30)
print("campus student club system")
print("="*30)
print( "Club : ",  club.getClubName())
while True:
    print("1.  Add event")
    print("2.  Enroll student")
    print("3. Register student for Event")
    print("4. Cancel Registration")
    print("5. View student Registered Events")
    print("6. View all events")
    print("7.  Exit")
    choice = input("Enter  choice: ")
    if choice == "1":
        title=input("Enter  event title: ")
        date=input("Enter date(YYYY-MM-DD): ")
        while True:
            capacity=int(input("Enter event capacity: "))
            event=Event(title,date,capacity)
            if capacity >0 :
                club.addEvent(event)
                print("Event "+event.get_title()+" added successfully")
                break
            else:
                print("Error: capacity must be greater than 0")


    elif choice == "2":
        name=input("Enter student name: ")
        student_id=int(input("Enter student id: "))    # oytput same as simple but we dont know if it wiil affect phase 2 because in all case it will be added to list
        student=Student(name,student_id)
        club.enrollStudent(student)
        print("student "+student.get_name()+" enrolled successfully")
        print()
    elif choice == "3":
        student_id=int(input("Enter student id: "))
        event_title=input("Enter student name: ")
        club.
        print("student "+name+" enrolled successfully")
    elif  choice == "7":
        print("Good bye!")
        break




