
from PyQt5 import QtCore, QtWidgets

from BASE.DATABASE.Database import Database
from BASE.SERVICES.LeagueService import get_highest_mastery_entry_for
from BASE.Utility import convert_champ_name_to_id
from GUI.SetUp import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.searchButton.clicked.connect(self.get_max_entry)


    @QtCore.pyqtSlot()
    def update_interface_with_entry(self, max_entry):
        if max_entry == None: # no information for the specified champ
            self.summoner_value.setText("No data for specified champion")
            self.rank_value.setText("")
            self.point_value.setText("")
            return
        else:
            db = Database()
            summoner_name = max_entry[0]
            points = str(max_entry[1])
            profile = db.select("tier FROM profiles WHERE summonername = \"{}\"".format(summoner_name))
            rank = profile[0][0]

            self.summoner_value.setText(summoner_name)
            self.point_value.setText(points)
            self.rank_value.setText(rank)

    # actions for button click
    @QtCore.pyqtSlot()
    def get_max_entry(self):
        champ_name = self.lineEdit.text()
        champ_id = convert_champ_name_to_id(champ_name)
        # returns a tuple ("summoner_name",points, champ_id)
        max_entry = get_highest_mastery_entry_for(champ_id)

        if max_entry != None:
            self.update_interface_with_entry(max_entry)
        else:
            self.update_interface_with_entry(None)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.setStyleSheet("QMainWindow {background: rgb(49,51,74);}")
    window.show()
    sys.exit(app.exec_())