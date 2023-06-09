# Kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


 # KivyMD DatePicke
from kivymd.app import MDApp
 #KivyMD DatePicker
from kivymd.uix.pickers import MDDatePicker

# Google Sheet communication
import gspread
 # Authenticate with Google Sheets
from oauth2client.service_account import ServiceAccountCredentials




# Define screens

class MainMenu(Screen):
    pass


class ReceiveMenu(Screen):
    generalList = [
        "----------FERŐTLENÍTŐ----------", "Brado Clean 1L", "Brado Clean 5L",
        "Brado Plus 1000ML", "Brado Plus 250ML", "Bradogél 500ML",
        "Bradogél 1000ML", "Bradosept 1L", "Bradosept 5L", "Mikorzid AF 100ML",
        "Mikrozid szórófej", "Mikrozid dobozos törlőkendő 150x",
        "Mikrozid dobozos törlőkendő utántöltő 150x", "Sekusept Aktív",
        "Skinman Soft Protect", "Skinman Soft Plus", "Skinsan Scrub",
        "Imi Orange", "Melsept 1000ML", "----------KESZTYŰ----------", "XL Kesztyű",
        "L Kesztyű", "M Kesztyű", "S Kesztyű", "----------CÍMKÉK----------",
        "500-as címke", "80x80 donor címke hűtőházas", "Donorkártya címke 80x50",
        "1000-es címke (Mintacső)", "150x80 dobozos címkehűtőházas",
        "----------TAKARÍTÓ----------", "Lucart Jumbo WC papír 12x (donor?)",
        "Lucart kéztörlő 155 ID", "Lucart kéztörlő henger 140A",
        "Lucart WC papír 10x (személyzeti)", "Lucart Z kéztörlő 15x",
        "Tork Illatosító", "Tork folyékony szappan", "----------EGYÉB----------",
        "Szájmaszk", "Szájmaszk FFP2", "Fénymásoló papír 500x", "Vizes Ballon",
        "Műanyag pohár"
    ]

    receptionList = [
        "----------AJÁNDÉK----------", "Biotech USA műzli", "Belvita", "Sportszelet",
        "Swiss ital", "----------EGYÉB----------", "Függőmappa", "Függőmappa lefűző",
        "Lábzsák", "Archiváló doboz"
    ]

    donorList = [
        "----------CSÖVEK----------", "BD Vacutainer", "Biztonsági tű 21G", "NAT 4ML",
        "NAT 6ML", "S-Monovette Fehér", "S-Monovette Zöld", "S-Monovette Lila",
        "S-Monovette Piros", "Vérvételi harang", "----------EGYÉB----------",
        "Hányós zacskó", "Papírlepedő", "Omnisilk", "Pur-Zellin", "Peha-Haft"
    ]

    productionList = [
        "----------FŐ SEGÉDANYAG----------", "Szerelék ZBK", "Szerelék 4117",
        "Egyszer használatos kanül", "NaCl - Fresenius 250ML",
        "NaCl - Fresenius 500ML", "NaCl - B. Braun", "Citrát - Fresenius",
        "Citrát - Medites Pharma", "Citrát - Macopharma", "Citrát - Haemonetics",
        "----------SYSMEX----------", "Cellclean 50ML", "Cellpack 20L",
        "Stromatolyser", "Kontrollvér Low", "Kontrollvér Normal",
        "----------VESZÉLYES HULLADÉK----------"
        "Veszélyes hulladék kanna", "Veszélyes hulladék kuka 2L",
        "Veszélyes hulladék 5L", "Veszélyes hulladék 10L",
        "Veszélyes hulladék 20L", "Veszélyes hulladék 60L",
        "Veszélyes hulladék zsák", "----------EGYÉB----------",
        "Egyszerhasználatos köpeny", "Hőpapír", "Élvédő"
                                                "Gyorskötegelő", "NAT hungarocell", "NAT hungarocell nylon",
        "Raklapfólia", "Plazmatároló M5 rekesz fagyasztókamrához", "Élvédő"
    ]






    #ReceiveMenu Dropdown spinner logic
    def spinner_clicked(self, value):
        """
        Logic for changing the values in item_spinner by category_spinner
        """
        if value == "Általános":
            self.ids.item_spinner.values = self.generalList
            self.ids.item_spinner.text = "Általános"
        elif value == "Termelés":
            self.ids.item_spinner.values = self.productionList
            self.ids.item_spinner.text = "Termelés"
        elif value == "Donorterem":
            self.ids.item_spinner.values = self.donorList
            self.ids.item_spinner.text = "Donorterem"
        else:
            self.ids.item_spinner.values = self.receptionList
            self.ids.item_spinner.text = "Recepció"
        self.input_values_dictionary.update({"Részleg": value})

    def on_spinner_select(self, text):
        self.input_values_dictionary.update({"Anyag": text})

    #Datepicker
    # Átkellnézni meg átírni mert van benne feleslegs de még nem teljesen értem
    def show_date_picker(self, title, button_id):
        """
        Makes DatePicker Widget, binds on_save/on_cancel function to it, and opens it.
        """
        date_dialog = MDDatePicker(title=title)
        date_dialog.bind(
            on_save=lambda instance, value, date_range: self.on_save(instance, value, date_range, button_id),
            on_cancel=self.on_cancel)
        date_dialog.open()

    def on_save(self, instance, value, date_range, button_id):
        """
        Save function for DatePicker.
        def on_save(self, instance, value, date_range, ids):
        instance ->
        value -> The date data itself. (2777-07-07)
        date_range -> date_dialog= MDDatePicker(mode= "range") return a python list of the dates. [] Techically you can select a range of dates from 01 to 27.
        """
        # Access the button ID (button_id) here
        if button_id == "date_receive":
            converted_time = value.strftime('%Y-%m-%d')
            self.input_values_dictionary.update({"Beérkezés": converted_time})
        elif button_id == "date_production":
            converted_time = value.strftime('%Y-%m-%d')
            self.input_values_dictionary.update({"Gyártás": converted_time})
        else:
            converted_time = value.strftime('%Y-%m-%d')
            self.input_values_dictionary.update({"Lejárat": converted_time})
    def on_cancel(self, instance, value):
        pass

    def local_update(self):
        product_number = self.ids.product_number.text
        quantity = self.ids.quantity.text
        self.input_values_dictionary.update({"Gyártási szám": product_number})
        self.input_values_dictionary.update({"Mennyiség": quantity})
        self.sync_List.append(self.input_values_dictionary)
        #self.input_values_dictionary.clear()
        print(self.input_values_dictionary)
        print(self.sync_List)



    sync_List = []
    input_values_dictionary = {}


    def sync_data(self, syncList = sync_List):
          scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
          ]
          credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'rich-sprite.json', scope)
          client = gspread.authorize(credentials)

          # x axison megy örökké
          #16384 XFD
          def convertUniqueIDToColumn(uniqueID):
            dividend = uniqueID
            column_name = ''

            while dividend > 0:
              modulo = (dividend - 1) % 26
              column_name = chr(65 + modulo) + column_name
              dividend = (dividend - modulo) // 26

            return column_name

          for item in syncList:
            if item["Részleg"] == 'Általános':
              # Open an existing Google Sheets spreadsheet
              sheet = client.open("Inventory Management App").worksheet(
                "Általános")
              sheet.add_cols(1)
              uniqueID = int(sheet.cell(1, 1).value[1:])
              columnLetter = convertUniqueIDToColumn(uniqueID)
              #ide hogy mitötrténjen vele

              sheet.update_cell(1, uniqueID, "G" + columnLetter)  #mit column
              sheet.update_cell(2, uniqueID, item["Anyag"])
              sheet.update_cell(3, uniqueID, item["Beérkezés"])
              sheet.update_cell(4, uniqueID, item["Gyártás"])
              sheet.update_cell(5, uniqueID, item["Gyártási szám"])
              sheet.update_cell(6, uniqueID, item["Lejárat"])
              sheet.update_cell(7, uniqueID, item["Mennyiség"])
              #Img

              #ebbe megy a jelenlegi adat
              uniqueID = uniqueID + 1
              sheet.update_cell(1, 1, "G" + str(uniqueID))

            if item["Részleg"] == 'Termelés':
              # Open an existing Google Sheets spreadsheet
              sheet = client.open("Inventory Management App").worksheet("Termelés")
              sheet.add_cols(1)
              uniqueID = int(sheet.cell(1, 1).value[1:])
              columnLetter = convertUniqueIDToColumn(uniqueID)

              #ide hogy mitötrténjen vele

              sheet.update_cell(1, uniqueID, "P" + columnLetter)  #mit column
              sheet.update_cell(2, uniqueID, item["Anyag"])
              sheet.update_cell(3, uniqueID, item["Beérkezés"])
              sheet.update_cell(4, uniqueID, item["Gyártás"])
              sheet.update_cell(5, uniqueID, item["Gyártási szám"])
              sheet.update_cell(6, uniqueID, item["Lejárat"])
              sheet.update_cell(7, uniqueID, item["Mennyiség"])
              #Img

              #ebbe megy a jelenlegi adat
              uniqueID = uniqueID + 1
              sheet.update_cell(1, 1, "P" + str(uniqueID))

            if item["Részleg"] == 'Donorterem':
              # Open an existing Google Sheets spreadsheet
              sheet = client.open("Inventory Management App").worksheet(
                "Donorterem")
              sheet.add_cols(1)
              uniqueID = int(sheet.cell(1, 1).value[1:])
              columnLetter = convertUniqueIDToColumn(uniqueID)
              #ide hogy mitötrténjen vele

              sheet.update_cell(1, uniqueID, "D" + columnLetter)  #mit column
              sheet.update_cell(2, uniqueID, item["Anyag"])
              sheet.update_cell(3, uniqueID, item["Beérkezés"])
              sheet.update_cell(4, uniqueID, item["Gyártás"])
              sheet.update_cell(5, uniqueID, item["Gyártási szám"])
              sheet.update_cell(6, uniqueID, item["Lejárat"])
              sheet.update_cell(7, uniqueID, item["Mennyiség"])
              #Img

              #ebbe megy a jelenlegi adat
              uniqueID = uniqueID + 1
              sheet.update_cell(1, 1, "D" + str(uniqueID))

            if item["Részleg"] == 'Recepció':
              # Open an existing Google Sheets spreadsheet
              sheet = client.open("Inventory Management App").worksheet("Recepció")
              sheet.add_cols(1)
              uniqueID = int(sheet.cell(1, 1).value[1:])
              columnLetter = convertUniqueIDToColumn(uniqueID)
              #ide hogy mitötrténjen vele

              sheet.update_cell(1, uniqueID, "R" + columnLetter)  #mit column
              sheet.update_cell(2, uniqueID, item["Anyag"])
              sheet.update_cell(3, uniqueID, item["Beérkezés"])
              sheet.update_cell(4, uniqueID, item["Gyártás"])
              sheet.update_cell(5, uniqueID, item["Gyártási szám"])
              sheet.update_cell(6, uniqueID, item["Lejárat"])
              sheet.update_cell(7, uniqueID, item["Mennyiség"])
              #Img

              #ebbe megy a jelenlegi adat
              uniqueID = uniqueID + 1
              sheet.update_cell(1, 1, "R" + str(uniqueID))

          syncList.clear()



