# Fonksiyonumuzu oluşturduk ve Sonra değeri dışardan vermek için parantez içine değer koyduk
def tamBolenYazdirma(sayi):
    i =1
    # sayıları 1 den başlatmak için i ye 1 atadık
    while i<= sayi:
        # koşullu döndürme olan while`a ile 1 den girilecek sayi degerine kadar döndürmesini söyledik
        if (sayi%i==0):
            #if koşulu ile girilecek sayıyı i ye (i girilecek sayıya kadar artıyor) bölüp kalanı 0 olan sayıları
            # yazdırmasını istedik
            print(i),
            #burdada i yi yazdırıyo işte
        i = i+1

tamBolenYazdirma(24354)
#buraya da bahsettiğimiz dışarıdan değer verme olayını gerçekleştiriyoruz