# def add(*args):
#     # args is a tuple; * is the one that makes Unlimited Positional arguments possible,
#     # args can be renamed
#     su = 0
#     for n in args:
#         su += n
#     print(su)
#
#
# add(1,2,3,4)

def calculate(**kwargs):
    print(kwargs)
    print(kwargs['aji'])

calculate( aji = 23, als= 34)


# class Cars:
#     def __init__(self,**kwargs):