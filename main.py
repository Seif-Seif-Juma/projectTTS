import sys
import csv
import webbrowser
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QPushButton, QLabel, QLineEdit, 
                           QListWidget, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

class WhatsAppLauncher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.contacts = []  # List to store contacts
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('WhatsApp Chat Launcher')
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Import buttons layout
        import_layout = QHBoxLayout()
        self.import_csv_btn = QPushButton('Import CSV')
        self.import_vcf_btn = QPushButton('Import VCF')
        import_layout.addWidget(self.import_csv_btn)
        import_layout.addWidget(self.import_vcf_btn)
        layout.addLayout(import_layout)
        
        # Search bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText('Search contacts...')
        search_layout.addWidget(self.search_input)
        layout.addLayout(search_layout)
        
        # Contacts list
        self.contacts_list = QListWidget()
        layout.addWidget(self.contacts_list)
        
        # Chat button
        self.chat_btn = QPushButton('Open WhatsApp Chat')
        self.chat_btn.setEnabled(False)
        layout.addWidget(self.chat_btn)
        
        # Connect signals
        self.import_csv_btn.clicked.connect(self.import_csv)
        self.import_vcf_btn.clicked.connect(self.import_vcf)
        self.search_input.textChanged.connect(self.filter_contacts)
        self.contacts_list.itemSelectionChanged.connect(self.toggle_chat_button)
        self.chat_btn.clicked.connect(self.open_whatsapp)
        
        # Apply styling
        self.style_ui()
        
    def style_ui(self):
        # Set font
        app_font = QFont('Segoe UI', 10)
        self.setFont(app_font)
        
        # Style buttons
        button_style = '''
            QPushButton {
                background-color: #25D366;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #128C7E;
            }
            QPushButton:disabled {
                background-color: #cccccc;
            }
        '''
        self.import_csv_btn.setStyleSheet(button_style)
        self.import_vcf_btn.setStyleSheet(button_style)
        self.chat_btn.setStyleSheet(button_style)
        
        # Style search input
        self.search_input.setStyleSheet('''
            QLineEdit {
                padding: 8px;
                border: 1px solid #128C7E;
                border-radius: 4px;
            }
        ''')
        
        # Style contacts list
        self.contacts_list.setStyleSheet('''
            QListWidget {
                border: 1px solid #128C7E;
                border-radius: 4px;
            }
            QListWidget::item {
                padding: 8px;
            }
            QListWidget::item:selected {
                background-color: #128C7E;
                color: white;
            }
        ''')

    def import_csv(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Import CSV', '', 'CSV Files (*.csv)')
        if file_name:
            try:
                with open(file_name, 'r') as file:
                    csv_reader = csv.DictReader(file)
                    self.contacts = []
                    for row in csv_reader:
                        if 'name' in row and 'phone' in row:
                            self.contacts.append({
                                'name': row['name'],
                                'phone': row['phone']
                            })
                self.update_contacts_list()
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'Error importing CSV: {str(e)}')

    def import_vcf(self):
        # TODO: Implement VCF import functionality
        QMessageBox.information(self, 'Info', 'VCF import will be implemented in the next version')

    def filter_contacts(self):
        search_text = self.search_input.text().lower()
        self.contacts_list.clear()
        for contact in self.contacts:
            if search_text in contact['name'].lower():
                self.contacts_list.addItem(contact['name'])

    def update_contacts_list(self):
        self.contacts_list.clear()
        for contact in self.contacts:
            self.contacts_list.addItem(contact['name'])

    def toggle_chat_button(self):
        self.chat_btn.setEnabled(bool(self.contacts_list.selectedItems()))

    def open_whatsapp(self):
        selected_item = self.contacts_list.selectedItems()[0]
        selected_name = selected_item.text()
        selected_contact = next((c for c in self.contacts if c['name'] == selected_name), None)
        
        if selected_contact:
            # Clean phone number - remove spaces, dashes, etc.
            phone = ''.join(filter(str.isdigit, selected_contact['phone']))
            url = f'https://wa.me/{phone}'
            webbrowser.open(url)

def main():
    app = QApplication(sys.argv)
    launcher = WhatsAppLauncher()
    launcher.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()