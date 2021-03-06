"""Classes used throughout project"""

import pandas as pd

class ToDoList():

    purpose = 'Tell you what to do.'

    def __init__(self):
        self.my_to_do_list = {'Date': [], 'Event': []}
        self.number = 0
        self.index = []
        self.df = pd.DataFrame(self.my_to_do_list, self.index)
 
    def add_event(self, date, event):
        """Add an event to the to-do-list.
    
        Parameters
        ----------
        date : string
            The day of the event.
        event : string
            Name of the event added.
    
        Returns
        -------
        calender : pandas DataFrame
            A table showing the days and events.
        """
        
        # adding event to the DataFrame
        self.my_to_do_list['Date'].append(date)
        self.my_to_do_list['Event'].append(event)
        self.number = self.number + 1
        self.index.append(self.number) # this will create the index number list for the DataFrame
        self.df = pd.DataFrame(self.my_to_do_list, self.index)
        calender = self.df
        return calender

 
    def delete_event(self, date, event):
        """Delete an event from the to-do-list.
    
        Parameters
        ----------
        date : string
            The day of the event.
        event : string
            Name of the event deleted.
    
        Returns
        -------
        calender : pandas DataFrame
            A table showing the days and events.
        """
        
        # removing the specified date and event from the DataFrame
        if date in self.my_to_do_list['Date']:
            self.my_to_do_list['Date'].remove(date)
        else:
            return None
        
        if event in self.my_to_do_list['Event']:
            self.my_to_do_list['Event'].remove(event)
        else:
            return None
        
        # update the DataFrame
        self.number = self.number - 1 # to ensure the correct length for the index 
        self.index.remove(self.index[-1]) # delete the last number on the index list
        self.df = pd.DataFrame(self.my_to_do_list, self.index)
        calender = self.df
        return calender
        
    def change_event(self, old_date, old_event, new_date, new_event):
        """Update an event or its date.
    
        Parameters
        ----------
        old_date : string
            The original date of the event.
        old_event : string
            The original name of the event.
        new_date : string
            The new date of the event.
        new_event : string
            The new name of the event.
    
        Returns
        -------
        calender : pandas DataFrame
            A table showing the days and events.
        """
        
        # locate the event desired to be changed
        for index, day in enumerate(self.my_to_do_list['Date']):
            if day == old_date:
                self.my_to_do_list['Date'][index] = new_date # replace old_date with new_date
                self.my_to_do_list['Event'][index] = new_event # replace old_event with new_event
            else:
                continue
        
        # updating the DataFrame        
        self.df = pd.DataFrame(self.my_to_do_list, self.index)
        calender = self.df
        return calender
    
    def show_my_schedule(self):
        return self.df
        
    
    def plan(self, day):
        """Tell you the event that happens on the specified date.
    
        Parameters
        ----------
        date : string
            The date you want to check.
    
        Returns
        -------
        things : DataFrame
            The list of things happening on the specified date.
        msg : string
        """
        if day in self.my_to_do_list['Date']:
            things = self.df.loc[self.df['Date'] == day] # Pull out the events that happen on the specified date
            return things
        else:
            msg = 'No event added for this date.'
            return msg

