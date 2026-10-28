
def greet(name):
    name = name.strip()

    if not name:
        raise ValueError("Name cannot be empty")

    return "Hello, " + name + "!"
