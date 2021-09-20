import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    '''Открывает окно для  редактирования'''
    filepath = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if not filepath:
        return
    txt_ebit.delete('1.0', tk.END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        txt_ebit.insert(tk.END, text)
    window.title(f'Simple Text Ebitor - {filepath}')

def save_file():
    '''Сохраняет текущий файл как новый файл'''
    filepath = asksaveasfilename(
        defaultextension='text',
        filetypes=[('Текстовые файлы', '*.txt'), ('Все файлы', '*.*')]
        )
    if not filepath:
        return
    with open(filepath, 'w') as output_file:
        text = txt_ebit.get('1.0', tk.END)
        output_file.write(text)
    window.title(f'Простой текстовыйредактор - {filepath}')



window =  tk.Tk()
window.title('Простой текстовый редактор')

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_ebit = tk.Text(window)
fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text='Открыть', command=open_file)
btn_save = tk.Button(fr_buttons, text='Сохранить как...', command=save_file)

btn_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky='ew', padx=5)

fr_buttons.grid(row=0, column=0, sticky='ns')
txt_ebit.grid(row=0, column=1, sticky='nsew')

window.mainloop()