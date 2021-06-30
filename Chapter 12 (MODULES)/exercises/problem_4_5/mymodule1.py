my_age = 25
year = 2021
print("My name is", __name__)

if __name__ == "__main__":
    print("This won’t run if I’m imported.")    # printed when the module code is run
                                                # as __name__ is __main__ when this module is run