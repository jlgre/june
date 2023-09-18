#!/usr/bin/env python

from tkinter import Tk, Frame


def main():
    root = Tk()
    root.title("Frame Example")
    root.config(bg="skyblue")

    left_frame = Frame(root, width=200, height=400)
    left_frame.grid(row=0, column=0, padx=10, pady=5)

    right_frame = Frame(root, width=650, height=400)
    right_frame.grid(row=0, column=1, padx=10, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
