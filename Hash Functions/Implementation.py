# Hashsets
s = set()

# Add Values in the sets
s.add(1)
s.add(2)
s.add(3)
s.add(3)

# Look up in hashsets O(1).

if 1 in s:
    print(f'is the number present in the set? -> ', True)
print()

# Removing values in hashsets.

s.remove(2)
print('After removing a value in the set -> ', s)
print()


# Use cases

string = 'aaaaaaaaaabbbbbbbbbbbbbffffffffbdbdsljfdjfdbfbfbffjhffbf'

set_string = set(string)
print('Sets are used to remove the duplicate values from anything -> ', set_string)  # O(S) Space Complexity
print()


# Hashmaps - Dictionaries

d = {1: 'Anubhav', 2: 'Ankit', 3: 'Akash'}
print(d[1]) 
print()

# Adding in the dictionary

d[4] = 'Mukkoo'
print(d)
print()

# Checking presence of key in the dictionaries.

if 1 in d:
    print(True)
else: print(False)

# Print key value pair in the dictionaries

for key, val in d.items():
    print(('key', key, 'value', val))
print()


for val in d.values():
    print(val)