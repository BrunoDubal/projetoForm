import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

df = pd.read_excel('question.xlsx')
questions = df.sample(n=10).values.tolist()

score = 0
current_question = 0


def check_answer(answer):
    global score, current_question
    if answer == correct_answer.get():
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
    else:
        show_results()


def display_question():
    question, option1, option2, option3, option4, option5, answer = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: check_answer(4))
    option5_btn.config(text=option5, state=tk.NORMAL, command=lambda: check_answer(5))

    correct_answer.set(answer)


def show_results():
    messagebox.showinfo('Quiz finalizado', f"Parabens! Voce completou o quiz: \n\nPontuação final:{score}/{len(questions)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)
    option4_btn.config(state=tk.DISABLED)
    option5_btn.config(state=tk.DISABLED)
    option1_btn.pack_forget()
    option2_btn.pack_forget()
    option3_btn.pack_forget()
    option4_btn.pack_forget()
    option5_btn.pack_forget()
    app_label.pack_forget()
    question_label.pack_forget()
    label1 = tk.Label(janela, text='Deixe-nos saber um pouco mais sobre você:')
    label1.pack(padx=10, pady=10)

    listopt1 = ["JÁ PASSEI POR UM PROCESSO DE PATENTE", "QUERO PATENTEAR", "SOU APENAS CURIOSO"]

    cb_list1 = ttk.Combobox(janela, values=listopt1, width=60)
    cb_list1.set('Por favor, nos informe quais das opções abaixo mais se identifica com você:')
    cb_list1.pack(padx=10, pady=10)

    placeholder = 'Nome'

    def erase(event=None):
        if name.get() == placeholder:
            name.delete(0, 'end')

    def add(event=None):
        if name.get() == '':
            name.insert(0, placeholder)

    name = tk.Entry(janela, width=62)
    name.pack(padx=10, pady=10)

    add()
    name.bind('<FocusIn>', erase)
    name.bind('<FocusOut>', add)

    placeholder2 = 'E-mail'

    def erase2(event=None):
        if email.get() == placeholder2:
            email.delete(0, 'end')

    def add2(event=None):
        if email.get() == '':
            email.insert(0, placeholder2)

    email = tk.Entry(janela, width=62)
    email.pack(padx=10, pady=10)

    add2()
    email.bind('<FocusIn>', erase2)
    email.bind('<FocusOut>', add2)

    states = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']

    cb_states = ttk.Combobox(janela, values=states, width=60)
    cb_states.set('Por favor, informe sua região:')
    cb_states.pack(padx=10, pady=10)

    escolaridade = ['Ensino fundamental incompleto', 'Ensino fundamental completo', 'Ensino médio incompleto', 'Ensino médio completo', 'Ensino superior incompleto / cursando', 'Ensino superior completo', 'Mestrado/Doutorado']

    cb_escolaridade = ttk.Combobox(janela, values=escolaridade, width=60)
    cb_escolaridade.set('Por favor, nos informe seu grau de instrução:')
    cb_escolaridade.pack(padx=10, pady=10)

background_color = '#ECECEC'
text_color = '#333333'
button_color = '#4CAF50'
button_text_color = '#FFFFFF'

janela = tk.Tk()
janela.title('Quiz')
janela.geometry("900x600+450+100")

janela.config(bg=background_color)
janela.option_add('*Font', 'Arial')

app_icon = PhotoImage(file='icone.png')
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

question_label = tk.Label(janela, text='Pergunta', wraplength=380, bg=background_color, fg=text_color, font=('Arial', 12, 'bold'))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

option1_btn = tk.Button(janela, wraplength=400, width=50, state=tk.DISABLED,)
option1_btn.pack(pady=5)

option2_btn = tk.Button(janela, wraplength=400, width=50, state=tk.DISABLED)
option2_btn.pack(pady=5)

option3_btn = tk.Button(janela, wraplength=400, width=50, state=tk.DISABLED)
option3_btn.pack(pady=5)

option4_btn = tk.Button(janela, wraplength=400, width=50, state=tk.DISABLED)
option4_btn.pack(pady=5)

option5_btn = tk.Button(janela, wraplength=400, width=50, state=tk.DISABLED)
option5_btn.pack(pady=5)


display_question()
janela.mainloop()