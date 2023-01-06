# 装饰器

# def fitness():
#     print('fitting')
#     run()

# def run():
#     print('running')

# fitness()

def decoate(func):
  def in_func(new_func):
    func(new_func)
  return in_func

@decoate

