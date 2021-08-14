# -*- coding: utf-8 -*-
class BookItem:
    reserved_book_items = []
    
    @classmethod
    def addReservedBooks(cls, book):
        cls.reserved_book_items.append(book)
    
    def __init__(self,book,isbn,rack):
        self.book = book
        self.isbn = isbn
        self.rack = rack
        self.info = {}
        
    def updateIssuerInfo(self, name, student_id, days):
        self.info["Name"] = name
        self.info["Student ID"] = student_id
        self.info["Days"] = days
        
    def addToReservedList(self):
        BookItem.addReservedBooks(self)
        
    def removeFromReservedList(self):
        BookItem.reserved_book_items.remove(self)
        
    def clearIssuerInfo(self):
        self.info.clear()

    def extendDates(self, ext_days):
        if self.info["Days"] + ext_days <= 10:
            self.info["Days"] = self.info["Days"] + ext_days
            print("{} days extended successfully for {}".format(ext_days, self.isbn))
        else:
            print("Days cannot be extended over allowed maximum days.")