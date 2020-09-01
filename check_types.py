# https://stackoverflow.com/questions/34638457/how-to-determine-type-of-nested-data-structures-in-python


def type_spec_iterable(obj, name):
    tps = set(type_spec(e) for e in obj)
    if len(tps) == 1:
        return name + "<" + next(iter(tps)) + ">"
    else:
        return name + "<?>"


def type_spec_dict(obj):
    tps = set((type_spec(k), type_spec(v)) for (k,v) in obj.items())
    keytypes = set(k for (k, v) in tps)
    valtypes =  set(v for (k, v) in tps)
    kt = next(iter(keytypes)) if len(keytypes) == 1 else "?"
    vt = next(iter(valtypes)) if len(valtypes) == 1 else "?"
    return "dict<%s, %s>" % (kt, vt)


def type_spec_tuple(obj):
    return "tuple<" + ", ".join(type_spec(e) for e in obj) + ">"


def type_spec(obj):
    t = type(obj)
    res = {
        int: "int",
        str: "str",
        bool: "bool",
        float: "float",
        type(None): "(none)",
        list: lambda o: type_spec_iterable(o, 'list'),
        set: lambda o: type_spec_iterable(o, 'set'),
        dict: type_spec_dict,
        tuple: type_spec_tuple,
    }.get(t, lambda o: type(o).__name__)
    return res if type(res) is str else res(obj)


if __name__ == "__main__":
    class Foo(object):
        pass
    for obj in [
        1,
        2.3,
        None,
        False,
        "hello",
        [1, 2, 3],
        ["a", "b"],
        [1, "h"],
        (False, 1, "2"),
        set([1.2, 2.3, 3.4]),
        [[1,2,3],[4,5,6],[7,8,9]],
        [(1,'a'), (2, 'b')],
        {1:'b', 2:'c'},
        [Foo()], # todo - inheritance?
    ]:
        print(repr(obj), ":", type_spec(obj))