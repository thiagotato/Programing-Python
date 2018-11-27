import functools
def trace_function(f):
    """Add tracing before and after a function"""
    @functools.wraps(f)
    def new_f(*args):
        """The new function"""
        print(
                'Called {}({!r})'
                .format(f, *args))
        result = f(*args)
        print('Returing', result)
        return result
    return new_f

def memoize(f):
    print('Called memoize({!r})').format(f)
    cache  = {}
    @functools.wraps(f)
    def memoized_f(*args):
        print('Called memoized_f({!r})'.format(args))
        if args in cache:
            print('Cache hit!')
            return cache[args]
        if args not in cache:
            result = f(*args)
            cache[args] = result
            return result
    return memoized_f

@memoize
def add(first, second):
    """Return the sum of two arguments."""
    return first + second
