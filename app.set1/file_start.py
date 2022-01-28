def main():
    # Open a FILE for writing and create it if it doesn't exist
    f = open("mario.txt","w+")
    # Write some lines of data to the file
    for i in range(10):
        f.write("This is the Line: " + str(i) + "\r\n")
    # Close the File
    f.close()
    # Open the file for Appending test to the file
    f = open("Mario.txt","a")
    for i in range(10):
        f.write("Mais Linhas: " + str(i) + "\r\n")
    f.close()
    # Open the file for Read
    f = open("Mario.txt","r")
    if f.mode == 'r':
        conteudo = f.read()
        print(conteudo)
    f = open("Mario.txt",'r')
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            print(x)

if __name__ == "__main__":
    main()