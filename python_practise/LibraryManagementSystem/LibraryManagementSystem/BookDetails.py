

class BookDetails:

    def __init__(self,book,isbn,rack):
        self.book= book
        self.isbn= isbn
        self.rack=rack
        self.info= {}

    def updateIssuerInfo(self,name,studentId,days):
        self.info["name"]=name
        self.info["Student Id"]= studentId
        self.info["days"]= days
        return self.info

    def get_info(self):
        return self.info
book_details =BookDetails('start with why','1234544344','5')
book_details2 =BookDetails('start with why','1234544344','5')


print(book_details.book)
print(book_details.updateIssuerInfo('shivam','shivam@gmail.com',3))
print(book_details2.updateIssuerInfo('nandu','nandu@gmail.com',7))
print("book details are as follows",book_details2.get_info())





