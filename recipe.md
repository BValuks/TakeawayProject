1. Describe the Problem
As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as Thank you! Your order was placed and will be delivered before 18:52 after I have ordered.

                                            PERSONAL ORGANISER




                   ┌─────────────────────────┐
                   │ Menu                    │
                   │                         │
                   │ -init (Nested dict)     │
                   │                         │
                   │                         │◄─────────────────────────────────┐
                   │                         │                                  │
                   │                         ├──────────────────────────────┐   │
                   │                         │                              │   │
                   └───────────────────┬─────┘                              │   │
                                       │    ▲                               │   │
                                       │    │                               │   │
                                       │    │                               │   │
                                       │    │                               │   │
                                       │    │                               │   │
                                       ▼    │                               ▼   │
       ┌────────────┐              ┌────────┴───────────┐               ┌───────┴─┐
       │            │              │                    │               │         │
       │ TextSender │ ◄────────────┤   Order            │               │ Receipt │
       │            │              │                    ├─────────────► │         │
       └────────────┘              │-init (Receipt)     │               └─────────┘
                                   │      (Customer)    │
                                   │      (TextSender)  │
                                   │-view_menu          │
                                   │-place_order        │
                                   │    -send text      │
                                   │-view_receipt       │                 Nouns                 Verbs
                                   │                    │
                                   │                    │                 *Customer             *Check
                                   │                    │                 *List                 *Order
                                   │                    │                 *Dishes               *View
                                   │                    │                 *Prices               *Select
                                   └───┬────────────────┘                 *Meal                 *Verify
                                       │        ▲                         *Order                *Receive
                                       │        │                         *Receipt
                                       │        │                         *Grand total
                                       │        │                         *Text message
                                       │        │
                                       │        │
                                       ▼        │
                                  ┌─────────────┴───────┐
                                  │                     │
                                  │ Customer            │
                                  │                     │
                                  │-init (name, number) │
                                  │                     │
                                  │                     │
                                  │                     │
                                  │                     │
                                  └─────────────────────┘









Also design the interface of each class in more detail.

