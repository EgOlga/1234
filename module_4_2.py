def test_function():
    a = 1
    b = a+3
    print(a, b)
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()    # Process finished with exit code 0

test_function()         # + test_function()
                        # 1 4
                        # Я в области видимости функции test_function
                        # Process finished with exit code 0


inner_function()        # + inner_function()
                        # NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
                        # 1 4
                        # Я в области видимости функции test_function
                        # Process finished with exit code 1
