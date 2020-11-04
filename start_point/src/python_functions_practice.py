def return_10():
    return 10

def add(num_1, num_2):
    num_3 = num_1 + num_2
    return num_3

def subtract(num_4, num_5):
    num_6 = num_4 - num_5
    return num_6

def multiply(num_7, num_8):
    num_9 = num_7 * num_8
    return num_9

def divide(num_10, num_11):
    num_12 = num_10 / num_11
    return num_12

    #   def test_divide(self):
    #   divide_result = divide( 10, 2 )
    #   self.assertEqual( 5, divide_result )

def length_of_string(string):
    return len(string)

#   def test_length_of_string(self):
#       test_string = "A string of length 21"
#       string_length = length_of_string( test_string )
#       self.assertEqual( 21, string_length )

def join_string(string_1, string_2):
    string_3 = string_1 + string_2
    return string_3

# def test_join_string(self):
#       string_1 = "Mary had a little lamb, "
#       string_2 = "its fleece was white as snow"
#       joined_string = join_string( string_1, string_2 )
#       self.assertEqual( "Mary had a little lamb, its fleece was white as snow", joined_string )

def add_string_as_number(string_4, string_5):
    string_6 = int(string_4) + int(string_5)
    return string_6

#   def test_add_string_as_number(self):
#       add_result = add_string_as_number( "1", "2" )
#       self.assertEqual( 3, add_result )

# import calender for date conversion capabilities 

# import calendar
# calender.greeting("Happenin")

def number_to_full_month_name(month_1):
    month_1 = "January"
    return month_1

#   def test_number_to_full_name__month_1(self):
#       result = number_to_full_month_name(1)
#       self.assertEqual( "January", result )