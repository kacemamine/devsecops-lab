def greet(name):
    if not name.strip():
        raise ValueError("name must not be empty")
    return "Hello, " + name.strip() + "!"