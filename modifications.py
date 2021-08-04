import sqlite3
from tkinter import messagebox


def Hero_Modify(sens,id):

    is_number = False

    if not sens.isnumeric():
        try:
            float(sens)
            is_number = True
        except:
            messagebox.showerror("Error", f"Please enter a number")

    else:
        is_number = True

    if is_number:
        conn = sqlite3.connect('OWsenseDB.db')
        c = conn.cursor()

        c.execute(("UPDATE Sensitivity SET sensitivity=? WHERE hero_id=?"), (sens,id))

        conn.commit()
        conn.close()

def Get_Sensitivity(id):
    conn = sqlite3.connect('OWsenseDB.db')
    c = conn.cursor()

    get_sens = c.execute(("SELECT sensitivity FROM Sensitivity WHERE hero_id=?"), (id,))
    sens = get_sens.fetchone()[0]

    conn.commit()
    conn.close()

    return sens

