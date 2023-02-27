class MyCalc:
    ans = 0

    def _is_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def addition(self, b1, b2):
        if b1 == "ans":
            return self.addition(self.ans, b2)
        else:
            b1 = self._as_number(b1)
            b2 = self._as_number(b2)
            self.ans = b1+b2
        print(f"add={self.ans}")
        return self.ans
# Ucid:vc435; date:02/26/23; Defined the input variables for the addition function as b1, b2.
#  If the first number is "ans," self.addition is returned (self.ans, b2).
#  Otherwise, it holds b1 to the integer value "b1" and b2 to the string value "b2".
# Then it prints addition=self. ans + b2
# If it has the value "ans," the addition will then be self.addition(self.ans, b2) and the result will be self.ans.
# Or else, b1 will be converted to a number using _as number(), and b2 will also be converted to a number using _as number() ().
# By using the addition() function, the results of these two operations are added together and returned as an integer.
    def subtraction(self, b1, b2):
        if b1 == "ans":
            return self.subtraction(self.ans, b2)
        else:
            b1 = self._as_number(b1)
            b2 = self._as_number(b2)
            self.ans = b1-b2
        print(f"sub={self.ans}")
        return self.ans
# Ucid:vc435; date:02/26/23; 
# the above logic is when two numbers are given as iput variable the differece of the two numbers is returned.
# First determines whether b1 is equal to "ans".
# if b1 is equal to ans, the result of self.subtraction(self.ans, b2) is given back.
# else b1 is set to self._as_number(n1), and b2 is set to self._as_number(b2).
# b1 value is subtracted from the b2 value.  If b1 is equal to "ans" then the result will be self.subtraction(self.ans, b2) 
# which is equal to 0.
# If both values are integers, the result is a negative integer, which is stored in self.ans.


    def multiplication(self, b1, b2):
        if b1 == "ans":
            return self.multiplication(self.ans, b2)
        else:
            b1 = self._as_number(b1)
            b2 = self._as_number(b2)
            self.ans = b1*b2
        print(f"multiplication={self.ans}")
        return self.ans
# Ucid: vc435; date:02/26/23; This function is for multiplication.
# Here, the first number is stored in the variable b1 and the second number is stored in the variable b2.
# if b1 is equal to "ans", it returns self.multiplication(self.ans,b2) oe else it stores both values in variables b1 and b2.
# furthur multiplies the two values.
# firstly it checks if it is equal to"ans" and then returns self.multiplication(self.ans, b2) 
# else it sets n1 and n2 to be an instance of Number.
# finally, the multiplication value is printed.

    def division(self, b1, b2):
        if b1 == "ans":
            return self.division(self.ans, b2)
        else:
            b1 = self._as_number(b1)
            b2 = self._as_number(b2)
            if b2 == 0:
                    print("not divisible by zero")
            else:
                    self.ans = b1/b2
                    print(f"division={self.ans}")
        return self.ans
#ucid:vc435; date: 02/26/23
# the division function takes two arguments b1 and b2 as inputs, If b1 is "ans", then it returns the division of the b2 by 1.
# Both the numbers are divided if they are not equal to 0 and allocated them to self's variable ans.
# The code executes the function and divides b1/b2 If the input b2 is zero, the message of error is shown and no result is given back.
# else, returns b1 by b2 and gives the result to self.ans.


if __name__ == '__main__':
    is_running = True
    iSTR = input("Are you ready?:")
    res = 0
    Calc = MyCalc()
    if iSTR == "yes":
        while is_running:
            iSTR = input("type your equation:")
            if iSTR == "quit" or iSTR == "q":
                is_running = False
            else:
                print("The equation is " + str(iSTR))
                checks = ["+", "*", "//",  "/", "", "x", "-", "%"]
                handled = False
                for check in checks:
                    if not handled and check in iSTR:
                        #nums = iSTR.split(check)
                        # b1 = nums[0].strip()
                        # # if b1 == 'ans':
                        # #     n1 = res
                        # b2 = nums[1].strip()
                        if "+" in check:
                            nums = iSTR.split("+")
                            res = Calc.addition(nums[0].strip(),nums[1].strip())
# This first splits the string "+" into individual characters with split() method from String class.
#Then it uses these characters as indexes for iterating through all items in iSTR list and calculating 
# how many times addition would be performed on each item with Calc's addition function (Calc).
                        elif "/" in check:
                            nums = iSTR.split("/")
                            res = Calc.division(nums[0].strip(),nums[1].strip())
                        elif "*" in check:
                            nums = iSTR.split("*")
                            res = Calc.multiplication(nums[0].strip(),nums[1].strip())
                        elif "-" in check:
                            nums = iSTR.split("-")
                            res = Calc.subtraction(nums[0].strip(),nums[1].strip())
else:
 print("Calculator is closed")
 is_running = False