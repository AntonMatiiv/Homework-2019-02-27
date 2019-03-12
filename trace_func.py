from sys import settrace

def foo():
    friends = ["Bob", "Tom"]
    for f in friends:
        print("Hi %s!" % f)
    return len(friends)

def tracefunc(frame, event, args):
    if event == "return":
        print("functions:", frame.f_code.co_name,",", "local vars:", *frame.f_locals)
    return tracefunc

settrace(tracefunc)
foo()
