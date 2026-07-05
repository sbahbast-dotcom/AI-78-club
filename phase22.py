class Event:
    def __init__(self, title, date, capacity):
        self.__title = title
        self.__date = date
        self.__capacity = capacity

    def set_title(self, title):
        self.__title = title
    def get_title(self):
        return self.__title

    def set_date(self, date):
        self.__date = date
    def get_date(self):
        return self.__date

    def get_capacity(self):
        return self.__capacity
    def set_capacity(self, capacity):
        if capacity > 0:
            self.__capacity = capacity
            return True
        else:
            return False

    def increase_capacity(self):
        self.__capacity += 1
    def decrease_capacity(self):
        self.__capacity -= 1

    def __str__(self):
            return f"Event: {self.__title} | Date: {self.__date} | Available Seats: {self.__capacity}"

class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__registered_events = []

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_student_id(self, student_id):
        self.__student_id = student_id
    def get_student_id(self):
        return self.__student_id

    def set_registered_events(self, registered_events):
        self.__registered_events = registered_events
    def get_registered_events(self):
        return self.__registered_events

    def register_event(self, event_title):
        if event_title in self.__registered_events:
            return "Event already registered"
        elif len(self.__registered_events) < 3:
            self.__registered_events.append(event_title)
        else:
            return "You cannot register in more than 3 events."

    def remove_event(self, event_title):
        if event_title in self.__registered_events:
            self.__registered_events.remove(event_title)
            return True
        else:
            return False

    def __str__(self):
        return f"{self.__name} ({self.__student_id})"

class Club:
    def __init__(self, club_name):
        self.__club_name = club_name
        self.__events = []
        self.__students = []
        self.__log = []

    def get_club_name(self):
        return self.__club_name
    def set_club_name(self, name):
        self.__club_name = name

    def get_events(self):
        return self.__events

    def add_event(self, event):
        self.__events.append(event)

    def enroll_student(self, student):
        self.__students.append(student)

    def search_event(self, event_title):
        for event in self.__events:
            if event.get_title() == event_title:
                return event
        return None

    def search_student(self, student_id):
        for student in self.__students:
            if student.get_student_id() == student_id:
                return student
        return None

    def register_student_for_event(self, student_id, event_title):
        event = self.search_event(event_title)
        student = self.search_student(student_id)

        if not student:
            print("Student not found")
            return
        if not event:
            print("Event not found")
            return

        answer = student.register_event(event_title)

        if answer == "Event already registered":
            print(f"Event already registered in {event_title}")
        elif answer == "You cannot register in more than 3 events.":
            print("You cannot register in more than 3 events.")
        else:
            if event.get_capacity() > 0:
                event.decrease_capacity()
                print(f'{student.get_name()}  successfully registered event {event_title}')
                self.__log.append(student.get_name())
            else:
                print("Event is full")

    def cancel_registration_for_student(self, student_id, event_title):
        event = self.search_event(event_title)
        student = self.search_student(student_id)

        if not student:
            print("Student not found")
            return
        if not event:
            print("Event not found")
            return

        if student.remove_event(event_title):
            event.increase_capacity()
            print(f'{student.get_name()}  is cancelled in {event_title}')
            self.__log.append(f'{student.get_name()} is cancelled in {event_title}')
        else:
            print('student is not registered')
            return

    def view_student_events(self, student_id):
        student = self.search_student(student_id)
        if not student:
            print("Student not found")
            return

        print(f'student {student.get_name()} is registered events are:')
        events = student.get_registered_events()
        if not events:
            print("No events registered")
            return
        else:
            i = 1
            for event in events:
                print(f'{i}. {event}')
                i += 1
    def view_all_events(self):
        if not self.__events:
            print("No events available")
        else:
            for i in self.__events:
                print(i)

club = Club("AI Club")

print("=" * 30)
print("Campus Student Club System")
print("=" * 30)
print("Club:  ", club.get_club_name())

while True:
    print("1. Add Event")
    print("2. Enroll Student")
    print("3. Register Student for Event")
    print("4. Cancel Registration")
    print("5. View Student's Registered Events")
    print("6. View All Events")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter event title: ")
        date = input("Enter event date (YYYY-MM-DD): ")

        while True:
            capacity = int(input("Enter event capacity: "))
            if capacity > 0:
                event = Event(title, date, capacity)
                club.add_event(event)
                print(f'Event "{title}" added successfully.')
                break
            else:
                print("Capacity must be > 0")

    elif choice == "2":
        name = input("Enter student name:")
        student_id = input("Enter student ID:")
        student = Student(name, student_id)
        club.enroll_student(student)
        print(f"Student {name} ({student_id}) enrolled successfully.")

    elif choice == "3":
        student_id = input("Enter student ID: ")
        title = input("Enter event title: ")
        club.register_student_for_event(student_id, title)

    elif choice == "4":
        student_id= input("Enter student ID:")
        title = input("Enter event title: ")
        club.cancel_registration_for_student(student_id, title)
    elif choice == "5":
        student_id = input("Enter student ID:")
        club.view_student_events(student_id)

    elif choice == "6":
        print("---All Events----")
        for e in club.get_events():
            print(str(e))  # how can we format like the output

    elif choice == "7":
        print("Goodbye!")
        break