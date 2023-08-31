# What are Dictionaries?

## Drawback of lists and tuples: access only by index

In lists and tuples, individual elements can only be accessed by index.
- This is sometimes cumbersome

Take a telephone book as an example

```
Name            Telephone Number
P. McCartney    123 456
J. Lennon       987 654
G. Harrison     113 425
R. Starr        777 888
```
- You do not want to search for the 3rd number.
- You want to look up the number by a name.

This is what dictionaries are made for. The elements are accessed not by index but by a key.
- In the example with the telephone, the name is the key.

## Definition and handling of dictionaries

Dictionaries consist of key-value pairs. That means, there is always a key, which can be use to access the value.
- In the telephone book, the key is the name of a person and the value is the telephone number.

Syntax:
- Dictionaries are represented by curly braces {}
- The key-value pairs are separated by commas.
- Each key-value pair is represented as follows:
    ```key : value```

An individual value is accessed by putting the key in square brackets.

It is possible to add, change and delete entries in the dictionary.

Trying to access a nonexistent key leads to an error.

To access the elements by index is not possible
```
print(tel[2])
```

## Adding key-value pairs to a dictionary

A new key-value pair can easily be added to a dictionary using the following statement:

```
dictionary[key] = value
```

## Replacing the value for an existing array

If a key already exists when it is assigned to a dictionary, the existing value is overwritten by the new value. This can be used to change or update entries in the dictionary. But you need to be careful not to overwrite the wrong entries in your dictionary.

## More about keys and values

The values in a dictionary can be of all data types including lists, tuples and dictionaries.

The keys can be nearly of all data types. And data types can be mixed within one dictionary as demonstrated

```
stupid_dict = {
    123: "blablabla",
    True: 123456,
    "key": False,
    (123, "abc"): 1000,
    34.5: [0, 1, 2, 4, 5],
}

print(stupid_dict)
```