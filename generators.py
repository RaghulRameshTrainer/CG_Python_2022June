def remote_control():
    yield 'CNN'
    yield 'starsports'
    yield '24-7'
    yield 'vijaytv'

# prog=remote_control()
# print(prog.__next__())
# print(prog.__next__())
# print(prog.__next__())
# print(prog.__next__())
for x in remote_control():
    print(x)

