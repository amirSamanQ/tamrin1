# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:18:09 2023

@author: Saman
"""

from abc import ABC, abstractmethod
class Human(ABC):
    def __init__(self,fname,lname,birth,nation):
        self.__fname = fname
        self.__lname = lname
        self.__birth = birth
        self.__nation = nation
        self.name = fname + lname
    
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
    def __init__(self,fname,lname,birth,nation,list_of_books,language):
        super().__init__(fname,lname,birth,nation)
        self.class_topic = "Author"
        self.list_of_books = list_of_books
        self.language = language
   
    def num_of_books(self):
        return len(self.list_of_books)
    
    def add_book(self,name_of_book):
        self.list_of_books.append(name_of_book)
    
    def job(self):
        print("the writer of the book")

class Translater(Human):


    def __init__(self,fname,lname,birth,nation,translate_in_lang, list_of_books):
        super().__init__(fname,lname,birth,nation)
        self.translate_in_lang = translate_in_lang
        self.list_of_books = list_of_books
    def job(self):
        print("the translater of the book")
    def add_book(self,name_of_book):
        self.list_of_books.append(name_of_book)
class Book(ABC):
    def __init__(self,name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,translator=None):
        self.__name = name
        self.__author = author
        self.__appearanceObj = Appearance(No_of_pages,weight,paper_type,book_size,book_cover)
        self.publication = Publication(pub_name,address,phone,email)
        self.__ISNB = ISNB
        self.__translator = translator
        self.details =[author,self.publication,translator]
    def show_name(self):
        return self.__name
    
    def show_ISNB(self):
        return self.__ISNB
    
    def show_more_details(self):
        for i in self.details:
            print(f"{i.class_topic} of the book is {i.show_name()}")
    def have_translator(self):
        if(self.translator==None):
            print("No")
        
        else:
            print(f"Yes,{self.__translator.show_name()} is the translator of the book")
    def show_subject(self,obj):
        print(obj)
    @abstractmethod
    def about(self):
        pass
    

class Publication():
    def __init__(self,name,address,phone,email):
        self.class_topic = "publication"
        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__email = email
    
    def show_name(self):
        
        return self.__name
    
    def contact(self):
        print("email:",self.__email)
        print("phone:",self.__phone)
        
    def address(self):
        print("address:",self.__address)


class Appearance():
    
    
    def __init__(self,No_of_pages,weight,paper_type,book_size,book_cover):
            self.No_of_pages = No_of_pages
            self.weigh = weight
            self.paper_type = paper_type
            self.book_size = book_size
            self.book_cover = book_cover
    def print_pages(self):
        print(f"this book has {self.No_of_book} pages")
        
    def print_weigh(self):
        print(f"the weight of the book is {self.weight}")
        
    def print_size(self):
        print(f"the size of the book is {self.book_size[0]}*{self.book_size[1]}*{self.bookj_size[2]}")
    
    def print_cover(self):
        print(f"type of the cover of the book is {self.book_cover}")
    
    def print_paper(self):
        print(f"type of the paper of the book is {self.book_paper}")

class Novel_Book(Book):
    def __init__(self,name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,type_of_novel,summary,translator=None):
        super().__init__(name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,translator=None)
        self.subject = "Novel"
        self.type_of_novel = type_of_novel
        self.summary = summary
        
    def about(self):
        print(f"This is a novel book and the type of the novel is {self.type_of_novel}")
    
    def Summary(self):
        print("the summary of the book is :")
        print(self.summary)

class Poem_Book(Book):
    def __init__(self,name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,type_of_poem,translator=None):
        super().__init__(name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,translator=None)
        self.subject = "Poem"
        self.type_of_poem = type_of_poem
    def about(self):
        print(f"this is a poem book and the type of the poems is {self.type_of_poem}")

class History_Book(Book):
    def __init__(self,name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,start,end,translator=None):
        super().__init__(name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,translator=None)
        self.subject = "History"
        self.starting_date = start
        self.ending_date = end
    
    def about(self):
        print(f"This is a History book and it is about {self.starting_date} to {self.ending_date}")
        
class Science_Book(Book):
    def __init__(self,name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,major,translator=None):
        super().__init__(name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,translator=None)
        self.subject = "science"
        self.major = major
    
    def about(self):
        print(f"This is a science book and its major is {self.major}")

class Text_Book(Book):
    def __init__(self,name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,lesson,grade,translator=None):
        super().__init__(name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,translator=None)
        self.subject = "text book"
        self.lesson = lesson
        self.grade = grade
    
    def about(self):
        print(f"This is a textbook about {self.lesson} for grade {self.grade}")

class Politics_Book(Book):
    def __init__(self,name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,country,translator=None):
        super().__init__(name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,translator=None)
        self.subject = "politic"
        self.country =  country
    
    def about(self):
        print("This is a politics book about the country {self.country} ")

class Economics_Book(Book):
    def __init__(self,name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,country,translator=None):
        super().__init__(name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,translator=None)
        self.subject = "economics"
        self.country = country
    
    def about(self):
        print("This is a economics book about country {self.country}")
    
class Biography_Book(Book):
    def __init__(self,name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,person,translator=None):
        super().__init__(name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,translator=None) 
        self.subject = "Biography"
        self.person = person
    
    def about(self):
        print("This is a biography about {self.person}")
        
class Psychology_Book(Book):
    def __init__(self,name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,is_yellow,translator=None):  
        super().__init__(name,author,No_of_pages,weight,paper_type,book_size,book_cover,pub_name,address,phone,email,ISNB,is_yellow,translator=None)
        self.subject = "Psychology"
        self.is_yellow = is_yellow
    def about(self):
        print("This is a psychology book and the answer of is this a yellow book is {self.is_yellow}")