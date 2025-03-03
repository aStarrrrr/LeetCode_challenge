class Bank:
    def __init__(self, accn, acch):
        self.__accn = accn
        self.__acch = acch

    def display(self):
        print(self.__accn,self.__acch)
b1 = Bank(1234,'Abhinand')
# b1.acch = 'Kaattu'
# print(b1.acch)
b1.display()