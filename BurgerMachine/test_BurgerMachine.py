import pytest 
# make sure there's an _init_.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
import sys
sys.path.append("..")

from BurgerMachine import BurgerMachine
from BurgerMachine import STAGE
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm
@pytest.fixture
def machine1():
    bm1 = BurgerMachine()
    return bm1

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order, machine):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #machine.handle_pay(10000,"10000")
    return machine


def test_production_line(second_order):
    assert second_order is not None

#UCID: vc435
# date: 03/19/23
def test_first_selection(machine):
    assert machine.currently_selecting.name == STAGE.Bun.name
 #This test determines whether or not the bun is the first selection stage.

#UCID: vc435
# date: 03/19/23
def test_patties_in_stock(machine):
    machine.patties[0].quantity = 1
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    try:
        machine.handle_patty("veggie")
        assert machine.patties[0].quantity == 1
    except OutOfStockException:
        assert False
        #In order to determine whether the patties can be added again or not, the burger machine item quantity is changed to 1, 
        #and if the item is added, an OutOfStock Exception will be raised.

#UCID: vc435
# date: 03/19/23
def test_toppings_in_stock(machine):
    machine.toppings[0].quantity = 1
    machine.handle_bun("no bun")
    machine.handle_patty("next")
    machine.handle_toppings("cheese")
    try:
        machine.handle_toppings("cheese")
        assert machine.toppings[0].quantity == 1
    except OutOfStockException:
        assert False
    #By setting the amount of the first topping's machine to 1,
    #this test initially shows that there is only one unit of that topping in stock 
    #and shows that there is only one in the quantity of that topping. 
    #if the same topping is chosen twice, it raises an OutOfStock Exception.

#UCID: vc435
# date: 03/19/23
def test_max_patties(machine):
    machine.patties[0].quantity=10
    machine.handle_bun("no bun")
    for patty in range(machine.MAX_PATTIES - 1):
        machine.handle_patty("turkey")
    try:
        machine.handle_patty("turkey")
        assert machine.remaining_patties == 0
    except ExceededRemainingChoicesException:
        assert False

    #used to add a patty to a loop. 
    # When the limit of three patties is reached, the value of ExceededRemainingChoices will be increased.

#UCID: vc435
# date: 03/19/23
def test_max_toppings(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("next")
    # loop to choose (maximum - 1) number of toppings
    for scoop in range(machine.MAX_TOPPINGS - 1):
        machine.handle_toppings("cheese")
    try:
        machine.handle_toppings("cheese")
        assert machine.remaining_toppings == 0
    except ExceededRemainingChoicesException:
        assert False
        #This exception is used as a topping for a loop. The max toppings is used three times, 
        #If more than three patties are added, ExceededRemainingChoices will be raised.

#UCID: vc435
# date: 03/19/23
def test_total_cost(machine1):
    machine1.reset()
    machine1.handle_bun("no bun")
    machine1.handle_patty("turkey")
    machine1.handle_patty("veggie")
    machine1.handle_patty("beef")
    machine1.handle_patty("next")
    machine1.handle_toppings("cheese")
    machine1.handle_toppings("mayo")
    machine1.handle_toppings("lettuce")
    machine1.handle_toppings("done")
    assert machine1.calculate_cost() == 3.75
    #added a bun, a few options of patties from the list and toppings. 
    #All these ingredients are added together. The sum is calculated from the inputs.
    #declared that the sum is equal to the cost that is determined .

#UCID: vc435
# date: 03/19/23

def test_total_sales(machine1):
    machine1.handle_bun("no bun")
    machine1.handle_patty("turkey")
    machine1.handle_patty("veggie")
    machine1.handle_patty("next")
    machine1.handle_toppings("mayo")
    machine1.handle_toppings("done")
    burgerCost1 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost1, str(burgerCost1))

    machine1.handle_bun("lettuce wrap")
    machine1.handle_patty("beef")
    machine1.handle_patty("next")
    machine1.handle_toppings("mayo")
    machine1.handle_toppings("tomato")
    machine1.handle_toppings("done")
    burgerCost2 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost2, str(burgerCost2))

    machine1.handle_bun("white burger bun")
    machine1.handle_patty("veggie")
    machine1.handle_patty("next")
    machine1.handle_toppings("mayo")
    machine1.handle_toppings("tomato")
    machine1.handle_toppings("done")
    burgerCost3 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost3, str(burgerCost3))

    assert machine1.total_sales == burgerCost1 + burgerCost2 + burgerCost3
    #A bun, few of the list's options for patties, and toppings are added.  
    # Three separate burgers were included with a variety of options, and  payments are made for all three of them.  
    # The total sales were equivalent to the cost of the three burgers.

#UCID: vc435
# date: 03/19/23
def test_total_burgers(second_order,machine1):
    machine1.handle_bun("lettuce wrap")
    machine1.handle_patty("turkey")
    machine1.handle_patty("next")
    machine1.handle_toppings("done")
    burgerCost1 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost1, str(burgerCost1))

    machine1.handle_bun("white burger bun")
    machine1.handle_patty("next")
    machine1.handle_toppings("mayo")
    machine1.handle_toppings("done")
    burgerCost2 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost2, str(burgerCost2))

    machine1.handle_bun("wheat burger bun")
    machine1.handle_patty("next")
    machine1.handle_toppings("tomato")
    machine1.handle_toppings("done")
    burgerCost3 = float(machine1.calculate_cost())
    machine1.handle_pay(burgerCost3, str(burgerCost3))
    
    second_order = BurgerMachine()
    assert second_order.total_burgers == 0 and machine1.total_burgers == 3
    #added 3 separate burgers, accepted acceptable payments for 3 of them, 
    # and stated that the total number of burgers was 3.
    #Used the pytest fixture second order wchich is equated to 0 and total burgers to 3.