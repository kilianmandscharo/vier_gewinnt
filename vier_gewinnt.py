class board :

    def __init__(self) :
        self.stoneCounter = 42

        # Solange das Spiel laeuft, ist diese Variable auf 1
        self.game = 1

        # Haelt fest, welcher Spieler gerade am Zug ist (1/2)
        self.turn = 1

        # Koordinaten des zuletzt eingeworfenen Steins
        self.lastStone = [0, 0]

        self.boardArray = [[" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "],
                           [" ", " ", " ", " ", " ", " ", " "]]

    # ---------------------------------------------------------------------- #
    # Hier wird das Brett ausgegeben

    def __str__(self) :
        reVal = "\n"
        for row in self.boardArray :
            reVal += "|"
            for square in row :
                reVal += "(" + square + ")"
            reVal += "|" + "\n"
        reVal += " --------------------- \n"
        reVal += "  1  2  3  4  5  6  7"
        return reVal

    # ---------------------------------------------------------------------- #
    # Funktion, die einen Stein platziert, abhaengig davon, welcher Spieler
    # gerade am Zug ist und wie viele Steine bereits in der jeweiligen Spalte
    # platziert wurden. Außerdem werden die Koordinaten des eingeworfenen
    # Steins für die naechste Funktion in der Instanz gespeichert.

    def placeStone(self, column) :

        symbol = "X" if board1.turn == 1 else "O"

        column -= 1 # Wegen Null-Indexierung

        def saveLastStone(row) :
            self.lastStone[0] = row
            self.lastStone[1] = column

        if self.boardArray[1][column] == " ":
            if self.boardArray[2][column] == " ":
                if self.boardArray[3][column] == " ":
                    if self.boardArray[4][column] == " ":
                        if self.boardArray[5][column] == " ":
                            self.boardArray[5][column] = symbol
                            saveLastStone(5)
                        else :
                            self.boardArray[4][column] = symbol
                            saveLastStone(4)
                    else :
                        self.boardArray[3][column] = symbol
                        saveLastStone(3)
                else :
                    self.boardArray[2][column] = symbol
                    saveLastStone(2)
            else :
                self.boardArray[1][column] = symbol
                saveLastStone(1)
        else :
            self.boardArray[0][column] = symbol
            saveLastStone(0)

    # ---------------------------------------------------------------------- #
    # Die Funktion ueberprueft, ob sich ausgehend vom zuletzt eingeworfenen
    # Stein vier gleiche Steine nebeneinander (diagonal, vertikal, horizontal)
    # befinden.

    def winCheck(self) :

        # Ueberprueft die gefüllten arrays
        def arrayCheck(array) :
            counter = 0
            symbol = "X" if board1.turn == 1 else "O"
            for field in array :
                if counter >= 4 :
                    self.game = 0
                    break
                if field == symbol :
                    counter += 1
                else :
                    counter = 0
                if counter >= 4 :
                    self.game = 0
                    break

        # Koordinaten des letzten Steins werden übernommen
        row = self.lastStone[0]
        column = self.lastStone[1]

        # Vertikaler array wird gefuellt und geprueft
        vertical = []
        for i in range(6) :
            vertical.append(self.boardArray[5 - i][column])
        arrayCheck(vertical)

        # Horizontaler array wird geprueft
        arrayCheck(self.boardArray[row])

        # Diagonale Arrays werden gefuellt und geprueft
        diagonal1 = []
        diagonal1RowStart = row
        diagonal1ColumnStart = column

        # Schritte bis man das linke obere Ende der Diagonale erreicht
        stepsToStartOfDiagonal1 = row if row < column else column

        # Groeße der jeweiligen Diagonale, berechnet mithilfe der Koordinaten
        # des zuletzt eingeworfenen Steins
        diagonal1Size = 6 - (row - column) if row >= column else 6 - (column - row - 1)

        # Geht zum linken oberen Ende der Diagonale
        for i in range(stepsToStartOfDiagonal1) :
            if diagonal1RowStart == 0 or diagonal1ColumnStart == 0 :
                break
            diagonal1RowStart -= 1
            diagonal1ColumnStart -= 1

        # Lauft von dort die Diagonale nach rechts unten und speichert alle
        # Zeichen im array. Das Durchschreiten der Diagonale erfolgt auf diese
        # Art, sodass die genaue Reihenfolge der Steine erfasst wird; möglicherweise
        # waere es effektiver gewesen, vom letzten Stein aus in jede Richtung drei
        # Felder weit zugehen, und diese zu zählen, ich wollte es jedoch auf diese
        # Art versuchen
        for i in range(diagonal1Size) :
            diagonal1.append(self.boardArray[diagonal1RowStart][diagonal1ColumnStart])
            diagonal1RowStart += 1
            diagonal1ColumnStart += 1

        # Hier das ganze noch einmal für die Diagonale in die andere Richtung
        diagonal2 = []
        diagonal2RowStart = row
        diagonal2ColumnStart = column
        stepsToStartOfDiagonal2 = row if row > column else column
        diagonal2Size = row + column + 1 if row + column < 6 else 12 - (column + row)

        for i in range(stepsToStartOfDiagonal2) :
            if diagonal2RowStart == 0 or diagonal2ColumnStart == 6 :
                break
            diagonal2RowStart -= 1
            diagonal2ColumnStart += 1

        for i in range(diagonal2Size) :
            diagonal2.append(self.boardArray[diagonal2RowStart][diagonal2ColumnStart])
            diagonal2RowStart += 1
            diagonal2ColumnStart -= 1

        arrayCheck(diagonal1)
        arrayCheck(diagonal2)

    # ---------------------------------------------------------------------- #
    # In dieser Funktion wird ueberprueft, ob die vom Spieler gewählte Spalte
    # bereits voll ist

    def columnCheck(self, column) :
        column -= 1
        if self.boardArray[0][column] == " " :
            return 1
        else :
            print("\nDiese Spalte ist leider voll, wählen sie eine andere Spalte.")
            return 0

    # ---------------------------------------------------------------------- #
    # Pruefen, ob noch Steine verfuegbar sind

    def stoneCheck(self) :
        if self.stoneCounter == 0 :
            board1.game = 0

