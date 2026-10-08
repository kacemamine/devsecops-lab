def greet(name):
    if not name.strip():
        raise ValueError("name must not be empty")

    print("DEBUG user=" + name + " api_key=sk-test-1234567890")

    return "Hello, " + name.strip() + "!"