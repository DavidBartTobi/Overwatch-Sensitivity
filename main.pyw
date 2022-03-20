from tkinter import *
from PIL import ImageTk,Image
from hero_ui import Hero_ui
from tkinter import messagebox


def main():
    def center_window(win):
        win.update_idletasks()

        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        size = tuple(int(_) for _ in win.geometry().split('+')[0].split('x'))
        x = screen_width / 2 - size[0] / 2
        y = screen_height / 2 - size[1] / 2

        return x, y

    root = Tk()
    root.title("Overwatch Sensitivity")
    root.geometry("1140x909")
    root.resizable(width=False, height=False)
    w, h = center_window(root)
    root.geometry("+%d+%d" % (w, h-35))

    image = Image.open('icons/logo.png')
    image.thumbnail((300, 400))
    resized_image = ImageTk.PhotoImage(image)
    img_label = Label(root, image=resized_image, bg='black')
    img_label.grid(row=0,column=0, columnspan=8, sticky=W+N+E+S)

    lbl = Label(root, bg='black')
    lbl.grid(row=1, column=0, rowspan=18, columnspan=8, sticky=W+N+E+S)

    def reset():
        confirmation = messagebox.askyesno("Confirmation", "Are you sure?")
        if confirmation:
            group1.reset_fields()
            group2.reset_fields()
            group3.reset_fields()
            group4.reset_fields()

    reset_button = Button(root, text='Reset All', command= reset, bg='#F9B551')
    reset_button.grid(row=18, column=0, columnspan=8, pady=(0, 15))

    group1 = Hero_ui(root, "Ana", "Ashe", "Baptiste", "Bastion", "Brigitte", "D.Va", "Doomfist", "Echo", column=0, hero_id=1)
    group2 = Hero_ui(root, "Genji", "Hanzo", "Junkrat", "Lucio", "McCree", "Mei", "Mercy", "Moira", column=2, hero_id=9)
    group3 = Hero_ui(root, "Orisa", "Pharah", "Reaper", "Reinhardt", "Roadhog", "Sigma", "Soldier_76", "Sombra", column=4,
            hero_id=17)
    group4 = Hero_ui(root, "Symmetra", "Torbjorn", "Tracer", "Widowmaker", "Winston", "Wrecking_Ball", "Zarya", "Zenyatta", column=6,
            hero_id=25)

    root.mainloop()


if __name__ == '__main__':
    main()
