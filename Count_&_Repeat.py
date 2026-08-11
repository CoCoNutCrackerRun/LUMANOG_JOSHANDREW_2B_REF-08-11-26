class Repeater:
    
    def repeat(self):
        word = input("Enter a word: ")

        while True:
            try:
                rep = int(input("How many times? "))
                if rep < 0:
                    print("Please enter a non-negative number.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        for i in range(rep):
            print(word)

rep = Repeater()
rep.repeat()