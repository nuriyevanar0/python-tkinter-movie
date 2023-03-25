from tkinter import *
from PIL import ImageTk, Image

class MyApp:

    def __init__(self, root):
        root.resizable(False, False)
        root.title("Leflix")
        root.geometry("800x600")
        root.iconbitmap('logo.ico')


        label = Label(root)
        label.pack()

        global new_logo
        imglogo = Image.open("logo.png")
        new_logo = ImageTk.PhotoImage(imglogo)
        label2 = Label(root, image = new_logo)
        label2.place(x=500, y=100)

        soolehakkinda ='''
    Merhaba Sooleflix izleyicisi,

        Bu programda istedigin
        kategoride filmleri bula bilir
        ve kolaylikla izleyebilirsiniz.
        Sflix size iyi seyirler sunar.

    Sayinla Sooleflix Sirketi. '''

        text_box = Text(
            root,
            height=10,
            width=45
            )

        text_box.place(x=405, y=300)
        text_box.insert('end', soolehakkinda)
        text_box.config(state='disabled')

        #label["text"] = "New label text"
        #label["font"] = ("Courier", 40)

        label.configure(text="Sooleflix", font=("Courier", 20), bg="red", fg="white")

        button1 = Button(root, text="Bilim Kurgu filmleri", font=("Courier", 15), height= 2, width=20, command = bilimkurgu)
        button2 = Button(root, text="Komedi filmleri", font=("Courier", 15), height= 2, width=20, command = komedi)

        #button1.pack(side=BOTTOM, padx=5, pady=15)
        #button2.pack(side=BOTTOM, padx=5, pady=20)
        #button3.pack(side=BOTTOM, padx=5, pady=20)
        #button4.pack(side=BOTTOM, padx=5, pady=20)

        button1.place(x=30, y=200)
        button2.place(x=30, y=300)
        

def bilimkurgu():
    bilimkurgu = Toplevel()
    bilimkurgu.geometry("800x600")
    bilimkurgu.title("Bilim Kurgu Filmleri")
    bilimkurgu.iconbitmap('logo.ico')
    bilimkurguText1 = Label(bilimkurgu)
    bilimkurguText1.configure(text="Bilim Kurgu Film Kategorisi", font=("Courier", 20), bg="red", fg="white")
    bilimkurguText1.pack()

    #Interstellar Fotosu ve izle butonu
    imginterstellar = Image.open("interstellar_cover.jpg")
    res_interstellar = imginterstellar.resize((200,300))
    new_interstellar = ImageTk.PhotoImage(res_interstellar)
    label2 = Label(bilimkurgu, image = new_interstellar)
    label2.place(x=30, y=100)

    button_interstellar = Button(bilimkurgu, text="Izle", font=("Courier", 10), height= 2, width=20, command = interstellar)
    button_interstellar.place(x=45, y=415)

    #Inception Fotosu ve izle butonu
    imginception = Image.open("inception_cover.jpg")
    res_inception = imginception.resize((200,300))
    new_inception = ImageTk.PhotoImage(res_inception)
    label3 = Label(bilimkurgu, image = new_inception)
    label3.place(x=300, y=100)

    button_inception = Button(bilimkurgu, text="Izle", font=("Courier", 10), height= 2, width=20, command = inception)
    button_inception.place(x=315, y=415)

    #Matrix Fotosu ve izle butonu
    imgmatrix = Image.open("matrix_cover.jpg")
    res_matrix = imgmatrix.resize((200,300))
    new_matrix = ImageTk.PhotoImage(res_matrix)
    label4 = Label(bilimkurgu, image = new_matrix)
    label4.place(x=570, y=100)

    button_matrix = Button(bilimkurgu, text="Izle", font=("Courier", 10), height= 2, width=20, command = matrix)
    button_matrix.place(x=585, y=415)


    bilimkurgu.mainloop()


