'''
DIP -> Dependency Inversion Principle => The Dependency Inversion principle states that our classes should
depend upon interfaces or abstract classes instead of concrete classes and functions.
'''

# from enum import Enum
# class Relationship(Enum):
#     PARENT = 0
#     CHILD = 1
#     SIBLING = 2

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Relationships:
#     def __init__(self):
#         self.relations = [] # list of tuples

#     def add_parent_and_child(self, parent, child):
#         self.relations.append((parent, Relationship.PARENT, child))
#         self.relations.append((child, Relationship.CHILD, parent))

# class Research:
#     def __init__(self, relationships):
#         relations = relationships.relations
#         for r in relations:
#             if r[0].name == 'Ajay' and r[1] == Relationship.PARENT:
#                 print(f'Ajay has a child called {r[2].name}')

# parent = Person('Ajay')
# child1 = Person('Ankit')
# child2 = Person('Arpit')

# relationships = Relationships()
# relationships.add_parent_and_child(parent, child1)
# relationships.add_parent_and_child(parent, child2)

# research = Research(relationships)

'''
so it might look as though everything is ok, but there is a huge problem with "self.relations = []. In this case,
we are accessing the internal storage mechanism of relationships which is a low level module into our high level
module, which is a bad thing. And that is so because we cannot change it to dictionary

if we have dependency on the storage implementation, then it is better to provide some sort of utility methods
inside the low level module to perform the search. Because if we change the storage implementation, the search
would look completely different
'''

from enum import Enum
from abc import abstractmethod
class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name):
        self.name = name

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass

class Relationships(RelationshipBrowser): # low level module
    def __init__(self):
        self.relations = [] # list of tuples

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))
    
    def find_all_children_of(self, name):
        relations = self.relations
        for r in relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research: # high-level module
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'Ajay' and r[1] == Relationship.PARENT:
    #             print(f'Ajay has a child called {r[2].name}')
    def __init__(self, relationships):
        for p in relationships.find_all_children_of('Ajay'):
            print(f'Ajay has a child called {p}')

parent = Person('Ajay')
child1 = Person('Ankit')
child2 = Person('Arpit')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

research = Research(relationships)

'''
so this is the ultimate goal of DIP, instead of depending on low level module directly, we introduced an interface
RelationshipBrowser. 
'''