class ExpendMenu(Screen):

    expendList = []

    def materialExpend(self):
        expendMaterialDictionary = {}
        expendMaterialDictionary.update({"ID": self.ids.expend_id.text})
        expendMaterialDictionary.update({"Quantity": self.ids.expend_quantity.text})
        self.expendList.append(expendMaterialDictionary)
        print(self.expendList)



    def eSychronizeData(self, syncList = expendList):

        def convertColumnToUniqueID(column_name):
            num = 0
            for c in column_name:
                if c.isalpha():
                    num = num * 26 + (ord(c.upper()) - ord('A')) + 1
            return num

        scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'rich-sprite.json', scope)
        client = gspread.authorize(credentials)

        for item in syncList:
            print(syncList)
            worksheet = item["ID"][0]
            id = item["ID"][1:]

            quantity = int(item["Quantity"])

            if worksheet == "G":
                # Open an existing Google Sheets spreadsheet
                sheet = client.open("Inventory Management App").worksheet(
                    "Általános")
                columnInt = convertColumnToUniqueID(id)
                rowValue = sheet.cell(7, columnInt).value
                print(rowValue)
                sheet.update_cell(7, columnInt, int(rowValue) - quantity)

            elif worksheet == "P":
                # Open an existing Google Sheets spreadsheet
                sheet = client.open("Inventory Management App").worksheet("Termelés")
                columnInt = convertColumnToUniqueID(id)
                rowValue = sheet.cell(7, columnInt).value
                print(rowValue)
                sheet.update_cell(7, columnInt, int(rowValue) - quantity)
            elif worksheet == "D":
                # Open an existing Google Sheets spreadsheet
                sheet = client.open("Inventory Management App").worksheet(
                    "Donorterem")
                columnInt = convertColumnToUniqueID(id)
                rowValue = sheet.cell(7, columnInt).value
                print(rowValue)
                sheet.update_cell(7, columnInt, int(rowValue) - quantity)
            else:
                # Open an existing Google Sheets spreadsheet
                sheet = client.open("Inventory Management App").worksheet("Recepció")
                columnInt = convertColumnToUniqueID(id)
                rowValue = sheet.cell(7, columnInt).value
                print(rowValue)
                sheet.update_cell(7, columnInt, int(rowValue) - quantity)

            # ide hogy mitötrténjen vele

    expendList.clear()
    print(len(expendList))




class WindowManager(ScreenManager):
    pass




class MyApp(MDApp):
    def build(self):
        kv = Builder.load_file(
            'MyApp.kv')  # returnnél visszaadom mivel ez vonatkozik a kv fájlra ami tartalmazni fogja a windowokat
        return kv


if __name__ == '__main__':
    MyApp().run()