# The Dark Night izle
def interstellar():
    interstellar = Toplevel()
    interstellar.geometry("800x600")
    interstellar.title("Interstellar")
    interstellar.iconbitmap('logo.ico')

    l = Label(interstellar, text = "Interstellar IMDB RATING: 8.6")
    l.config(font =("Courier", 14))

    T = Text(interstellar, height = 40, width = 60)

    Fact = """
    Yıldızlararası (İngilizce: Interstellar), 
    Christopher Nolan tarafından yönetilen epik 
    bilimkurgu türündeki, 2014 yapımı ABD filmi. 
    Başrollerinde Matthew McConaughey, Anne Hathaway, 
    Jessica Chastain ve Michael Caine yer almaktadır. 
    Filmde bir grup astronotun bir solucan deliğinden 
    geçerek insanların yaşayabileceği yeni bir yer 
    arayışı konu edilmektedir.
    
    Konusu
    Yıldızlararası'nda, teknik bilgisi ve becerisi 
    yüksek olan Cooper, geniş mısır tarlalarında 
    çiftçilik yaparak geçinmektedir; amacı iki 
    çocuğuna güvenli bir hayat sunmaktır. 
    Onlarla yaşayan Büyükbaba Donald çocuklara 
    göz kulak olurken, henüz 10 yaşındaki kızı 
    Murph şaşırtıcı bir zekaya sahiptir. 
    Geçmişte bıraktığı biliminsanı kariyerini 
    özleyen Cooper'un karşısına bir gün beklenmedik 
    bir teklif çıkar ve ailesinin, dahası insanlığın 
    güvenliği için zorlu bir karar alması gerekir... 

    Christopher Nolan'ın, Jonathan Nolan ile kaleme 
    aldığı ve yönetmenliğini sırtladığı filmin 
    yıldız oyunculardan oluşan oyuncu kadrosunda 
    Matthew McConaughey, Anne Hathaway, Jessica Chastain, 
    Matt Damon, Bill Irwin, John Lithgow ve Michael 
    Caine gibi isimler yer alıyor. Bilimkurgunun yanı 
    sıra dramatik öğeler de içeren filmin senaryosu 
    Fizikçi Kip S. Thorne'nun evrendeki 
    'Solucan Delikleri' teorisinden ilham alıyor.
    """

    l.pack()
    T.pack(padx=5, pady=20)

    T.insert("end", Fact)



    interstellar.mainloop()

# Inception izle
def inception():
    inception = Toplevel()
    inception.geometry("800x600")
    inception.title("The Dark Night")
    inception.iconbitmap('logo.ico')
    inception = Label(inception)
    inception.configure(text="Inception", font=("Courier", 20), bg="red", fg="white")
    inception.pack()

    inception.mainloop()

# The Matrix Izle
def matrix():
    matrix = Toplevel()
    matrix.geometry("800x600")
    matrix.title("The Dark Night")
    matrix.iconbitmap('logo.ico')
    matrix = Label(matrix)
    matrix.configure(text="Matrix", font=("Courier", 20), bg="red", fg="white")
    matrix.pack()

    matrix.mainloop()

def komedi():
    komedi = Toplevel()
    komedi.geometry("800x600")
    komedi.title("Aksiyon Filmleri")
    komedi.iconbitmap('logo.ico')
    komediText1 = Label(komedi)
    komediText1.configure(text="Komedi Film Kategorisi", font=("Courier", 20), bg="red", fg="white")
    komediText1.pack()

    #Recep Ivedik 1 Fotosu ve izle butonu
    imgrecep_ivedik1 = Image.open("recep_ivedik1_cover.jpg")
    res_recep_ivedik1 = imgrecep_ivedik1.resize((200,300))
    new_recep_ivedik1 = ImageTk.PhotoImage(res_recep_ivedik1)
    label5 = Label(komedi, image = new_recep_ivedik1)
    label5.place(x=30, y=100)

    button_recep_ivedik1 = Button(komedi, text="Izle", font=("Courier", 10), height= 2, width=20)
    button_recep_ivedik1.place(x=45, y=415)

    #Recep Ivedik 2 Fotosu ve izle butonu
    imgrecep_ivedik2 = Image.open("recep_ivedik2_cover.jpg")
    res_recep_ivedik2 = imgrecep_ivedik2.resize((200,300))
    new_recep_ivedik2 = ImageTk.PhotoImage(res_recep_ivedik2)
    label6 = Label(komedi, image = new_recep_ivedik2)
    label6.place(x=300, y=100)

    button_recep_ivedik2 = Button(komedi, text="Izle", font=("Courier", 10), height= 2, width=20)
    button_recep_ivedik2.place(x=315, y=415)

    #Recep Ivedik 3 Fotosu ve izle butonu
    imgrecep_ivedik3 = Image.open("recep_ivedik3_cover.jpg")
    res_recep_ivedik3 = imgrecep_ivedik3.resize((200,300))
    new_recep_ivedik3 = ImageTk.PhotoImage(res_recep_ivedik3)
    label7 = Label(komedi, image = new_recep_ivedik3)
    label7.place(x=570, y=100)

    button_matrix = Button(komedi, text="Izle", font=("Courier", 10), height= 2, width=20)
    button_matrix.place(x=585, y=415)


    komedi.mainloop()


root = Tk()
MyApp(root)
root.mainloop()


        