# ========================================================================== #

class player :

    def __init__(self, name) :
        self.name = name

    # ---------------------------------------------------------------------- #
    # Pruefen, ob die eingegebene Spalte gültig ist

    def inputCheck(self, playerInput) :
        permittedInput = [1, 2, 3, 4, 5, 6, 7]
        if playerInput in permittedInput :
            return 1
        else :
            print("\nDie Eingabe war keine der erlaubten Spalten. Geben sie eine Zahl von 1 bis 7 ein.")
            return 0

# ========================================================================== #
# Brett und Spieler werden initialisiert.

print("\n======= Herzlich Willkommen zu Vier Gewinnt! =======\n")
player1Name = input("Geben sie hier den Namen für Spieler 1 ein: ")
player2Name = input("Geben sie hier den Namen für Spieler 2 ein: ")

board1 = board()
print(board1)
player1 = player(player1Name)
player2 = player(player2Name)

# ========================================================================== #
# Hauptschleife, in der sich der Spielablauf befindet.

while board1.game :

    if board1.turn == 1 :
        print(f"\n======= {player1.name} ist am Zug. =======")
    else :
        print(f"\n======= {player2.name} ist am Zug. =======")

    #Wird solange wiederholt, bis der Input richtig und die gewählte
    #Spalte noch frei ist
    while True :
        try:
            inputPlayer = int(input("In welche Spalte wollen sie ihren Stein werfen? "))
        except (ValueError) as e:
            print("Keine Zahl. Bitte noch einmal versuchen.", e)
            continue
        if player1.inputCheck(inputPlayer) and board1.columnCheck(inputPlayer):
            break

    board1.placeStone(inputPlayer) #Stein wird platziert
    print(board1)
    board1.winCheck() #Test, ob jemand gewonnen hat

    #Stein abgezogen und Test, ob noch Steine da sind
    board1.stoneCounter -= 1
    board1.stoneCheck()

    if board1.game :
        if board1.turn == 1 :
            board1.turn = 2
        else:
            board1.turn = 1

    # ---------------------------------------------------------------------- #

#Test, wer gewonnen hat oder ob es unentschieden ausgegangen ist

if board1.stoneCounter == 0 :
    print("\nEs gibt keine Steine mehr, das Spiel ist nicht entschieden.")
else :
    if board1.turn == 1 :
        print(f"\n======= {player1.name} hat gewonnen! =======")
    elif board1.turn == 2 :
        print(f"\n======= {player2.name} hat gewonnen! =======")


