''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
from memo___app import app 

class Question():
    def __init__ (self,question,right_asnw,wrong_answ1,wrong_answ2,wrong_answ3):
        self.question = question
        self.right_asnw = right_asnw
        self.wrong1 = wrong_answ1
        self.wrong2 = wrong_answ2
        self.wrong3 = wrong_answ3
        self.attems = 0
        self.correct = 0

    def got_right(self):
        print('Це правильна відповідь!')
        self.attems += 1
        self.correct += 1

    def got_wrong(self):
        print('Відповіть невірна')
        self.attems += 1
Q1 = Question('Яблуко','apple','orange','cucumber','banana')
Q2 = Question('Стол','table','chair','mouse','rug')
Q3 = Question('Рука','hand','leg','cheese','cream')


# віджети, які треба буде розмістити:
menu = QPushButton('Меню') #line1 H
relax = QPushButton('Відпочити') #line1 H
relax_time = QSpinBox() #line1 H
relax_time.setValue(30) #line1 H
minute = QLabel('хвилин') #line1 H


question = QLabel('?') #line 2 H
ok = QPushButton('Відповісти') # line6 H


groupbox = QGroupBox('Варіанти відповідей') # line 3 H
main_btn = QButtonGroup()

rbtn1 = QRadioButton('*') #groupbox_layout1 true
rbtn2 = QRadioButton('*') #groupbox_layout1 false
rbtn3 = QRadioButton('*') #groupbox_layout2 false
rbtn4 = QRadioButton('*') #groupbox_layout2 false

main_btn.addButton(rbtn1)
main_btn.addButton(rbtn2)
main_btn.addButton(rbtn3)
main_btn.addButton(rbtn4)

radio_btn = [rbtn1,rbtn2,rbtn3,rbtn4]



# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів

# Опиши панень з результатами
group_panel = QGroupBox('Результат теста')
lb_answ = QLabel('*')
lb_true = QLabel('**')
group_main = QVBoxLayout()

group_main.addWidget(lb_answ, alignment=(Qt.AlignLeft | Qt.AlignTop))
group_main.addWidget(lb_true, alignment= Qt.AlignCenter)
group_panel.setLayout(group_main)

group_panel.hide()


# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card
layout_card = QVBoxLayout()
Hline1 = QHBoxLayout()
Hline2 = QHBoxLayout()
Hline3 = QHBoxLayout()
Hline4 = QHBoxLayout()

groupbox_all = QHBoxLayout()
groupbox_layout1 = QVBoxLayout()
groupbox_layout2 = QVBoxLayout()

groupbox_layout1.addWidget(rbtn1)
groupbox_layout1.addWidget(rbtn2)
groupbox_layout2.addWidget(rbtn3)
groupbox_layout2.addWidget(rbtn4)

groupbox_all.addLayout(groupbox_layout1)
groupbox_all.addLayout(groupbox_layout2)

groupbox.setLayout(groupbox_all)

Hline1.addWidget(menu, alignment=Qt.AlignLeft)
Hline1.addStretch()
Hline1.addWidget(relax, alignment=Qt.AlignRight)
Hline1.addWidget(relax_time, alignment=Qt.AlignRight)
Hline1.addWidget(minute, alignment=Qt.AlignRight)

Hline2.addWidget(question, alignment=Qt.AlignCenter)

Hline3.addWidget(groupbox)
Hline3.addWidget(group_panel)

Hline4.addWidget(ok,alignment=Qt.AlignCenter)


layout_card.addLayout(Hline1)
layout_card.addLayout(Hline2)
layout_card.addLayout(Hline3)
layout_card.addLayout(Hline4)



# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    groupbox.hide()
    group_panel.show()
    ok.setText('Наступне питання')


def show_question():
    ''' показати панель запитань '''
    group_panel.hide()
    groupbox.show()
    ok.setText('Відповісти')
    main_btn.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    main_btn.setExclusive(True)

    
    
