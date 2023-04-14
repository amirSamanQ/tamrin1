# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 17:09:31 2023

@author: Saman
"""
from abc import ABC, abstractmethod
class Human(ABC):
    def __init__(self,fname,lname,birth,nation):
        self.__fname = fname
        self.__lname = lname
        self.__birth = birth
        self.__nation = nation
    
    def show_name(self):
        return(self.__fname+self.__lname)
    
    def show_birth(self):
        return self.__birth
    
    def show_nation(self):
        return self.__nation
    def print_details(self):
        print(self.__fname,self.__lname,self.__birth,self.__nation)
    @abstractmethod
    def job(self):
        pass
        
class Author(Human):
    def __init__(self,list_of_books,language):
        self.list_of_books = list_of_books
        self.language = language
   
    def num_of_books(self):
        return len(self.list_of_books)
    
    def add_book(self,name_of_book):
        self.list_of_books.append(name_of_book)
    
    def job(self):
        print("the writer of the book")

class translater(Human):
    def __init__(self, translate_in_lang, list_of_books):
        self.translate_in_lang = translate_in_lang
        self.list_of_books = list_of_books
    def job(self):
        print("the translater of the book")
    def add_book(self,name_of_book):
        self.list_of_books.append(name_of_book)
    



