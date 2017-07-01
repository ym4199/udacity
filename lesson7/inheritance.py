class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Counstructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name,eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - " + self.eye_color)
        print("Number of toys - " + str(self.number_of_toys))

billy_cyrus = Parent("Cyrus", "blue")
milly_cyrus = Child("cyrus", "BLUE", "5")
# billy_cyrus.show_info()
# Parent("robert","brown").show_info()
milly_cyrus.show_info()