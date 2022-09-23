import tkinter as tk
import random as rnd

point = 0
kon = 13

def click_yes():
    global point, kon
    point += kon
    kon = rnd.randint(1, 13)
    lbl_point.config(text = str(point))
    lbl_card.config(text = str(kon))
    if point == 21:
        lbl_win = tk.Label(text="ПОБЕДА!", font=("Aria", "50"), bg="#FF0000")
        lbl_win.place(x=180, y=350)   
    if point > 21:
        lbl_win = tk.Label(text="ПРОИГРАЛ!", font=("Aria", "50"), bg="#FF0000")
        lbl_win.place(x=180, y=350)       
    
    
def click_no():
    global point, kon
    kon = rnd.randint(1, 13)
    lbl_card.config(text = str(kon))
    
win = tk.Tk()
win.geometry("800x500")
win.title("Очко или BlackJeck")

btn_yes = tk.Button(text="беру", font=("Aria", "30"), bg="#0000FF", command=click_yes)
btn_yes.place(x=50, y=100, width=230, height=130, )


btn_no = tk.Button(text="НЕ беру", font=("Aria", "30"), bg="#00FF00", command = click_no)
btn_no.place(x=500, y=100, width=230, height=130)


lbl_card_label = tk.Label(text="Выпала карта", font=("Aria", "20"), bg="#EEEEEE")
lbl_card_label.place(x=300, y=10)
lbl_point_label = tk.Label(text="Набранно очков", font=("Aria", "20"), bg="#EEEEEE")
lbl_point_label.place(x=300, y=230)

lbl_point = tk.Label(text="0", font=("Aria", "50"))
lbl_point.place(x=350, y=270)
lbl_card = tk.Label(text="13", font=("Aria", "50"))
lbl_card.place(x=350, y=50)

win.mainloop()