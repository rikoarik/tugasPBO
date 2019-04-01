class pecahan():
    def __init__(self,pembilang,penyebut):
        self.pembilang=pembilang
        self.penyebut=penyebut
    def pecahansederhana(self):
        a=int(self.pembilang/self.penyebut)
        b=self.pembilang%self.penyebut
        if self.pembilang>self.penyebut:
            if b==0:
                print("Bentuk sederhana nya dalah = ",a)
            else:
                print("Bentuk sederhana nya Adalah = ",a,"",b,"/")
        else:
            aa=self.pembilang
            ab=self.penyebut

            if self.pembilang%self.penyebut==0:
                print("Bentuk sederhana nya Adalah = 1")
            else:
                while self.pembilang%self.penyebut!=0:
                      c=self.pembilang%self.penyebut
                      self.pembilang=self.penyebut
                      self.penyebut=c
                print("Bentuk sederhananya Adalah = ",(int(aa/c)),"/",(int(ab/c)))
tampil=pecahan(45,50)
tampil.pecahansederhana()
