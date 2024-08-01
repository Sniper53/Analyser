# This Python file uses the following encoding: utf-8
import sys
import Hdf5Worker
import CompareWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTreeWidgetItem

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside6-uic compare_window.ui -o compare_window.py
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_MainWindow

MAXIMUM_GROUPS = 10

class Worker():
    def __init__(self):
        pass
    #Функция ищет в словаре борт соответствующий выбранному индексу
    def FindBortByIndex(self, indexTree, dictOpenBords):
        index = -1 #Индекс соответствующий верхнему узлу должен досчитать до indexTree
        for fileName, bortsInFile in dictOpenBords.items():
            if len(bortsInFile) > 1:
                for bort in bortsInFile:
                    index += 1
                    if index == indexTree:
                        return (fileName, bort)
            else:
                index += 1
                if index == indexTree:
                    return (fileName, bortsInFile[0])

    def GetFlightsGroupInfo(self, bortIndexes, dictOpenBords):
        bortsInfo = []
        for index in bortIndexes:
            bortsInfo.append(self.FindBortByIndex(index, dictOpenBords))
        return bortsInfo


class MainWindow(QMainWindow):
    __hdfWorker = Hdf5Worker.Hdf5Worker()
    __dictOpenBords = {}
    __worker = Worker()
    __compareWindow = CompareWindow.CompareWindow
    # __compareWindow.show()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pb_addBort.clicked.connect(self.pb_AddBortClick)
        self.ui.pb_removeBort.clicked.connect(self.pb_RemoveBortClick)
        self.ui.pb_createGroup.clicked.connect(self.CreateGroupFlights)
        self.ui.pb_delGroupOrFlight.clicked.connect(self.RemoveGroupsOrFlights)
        self.ui.tw_borts.itemClicked.connect(self.SelectAllChildrenItems)
        self.ui.tw_groupsFlights.itemClicked.connect(self.SelectAllChildrenItems)
        self.ui.pb_compare.clicked.connect(self.OpenCompareWindow)
        self.__compareWindow = CompareWindow.CompareWindow(self)

    def pb_AddBortClick(self):
        fileName = self.OpenBort()
        if (fileName is None):
            self.ui.statusbar.showMessage("Ошибка открытия файла или файл не указан", 5000)
            return

        borts = self.__hdfWorker.GetBortsNames(fileName)
        if borts is None:
            self.ui.statusbar.showMessage("Борта в файле не обнаружены", 5000)
            return
        self.__dictOpenBords[fileName] = borts

        listBortFlights = self.GetBortsFlights(fileName)
        if (len(listBortFlights) == 0):
            self.ui.statusbar.showMessage("Борта в файле не обнаружены", 5000)
            return

        self.PrintTreeBortsAndFlights(listBortFlights)

    def pb_RemoveBortClick(self):
        if (len(self.__dictOpenBords) == 0):
            return
        index = self.ui.tw_borts.currentIndex().row()

        if self.ui.tw_borts.currentItem().parent() is not None:
            return

        listFileNames = self.__worker.FindBortByIndex(index, self.__dictOpenBords)

        listRemoveFligtsInGroups = self.__hdfWorker.GetGroupNamesAndIdexFlightsInGroup(listFileNames)
        # Покольку очистка происходит по индексам полетов в группах, они должны быть отсортированы в
        # порядке убывания
        listRemoveFligtsInGroups = sorted(listRemoveFligtsInGroups, key=lambda x : x[1], reverse=True)
        self.__hdfWorker.RemoveFlights(listRemoveFligtsInGroups)
        countTolItems = self.ui.tw_groupsFlights.topLevelItemCount( )

        for group, indexChild in listRemoveFligtsInGroups :
            for indexGroup in range(countTolItems) :
                if self.ui.tw_groupsFlights.topLevelItem(indexGroup).text(0) == group :
                    self.ui.tw_groupsFlights.topLevelItem(indexGroup).takeChild(indexChild)

        # Проверка, что не осталось пустых групп, если остались, удаляем, также в порядке убывания
        for indexGroup in range(countTolItems-1, -1, -1) :
            countChild = self.ui.tw_groupsFlights.topLevelItem(indexGroup).childCount()
            if countChild == 0 :
                groupName = self.ui.tw_groupsFlights.topLevelItem(indexGroup).text(0)
                self.__hdfWorker.RemoveGroupFlights([groupName])
                self.ui.tw_groupsFlights.takeTopLevelItem(indexGroup)

        if (len(self.__dictOpenBords[listFileNames[0]]) > 1):
            key = listFileNames[1]
            self.__dictOpenBords[listFileNames[0]].remove(key)
            self.ui.tw_borts.takeTopLevelItem(index)
        else:
            del self.__dictOpenBords[listFileNames[0]]
            self.ui.tw_borts.takeTopLevelItem(index)
            self.__hdfWorker.CloseFile(listFileNames[0])


    def OpenBort(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open bort", "", "HDF5 files(*.h5 *.HDF5)")
        code = 0

        if (fileName.strip() != ""):
            code = self.__hdfWorker.OpenFile(fileName)

        if (code == Hdf5Worker.BORT_OPEN):
            return fileName
        elif (code == Hdf5Worker.BORT_ALREADY_OPEN):
            return None

        elif (code == Hdf5Worker.ERROR_OPEN_FILE):
            return None



    def GetBortsFlights(self, fileName):

        listBortsNames = self.__dictOpenBords[fileName]
        listBortsFlights = {}
        for bort in listBortsNames:
            listBortsFlights[bort] = self.__hdfWorker.GetListFlights(fileName, bort)

        return listBortsFlights

    def PrintTreeBortsAndFlights(self, listBortsFlights):
        borts = listBortsFlights.keys()

        for bort in borts:
            itemBort = QTreeWidgetItem()
            itemBort.setText(0, str(bort))
            for flight in listBortsFlights[bort]:
                flightItem = QTreeWidgetItem(itemBort)
                flightItem.setText(0, flight[0])
                flightItem.setText(1, flight[1])
            self.ui.tw_borts.addTopLevelItem(itemBort)

    def GetGroupName(self):
        coutnItems = self.ui.tw_groupsFlights.topLevelItemCount()
        listCurrentGroups = []

        for index in range(coutnItems):
            listCurrentGroups.append(self.ui.tw_groupsFlights.topLevelItem(index).text(0))

        for numberCurrentGroup in range(1, MAXIMUM_GROUPS + 1):
            newName = "Группа " + str(numberCurrentGroup)
            if newName not in listCurrentGroups:
                return newName

    #Функция создает группы полетов для анализа
    def CreateGroupFlights(self):

        listFlights = []
        #Уникальные полеты передаются в HDF5Worker для создания объектов. Если полеты будут повторяться,
        # то там будет дублирование объектов.

        selectedItems = self.ui.tw_borts.selectedItems()
        for item in selectedItems:
            if item.parent() is None:
                continue
            bortIndex = [self.ui.tw_borts.indexOfTopLevelItem(item.parent())]
            bortInfo = self.__worker.GetFlightsGroupInfo(bortIndex, self.__dictOpenBords)
            flightName = item.text(0)
            listFlights.append((bortInfo[0], flightName))

        if (len(listFlights) == 0):
            return

        numGroups = self.ui.tw_groupsFlights.topLevelItemCount()
        if (numGroups >= MAXIMUM_GROUPS):
            self.ui.statusbar.showMessage("Не может быть больше 10 групп", 2000)
            return

        groupName = self.GetGroupName()

        groupItem = QTreeWidgetItem()
        groupItem.setText(0, groupName)
        for bortInfo, flight in listFlights:
            flightItem = QTreeWidgetItem(groupItem)
            flightItem.setText(0, bortInfo[1] + "/" + flight)

        self.ui.tw_groupsFlights.addTopLevelItem(groupItem)
        self.__hdfWorker.CreateGroupFlightsObject(listFlights, groupName)

    def RemoveGroupsOrFlights(self):

        listSelectedItems = self.ui.tw_groupsFlights.selectedItems()
        #Кортеж (индекс родителя, индекс item)
        listRemoveGroups = []
        listRemoveFlights = []
        if (len(listSelectedItems) == 0):
            return

        for item in listSelectedItems:
            if item.parent() is None:
                listRemoveGroups.append(item.text(0))
                indexOfTopLevelItem = self.ui.tw_groupsFlights.indexOfTopLevelItem(item)
                self.ui.tw_groupsFlights.takeTopLevelItem(indexOfTopLevelItem)
            else:
                parentItem = item.parent()
                parentIndex = self.ui.tw_groupsFlights.indexOfTopLevelItem(parentItem)
                #Если выбрана группа и полет, то полет не добавляем, т.к. группа будет полностью удалена
                if parentItem.text(0) in listRemoveGroups:
                    continue
                else:
                    listRemoveFlights.append((parentItem.text(0), parentItem.indexOfChild(item)))
                    parentItem.takeChild(parentItem.indexOfChild(item))
                #Если после удаления полета в группе не осталось полетов то удаляем группу
                if (parentItem.childCount() == 0):
                    listRemoveGroups.append(parentItem.text(0))
                    self.ui.tw_groupsFlights.takeTopLevelItem(parentIndex)

        # В зависимости от порядка как пользователь в нтерфейсе выберет полеты
        # проверка if(parentItem.childCount() == 0) может не сработать, т.к.
        # сначала может быть добавлен полет на удаление, а потом группа. Чтобы избежать ситуации,
        # когда будет удалена группа, а потом полет, то сначала проводится удалене полетов, а потом
        # групп

        listRemoveFlights = sorted(listRemoveFlights, key=lambda x: x[1], reverse=True)
        self.__hdfWorker.RemoveFlights(listRemoveFlights)

        self.__hdfWorker.RemoveGroupFlights(set(listRemoveGroups))

    #При выборе узлового item выделяет все дочерние
    def SelectAllChildrenItems(self, clickedItem, column):
        if clickedItem.parent() is None:
            countChild = clickedItem.childCount()
            for i in range(countChild):
                clickedItem.child(i).setSelected(True)

    def GetListBortsAndGroups(self):
        listBortGroup = []
        coutGroups = self.ui.tw_groupsFlights.topLevelItemCount()
        for indexGroup in range(coutGroups):
            group = self.ui.tw_groupsFlights.topLevelItem(indexGroup)
            coutChildren = group.childCount()
            for indexChild in range(coutChildren):
                child = self.ui.tw_groupsFlights.child(indexChild)

    def OpenCompareWindow(self):
        hdf5flightsObject = self.__hdfWorker.GetHdf5FlightObject()
        self.__compareWindow.SetHdf5Objects(hdf5flightsObject)
        self.__compareWindow.BuildTree( )
        self.__compareWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    compareWindow = CompareWindow.CompareWindow(widget)
    widget.show()
    sys.exit(app.exec())
