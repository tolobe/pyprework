
#Question 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(Tomas):
name = input('What is your name?\n')
print ('hello_name')
                
#Question 2 Print first 100 odd numbers in Python. def one_to_hundred():
def one_to_hundred:
    x=1
        for x in range(1,100, 2):
        print(x)

        one_to_hundred()

#Question 3 Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.


    def bubble_sort(a_list):
        for i in range(len(a_list) - 1):
            for j in range(len(a_list) - i - 1):
                if a _list[j] > a_list[j+1]:
                    a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
        return a_list[-1]
                
#Question 4 Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def get_leap_years():
    currentIteration = 1
    year = 2000

    while year < 3001:
        if year%4==0 and year%100!=0 or year%400==0:
            print(f"{currentIteration}: {year}")
            currentIteration += 1
        year += 1

get_leap_years()

                
#Question 5 Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    for i in range(len(a_list) - 1):
        if a_list[i] + 1 != a_list[i+1]:
            return False
    return True
 