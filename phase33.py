class Event:
    def __init__(self, title, date, capacity):
        self.__title = title
        self.__date = date
        self.set_capacity(capacity)

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
        if capacity <= 0:
           raise ValueError("Capacity must be greater than 0")
        self.__capacity = capacity

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
            return "Event registered successfully"
        else:
            return "You cannot register in more than 3 events."

    def remove_event(self, event_title):
        if event_title in self.__registered_events:
            self.__registered_events.remove(event_title)
            return True
        else:
            return False

    def __str__(self):
        return f"{self.__name} ({self.__student_id} {self.__registered_events})"


class ClubManager(Student):
    def register_event(self, event_title):
        if event_title in self.get_registered_events():
            return "Event already registered"
        elif len(self.get_registered_events()) < 6:
            self.get_registered_events().append(event_title)
            return "Event registered successfully"
        else:
            return "You cannot register in more than 6 events."

    def __str__(self):
        return f"Club manager {self.get_name()} {self.get_student_id()}"


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

    def register_student_for_event(self, student_id, event_title):#*************88
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
                print(f'{student.get_name()} successfully registered event {event_title}-{event.get_date()}')
                self.__log.append(f"{student.get_name()} registered in {event_title}")
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
            print(f'{student.get_name()} is cancelled in {event_title}')
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

    def saved_data(self):
        print("saving data .....")
        with open("club_data.txt", "w") as file:
            for event in self.__events:
                file.write("event," + event.get_title() + "," + event.get_date() + "," + str(event.get_capacity()) + "\n")

            for student in self.__students:
                category = "manager" if isinstance(student, ClubManager) else "regular"
                l = "student," + student.get_name() + "," + student.get_student_id() + "," + category

                for event in student.get_registered_events():
                    l += "," + event

                file.write(l + "\n")

            for log in self.__log:
                file.write("log" +log + "\n")

        print("data saved successfully")

    def load_data(self):
        print("Loading saved data...")
        try:
            file = open("club_data.txt", "r")

            for line in file:
                data = line.strip().split(",")

                if data[0] == "event":
                    self.add_event(Event(data[1], data[2], int(data[3])))

                elif data[0] == "student":
                    if data[3] == "manager":
                        student = ClubManager(data[1], data[2])
                    else:
                        student = Student(data[1], data[2])

                    self.enroll_student(student)

                    for i in range(4, len(data)):
                        student.get_registered_events().append(data[i])

                elif data[0] == "log":
                    self.__log.append(data[1])

            file.close()
            print("Data loaded successfully.")

        except FileNotFoundError:
            print("No saved data found")

    def view_log(self):
        print("Transaction History")
        if not self.__log:
            print("no transaction history")
        else:
            i = 1
            for log in self.__log:
                print(f'{i}. {log}')
                i += 1

    def view_student_activity(self, student_id):
        student = self.search_student(student_id)

        if not student:
            print("Student not found")
            return

        category = "manager" if isinstance(student, ClubManager) else "regular"

        print(f"{student.get_name()}, {category}, {student_id}")
        print("registered events:")

        events = student.get_registered_events()

        if not events:
            print("No events")
        else:
            i = 1
            for e in events:
                print(e)
                i += 1

        if isinstance(student, ClubManager):
            print("(Can register for up to 6 events)")


def input_number(numbers):
    while True:
        try:
            return int(input(numbers))
        except ValueError:
            print("Please enter a number.")


def input_text(message):
    while True:
        try:
            text = input(message).strip()
            if text == "":
                raise ValueError("Input cannot be empty")
            return text
        except ValueError as e:
            print("input cannot be empty",e)

club = Club("AI Club")
club.load_data()

print("=" * 30)
print("Campus student club system")
print("=" * 30)
print("Club: ", club.get_club_name())

while True:
    print("1. Add Event")
    print("2. Enroll Student")
    print("3. Register Student for Event")
    print("4. Cancel Registration")
    print("5. view all events")
    print("6. view student activity")
    print("7. view transaction history")
    print("8. Exit")

    choice = input_number("Enter choice: ")

    if choice < 1 or choice > 8:
        print("Invalid choice,you have to chose between 1 and 8")
        continue

    if choice == 1:
        title = input("Enter event title: ")
        date = input("Enter event date (YYYY-MM-DD): ")

        while True:
            try:
                capacity = int(input("Enter event capacity: "))#***********
                if capacity <= 0:
                    raise ValueError("Invalid capacity,must be greater than0")
                event = Event(title, date, capacity)
                club.add_event(event)
                print(f"event{title} added  successfully")
                break
            except ValueError as e:
                print(e)

    elif choice == 2:
        name = input("Enter student name: ")
        student_id = input_text("Enter student ID: ")
        category = input_number("Enter event category: 1 for manager ,2 for regular student ")

        if category == 1:
            student = ClubManager(name, student_id)
        else:
            student = Student(name, student_id)

        club.enroll_student(student)
        print(f"student {student} is registered successfully.")

    elif choice == 3:
        student_id = input_text("Enter student ID: ")
        title = input("Enter event title: ")
        club.register_student_for_event(student_id, title)

    elif choice == 4:
        student_id = input_text("Enter student ID: ")
        title = input("Enter event title: ")
        club.cancel_registration_for_student(student_id, title)

    elif choice == 5:
        print("---All Events----")
        club.view_all_events()

    elif choice == 6:
        student_id = input_text("Enter student ID: ")
        club.view_student_activity(student_id)

    elif choice == 7:
        club.view_log()

    elif choice == 8:
        club.saved_data()
        print("Goodbye!")
        break