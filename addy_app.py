
#import modules
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import addressbk as addbk
import sys

class AddyBook(QtWidgets.QMainWindow, addbk.Ui_addr_widget):
#initialize the buttons and widget
    def __init__(self, parent = None):
        super(AddyBook, self).__init__(parent)
        self.setupUi(self)
        self.sub_btn.clicked.connect(self.submit_form)
        self.clr_btn.clicked.connect(self.clear_form)
        self.af_list = [chr(num) for num in range(97, 103)]
        self.gl_list = [chr(num) for num in range(103, 109)]
        self.mr_list = [chr(num) for num in range(109, 115)]
        self.sw_list = [chr(num) for num in range(115, 120)]
        self.xz_list = [chr(num) for num in range(120, 123)]

#pull all entries from address entry form and put them into a dictionary
    def submit_form(self):
        entry_dict = {
        'FirstName': self.fname_ent.text(),
        'LastName': self.lname_ent.text(),
        'AddressOne': self.add1_ent.text(),
        'AddressTwo': self.add2_ent.text(),
        'City': self.city_ent.text(),
        'Province': self.prov_ent.text(),
        'Country': self.country_ent.text(),
        'PostalCode': self.postal_ent.text(),
        'Email': self.email_ent.text(),
        'PhoneOne': self.ph1_ent.text(),
        'PhoneTwo': self.ph2_ent.text()}
    
        self.pop_book(self.af_list, entry_dict)
        self.pop_book(self.gl_list, entry_dict)
        self.pop_book(self.mr_list, entry_dict)
        self.pop_book(self.sw_list, entry_dict)
        self.pop_book(self.xz_list, entry_dict)

#write to specific file using starting letter of last name
#each file represents a different tab on the address browser
#try and except blocks to make sure first or last name has an entry
#the '\n' is to prettify text in the file, the '<br>' is to prettify text on the text browser widget
    def pop_book(self, alpha_lst, ent_dict):
        try:
            if ent_dict['LastName'][0].lower() in alpha_lst:
                with open('Address_' + alpha_lst[0] + alpha_lst[-1] + '.txt', 'a') as ab:
                    for key, value in ent_dict.items():
                        ab.write(key + ': ' + value + '\n' + '<br>')
                    ab.write('<br>')
        except IndexError:
            try:
                if ent_dict['FirstName'][0].lower() in alpha_lst:
                    with open('Address_' + alpha_lst[0] + alpha_lst[-1] + '.txt', 'a') as ab:
                        for key, value in ent_dict.items():
                            ab.write(key + ': ' + value + '\n' + '<br>')
                        ab.write('<br>')
            except IndexError:
                pass

        self.add_disp_af.reload()  
        self.add_disp_gl.reload()
        self.add_disp_mr.reload()
        self.add_disp_sw.reload()
        self.add_disp_xz.reload()
        
#clears all entries on form (form also has a single line clear option)            
    def clear_form(self):
        self.fname_ent.clear()
        self.lname_ent.clear()
        self.add1_ent.clear()
        self.add2_ent.clear()
        self.city_ent.clear()
        self.prov_ent.clear()
        self.country_ent.clear()
        self.postal_ent.clear()
        self.email_ent.clear()
        self.ph1_ent.clear()
        self.ph2_ent.clear()

#create and call instances
def main():
    app = QApplication(sys.argv)
    form = AddyBook()
    form.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
