#!/usr/bin/python3
from samplebase import SampleBase
import time
import sys
import threading
from flask import Flask
from flask_restful import reqparse, Resource, Api

# flask rest
app = Flask(__name__)
api = Api(app)

# flask parser
parser = reqparse.RequestParser()
parser.add_argument('red')
parser.add_argument('green')
parser.add_argument('blue')
parser.add_argument('brightness')
parser.add_argument('waitTime')

# colors for the screen
colorRed = 255
colorGreen = 0
colorBlue = 0
colorBrightness = 0.10
# while loop sleep time in seconds
waitTime = 5

# flask rest
class HelloWorld(Resource):
    def get(self):
        return {'red': colorRed,
                'green': colorGreen,
                'blue': colorBlue,
                'brightness': colorBrightness,
                'waitTime': waitTime}

    def put(self):
        args = parser.parse_args()
        try:
            global colorRed
            global colorGreen
            global colorBlue
            global colorBrightness
            global waitTime

            colorRed = args['red']
            print ("red: "+colorRed)
            colorGreen = args['green']
            print ("green: "+colorGreen)
            colorBlue = args['blue']
            colorBrightness = args['brightness']
            waitTime = args['waitTime']
        except Exception as e:
            print ('fail '+str(e))
        return "success", 201

api.add_resource(HelloWorld, '/')

# starting rest
def startRest():
    app.run(host='192.168.10.50')
