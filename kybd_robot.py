#My robot program
'''A module for controllong my Zumo robot.'''
import RPi.GPIO as robot
import time
import curses

def main():

    #use constants rather than pin numbers
    #to id pins in calls to GPIO
    rf = 7
    rr = 11
    lf = 15
    lr = 13

    #get the cursese window, turn off echoing of keyboard to screen, turn on
    #instant (no waiting) key sesponse, and use special values for cursor keys
    screen = curses.initscr()
#    curses.noecho()
    curses.cbreak()
    screen.keypad(True)
    
    #set up GPIO
    robot.setmode(robot.BOARD)
    robot.setup(rf,robot.OUT)
    robot.setup(rr,robot.OUT)
    robot.setup(lf,robot.OUT)
    robot.setup(lr,robot.OUT)

    #methods (navigation commands) to control robots movement
    def forward():
        change()
        robot.output(rf,True)
        robot.output(lf,True)
        robot.output(rr,False)
        robot.output(lr,False)

    def reverse():
        change()
        robot.output(rf,False)
        robot.output(lf,False)
        robot.output(rr,True)
        robot.output(lr,True)

    def stop():
        robot.output(rf,False)
        robot.output(lf,False)
        robot.output(rr,False)
        robot.output(lr,False)

    def left():
        change()
        robot.output(rf,False)
        robot.output(lf,True)
        robot.output(rr,True)
        robot.output(lr,False)

    def right():
        change()
        robot.output(rf,True)
        robot.output(lf,False)
        robot.output(rr,False)
        robot.output(lr,True)

    def change ():
        stop()
        time.sleep(.2)

    try:
	print "Use the Arrow keys to control the robot"
        while True:
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                 forward()
            elif char == curses.KEY_DOWN:
                 reverse()
            elif char == curses.KEY_LEFT:
                left()
            elif char == curses.KEY_RIGHT:
                right()
            elif char == 10:
                 stop()

    finally:
        #close down curses properly, including turn echo back on
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
        robot.cleanup()
	print "Thank You for Enjoying the Robot"


if __name__ == "__main__":
    main()

