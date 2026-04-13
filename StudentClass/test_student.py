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
        #test that the number is in the list
        self.assertIn(100, student.grades)

    def test_multiple_add_grades(self):
        student = Student("James", [])
        student.add_grade(90)
        student.add_grade(65)
        student.add_grade(90)
        self.assertEqual([90,65,90], student.grades)
        self.assertEqual(len(student.grades),3)

    def test_highest_with_duplicates(self):
        student = Student("James", [90,65,90])
        self.assertEqual(student.get_highest(), 90)

#edge cases
    def test_single_grade(self):
        student = Student("James",[90])
        self.assertEqual(student.get_average(), 90)

    def test_empty_list(self):
        student = Student("James", [])
        self.assertIsNone(student.get_average(), None)

    def test_zero_grade(self):
        student = Student("James",[0])
        self.assertEqual(student.get_average(),0)

#negative tests
    def test_invalid_grade(self):
        student = Student("James", [89,90,55])
        with self.assertRaises(TypeError):
            student.add_grade("A")

    def test_negative_grade(self):
        student = Student("James", [89, 90, 55])
        with self.assertRaises(TypeError):
            student.add_grade(-5)


if __name__ == '__main__':
    unittest.main()