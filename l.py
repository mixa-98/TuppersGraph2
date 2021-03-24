from flask import Flask, render_template, request


to_do = [
    'die',
    'do a list to do'
]


fleks = Flask(__name__)
field = [[True] * 106 for i in range(17)]
rects = []

#       _
#n^2 = |n|
#       ¯


def calcpositions(num):
    if (num == 0):
        return
    num //= 17
    rslt = [False for i in range(1802)]
    i = 1801
    while (num > 0):
        rslt[i] = True if num % 2 else False
        num //= 2
        i -= 1
    for j in range(len(field[0])):
        for i in range(len(field)):
            field[i][len(field[0]) - 1 - j] = rslt[j * 17 + i]
    return




@fleks.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        num = int((request.form["संख्या"]).replace(" ", ""))
        calcpositions(num)
    for i in range(len(field)):
        for j in range(len(field[0])):
            color = "#000000" if field[i][j] else "#ffffff"
            rects.append(((j)*10, i * 10, color))
    return render_template('index.html', title="UNTITLED", hello="GOOSE", field=rects)


@fleks.route("/about")
def notmain():
    return "We are"