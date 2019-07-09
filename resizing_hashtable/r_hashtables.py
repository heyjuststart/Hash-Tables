

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
        self.count = 0
        self.original_capacity = capacity


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
        hash_table.count += 1
    else:
        while True:
            if ll.key == key:
                ll.value = value
                return
            if ll.next is None:
                break
            ll = ll.next
        ll.next = LinkedPair(key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    ll = hash_table.storage[index]
    if ll is None:
        print(f"Warning, attempted to remove nonexistent key")

    prev_ll = None
    while ll.key != key and ll.next is not None:
        prev_ll = ll
        ll = ll.next

    if ll.key == key:
        if ll.next is not None:
            prev_ll.next = ll.next
        else:
            if prev_ll is None:
                # there was only one item here and we're removing it
                hash_table.storage[index] = None
                hash_table.count -= 1
            else:
                prev_ll.next = None
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
    load_factor = hash_table.count / hash_table.capacity
    new_hash_table = hash_table
    needs_resize = False

    # if load limits exceeded,
    # make a new hash table with half the capacity and
    # insert each element from the old one
    if load_factor > 0.7:
        new_hash_table = HashTable(hash_table.capacity * 2)
        new_hash_table.original_capacity = hash_table.capacity
        needs_resize = True
    elif (hash_table.original_capacity != hash_table.capacity
    and load_factor < 0.2):
        new_hash_table = HashTable(hash_table.capacity // 2)
        needs_resize = True

    if needs_resize:
        for i in range(hash_table.count):
            ll = hash_table.storage[i]
            while True:
                if ll is None:
                    break
                hash_table_insert(new_hash_table, ll.key, ll.value)
                ll = ll.next

    return new_hash_table


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


Testing()
