import crypt

class Main:
    def __init__(self):
        self.run = True

    def __del__(self):
        pass 

    def mode(self, number):
        if number == '1':
            files = input("Path: ")
            salt = input("Salt: ")

            File.open(files, salt)
        elif number == '2':
            pass
        elif number == '3':
            self.run = False

        else:
            print("Input 1 or 2 or 3")

class File:
    def __init__(self):
        self.dir = None
        self.line = None
        self.salt = None

    def __del__(self):
        pass

    def open(self, files, salt):
        try:
            self.dir = open(files, 'r')
            self.salt = salt

            while True:
                self.line = self.dir.readline().strip()
                if not self.line: 
                    break

                self.crack()

        except FileNotFoundError:
            print("Error.")

        finally:
            self.dir.close()
    
    def crack(self):
        print(self.line)
        print(self.salt)
        h = crypt.crypt(self.line, self.salt)
        print("password: " + self.line + "salt: " + self.salt)
        print("hash: " + h)

Main = Main()
File = File()

while(Main.run):
    print("1.password dictionary 2.password cracking 3. quit")
    number = input("Input: ")

    Main.mode(number)