import unittest

class TestLab3(unittest.TestCase):

    # Task 1: Working with Strings
    def test_string_slicing(self):
        # The student will provide their own favorite food string
        student_code = "Pizza"  # Example input; change as necessary to test

        # Student should manipulate `food` string
        food = student_code  # We are using their input value
        
        # Test: First 3 characters of string
        self.assertEqual(food[:3], food[0:3])  # First 3 characters
        
        # Test: Last 3 characters of string
        self.assertEqual(food[-3:], food[len(food)-3:])  # Last 3 characters
        
        # Test: Concatenation of first and last characters
        self.assertEqual(food[0] + food[-1], food[0] + food[-1])  # First + Last characters

    def test_split_and_join(self):
        food = "Pizza is delicious"
        split_list = food.split()
        self.assertEqual(split_list, ['Pizza', 'is', 'delicious'])  # Test split method
        self.assertEqual(' '.join(split_list), food)  # Test join method

    def test_list_operations(self):
        number_list = [1, 2, 3, 4, 5]
        number_list.append(6)
        self.assertEqual(number_list, [1, 2, 3, 4, 5, 6])  # Test append
        number_list.insert(2, 10)
        self.assertEqual(number_list, [1, 2, 10, 3, 4, 5, 6])  # Test insert
        number_list.pop()
        self.assertEqual(number_list, [1, 2, 10, 3, 4, 5])  # Test pop
        number_list.remove(2)
        self.assertEqual(number_list, [1, 10, 3, 4, 5])  # Test remove
        self.assertEqual(number_list[:3], [1, 10, 3])  # Test slicing (first 3 elements)
        self.assertEqual(number_list[-3:], [3, 4, 5])  # Test slicing (last 3 elements)

    def test_dictionary_operations(self):
        books = {
            'Dr. Seuss': 'Cat in the Hat',
            'JK Rowling': 'Harry Potter',
            'George Orwell': '1984',
            'J.R.R. Tolkien': 'The Hobbit'
        }
        self.assertEqual(list(books.keys()), ['Dr. Seuss', 'JK Rowling', 'George Orwell', 'J.R.R. Tolkien'])
        self.assertEqual(list(books.values()), ['Cat in the Hat', 'Harry Potter', '1984', 'The Hobbit'])
        self.assertEqual(books.get('JK Rowling'), 'Harry Potter')  # Test get method
        books.pop('George Orwell')  # Remove a key-value pair
        self.assertNotIn('George Orwell', books)  # Ensure it's removed
        del books['Dr. Seuss']  # Remove another key-value pair
        self.assertNotIn('Dr. Seuss', books)  # Ensure it's removed


if __name__ == '__main__':
    unittest.main()
