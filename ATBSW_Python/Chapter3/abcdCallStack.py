def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

#When a() is called, it executes print('a() starts') before it calls b(), which follows similar parameters prior to calling c()
#After the stack initially calls c(),it returns to b() and calls the next -and final line of the code for the function- before calling the next frame object in the stack
#Next frame object is a() which calls d()
#After calling d() the stack returns to a() - the final frame object - and calls the last argument of the a() function; print('a() returns')
