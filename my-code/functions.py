def unlimited_arguments(*args, **kwargs):
    print(args)
    for arg in args:
        print(arg)

    print(kwargs)
    for key, val in kwargs.items():
        print("key: {}, val: {}".format(key, val))


unlimited_arguments(1, 2, 3, "abcd", kw1 = 11, kw2 = 22, kw3 = 33)
unlimited_arguments(*[1, 2, 3, "abcd"], **{ "kw1": 11, "kw2": 22, "kw3": 33 })


a = [1, 2, 3]
'Some text: {} {} {}'.format(*a)