class Diary:

    def __init__(self):
        # entry_list: blank list for diary entries
        # number_extractor: an instance of PhoneNumberExtractor class

    def add(self, diary_entry):
        # Parameters:
        #   diary_entry: an instance of DiaryEntry class
        # Side-effects:
        #   Adds the diary entry to the self.entry_list
        pass # No code here yet

    def all(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of all entries within self.entry_list
        # Side-effects:
        #   None
        pass # No code here yet

    def count_words(self):
        # Parameters:
        #   None
        # Returns:
        #   A count of all the words in the diary entries within self.entry_list
        pass # No code here yet

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: the speed that the user can read at
        # Returns:
        #   The time it would take the user to read all the diary entries within the self.entry_list
        pass # No code here yet

    def list_numbers(self):
        # Parameters:
        #   None
        # Returns:
        #   a list of all the phone numbers contained within the diary entries in the list
        pass # No code here yet

    def best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm: reading speed
        #   minutes: and integer representing the number of minutes the user has to read
        # Returns:
        #   the longest diary entry the user could read in the alloted time
        pass # No code here yet


class DiaryEntry:

    def __init__(self, date, name, contents):
        # Parameters:
        #   date: string representing a date
        #   name: string representing a name
        #   contents: string representing the diary entry
        # Attributes:
        #   self.entry: a string representing a formatted diary entry
        #   self.chunk_count: integer representing the number of times #reading_chunk has been run
        # Side-effects:
        #   Sets the date, name and contents properties
        pass # No code here yet

    def word_count(self):
        # Parameters:
        #   None
        # Returns:
        #   The number of words in the diary entry
        pass # No code here yet

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the users reading speed
        # Returns:
        #   the time it would take to read the entry at the given speed
        pass # No code here yet

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the users reading speed
        #   minutes: an integer representing the number of minutes the user has to read
        # Returns:
        #   The chunk of diary entry the user can read in the alloted time. If called again it will give the next chunk.
        #   Once the diary entry is finished, the entry is reset
        pass # No code here yet

class PhoneNumberExtractor:

    def __init__(self):
        # Parameters:
        #   None
        # Attributes:
        #   None
        # Side-effects:
        #   None
        pass # No code here yet

    def list_numbers(self, entry_list):
        # Parameters:
        #   entry_list: a list of diary entries
        # Returns:
        #   a list of all the phone numbers with the names attached
        pass # No code here yet

class EntrySelector:

    def __init__(self):
        # Parameters:
        #   None
        # Attributes:
        #   None
        # Side-effects:
        #   None
        pass # No code here yet

    def best_entry_for_reading_time(self, wpm, minutes, entry_list):
        # Parameters:
        #   wpm: reading speed
        #   minutes: and integer representing the number of minutes the user has to read
        #   entry_list: a list of diary entries
        # Returns:
        #   the longest diary entry the user could read in the alloted time
        pass # No code here yet

class TodoList:

    def __init__(self):
        # Parameters:
        #   None
        # Attributes:
        #   todo_list: an empty string to store the todo tasks
        # Side-effects:
        #   None
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: an instance of #Todo class
        # Returns:
        #   a string stating that the last has been added
        # Side-effects:
        #   the task gets added to self.todo_list
        pass # No code here yet

    def incomplete(self):
        # Parameters:
        #   None
        # Returns:
        #   a list of all the incomplete tasks
        # Side-effects:
        #   None
        pass # No code here yet

    def complete(self):
        # Parameters:
        #   None
        # Returns:
        #   a list of all the complete tasks
        # Side-effects:
        #   None
        pass # No code here yet

    def give_up(self):
        # Parameters:
        #   None
        # Returns:
        #   a string stating that all tasks have been set to complete
        # Side-effects:
        #   all tasks are set to complete
        pass # No code here yet

class Todo:

    def __init__(self, task):
        # Parameters:
        #   task: a string representing a task
        # Attributes:
        #   task: a string representing a task
        #   complete: a boolean representing whether the task is complete
        # Side-effects:
        #   None
        pass # No code here yet

    def mark_complete(self):
        # Parameters:
        #   None
        # Returns:
        #   None
        # Side-effects:
        #   the task gets marked as complete
        pass # No code here yet

3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations and combinations that reflect the ways in which the system will be used.

# EXAMPLE

"""
Given a Diary
When we add two diary entries
We see the entries in the entry_list
"""
diary = Diary()
entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Contact number: 02083619836')
entry2 = DiaryEntry('2nd Jan', 'Jane Seymour', 'Meeting to discuss new clients. Contact number: 07926158773')
diary.add(entry1)
diary.add(entry2)
diary.entry_list => [entry1, entry2]

"""
Given a Diary
When we add two diary entries and use #all
We see a list of formatted diary entries
"""
diary = Diary()
entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Contact number: 02083619836')
entry2 = DiaryEntry('2nd Jan', 'Jane Seymour', 'Meeting to discuss new clients. Contact number: 07926158773')
diary.add(entry1)
diary.add(entry2)
diary.all() => ['1st Jan: John Doe - Meeting to discuss stock chain. Contact number: 02083619836', '2nd Jan: Jane Seymour - Meeting to discuss new clients. Contact number: 07926158773']

"""
Given a Diary
When we add two diary entries and use #count_words
We see a number representing the number of words in all the diary entries combines
"""
diary = Diary()
entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Contact number: 02083619836')
entry2 = DiaryEntry('2nd Jan', 'Jane Seymour', 'Meeting to discuss new clients. Contact number: 07926158773')
diary.add(entry1)
diary.add(entry2)
diary.count_words() => 24

"""
Given a Diary
When we add two diary entries and use #list_numbers
We see a list of number contained within the diary entries with the names attached
"""
diary = Diary()
entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Contact number: 02083619836')
entry2 = DiaryEntry('2nd Jan', 'Jane Seymour', 'Meeting to discuss new clients. Contact number: 07926158773')
diary.add(entry1)
diary.add(entry2)
diary.list_numbers() => ['John Doe: 02083619836', 'Jane Seymour: 07926158773']

"""
Given a Diary
When we add two diary entries and use #best_entry_for_reading_time
We see a formatted string representing the longest diary entry the user can read in the allotted time
"""
diary = Diary()
entry1 = DiaryEntry('1st Jan', 'John Doe', 'Meeting to discuss stock chain. Changes to be made. Contact number: 02083619836')
entry2 = DiaryEntry('2nd Jan', 'Jane Seymour', 'Meeting to discuss new clients. Contact number: 07926158773')
diary.add(entry1)
diary.add(entry2)
diary.best_entry_for_reading_time(7, 2) => '2nd Jan: Jane Seymour - Meeting to discuss new clients. Contact number: 07926158773'

'''
Use #add and #incomplete on an instance of TodoList
Should add todos to class list and return a list 
'''
def test_add_method_on_todolist_should_list_todos_as_incomplete():
    todo_list = TodoList()
    task1 = Todo('Example task 1')
    task2 = Todo('Example task 2')
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.incomplete() == [task1, task2]

'''
Use #add on instance of TodoList, use #mark_complete on
instance of Todo, use #complete on instance of TodoList
Should return a list with the instance of Todo that has
been complete
'''
def test_complete_method_should_list_completed_todos():
    todo_list = TodoList()
    task1 = Todo('Example task 1')
    task2 = Todo('Example task 2')
    todo_list.add(task1)
    todo_list.add(task2)
    task1.mark_complete()
    assert task1.complete == True
    assert todo_list.complete() == [task1]
    assert todo_list.incomplete() == [task2]

'''
Use #give_up on instance of TodoList containg todos
Should mark all todos as complete
'''
def test_give_up_method_should_mark_all_todos_as_complete():
    todo_list = TodoList()
    task1 = Todo('Example task 1')
    task2 = Todo('Example task 2')
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.give_up()
    assert todo_list.incomplete() == []
    assert todo_list.complete() == [task1, task2]

4. Create Examples as Unit Tests
Create examples, where appropriate, of the behaviour of each relevant class at a more granular level of detail.

# EXAMPLE

--------------------------------------DIARY
"""
Given a Diary
It initialises with an empty list
"""
diary = Diary()
diary.entry_list => []

--------------------------------------DIARYENTRY
"""
Given a DiaryEntry
It initialises with date, name, contents, entry and chunk_count
"""
entry = DiaryEntry('Date1', 'Name1', 'Contents1')
entry.date = 'Date1'
entry.name = 'Name1'
entry.contents = 'Contents1'
entry.entry = 'Date1: Name 1 - Contents1'
entry.chunk_count => 0

"""
Given a DiaryEntry
Using #word_count returns the number of words in a diary entry
"""
entry = DiaryEntry('Date1', 'Name1', 'Contents1')
entry.word_count => 3

"""
Given a DiaryEntry
Using #reading_time returns the time in minutes it would take to read the entry at the given speed
"""
entry = DiaryEntry('Date1', 'Name1', 'This here is contents')
entry.reading_time(6) => 1
entry.reading_time(3) => 2
entry.reading_time(2) => 3
entry.reading_time(1) => 6

--------------------------------------TODOLIST
''' 
Initialise an instance of TodoList
Should be initialised with a blank list
'''
def test_initialise_todolist():
    todo_list = TodoList()
    assert todo_list.todo_list == []

--------------------------------------TODO
'''
Initialise an instance of Todo
Should initialise with a task and with a class property
'''
def test_inialise_todo():
    task = Todo('Walk the dog')
    assert task.task == 'Walk the dog'
    assert task.complete == False

'''
Call #mark_complete on an instance of Todo
Should change the class property from False to True
'''
def test_mark_complete_change_variable_to_true():
    task = Todo('Charge my laptop')
    task.mark_complete()
    assert task.complete == True

5. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.