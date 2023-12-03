import tkinter as tk

NBj = 60 #Largeur
NBi = 30 #Hauteur
###############
## AFFICHAGE ##
###############

# Fonction appelée lorsqu'une case est cliquée
def toggle_value(row, col):
    if table[row][col] == 0:
        table[row][col] = 1
        canvas.itemconfig(cells[row][col], fill='black')
    else:
        table[row][col] = 0
        canvas.itemconfig(cells[row][col], fill='white')


table = [[0 for j in range(NBj)] for i in range(NBi)]

tableNeighbors = [[0 for j in range(NBj)] for i in range(NBi)]



def neighborsCounter(i, j): 
    neighbors = 0
    if i-1 >= 0 and i-1 <= NBi-1 and j-1 >= 0 and j-1 <= NBj-1:
        if table[i - 1][j - 1] == 1:
            neighbors = neighbors + 1
    if i-1 >= 0 and i-1 <= NBi-1 and j+0 >= 0 and j+0 <= NBj-1:
        if table[i - 1][j + 0] == 1:
            neighbors = neighbors + 1
    if i-1 >= 0 and i-1 <= NBi-1 and j+1 >= 0 and j+1 <= NBj-1:
        if table[i - 1][j + 1] == 1:
            neighbors = neighbors + 1
    if i+0 >= 0 and i+0 <= NBi-1 and j-1 >= 0 and j-1 <= NBj-1:
        if table[i + 0][j - 1] == 1:
            neighbors = neighbors + 1
    if i+0 >= 0 and i+0 <= NBi-1 and j+1 >= 0 and j+1 <= NBj-1:
        if table[i + 0][j + 1] == 1:
            neighbors = neighbors + 1
    if i+1 >= 0 and i+1 <= NBi-1 and j-1 >= 0 and j-1 <= NBj-1:
        if table[i + 1][j - 1] == 1:
            neighbors = neighbors + 1
    if i+1 >= 0 and i+1 <= NBi-1 and j+0 >= 0 and j+0 <= NBj-1:
        if table[i + 1][j + 0] == 1:
            neighbors = neighbors + 1
    if i+1 >= 0 and i+1 <= NBi-1 and j+1 >= 0 and j+1 <= NBj-1:
        if table[i + 1][j + 1] == 1:
            neighbors = neighbors + 1

    tableNeighbors[i][j] = neighbors

def TestNeighbors():
    currentI = 0
    currentJ = 0

    while NBi-1 >= currentI:
        
        while NBj-1 >= currentJ:
            neighborsCounter(currentI, currentJ)
            currentJ = currentJ + 1
        currentJ = 0
        currentI = currentI + 1


def evolution():
    TestNeighbors()

    currentIBis = 0
    currentJBis = 0
    while NBi-1 >= currentIBis:
        
        while NBj-1 >= currentJBis:
            if table[currentIBis][currentJBis] == 0 and tableNeighbors[currentIBis][currentJBis] == 3:
                table[currentIBis][currentJBis] = 1
                canvas.itemconfig(cells[currentIBis][currentJBis], fill='black')
            if table[currentIBis][currentJBis] == 1 and tableNeighbors[currentIBis][currentJBis] == 2 or tableNeighbors[currentIBis][currentJBis] == 3:
                table[currentIBis][currentJBis] = 1
                canvas.itemconfig(cells[currentIBis][currentJBis], fill='black')
            else:
                table[currentIBis][currentJBis] = 0
                canvas.itemconfig(cells[currentIBis][currentJBis], fill='white')
            
            currentJBis = currentJBis + 1
        currentJBis = 0
        currentIBis = currentIBis + 1

def clearGrid():
    currentIBis = 0
    currentJBis = 0
    while NBi-1 >= currentIBis:
        
        while NBj-1 >= currentJBis:    
            table[currentIBis][currentJBis] = 0
            canvas.itemconfig(cells[currentIBis][currentJBis], fill='white')
            
            currentJBis = currentJBis + 1
        currentJBis = 0
        currentIBis = currentIBis + 1

# Fonction pour créer la grille
def create_grid(rows, cols):
    global canvas, cells, table
    

    root = tk.Tk()
    root.title("Le Jeu de La Vie - HugLep")

    canvas = tk.Canvas(root, width=cols*30, height=rows*30)
    canvas.pack()

    cells = [[None for _ in range(cols)] for _ in range(rows)]

    for j in range(cols):
        for i in range(rows):
            x1 = j * 30
            y1 = i * 30
            x2 = x1 + 30
            y2 = y1 + 30
            cells[i][j] = canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')
            canvas.tag_bind(cells[i][j], '<Button-1>', lambda e, row=i, col=j: toggle_value(row, col))

    table[0][3] = 1
    canvas.itemconfig(cells[0][3], fill='black')
    table[1][4] = 1
    canvas.itemconfig(cells[1][4], fill='black')
    table[2][2] = 1
    canvas.itemconfig(cells[2][2], fill='black')
    table[2][3] = 1
    canvas.itemconfig(cells[2][3], fill='black')
    table[2][4] = 1
    canvas.itemconfig(cells[2][4], fill='black')

    update_button = tk.Button(root, text="Evolution", command=evolution)
    update_button.pack(side=tk.TOP)

    clear_button = tk.Button(root, text="Clear", command=clearGrid)
    clear_button.pack(side=tk.RIGHT)

    root.mainloop()


# Appel de la fonction pour créer une grille 
create_grid(NBi, NBj)
