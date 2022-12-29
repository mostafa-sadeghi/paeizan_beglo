# Multi level Inheritance
import dey5
from abc import ABC, abstractmethod


class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


# Multiple Inheritance
# class Employee:
#     def greet(self):
#         print("Employee greeting")


# class Person:
#     def greet(self):
#         print("Person greeting")


# class Manager(Employee, Person):
#     # class Manager(Person, Employee):
#     pass


# manager = Manager()
# manager.greet()

# class Flyer:
#     def fly(self):
#         pass

# class Swimmer:
#     def swim(self):
#         pass

# class FlyingFish(Flyer, Swimmer):
#     pass


# Abstract Base class:


# class Stream(ABC):
#     # @abstractmethod
#     def read(self):
#         pass


# class MemoryStream(Stream):
#     def read(self):
#         print("memory Stream")


# class FileStream(Stream):
#     def read(self):
#         print("file Stream")


# mstream = MemoryStream()
# mstream.read()
# filestream = FileStream()
# filestream.read()


# polymorphism


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class TextBox(UIControl):
#     def draw(self):
#         print("Textbox")


# class Button(UIControl):
#     def draw(self):
#         print("Button")


# def draw(controls):
#     for control in controls:
#         control.draw()
# textbox = TextBox()
# button = Button()

# draw([textbox, button])


# Duck Typing

class TextBox:
    def draw(self):
        print("Textbox")


class Button:
    def draw(self):
        print("Button")


def draw(controls):
    for control in controls:
        control.draw()


textbox = TextBox()
button = Button()

draw([textbox, button])
