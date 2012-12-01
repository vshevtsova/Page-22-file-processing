import os.path

FILE_PATH = 'D:\\Vita\\Python\\file_generator'

def read_sym(fd):
    sym = fd.read(1)
    while sym != '':
        yield sym
        sym = fd.read(1)

def iter_lines(f):
    it = iter(f)
    line = ''
    for sym in it:
        line += sym
        if sym == '\n':
            yield line
            line = ''
    yield line

def strip_spaces(f):
    it = iter(f)
    for L in it:
        yield L.strip()

def drop_empty(f):
    it = iter(f)
    for L in it:
        if L != '\n' and L != '':
            yield L

def split_items(f):
    it = iter(f)
    for L in it:
        L = L.split(' ', 1)
        while True:
            try:
                v = int(L[0])
                yield v
            except ValueError:
                try:
                    v = float(L[0])
                    yield v
                except ValueError:
                    yield L[0]
            if  len(L) > 1:
                L = L[1].split(' ', 1)
            else:
                break

def get_ints(f):
    it = iter(f)
    for L in it:
        if isinstance(L, int):
            yield L

def my_sum(f):
    it = iter(f)
    return reduce(lambda x, y: x + y, (x for x in it), 0)


fn = os.path.join(FILE_PATH, '1.txt')
print fn

print 'iter_lines'
fd = open(fn)
print list(iter_lines(read_sym(fd)))
fd.close()

print 'strip_spaces'
fd = open(fn)
print list(strip_spaces(iter_lines(read_sym(fd))))
fd.close()

print 'drop_empty'
fd = open(fn)
print list(drop_empty(strip_spaces(iter_lines(read_sym(fd)))))
fd.close()

print 'split_items'
fd = open(fn)
print list(split_items(drop_empty(strip_spaces(iter_lines(read_sym(fd))))))
fd.close()

print 'get_ints'
fd = open(fn)
print list(get_ints(split_items(drop_empty(strip_spaces(iter_lines(read_sym(fd)))))))
fd.close()

print 'my_sum'
fd = open(fn)
print my_sum(get_ints(split_items(drop_empty(strip_spaces(iter_lines(read_sym(fd)))))))
fd.close()