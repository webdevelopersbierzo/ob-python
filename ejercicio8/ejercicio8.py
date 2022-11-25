
def main():
    file = open('./fichero.txt', 'a+');
    file.write("Primer acceso")
    file.close();

    file = open('./fichero.txt', 'a')
    file.write(" Segundo acceso");
    file.close();


if __name__ == '__main__':
    main()
