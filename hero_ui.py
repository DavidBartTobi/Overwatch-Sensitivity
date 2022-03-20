from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import modifications


class Hero_ui:

    def __init__(self, root, h1, h2, h3, h4, h5, h6, h7 ,h8, column, hero_id):

        self.root = root
        self.hero_id = hero_id

        try:

            self.image = Image.open(f'icons/Icon-{h1}.png')
            self.image.thumbnail((60, 60))
            self.resized_image1 = ImageTk.PhotoImage(self.image)
            self.h1_img_label = Label(self.root, image=self.resized_image1, bg='black')
            self.h1_img_label.image = self.resized_image1
            self.h1_img_label.grid(row=2, column=column, padx=20, pady=10, rowspan=2)

            self.image2 = Image.open(f'icons/Icon-{h2}.png')
            self.image2.thumbnail((60, 60))
            self.resized_image2 = ImageTk.PhotoImage(self.image2)
            self.h2_img_label = Label(self.root, image=self.resized_image2, bg='black')
            self.h2_img_label.image2 = self.resized_image2
            self.h2_img_label.grid(row=4, column=column, padx=20, pady=10, rowspan=2)

            self.image3 = Image.open(f'icons/Icon-{h3}.png')
            self.image3.thumbnail((60, 60))
            self.resized_image3 = ImageTk.PhotoImage(self.image3)
            self.h3_img_label = Label(self.root, image=self.resized_image3, bg='black')
            self.h3_img_label.image3 = self.resized_image3
            self.h3_img_label.grid(row=6, column=column, padx=20, pady=10, rowspan=2)

            self.image4 = Image.open(f'icons/Icon-{h4}.png')
            self.image4.thumbnail((60, 60))
            self.resized_image4 = ImageTk.PhotoImage(self.image4)
            self.h4_img_label = Label(self.root, image=self.resized_image4, bg='black')
            self.h4_img_label.image4 = self.resized_image4
            self.h4_img_label.grid(row=8, column=column, padx=20, pady=10, rowspan=2)

            self.image5 = Image.open(f'icons/Icon-{h5}.png')
            self.image5.thumbnail((60, 60))
            self.resized_image5 = ImageTk.PhotoImage(self.image5)
            self.h5_img_label = Label(self.root, image=self.resized_image5, bg='black')
            self.h5_img_label.image5 = self.resized_image5
            self.h5_img_label.grid(row=10, column=column, padx=20, pady=10, rowspan=2)

            self.image6 = Image.open(f'icons/Icon-{h6}.png')
            self.image6.thumbnail((60, 60))
            self.resized_image6 = ImageTk.PhotoImage(self.image6)
            self.h6_img_label = Label(self.root, image=self.resized_image6, bg='black')
            self.h6_img_label.image6 = self.resized_image6
            self.h6_img_label.grid(row=12, column=column, padx=20, pady=10, rowspan=2)

            self.image7 = Image.open(f'icons/Icon-{h7}.png')
            self.image7.thumbnail((60, 60))
            self.resized_image7 = ImageTk.PhotoImage(self.image7)
            self.h7_img_label = Label(self.root, image=self.resized_image7, bg='black')
            self.h7_img_label.image7 = self.resized_image7
            self.h7_img_label.grid(row=14, column=column, padx=20, pady=10, rowspan=2)

            self.image8 = Image.open(f'icons/Icon-{h8}.png')
            self.image8.thumbnail((60, 60))
            self.resized_image8 = ImageTk.PhotoImage(self.image8)
            self.h8_img_label = Label(self.root, image=self.resized_image8, bg='black')
            self.h8_img_label.image8 = self.resized_image8
            self.h8_img_label.grid(row=16, column=column, padx=20, pady=(10, 25), rowspan=2)

        except:
            messagebox.showerror("Error", f"Error loading icons from library")


        entry_bg = '#8A8885'
        fg = '#f89d19'
        font = 'Calibari 12 bold'

        self.h1_entry = Entry(self.root, width=13, bg=entry_bg, fg=fg, font=font, justify=CENTER)
        self.h1_entry.grid(row=2, column=column+1, padx=30, pady=(10, 0))
        self.h1_entry.insert(0, modifications.get_sensitivity(self.hero_id))
        self.hero_id += 1

        self.h2_entry = Entry(self.root, width=13, bg=entry_bg, fg=fg, font=font, justify=CENTER)
        self.h2_entry.grid(row=4, column=column+1, padx=30, pady=(10, 0))
        self.h2_entry.insert(0, modifications.get_sensitivity(self.hero_id))
        self.hero_id += 1

        self.h3_entry = Entry(self.root, width=13, bg=entry_bg, fg=fg, font=font, justify=CENTER)
        self.h3_entry.grid(row=6, column=column+1, padx=30, pady=(10, 0))
        self.h3_entry.insert(0, modifications.get_sensitivity(self.hero_id))
        self.hero_id += 1

        self.h4_entry = Entry(self.root, width=13, bg=entry_bg, fg=fg, font=font, justify=CENTER)
        self.h4_entry.grid(row=8, column=column+1, padx=30, pady=(10, 0))
        self.h4_entry.insert(0, modifications.get_sensitivity(self.hero_id))
        self.hero_id += 1

        self.h5_entry = Entry(self.root, width=13, bg=entry_bg, fg=fg, font=font, justify=CENTER)
        self.h5_entry.grid(row=10, column=column+1, padx=30, pady=(10, 0))
        self.h5_entry.insert(0, modifications.get_sensitivity(self.hero_id))
        self.hero_id += 1

        self.h6_entry = Entry(self.root, width=13, bg=entry_bg, fg=fg, font=font, justify=CENTER)
        self.h6_entry.grid(row=12, column=column+1, padx=30, pady=(10, 0))
        self.h6_entry.insert(0, modifications.get_sensitivity(self.hero_id))
        self.hero_id += 1

        self.h7_entry = Entry(self.root, width=13, bg=entry_bg, fg=fg, font=font, justify=CENTER)
        self.h7_entry.grid(row=14, column=column+1, padx=30, pady=(10, 0))
        self.h7_entry.insert(0, modifications.get_sensitivity(self.hero_id))
        self.hero_id += 1

        self.h8_entry = Entry(self.root, width=13, bg=entry_bg, fg=fg, font=font, justify=CENTER)
        self.h8_entry.grid(row=16, column=column+1, padx=30, pady=(10, 0))
        self.h8_entry.insert(0, modifications.get_sensitivity(self.hero_id))

        
        button_bg = '#F9B551'
        
        h1_button = Button(self.root, text='Modify', command=lambda: modifications.hero_modify(self.h1_entry.get(), self.hero_id-7),
                           bg=button_bg)
        h1_button.grid(row=3, column=column+1, pady=(0, 10))

        h2_button = Button(self.root, text='Modify', command=lambda: modifications.hero_modify(self.h2_entry.get(), self.hero_id-6),
                           bg=button_bg)
        h2_button.grid(row=5, column=column+1, pady=(0, 10))

        h3_button = Button(self.root, text='Modify', command=lambda: modifications.hero_modify(self.h3_entry.get(), self.hero_id-5),
                                 bg=button_bg)
        h3_button.grid(row=7, column=column+1, pady=(0, 10))

        h4_button = Button(self.root, text='Modify', command=lambda: modifications.hero_modify(self.h4_entry.get(), self.hero_id-4),
                                bg=button_bg)
        h4_button.grid(row=9, column=column+1, pady=(0, 10))

        h5_button = Button(self.root, text='Modify', command=lambda: modifications.hero_modify(self.h5_entry.get(), self.hero_id-3),
                                 bg=button_bg)
        h5_button.grid(row=11, column=column+1, pady=(0, 10))

        h6_button = Button(self.root, text='Modify', command=lambda: modifications.hero_modify(self.h6_entry.get(), self.hero_id-2),
                           bg=button_bg)
        h6_button.grid(row=13, column=column+1, pady=(0, 10))

        h7_button = Button(self.root, text='Modify', command=lambda: modifications.hero_modify(self.h7_entry.get(), self.hero_id-1),
                                 bg=button_bg)
        h7_button.grid(row=15, column=column+1, pady=(0, 10))

        h8_button = Button(self.root, text='Modify', command=lambda: modifications.hero_modify(self.h8_entry.get(), self.hero_id),
                           bg=button_bg)
        h8_button.grid(row=17, column=column+1, pady=(0, 25))


    def reset_fields(self):

        self.h1_entry.delete(0, "end")
        self.h2_entry.delete(0, "end")
        self.h3_entry.delete(0, "end")
        self.h4_entry.delete(0, "end")
        self.h5_entry.delete(0, "end")
        self.h6_entry.delete(0, "end")
        self.h7_entry.delete(0, "end")
        self.h8_entry.delete(0, "end")

        self.h1_entry.insert(0, 0)
        self.h2_entry.insert(0, 0)
        self.h3_entry.insert(0, 0)
        self.h4_entry.insert(0, 0)
        self.h5_entry.insert(0, 0)
        self.h6_entry.insert(0, 0)
        self.h7_entry.insert(0, 0)
        self.h8_entry.insert(0, 0)

        modifications.hero_modify(self.h1_entry.get(), self.hero_id - 7)
        modifications.hero_modify(self.h2_entry.get(), self.hero_id - 6)
        modifications.hero_modify(self.h3_entry.get(), self.hero_id - 5)
        modifications.hero_modify(self.h4_entry.get(), self.hero_id - 4)
        modifications.hero_modify(self.h5_entry.get(), self.hero_id - 3)
        modifications.hero_modify(self.h6_entry.get(), self.hero_id - 2)
        modifications.hero_modify(self.h7_entry.get(), self.hero_id - 1)
        modifications.hero_modify(self.h8_entry.get(), self.hero_id)
