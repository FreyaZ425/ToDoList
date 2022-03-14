"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

import pandas as pd
from classes import ToDoList

planner1 = ToDoList()
planner1.add_event('April 25', 'Birthday')
planner1.add_event('March 9', 'COGS18 Test')
planner1.add_event('Decemebr 25', 'Christmas Day')
planner1.change_event('April 25', 'Birthday', 'April 24', 'Birthday')


def test_plan():
    assert type(planner1.plan('April 24')) == pd.DataFrame
    assert planner1. plan('Jun 15') == 'No event added for this date.'

def test_add_event():
    assert type(planner1.add_event('April 25', 'Birthday')) == pd.DataFrame

    
def test_change_event():

    assert type(planner1.change_event('April 25', 'Birthday', 'April 24', 'Birthday')) == pd.DataFrame
    

def test_show_my_schedule():

    assert type(planner1.show_my_schedule()) == pd.DataFrame
    



                 
    