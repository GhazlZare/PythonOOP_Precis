class Students:
    def __init__(self, name, age, grades=[]):
        self.name = name
        self.age = age
        self.grades = grades

    def add_grade(self, new_grade):
        if isinstance(new_grade, (float, int)):
            self.grades.append(new_grade)
            print(f"Grade: {new_grade} added")
        else:
            raise ValueError("Grade type must be float")

    def avg_grades(self):
        if self.grades:
            len_grade = len(self.grades)
            sum = 0
            for grade in self.grades:
                sum += grade
            avg = sum / len_grade
            return avg

    def display_details(self):
        return(f"Student Name: {self.name}, Student Age: {self.age}, Student Grades: {self.grades}")

def main():
    st1 = Students("Ghazal", 15, [12, 14.75, 18])
    st1.add_grade(19)
    st1.display_details()

if __name__ == "__main__":
    main()
