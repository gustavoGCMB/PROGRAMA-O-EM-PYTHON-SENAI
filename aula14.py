numero =  100


match numero:
    case x if x == 100:
        print('é 100')
    case x if x > 100:
        print('x é > 100')
    case x if x < 100:
        print('numero é menor que 100')