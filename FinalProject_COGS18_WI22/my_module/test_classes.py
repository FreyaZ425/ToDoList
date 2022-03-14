"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

import pandas as pd
from classes import ToDoList
#from classes import add_event, delete_event, change_event, plan
##
##
planner1 = ToDoList()
planner1.add_event('April 25', 'Birthday')
planner1.add_event('March 9', 'COGS18 Test')
planner1.add_event('Decemebr 25', 'Christmas Day')

def test_add_event():

    assert callable(add_event())

def test_delete_event():

    assert callable(delete_event())
    
def test_change_event():

    assert callable(change_event())
    
def test_plan():
    assert type(planner1.plan('April 24')) == pd.DataFrame
    assert planner1. plan('Jun 15') == 'No event added for this date.'
    
def test_show_my_schedule():

    assert callable(show_my_schedule())
    



                 
    