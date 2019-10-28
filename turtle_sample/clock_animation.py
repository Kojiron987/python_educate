#!/usr/bin/env python3
"""       turtle-example-suite:

             tdemo_clock.py

Enhanced clock-program, showing date
and time
  ------------------------------------
   Press STOP to exit the program!
  ------------------------------------
"""
from turtle import *
from datetime import datetime

def jump(distance, angle=0):
    penup()
    right(angle)
    forward(distance)
    left(angle)
    pendown()


def draw_hand(length, top_size):
    forward(length*1.15)
    right(90)
    forward(top_size/2.0)
    left(120)
    forward(top_size)
    left(120)
    forward(top_size)
    left(120)
    forward(top_size/2.0)


def create_hand(length, top_size):
    begin_poly()
    draw_hand(length, top_size)
    end_poly()
    return get_poly()


def make_hand_shape(name, length, top_size):
    reset()
    # 秒針の描画位置を真ん中からずらす
    jump(-length*0.15)
    hand_form = create_hand(length, top_size)
    register_shape(name, hand_form)


def draw_clock_boudary(clock_size):
    reset()
    pensize(7)
    angle = 6
    for i in range(0, 360, angle):
        jump(clock_size)
        # 5つごとに縦棒を描画する
        if i % 5 == 0:
            forward(25)
            jump(-clock_size-25)
        # そのほかの場合、点を描画
        else:
            dot(3)
            jump(-clock_size)
        right(angle)


def setup():
    tracer(False)
    mode("logo")
    make_hand_shape("second_hand", 125, 25)
    make_hand_shape("minute_hand",  130, 25)
    make_hand_shape("hour_hand", 90, 25)
    draw_clock_boudary(160)

    second_hand = Turtle(shape='second_hand')
    second_hand.color("gray20", "gray80")

    minute_hand = Turtle(shape='minute_hand')
    minute_hand.color("blue1", "red1")

    hour_hand = Turtle(shape='hour_hand')
    hour_hand.color("blue3", "red3")

    for hand in second_hand, minute_hand, hour_hand:
        hand.resizemode("user")
        hand.shapesize(1, 1, 3)
        hand.speed(0)
    hideturtle()
    writer = Turtle()
    writer.hideturtle()
    writer.penup()
    writer.backward(85)

    return (second_hand, minute_hand, hour_hand, writer)


def get_weekday(d):
    weekdays = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[d.weekday()]


def get_date(d):
    months = {1: 'Jan.', 2: 'Feb.', 3: 'Mar', 4: 'Apr.', 5: 'May', 6: 'June',
              7: 'July', 8: 'Aug.', 9: 'Sep.', 10: 'Oct.', 11: 'Nov.', 12: 'Dec.'}
    return f"{d.day} {months[d.month]} {d.year}"


def draw_date(pen, d):
    pen.clear()
    pen.home()

    # 曜日の描画
    pen.forward(65)
    pen.write(get_weekday(d),
                 align="center", font=("Courier", 14, "bold"))
    pen.home()

    # 日にちの描画
    pen.back(85)
    pen.write(get_date(d),
              align="center", font=("Courier", 14, "bold"))
    pen.home()


def set_tick_paramter(second_hand, minute_hand, hour_hand, writer):
    def tick():
        today = datetime.today()
        second = today.second + today.microsecond*0.000001
        minute = today.minute + second/60.0
        hour = today.hour + minute/60.0
        try:
            tracer(False)
            draw_date(writer, today)
            tracer(True)
            second_hand.setheading(6*second)
            minute_hand.setheading(6*minute)
            hour_hand.setheading(30*hour)
            ontimer(tick, 100)
        except Terminator:
            pass  # turtledemo user pressed STOP
    return tick

def main():
    pens = setup()
    tick = set_tick_paramter(*pens)
    tick()
    return "EVENTLOOP"


if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
