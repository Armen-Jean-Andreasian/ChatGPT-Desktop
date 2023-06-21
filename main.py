from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QComboBox
from PyQt6.QtGui import QIcon

import sys
from backend import ChatBot
import threading


class ChatBotWindow(QMainWindow):
    def __init__(self):
        self._icon = 'chatbot-data.png'
        self._title = 'Chat with ChatGBT'
        super().__init__()

        # set window icon
        self.setWindowIcon(QIcon(self._icon))

        # Set the window title
        self.setWindowTitle(self._title)

        self.setMinimumSize(610, 400)

        # Set the style sheet for light mode
        self.set_light_mode()

        # Dropdown list for mode selection
        self.mode_dropdown = QComboBox(self)
        self.mode_dropdown.setGeometry(500, 10, 100, 30)
        self.mode_dropdown.addItem("Light Mode")
        self.mode_dropdown.addItem("Dark Mode")
        self.mode_dropdown.currentIndexChanged.connect(self.change_mode)

        # chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)  # 10 pixels from left border. 10 from top. 480:w, 320:h
        self.chat_area.setReadOnly(True)

        # input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)  # 10 pixels from left border. 340 from top. 480:w, 40:h
        self.input_field.setPlaceholderText("Type your message here")  # Placeholder text
        self.input_field.returnPressed.connect(self.send_message)  # turning on "Enter" key to send


        # button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)  # 500 pixels from left border. 10 from top. 480:w, 320:h
        self.button.clicked.connect(self.send_message)

        # chatbot instance
        self.chatbot = ChatBot()

        # show
        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        if len(user_input) > 0:
            # self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'> Me: {user_input}</p>")
            self.chat_area.append(f"<p>Me: {user_input}</p>")
            self.input_field.clear()

            # making second thread
            thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
            thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        # self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'> ChatGPT: {response}</p>")
        self.chat_area.append(f"<p>ChatGPT: {response}</p>")


    def change_mode(self, index):
        if index == 0:
            self.set_light_mode()
        elif index == 1:
            self.set_dark_mode()

    def set_light_mode(self):
        # Set the light mode style sheet
        style_sheet = """
            QMainWindow {
                background-color: #FFFFFF;
            }
            QLineEdit, QTextEdit {
                background-color: #FFFFFF;
                color: #000000;
            }
            QPushButton {
                background-color: #FFFFFF;
                color: #000000;
                border: 1px solid #000000;
            }
        """
        self.setStyleSheet(style_sheet)

    def set_dark_mode(self):
        # Set the dark mode style sheet
        style_sheet = """
            QMainWindow {
                background-color: #1B1B1B;
            }
            QLineEdit, QTextEdit {
                background-color: #1B1B1B;
                color: #FFFFFF;
            }
            QPushButton {
                background-color: #1B1B1B;
                color: #FFFFFF;
                border: 1px solid #FFFFFF;
            }
        """
        self.setStyleSheet(style_sheet)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ChatBotWindow()
    sys.exit(app.exec())
    main_window.show()
