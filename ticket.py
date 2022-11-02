

class busSeats:
    def showSeats(self):
        for i in range(1, 28):
            print("-- ", end='')
        print()
        for i in range(1, 61):
            if (i == 1 or i == 16 or i == 31 or i == 46):
                print("| ", end="")
            print("⚫🟢", end=" ")
            if (i == 15 or i == 45):
                print(" |")
            elif (i == 30):
                print(" |\n")
            elif (i == 60):
                print(" |")
        for i in range(1, 18):
            print("-- ", end='')
        print()

    def seats():
        pass


b = busSeats()
b.showSeats()
