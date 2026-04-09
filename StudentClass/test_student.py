from student import Student
import unittest

class TestStudent(unittest.TestCase):
    #test that average is correct
    def test_get_average(self):
        student = Student("James", [88, 90, 57, 80,95])
        self.assertEqual(student.get_average(),82)

    def test_highest(self):
        student = Student("James", [88, 90, 57, 80,95])
        #test that the highest score is correct
        self.assertEqual(student.get_highest(), 95)
        #test that number is in the list
        self.assertIn(57,student.grades)

    def test_add_grade(self):
        student = Student("James", [88, 90, 57, 80,95])
        student.add_grade(100)
        #test that the number is added
        self.assertIn(100, student.grades)

    def test_single_grade(self):
        student = Student("James",[90])
        self.assertEqual(student.get_average(), 90)

    def test_empty_list(self):
        student = Student("James", [])
        self.assertIsNone(student.get_average(), None)

    def test_multiple_add_grades(self):
        student = Student("James", [])
        student.add_grade(100)
        student.add_grade(95)
        self.assertEqual([100,95], student.grades)

if __name__ == '__main__':
    unittest.main()