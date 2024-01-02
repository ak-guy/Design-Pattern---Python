'''
OCP -> Open Closed Principle => The Open-Closed Principle requires that classes should be open for extension and
closed to modification. Modification means changing the code of an existing class, and extension means adding 
new functionality. 
'''
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size) -> None:
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p
    
    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p

    def filter_by_size_or_color(self, products, size, color):
        pass
'''
so now we have violated the open closed principle. The OCP suggest when we add new functionality we should add via
extension not via modification.

Because here there is two parameter color and size which will yield for (2^n - 1) = 3 different filters 
(considering only AND operation)
'''

class Specification:
    def is_satisfied(self, item):
        pass

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color
    
class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec : spec.is_satisfied(item), self.args
        ))

class BetterProductFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # bad(old) way
    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    # good(new) way
    bpf = BetterProductFilter()
    print('\nGreen products (new):')
    green = ColorSpecification(Color.GREEN)
    for p in bpf.filter(products, green):
        print(f' - {p.name} is green')

    print('\nLarge products (new):')
    large = SizeSpecification(Size.LARGE)
    for p in bpf.filter(products, large):
        print(f' - {p.name} is large')

    print('\nLarge and Blue products (new):')
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bpf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')

'''
Basically the idea is that we dont want to end up in a situation where we keep modifying code thats already been
written, tested and put into production
'''