threadt = threading.Thread(target=startRest)
threadt.daemon = True 
# led screen
class SimpleClock(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SimpleClock, self).__init__(*args, **kwargs)

    def run(self):
        offset_canvas = self.matrix.CreateFrameCanvas()

        # define the 'font' for time
        number0 = [
            " ### ",
            "#   #",
            "#   #",
            "#   #",
            "#   #",
            "#   #",
            "#   #",
            "#   #",
            " ### "]
        number1 = [
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #"]
        number2 = [
            " ### ",
            "    #",
            "    #",
            "    #",
            " ### ",
            "#    ",
            "#    ",
            "#    ",
            " ### "]
        number3 = [
            " ### ",
            "    #",
            "    #",
            "    #",
            " ### ",
            "    #",
            "    #",
            "    #",
            " ### "]
        number4 = [
            "#   #",
            "#   #",
            "#   #",
            "#   #",
            " ####",
            "    #",
            "    #",
            "    #",
            "    #"]
        number5 = [
            " ### ",
            "#    ",
            "#    ",
            "#    ",
            " ### ",
            "    #",
            "    #",
            "    #",
            " ### "]
        number6 = [
            " ### ",
            "#    ",
            "#    ",
            "#    ",
            "#### ",
            "#   #",
            "#   #",
            "#   #",
            " ### "]
        number7 = [
            " ####",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #",
            "    #"]
        number8 = [
            " ### ",
            "#   #",
            "#   #",
            "#   #",
            " ### ",
            "#   #",
            "#   #",
            "#   #",
            " ### "]
        number9 = [
            " ### ",
            "#   #",
            "#   #",
            "#   #",
            " ####",
            "    #",
            "    #",
            "    #",
            " ### "]
        numberd = [
            "    ",
            "    ",
            " ## ",
            " ## ",
            "    ",
            " ## ",
            " ## ",
            "    ",
            "    "]
        numbers = [number0, number1, number2, number3, number4,
                   number5, number6, number7, number8, number9,numberd]

        # define 'font' for date
        numberD0 = [
            " # ",
            "# #",
            "# #",
            "# #",
            " # "]
        numberD1 = [
            "  #",
            "  #",
            "  #",
            "  #",
            "  #"]
        numberD2 = [
            "## ",
            "  #",
            " # ",
            "#  ",
            " ##"]
        numberD3 = [
            "## ",
            "  #",
            "## ",
            "  #",
            "## "]
        numberD4 = [
            "# #",
            "# #",
            " ##",
            "  #",
            "  #"]
        numberD5 = [
            " ##",
            "#  ",
            " # ",
            "  #",
            "## "]
        numberD6 = [
            " # ",
            "#  ",
            "## ",
            "# #",
            " # "]
        numberD7 = [
            "###",
            "  #",
            "  #",
            "  #",
            "  #"]
        numberD8 = [
            " # ",
            "# #",
            " # ",
            "# #",
            " # "]
        numberD9 = [
            " # ",
            "# #",
            " ##",
            "  #",
            " # "]
        numberDd = ["   ", "   ", "   ", "   ", " # "]
        numbersD = [numberD0, numberD1, numberD2, numberD3, numberD4,
                    numberD5, numberD6, numberD7, numberD8, numberD9,
                    numberDd]

        # define 'font' for weekdays (Finnish)
        dayMon = [
            "#   #   ##",
            "## ##  #  #",
            "# # #  ####",
            "# # #  #  #",
            "#   #  #  #"]
        dayTue = [
            "#####  #   ",
            "  #    #   ",
            "  #    #   ",
            "  #    #   ",
            "  #    #   "]
        dayWed = [
            "#  #  ###",
            "# #   #   ",
            "##    ###",
            "# #   #   ",
            "#  #  ###"]
        dayThu = [
            "#####   ## ",
            "  #    #  #",
            "  #    #  #",
            "  #    #  #",
            "  #     ## "]
        dayFri = [
            "###   ###  ",
            "#  #  #    ",
            "###   ###  ",
            "#     #    ",
            "#     ###  "]
        daySat = [
            "#      ##",
            "#     #  #",
            "#     ####",
            "#     #  #",
            "####  #  #"]
        daySun = [
            " ###  #  #",
            "#     #  #",
            " ##   #  #",
            "   #  #  #",
            "###    ## "]
        days = [daySun, dayMon, dayTue, dayWed, dayThu, dayFri, daySat]

        # prints given number or text (defined above) at given X and Y coordinates
        def printNumber(number, numX, numY):
            # calculate colors
            cRed = colorRed * colorBrightness
            cGreen = colorGreen * colorBrightness
            cBlue = colorBlue * colorBrightness
            # store starting X coordinate
            vara = numX
            # loop through rows in 'number'
            for row in number:
                # loop through characters in each row
                for char in row:
                    # if character is '#' print that pixel with calculated colors, if not paint it black
                    if char == "#":
                        offset_canvas.SetPixel(numX, numY, cRed, cGreen, cBlue)
                    else:
                        offset_canvas.SetPixel(numX, numY, 0, 0, 0)
                    # advance one pixel to the right after each char
                    numX += 1
                # advance one pixel down and return to the starting X coordinate
                numY += 1
                numX = vara

        # while loop updating the clock
        while True:
            # if the .txt reads 'stop' then exit everything
            if open("/home/sortsit/git/ledClock/txtClock.txt").read() == "stop\n":
                print("txtStop")
                sys.exit(0)

            # get current hours and minutes
            hours = int(time.strftime("%H"))
            minutes = int(time.strftime("%M"))
            # split them to individual variables (eg. 15 minutes -> 1 and 5)
            hour1 = int(hours / 10)
            hour2 = hours - (hour1 * 10)
            min1 = int(minutes / 10)
            min2 = minutes - (min1 * 10)

            # print each digit at specific X and Y coordinate
            printNumber(numbers[hour1], 0, 0)
            printNumber(numbers[hour2], 7, 0)
            # dots separating hours and minutes
            printNumber(numbers[10], 14, 0)
            printNumber(numbers[min1], 20, 0)
            printNumber(numbers[min2], 27, 0)

            # get current weekday and print it
            weekDay = int(time.strftime("%w"))
            printNumber(days[weekDay], 0, 11)

            # get current day and month and print them the same way as hours and minutes
            month = int(time.strftime("%m"))
            day = int(time.strftime("%d"))
            month1 = int(month / 10)
            month2 = month - (month1 * 10)
            day1 = int(day / 10)
            day2 = day - (day1 * 10)

            printNumber(numbersD[day1], 15, 11)
            printNumber(numbersD[day2], 19, 11)
            printNumber(numbersD[month1], 24, 11)
            printNumber(numbersD[month2], 28, 11)

            # update led screen
            offset_canvas = self.matrix.SwapOnVSync(offset_canvas)

            # wait before starting while loop again
            time.sleep(waitTime)


# Main function
if __name__ == "__main__":
    # Thread the Flask Restful
    threadt.start()
    # start led screen
    simple_clock = SimpleClock()
    if not simple_clock.process():
        simple_clock.print_help()
