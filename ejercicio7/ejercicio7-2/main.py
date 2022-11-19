import functions


def main():
    if functions.horaLocal() >= 19:
       print(" Es hora de ir para casa")
    else:
        hourExit = functions.diferencia()
        print("Te quedan: ", hourExit)



if __name__ == '__main__':
    main()
