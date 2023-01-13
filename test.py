print('Hello world')

def sep(func):
  def wrapper(*argc, **kvargs):
    print('----')
    res = func(*argc, **kvargs)
    print('----')
    return res

  return wrapper


@sep
def some_func():
  print('Hello everyone')


some_func()
