class Student(object):

    def __init__ (self,name,marks,application_successful):
        self.name = name
        self. = marks
        self.application_successful = application_successful
    def Interview(self,marks,application_successful):

        if application_successful == "Yes" and marks>= 85:
            return "You are Invited for Interview"
        else:
            return "Application not Successful"
    def Online_exams(self,Interview_score):
        if Interview_score >= 85:
            return "Congratulations! You made it to campus"
        else:
            return "Please apply again"
    def Fellowship(self,Online_exams):
        if Online_exams >= 90:
            return "Welcome"
        else:
            "Try again next time"
