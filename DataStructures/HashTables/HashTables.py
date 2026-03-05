class HashTable:
    def __init__(self, size = 7):

        self.data_map = [None] * size

    def __hash(self, key):

        my_hash = 0

        for letter in key:

            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):

        for i, v in enumerate(self.data_map):
            print(f'index = {i} : value = {v}')

    def set_item(self, key, value):
        index = self.__hash(key)

        if not self.data_map[index]:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


    def get_item(self, key):

        index = self.__hash(key)

        if self.data_map[index]:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def get_keys(self):
        all_keys = []

        for i in range(len(self.data_map)):

            if self.data_map[i]:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


tab = HashTable()

tab.set_item('bolts', 9000)
tab.set_item('washers', 700)
tab.set_item('hammer', '100')
print('get', tab.get_item('washers'))

tab.print_table()