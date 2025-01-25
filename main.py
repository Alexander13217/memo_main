from memo___card_layout import *
from PyQt5.QtWidgets import QWidget
from random import shuffle # будем перемешивать ответы в карточке вопроса


card_width, card_height = 600, 500 # начальные размеры окна "карточка"
questions = [Q1,Q2,Q3]
index = 0

def show_data():
    ''' показывает на экране нужную информацию '''
    pass


def check_result():
    ''' проверка, правильный ли ответ выбран
    если ответ был выбран, то надпись "верно/неверно" приобретает нужное значение
    и показывается панель ответов '''
    answ = Q1.right_asnw
    correct = False
    for answer in radio_btn:
        if answer.isChecked():
            if answer.text() == answ:
                lb_answ.setText('Правильно')
                correct = True
                show_result()
                
            
        elif correct == False:
            lb_answ.setText('Не правильно')
            show_result()

   

def set_card():
    win_card.resize(card_width,card_height)
    win_card.move(300,300)
    win_card.setWindowTitle('Memory Card')
    win_card.setLayout(layout_card)


def show():
    number_index = questions[index]
    question.setText(number_index.question)

    shuffle(radio_btn)
    radio_btn[0].setText(number_index.right_asnw)
    radio_btn[1].setText(number_index.wrong1)
    radio_btn[2].setText(number_index.wrong2)
    radio_btn[3].setText(number_index.wrong3)
    
def on_click():
    global index
    if ok.text() == 'Відповісти':
        check_result()       

    elif ok.text() == 'Наступне питання':
        index += 1

        if index >= len(questions):
            index = 0
            print(index)


        show_question() 
        show()
        



        
app = QApplication([])
win_card = QWidget()
#здесь должны быть параметры окна
show()
ok.clicked.connect(on_click)



set_card()
win_card.show()
app.exec_()

