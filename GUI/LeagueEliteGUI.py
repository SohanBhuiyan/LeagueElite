
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

    # actions for button click
    @QtCore.pyqtSlot()
    def update_interface_with(self, max_entry):
        db = Database()

        summoner_name = max_entry[0]
        points = str(max_entry[1])
        profile = db.select("tier FROM profiles WHERE summonername = \"{}\"".format(summoner_name))
        rank = profile[0][0]

        self.summoner_value.setText(summoner_name)
        self.point_value.setText(points)
        self.rank_value.setText(rank)

    @QtCore.pyqtSlot()
    def get_max_entry(self):
        champ_name = self.lineEdit.text()
        champ_id = convert_champ_name_to_id(champ_name)
        # returns a tuple ("summoner_name",points, champ_id)
        max_entry = get_highest_mastery_entry_for(champ_id)

        if max_entry != None:
            self.update_interface_with(max_entry)
        else:
            print("No data for given champ")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())