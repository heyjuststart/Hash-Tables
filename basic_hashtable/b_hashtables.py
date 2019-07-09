

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        self.capacity = capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(key):
    hash = 5381
    for c in key:
        hash = (hash * 33) + ord(c)
    return hash

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key) % hash_table.capacity
    current_value = hash_table.storage[index]
    if current_value is not None:
        print(f"Overwrite warning for {key}: {value}, previous value: {current_value}")

    hash_table.storage[index] = value



# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key) % hash_table.capacity
    if hash_table.storage[index] is None:
        print("Warning: Removing a key that doesn't exist")

    hash_table.storage[index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key) % hash_table.capacity
    if index > hash_table.capacity:
        return None
    return hash_table.storage[index]


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
