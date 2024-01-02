# SRP - > Single Responsibility Principle => The Single Responsibility Principle states that a class should do one thing and therefore it should have only a single reason to change. 
# or SOC -> Seperation of Concerns

# class Journal:
#     def __init__(self) -> None:
#         self.entries = []
#         self.count = 0

#     def add_entry(self, text):
#         self.count += 1
#         self.entries.append(f'{self.count} : {text}')

#     def remove_entry(self, pos):
#         del self.entries[pos]

#     def __str__(self) -> str:
#         return '\n'.join(self.entries)
    
# j = Journal()

# j.add_entry('I already had dinner.')
# j.add_entry('No i didnot finished the dinner yet.')

# print(f'Entries in Journal:\n{j}')

'''
Till here it is okay
but if we add other functionality like saving the data in text file, loading the journal from some file or load from web resource 
'''

# class Journal:
#     def __init__(self) -> None:
#         self.entries = []
#         self.count = 0

#     def add_entry(self, text):
#         self.count += 1
#         self.entries.append(f'{self.count} : {text}')

#     def remove_entry(self, pos):
#         del self.entries[pos]

#     def __str__(self) -> str:
#         return '\n'.join(self.entries)
    
#     def save(self, filename):
#         file = open(filename, 'w')
#         file.write(str(self))
#         file.close()

#     def load(self, filename):
#         pass

#     def load_from_web(self, uri):
#         pass

    
# j = Journal()

# j.add_entry('I already had dinner.')
# j.add_entry('No i didnot finished the dinner yet.')

# print(f'Entries in Journal:\n{j}')

'''
Now the problem is we have added a secondary responsibility to the journal, not only does the journal now stores
entries and allow us to manipulate the entries, but now it is taking on the responsiblty of persistence by 
providing functionality for saving and loading the journal from some resources.

This is a bad idea for multiple reasons. if you think about a complete application where in addition to journals,
there is other different types, and all of those types might have their own save and their own load and load from web
and so on. And this functionality might have to be centrally change at some point. For example when saving a file,
you might want to add additional code for checking that you are allowed to write to a particular directory.

Now, the problem is, if we adopt this approach, whats going to happen is we will have to go into every single class
inside our application and change their save method or change their load method. And that will be tedious

So we want to take the responsibility of persistence and stick it to other seperate class
'''

class Journal:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count} : {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)
    
    # def save(self, filename):
    #     file = open(filename, 'w')
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass

class PersistenceManager:
    @staticmethod
    def save(journal, filename):
        file = open(filename, 'w')
        file.write("\nThis is saved file content: \n")
        file.write(str(journal))
        file.close()

j = Journal()

j.add_entry('I already had dinner.')
j.add_entry('No i didnot finished the dinner yet.')

print(f'Entries in Journal:\n{j}')

file = r'/home/arpit/Downloads/journal.txt'
PersistenceManager.save(j, file)

with open(file) as fh:
    print(fh.read())

'''
Take away from this principle is that we should not overload our objects with too many responsibilities.
'''