class Parent():
    def __init__(self, eye_color, blood_group):
        print("Parent constructor called")
        self.eye_color = eye_color
        self.blood_group = blood_group

class Child(Parent):
    def __init__(self,eye_color,blood_group,last_name):
        print("Child constructor called")
        Parent.__init__(self,eye_color,blood_group)
        self.last_name = last_name

#arti_bala = Parent("black","O+")

srishti_sinha = Child("black","O+","Sinha")

print(srishti_sinha.eye_color)
print(srishti_sinha.last_name)
