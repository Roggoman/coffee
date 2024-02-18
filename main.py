import sqlite3
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication

def display_coffee_info():
    # Подключение к базе данных
    conn = sqlite3.connect('coffee.sqlite')
    cursor = conn.cursor()

    # Получение данных о кофе из базы данных
    cursor.execute("SELECT * FROM coffee")
    coffee_data = cursor.fetchall()

    # Вывод информации о кофе
    for coffee in coffee_data:
        print("ID:", coffee[0])
        print("Название сорта:", coffee[1])
        print("Степень обжарки:", coffee[2])
        print("Молотый/в зернах:", coffee[3])
        print("Описание вкуса:", coffee[4])
        print("Цена:", coffee[5])
        print("Объем упаковки:", coffee[6])
        print()

    # Закрытие соединения с базой данных
    conn.close()


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        view = QTableView(self)
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)
        self.setGeometry(300, 100, 650, 450)
        self.setWindowTitle('Пример работы с QtSql')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())