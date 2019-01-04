# TODO
    # Decide on the task to be done.
    # Set the pomodoro timer (traditionally to 25 minutes).[1]
    # Work on the task.
    # End work when the timer rings and put a checkmark on a piece of paper.[5]
    # If you have fewer than four checkmarks, take a short break (3–5 minutes), then go to step 2.
    # After four pomodoros, take a longer break (15–30 minutes), reset your checkmark count to zero, then go to step 1.

#!/usr/bin/python
# -*- coding: utf-8 -*-

def main():
    print_header()
    task()

def print_header():
    print('-----------------------')
    print('    Pomodoro Timer')
    print('-----------------------')

def task():
    task = input("What is your task? ")
    print("Your task is: ", task)
    type(task)

if __name__ == '__main__':
    main()