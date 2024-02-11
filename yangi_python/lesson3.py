def strike(text):
    """Renders string with strike-through characters through it.
    strike('hello world') -> '̶h̶e̶l̶l̶o̶ ̶w̶o̶r̶l̶d'
    Notes
    -----
    \u0336 is a special strike-through unicode character; it
    is not unique to Python."""
    return ''.join('\u0336{}'.format(c) for c in text)

class ShoppingList:
    def __init__(self, items):
        self._needed = set(items)
        self._purchased = set()

    def __repr__(self):
        """ Returns formatted shopping list as a string with
            purchased items being crossed out.

            Returns
            -------
            str"""
        if self._needed or self._purchased:
            remaining_items = [str(i) for i in self._needed]
            purchased_items = [strike(str(i)) for i in self._purchased]
            # You wont find the • character on your keyboard. I simply
            # googled "unicode bullet point" and copied/pasted it here.
            return "• " + "\n• ".join(remaining_items + purchased_items)

    def add_new_items(self, items):
        self._needed.update(items)

    def mark_purchased_items(self, items):
        self._purchased.update(set(items) & self._needed)
        self._needed.difference_update(self._purchased)



l = ShoppingList(["grapes", "beets", "apples", "milk", "melon", "coffee"])
l.mark_purchased_items(["grapes", "beets", "milk"])
# print(l)

# Method

# Signature

# Explanation

# Add

# add(self, other)

# x + y invokes x.add(y)

# Subtract

# sub(self, other)

# x - y invokes x.sub(y)

# Multiply

# mul(self, other)

# x * y invokes x.mul(y)

# Divide

# truediv(self, other)

# x / y invokes x.truediv(y)

# Power

# pow(self, other)

# x ** y invokes x.pow(y)




def __add__(self, other):
    """ Add the unpurchased and purchased items from another shopping
        list to the present one.

        Parameters
        ----------
        other : ShoppingList
            The shopping list whose items we will add to the present one.
        Returns
        -------
        ShoppingList
            The present shopping list, with items added to it."""
    new_list = ShoppingList([])
    # populate new_list with items from self and other
    for l in [self, other]:
        new_list.add_new_items(l._needed)

        # add purchased items to list, then mark as purchased
        new_list.add_new_items(l._purchased)
        new_list.mark_purchased_items(l._purchased)
    return new_list



# # set __add__ as a method of ShoppingList
setattr(ShoppingList, "__add__", __add__)

food = ShoppingList(["milk", "flour", "salt", "eggs"])
food.mark_purchased_items(["flour", "salt"])

office_supplies = ShoppingList(["staples", "pens", "pencils"])
office_supplies.mark_purchased_items(["pencils"])

clothes = ShoppingList(["t-shirts", "socks"])

# # # combine all three shopping lists
all_products = food + office_supplies + clothes
print(all_products)
# print(all_products)
# • t-shirts
# • eggs
# • pens
# • milk
# • staples
# • socks
# • ̶f̶l̶o̶u̶r
# • ̶s̶a̶l̶t
# • ̶p̶e̶n̶c̶i̶l̶s



# Method

# Signature

# Explanation

# Length

# len(self)

# len(x) invokes x.len()

# Get Item

# getitem(self, key)

# x[key] invokes x.getitem(key)

# Set Item

# setitem(self, key, item)

# x[key] = item invokes x.setitem(key, item)

# Contains

# contains(self, item)

# item in x invokes x.contains(item)

# Iterator

# iter(self)

# iter(x) invokes x.iter()

# Next

# next(self)

# next(x) invokes x.next()



class MyList:
    def __init__(self, *args):
        if len(args) == 1 and hasattr(args[0], 'iter'):
            # handles `MyList([1, 2, 3])
            self._data = list(args[0])
        else:
            # handles MyList(1, 2, 3)
            self._data = list(args)

    def getitem(self, index):
        out = self._data[index]
        # slicing should return a MyList instance
        # otherwise, the individual element should be returned as-is
        return MyList(out) if isinstance(index, slice) else out

    def setitem(self, key, value):
        self._data[key] = value

    def len(self):
        return len(self._data)
    def repr(self):
        """ Use the character | as the delimiter for our list"""
        # self._data.__repr__() returns '[ ... ]',
        # thus we can slice to get the contents of the string
        # and exclude the square-brackets, and add our own
        # delimiters in their place
        return "|" + self._data.repr()[1:-1] + "|"

    def contains(self, item):
        return item in self._data

    def append(self, item):
        self._data.append(item)

# # MyList can accept any iterable as its
# # first (and only) input argument
# x = MyList("hello")
# print(x)
# |'h', 'e', 'l', 'l', 'o'|

# # MyList accepts an arbitrary number of arguments
# x = MyList(1, 2, 3, 4, 5)
# print(x)

# print(x[0])
# 5

# # getting an item
# >>> x[0]
# 1

# # slicing returns a MyList instance
# >>> x[2:4]x
# print(x[2:4])
# |3, 4|

# # setting an item
# x[0] = -1
# print(-1 in x)
# >>> x[0] = -1
# >>> x
# |-1, 2, 3, 4, 5|

# # checking membership
# >>> 10 in x
# False

# >>> MyList()
# ||

