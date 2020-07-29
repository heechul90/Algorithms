class HashTable:
    def __init__(self):
        self.hash_table = list([0 for i in range(8)])

    def hash_function(self, key):
        return key % 8

    def insert(self, key, value):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)

        if self.hash_table[hash_value] != 0:
            for i in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][i][0] == gen_key:
                    self.hash_table[hash_value][i][1] = value
                    return

            self.hash_table[hash_value].append([gen_key, value])
        else:
            self.hash_table[hash_value] = [[gen_key, value]]

    def read(self, key):
        gen_key = hash(key)
        hash_value = self.hash_function(gen_key)

        if self.hash_table[hash_value] != 0:
            for i in range(len(self.hash_table[hash_value])):
                if self.hash_table[hash_value][i][0] == gen_key:
                    return self.hash_table[hash_value][i][1]
            return None
        else:
            return None

    def print(self):
        print(self.hash_table)


