import mymodule1
import mymodule2

print((mymodule2.my_age - mymodule1.my_age) == (mymodule2.year - mymodule1.year))
# both module names are printed.
# because the print statements are executed when the modules are imported

# doesn't print the condition __name__ == "__main__" from mymodule1, as the __name__ change when imported.