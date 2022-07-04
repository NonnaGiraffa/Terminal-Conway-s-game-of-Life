import GumbUI as ui
#Setting up GumbUI.
ui.set_matrix(20, 20, "·")
CELL = "#"

#Returns how many cells a point is touching (ITSELF NOT INCLUDED).
def touch(x, y):
    output = 0
    for i in range(y + 1, y - 2, -1):
        for j in range(x - 1, x + 2, 1):
            if j == x and i == y:
                pass
            elif ui.point(j, i) == CELL:
                output += 1
    return output

def update():
    cell_buffer = []
    kill_buffer = []
    for i in range(ui.height):
        for j in range(ui.width):
            tch = touch(j, i)
            if ui.point(j, i) == CELL:
                #* Solitude
                if tch <= 1:
                    kill_buffer.append((i, j))
                #* Overpopulation
                if tch >= 4 or tch == 0:
                    kill_buffer.append((i, j))
            elif tch == 3:
                cell_buffer.append((i, j))
    digest(cell_buffer, "CELL")
    digest(kill_buffer, "KILL")

def digest(temp, type):
    if type == "CELL":
        for y, x in temp:
            ui.point(x, y, CELL)
    elif type == "KILL":
        for y, x in temp:
            ui.point(x, y, ui.background)

def conways():
    while True:
        ui.view()
        input()
        update()

ui.schematic.load(ui.width // 2.5, ui.height // 2.5, "pattern")
ui.view()

conways()