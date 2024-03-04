name: tuple[bool, int, float, str] = (True, 1234, 53.24, "Pakistan")
print(name)
print(type(name)) #type
print(id(name)) #physical address
print(i for i in dir(name) if "__" not in i) # method and attributes
