class GradedActivity:
    def __init__(self, score):
        self.__score = score

    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        elif self.__score >= 70:
            return 'C'
        elif self.__score >= 60:
            return 'D'
        else:
            return 'F'
            
    def __str__(self):
        return 'Score: ' + str(self.__score) + ', Grade: ' + self.get_grade()

class PassFailActivity(GradedActivity):
    def __init__(self, score, min_passing_score):
        super().__init__(score)
        self.__min_passing_score = min_passing_score

    def get_grade(self):
        if self.get_score() >= self.__min_passing_score:
            return super().get_grade() + ' Pass'
        else:
            return super().get_grade()+' Fail'

class PassFailExam(PassFailActivity):
    def __init__(self, score, min_passing_score, num_questions, num_missed):
        super().__init__(score, min_passing_score)
        self.__num_questions = num_questions
        self.__num_missed = num_missed
        self.__points_each = 100.0 / self.__num_questions
        numeric_score = 100.0 - (num_missed * self.__points_each)
        self.set_score(numeric_score)
    def getPtsEach(self):
        return self.__points_each
    def getNumMissed(self):
        return self.__num_missed
    
    def equals(self,GradedActivity):
        if self.get_score() == GradedActivity.get_score():
            return True
        else:
            return False
    
    def greater(self, GradedActivity):
        if self.get_score() > GradedActivity.get_score():
            return (True, self.get_score())
        else:
            return (False, GradedActivity.get_score())

class Essay(GradedActivity):
    def __init__(self, score, grammar, spelling, length, content):
        super().__init__(score)
        self.__grammar = grammar
        self.__spelling = spelling
        self.__length = length
        self.__content = content

    def getTotal(self):
        return self.__grammar + self.__spelling + self.__length + self.__content

    def get_grade(self):
        return super().get_grade()


class CourseGrades(GradedActivity):
    def __init__(self):
        self.__grades = [GradedActivity] * 3
    
    def setLab(self, GradedActivity):
        self.__grades[0] = GradedActivity
    
    def setPassFailExam(self, PassFailExam):
        self.__grades[1] = PassFailExam
    
    def setEssay(self, Essay):
        self.__grades[2] = Essay
    
    def __str__(self):
        return 'Lab: ' + str(self.__grades[0]) + '\nPass/Fail Exam: ' + str(self.__grades[1]) + '\nEssay: ' + str(self.__grades[2])
        

def main():
    exam1 = PassFailExam(70, 60, 10, 3)
    exam2 = PassFailExam(60, 60, 10, 3)

    print(exam1.greater(exam2))

    grades = CourseGrades()

    grades.setLab(GradedActivity(90))
    grades.setPassFailExam(exam1)
    grades.setEssay(Essay(80, 20, 20, 20, 20))

    print(grades)

main()