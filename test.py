from hash_table.HashTable import HashTable


def test_HashTable():
    ht = HashTable()
    ht.insert(1, 'a')
    ht.print()
    ht.insert('name', 'lee')
    ht.print()
    ht.insert(2, 'b')
    ht.print()
    ht.insert(3, 'c')
    ht.print()
    print(ht.read(2))
    ht.insert(4, 'd')
    ht.print()


def main():
    test_HashTable()


if __name__ == "__main__":
    main()