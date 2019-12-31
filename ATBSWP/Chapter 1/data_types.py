#!/bin/python3 

print("Mutable types: ")

print("[\"test list\"]")
print(type(["test list"]))

print("{\"key:\" \"value\"}")
print(type({"key": "value"}))

print("{1, 2, 3}")
print(type({1, 2.0, "trois"}))

print("Immutable types: ")

print("32")
print(type(32))

print("32.4")
print(type(32.4))

print("Hello World")
print(type("Hello World"))

print("(test, 2)")
print(type(("test", 2)))

print("True")
print(type(True))
