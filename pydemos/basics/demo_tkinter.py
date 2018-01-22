# coding=utf-8

from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as dl

root = Tk()
num = dl.askinteger("info", "请输入一个整数:")

mb.showinfo("info", "你输入的数字是{0}".format(num))
