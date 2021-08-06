class ListsSample():
    """Sample class to explore Lists Data Structure.

        - Store multiple items sequentially.
        - Order is maintained.
        - Accept duplicate values.
        - Items can be modified (mutable).
        - Each position has an index [0,n].

        Some Methods:
            - append('new item') - add a new item to a given list.
            - extend(new_list) - add all items from another list.
            - remove('specific item') - remove value from list.
            - pop(0) - remove item at given index and return value.

        When using lists?
        - Make changes to items during execution.
        - Items are not unique.
        - Maintain the order of items in list.
    """

    @staticmethod
    def make_some_lists():
        names = ['Jane', 'Tracy', 'Paul']

        # print all items from the list
        print(names)

        # print tape of variable names
        print(type(names))

        # print valeu of a given index/position
        print(names[1])

        # update value of a specific index
        names[1] = 'Jack'
        print(names[1])

        # append new item
        names.append('Jessica')
        print(names)

        # extend three more items
        names.extend(['Beth', 'Craig', 'Bill'])
        print(names)

        # removing velue
        names.remove('Beth')
        print(names)

        # removing based on index
        names.pop(3)
        print(names)

        if 'Bill' in names:
            print("Yeah!!!")

        if 'Beth' not in names:
            print("Beth is not there!")

    @staticmethod
    def loop_through_list(l: list):
        for i in l:
            print(i)



if __name__ == '__main__':
    l = ListsSample()
    items = ['Apple', 'Banana', 'Apple', 'Orange']
    a = {'Jessica', 'Bento'}
    b = {'Esequiel', 'Bento'}
    tup = ('Esequiel', 'Jessica', 'Bento', 'Bento')

    l.make_some_lists()
    l.loop_through_list(items)
