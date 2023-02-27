import unittest
from MyCalc import MyCalc


def test_mul():
    calc = MyCalc()
    assert calc.multiplication(2, 6) == 12


def test_number_mul_number():
    calc = MyCalc()
    data = [{
        "b1": "5",
        "b2": "5",
        "res": "25"
    },
        {
        "b1": "3",
        "b2": "4",
        "res": "12"
    },
        {
        "b1": "6",
        "b2": "6",
        "res": "36"
    },]
    for d in data:
        assert calc.multiplication(d["b1"], d["b2"]) == int(d["res"])
        #checks if the arguments b1 and b2 can perform multiplication function
        #It loops through a data list, calling the addition function for each argument item on the list.
        #b1 and b2 values are given as input values and the resut is stored in "res"



def test_ans_mul_number():
    calc = MyCalc()
    data = [{
        "b1": "10",
        "b2": "3",
        "res": "30"
    },
        {
        "b1": "ans",
        "b2": "5",
        "res": "150"
    },
        {
        "b1": "ans",
        "b2": "2",
        "res": "300"
    },]
    for d in data:
        assert calc.multiplication(d["b1"], d["b2"]) == int(d["res"])
        #checks if the arguments values b1 and b2 can perform multiplication function by taking the result as input for the next argument b1 value.
        #It loops through a data list, calling the addition function for each argument item on the list.
        #b1 and b2 values are given as input values and the resut is stored in "res" and the output of b1 amd b2 which is "res" is taken as input value for b1.
        #given the b2 value the operation is performed and result is again taken as one of the input for the set of operation.


def test_div():
    calc = MyCalc()
    assert calc.division(40, 2) == 20


def test_number_div_number():
    calc = MyCalc()
    data = [{
        "b1": "6",
        "b2": "3",
        "res": "2"
    },
        {
        "b1": "14",
        "b2": "7",
        "res": "2"
    },
        {
        "b1": "18",
        "b2": "6",
        "res": "3"
    },]
    for d in data:
        assert calc.division(d["b1"], d["b2"]) == float(d["res"])
        #checks if the arguments b1 and b2 can perform division function
        #It loops through a data list, calling the addition function for each argument item on the list.
        #b1 and b2 values are given as input values and the resut is stored in "res"


def test_ans_div_number():
    calc = MyCalc()
    data = [{
        "b1": "30",
        "b2": "5",
        "res": "6"
    },
        {
        "b1": "ans",
        "b2": "2",
        "res": "3"
    },
        {
        "b1": "ans",
        "b2": "3",
        "res": "1"
    },]
    for d in data:
        assert calc.division(d["b1"], d["b2"]) == float(d["res"])
         #checks if the arguments values b1 and b2 can perform multiplication function by taking the result as input for the next argument b1 value.
        #It loops through a data list, calling the addition function for each argument item on the list.
        #b1 and b2 values are given as input values and the resut is stored in "res" and the output of b1 amd b2 which is "res" is taken as input value for b1.
        #given the b2 value the operation is performed and result is again taken as one of the input for the set of operation.


def test_sub():
    calc = MyCalc()
    assert calc.subtraction(18, 2) == 16


def test_number_sub_number():
    calc = MyCalc()
   
    data = [{
        "b1": "5",
        "b2": "4",
        "res": "1"
    },
        {
        "b1": "12",
        "b2": "6",
        "res": "6"
    },
        {
        "b1": "2",
        "b2": "5",
        "res": "-3"
    },]
    for d in data:
        assert calc.subtraction(d["b1"], d["b2"]) == int(d["res"])
        #checks if the arguments b1 and b2 can perform subtraction function
        #It loops through a data list, calling the addition function for each argument item on the list.
        #b1 and b2 values are given as input values and the resut is stored in "res"

def test_ans_sub_number():
    calc = MyCalc()
    data = [{
        "b1": "5",
        "b2": "2",
        "res": "3"
    },
        {
        "b1": "ans",
        "b2": "5",
        "res": "-2"
    },
        {
        "b1": "ans",
        "b2": "2",
        "res": "0"
    },]
    for d in data:
        assert calc.subtraction(d["b1"], d["b2"]) == int(d["res"])
         #checks if the arguments values b1 and b2 can perform multiplication function by taking the result as input for the next argument b1 value.
        #It loops through a data list, calling the addition function for each argument item on the list.
        #b1 and b2 values are given as input values and the resut is stored in "res" and the output of b1 amd b2 which is "res" is taken as input value for b1.
        #given the b2 value the operation is performed and result is again taken as one of the input for the set of operation.

def test_add():
    calc = MyCalc()
    assert calc.addition(12, 2) == 14


def test_number_add_number():
    calc = MyCalc()

    data = [{
        "b1": "8",
        "b2": "2",
        "res": "10"
    },
        {
        "b1": "6",
        "b2": "3",
        "res": "9"
    },
        {
        "b1": "11",
        "b2": "1",
        "res": "12"
    },]
    for d in data:
        assert calc.addition(d["b1"], d["b2"]) == int(d["res"])
#checks to see if MyCalc(addition )'s function can add two numbers.
#It loops through a data list, calling the addition function for each argument item on the list.
#b1 and b2 values are given as input values and the resut is stored in "res"

def test_ans_add_number():
    calc = MyCalc()
    
    data = [{
        "b1": "14",
        "b2": "6",
        "res": "20"
    },
        {
        "b1": "ans",
        "b2": "5",
        "res": "25"
    },
        {
        "b1": "ans",
        "b2": "3",
        "res": "28"
    },]
    for d in data:
        assert calc.addition(d["b1"], d["b2"]) == int(d["res"])
         #checks if the arguments values b1 and b2 can perform multiplication function by taking the result as input for the next argument b1 value.
        #It loops through a data list, calling the addition function for each argument item on the list.
        #b1 and b2 values are given as input values and the resut is stored in "res" and the output of b1 amd b2 which is "res" is taken as input value for b1.
        #given the b2 value the operation is performed and result is again taken as one of the input for the set of operation.