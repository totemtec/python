import hello

hello.test()

print(hello.__doc__)

print(hello.greeting('Ma'))

# 私有方法以 _ 或者 __ 开头，可以调用，但是不建议直接调用
print(hello._private_1('Ma111'))

print(hello._private_2('Ma222'))
