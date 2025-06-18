def devolver_distintos(*args):

    if sum(args) > 15:
        print(max(args))
    if sum(args) < 10:
        print(min(args))
    if sum(args) in range(10,15):
        print(sum(args)-max(args)-min(args))

devolver_distintos(8,5,5)
