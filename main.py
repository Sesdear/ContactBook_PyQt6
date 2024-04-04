import sys
from PyQt6.QtWidgets import QFrame, QApplication
from assets.gui import Ui_Frame
import sqlite3
class ContactBook(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Frame()
        self.ui.setupUi(self)

        self.ui.buttonDelete.clicked.connect(self.buttonDelete)
        self.ui.buttonAdd.clicked.connect(self.buttonAdd)

        self.ui.buttonShow.clicked.connect(self.buttonShow)


        self.conn = sqlite3.connect('notes.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                            name TEXT,
                            phone_number TEXT
                        )''')
        self.conn.commit()
        self.load_contacts()
        self.show()
    def load_contacts(self):
        self.ui.contactList.clear()
        self.cursor.execute('''SELECT name FROM contacts''')
        contacts = self.cursor.fetchall()
        for contact in contacts:
            name = contact[0]
            self.ui.contactList.addItem(name)

    def buttonAdd(self):
        new_contact_name = self.ui.NameEntry.text()
        new_contact_num = self.ui.NumberEntry.text()
        self.cursor.execute('INSERT INTO contacts (name, phone_number) VALUES (?, ?)', (new_contact_name, new_contact_num))
        self.conn.commit()
        self.ui.contactList.addItem(new_contact_name)

    def buttonDelete(self):
        selected_item = self.ui.contactList.currentItem()
        if selected_item:
            contact_name = selected_item.text()
            self.cursor.execute('DELETE FROM contacts WHERE name = ?', (contact_name,))
            self.conn.commit()
            self.ui.contactList.takeItem(self.ui.contactList.currentRow())

    def buttonShow(self):
        selected_item = self.ui.contactList.currentItem()
        if selected_item:
            contact_name = selected_item.text()
            self.cursor.execute('SELECT phone_number FROM contacts WHERE name = ?', (contact_name,))
            result = self.cursor.fetchone()
            self.ui.showLabelName.setText(contact_name)
            if result:
                phone_number = result[0]
                self.ui.showLabelNumber.setText(phone_number)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactBook()
    sys.exit(app.exec())