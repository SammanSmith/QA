from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
from string import ascii_lowercase, digits, ascii_uppercase, punctuation
from pyperclip import copy

bg_color = '#03406A'
fg_color = '#FF9000'
btn_color = '#64AAD0'
btn_color2 = '#FFBF73'

window = Tk()
window.title('Password Generator')
window_width = 450
window_height = 410
center_x = int(window.winfo_screenwidth() / 2 - window_width / 2)
center_y = int(window.winfo_screenheight() / 2 - window_height / 2)
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
window.resizable(False, False)
window['padx'] = 10
window['pady'] = 10
window['bg'] = bg_color

LEN_PASS = IntVar()
CHAR = [IntVar(), IntVar(), IntVar(), IntVar()]
for i in range(4):
    CHAR[i].set(1)

window.iconbitmap(r'E:\_python\Профессионал\Проекты\Генератор паролей\icons\password.ico')
copy_icon = PhotoImage(file=r'E:\_python\Профессионал\Проекты\Генератор паролей\img\copy.png')
clear_icon = PhotoImage(file=r'E:\_python\Профессионал\Проекты\Генератор паролей\img\clean.png')

# ------------------------------------ LOGIC ------------------------------------------------
def copy_pass():
    if display_pass['text'] != '*' * 20:
        copy(display_pass['text'])


def gen_pass():
    password = []
    list_chars = [ascii_uppercase, ascii_lowercase, digits, punctuation]
    chars = []

    for i in range(4):
        if CHAR[i].get() == 1:
            chars.append(list_chars[i])

    if not chars:
        messagebox.showinfo('Внимание', 'Нельзя из воздуха составить пароль...\n'
                                        'Нужно выбрать хотя бы одну группу символов', icon='warning')
    else:
        for i in range(LEN_PASS.get()):
            if i < len(chars):
                password.append(choice(chars[i]))
            else:
                password.append(choice(chars[randint(0, len(chars) - 1)]))
        shuffle(password)
        display_pass['text'] = ''.join(password)


def clear_all():
    display_pass['text'] = '*' * 20
    len_pass.set(8)
    copy('')
    for i in range(4):
        CHAR[i].set(1)


# ------------------------------- DESIGN -----------------------------------------------
lbl_name = Label(window, text='PASSWORD', font=('Arial', 16, 'bold'), bg=bg_color, fg=fg_color)
display_pass = Label(window, text='*' * 20, width=28, relief=SUNKEN, height=2,
                     font=('Arial', 16, 'bold'), bd=3, fg=fg_color)
copy_btn = Button(window, text='Copy', font=('Arial', 12, 'bold'),
                  command=copy_pass, image=copy_icon, width=50, bg=btn_color2)
len_pass = Scale(window, orient=HORIZONTAL, length=200, from_=8, to=30, font=('Arial', 16, 'bold'),
                 variable=LEN_PASS, bg=bg_color, bd=1, troughcolor='SkyBlue', highlightthickness=0,
                 fg=fg_color)

frame_change = LabelFrame(window, text='CHARACTERS IN PASSWORD', padx=25, pady=15,
                          borderwidth=5, font=('Arial', 12, 'bold'), bg=bg_color, fg=fg_color)
check_ul = Checkbutton(frame_change, text='A - Z', font=('Arial', 14, 'bold'),
                       variable=CHAR[0], offvalue=0, onvalue=1, bg=bg_color, fg=fg_color,
                       activebackground=bg_color, selectcolor='Black')
check_ll = Checkbutton(frame_change, text='a - z', font=('Arial', 14, 'bold'),
                       variable=CHAR[1], offvalue=0, onvalue=1, bg=bg_color, fg=fg_color,
                       activebackground=bg_color, selectcolor='Black')
check_d = Checkbutton(frame_change, text='0 - 9', font=('Arial', 14, 'bold'),
                      variable=CHAR[2], offvalue=0, onvalue=1, bg=bg_color, fg=fg_color,
                      activebackground=bg_color, selectcolor='Black')
check_sc = Checkbutton(frame_change, text='! @ # [ { (', font=('Arial', 14, 'bold'),
                       variable=CHAR[3], offvalue=0, onvalue=1, bg=bg_color, fg=fg_color,
                       activebackground=bg_color, selectcolor='Black')

generate_pass = Button(window, text='GENERATE', height=2, font=('Arial', 16, 'bold'),
                       command=gen_pass, bg=btn_color, fg='#A65A00')
clear = Button(window, text='Clear', font=('Arial', 12, 'bold'), command=clear_all,
               image=clear_icon, bg=btn_color2)

# ------------------------ GRID ----------------------
lbl_name.grid(row=0, column=0, pady=10)
display_pass.grid(row=1, column=0, sticky=NSEW)
copy_btn.grid(row=1, column=1, sticky=NSEW)
len_pass.grid(row=2, column=0, columnspan=2, sticky='EW')

frame_change.grid(row=3, column=0, columnspan=2, sticky=NSEW, ipady=5, pady=15)
check_ul.grid(row=0, column=0)
check_ll.grid(row=1, column=0)
check_d.grid(row=1, column=1, sticky='W', ipadx=80)
check_sc.grid(row=0, column=1, sticky='W', ipadx=80)

generate_pass.grid(row=4, column=0, sticky='NSEW')
clear.grid(row=4, column=1, sticky='NSEW')

if __name__ == '__main__':
    window.mainloop()
