

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for c in string:
        hash = (hash * 33) + ord(c)
    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    ll = hash_table.storage[index]
    if ll is None:
        ll = LinkedPair(key, value)
        hash_table.storage[index] = ll
    else:
        while ll.next is not None:
            if ll.key == key:
                ll.value = value
                return
            ll = ll.next
        ll.next = LinkedPair(key, value)



# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    ll = hash_table.storage[index]
    if ll is None:
        return None

    while ll.key != key and ll.next is not None:
        ll = ll.next

    if ll.key == key:
        return ll.value
    else:
        return None



# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


# Testing()
