def announce(f):
    def wrapper():
        print("about to run the function...")
        f()
        print("Done with the Function")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()