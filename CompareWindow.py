
from PySide6.QtWidgets import QApplication, QDialog, QTreeWidgetItem, QTreeWidget
import h5py, Hdf5Worker, time, Math, GraphicsWorker as np

import GraphicsWorker, Math
from compare_window import Ui_CompareWindow
from enum import Enum

####Константы деревьев####

class EnTopNodes(Enum) :
    SUBSYSTEMS      = "Подсистемы"
    DATA_TYPES      = "Типы данных"
    HELICOPTER_AXIS = "Оси вертолета"

class EnSubsystems(Enum) :
    SUBSYSTEM_VIBRATION   = "Вибрация"
    SUBSYSTEM_DEFORMATION = "Деформация"

class EnDataTypes(Enum) :
    DISTRIBUTIONS = "Гистограммы"
    SPECTRUMS     = "Спектры"

class EnAxis(Enum) :
    AXIS_X = "Продольная ось"
    AXIS_Y = "Вертикальная ось"
    AXIS_Z = "Поперечная ось"

####Имена групп HDF5#####

#Подсистемы
class EnTypeOfData(Enum) :
    VIBRATION_DATA   = "Данные по вибрации"
    DEFORMATION_DATA = "Данные по деформации"


#Детали по вибрации (Они же группы)
class EnVibrationDetailes(Enum) :
    GOES            = "ГОЭС"
    ILS             = "ИЛС"
    LeftPlace       = "Левое кресло"
    RightPlace      = "Правое кресло"
    LeftWing        = "Левое крыло"
    RightWing       = "Правое крыло"
    PowerUnit       = "ВСУ"
    Keel            = "Киль"
    RS80            = "РС-80"
    RightStab       = "Правый стабилизатор"
    Centr           = "Передняя стенка центроплана"
    MountStab       = "Шпангоут крепления стабилизатора"
    Rudder          = "Руль направления"
    FrontRightTrans = "Верхний узел правого переднего подкоса редуктора"
    FrontLeftTrans  = "Верхний узел левого переднего подкоса редуктора"
    BackRightTrans  = "Верхний узел правого заднего подкоса редуктора"
class EnDeformationDetailes(Enum):
    Traction_3OSH        = "Тяга 3ОШ"
    Traction_4OSH        = "Тяга 4ОШ"
    Traction_7PO         = "Тяга 7ПО"
    Traction_7PR         = "Тяга 7ПР"
    Traction_1DSH        = "Тяга 1ДШ"
    Traction_2DSH        = "Тяга 2ДШ"
    Traction_1RP         = "Тяга 1РП"
    FrontLeftStrutTrans  = "Передний левый подкос редуктора"
    FrontRightStrutTrans = "Передний правый подкос редуктора"
    BackLeftStrutTrans   = "Задний левый подкос редуктора"
    BackRightStrutTrans  = "Задний правый подкос редуктора"
    LeftStrutLeftEng     = "Левый подкос левого двигателя"
    RightStrutLeftEng    = "Правый подкос левого двигателя"
    LeftStrutRightEng    = "Левый подкос правого двигателя"
    RightStrutRightEng   = "Правый подкос правого двигателя"

class CompareWindow(QDialog):
    __hdf5Objects = []
    __hdf5Worker = Hdf5Worker.Hdf5Worker()
    __graphicWorker = GraphicsWorker.GraphicsWorker()
    __mathWorker = Math.Math()
    def __init__(self, parent=None, hdf5Objects=None):
        __hdf5Objects = hdf5Objects
        super().__init__(parent)
        self.ui = Ui_CompareWindow()
        self.ui.setupUi(self)
        self.ui.tw_filters.clear()
        self.ui.pb_buildTree.clicked.connect(self.BuildTree)
        self.ui.pb_clearTree.clicked.connect(self.ClearTree)
        self.ui.pb_compare.clicked.connect(self.ComparePressed)
        self.BuildFiltersTree()
        self.ui.tw_actions.expandAll()
        self.ui.tw_filters.expandAll()

    def ClearTree(self):
        self.ui.tw_modes.clear()

    def SetHdf5Objects(self, hdf5Object):
        self.__hdf5Objects = hdf5Object

    def BuildFiltersModesList(self):
        listFilters = []
        items = self.ui.tw_filters.selectedItems()
        for item in items:
            listFilters.append(item.text(0))
        return listFilters
    def BuildTree(self):

        listFilters = self.BuildFiltersModesList()
        start = time.time()
        self.ui.tw_modes.clear()
        self.BuilderFlightsAndModesInTree(self.__hdf5Objects, listFilters)
        # тесты
        # items1 = self.BuilderPathToData(self.__hdf5Objects, listFilters, None)
        # end = time.time()
        # print(start - end)
        # start = time.time()
        # построить ветку режимов
        # items2 = self.BuilderFlightsAndModesInTree(self.__hdf5Objects, listFilters)
        # end = time.time()
        # print(start - end)
        #
        # for i in range(len(items1)) :
        #     print(self.compare_tree_widget_items(items1[i], items2[i]))

        # countNodes = self.count_nodes_recursive(self.ui.tw_modes.invisibleRootItem())
        # print("Count nodes " + str(countNodes))
        pass

    def GetLeafItemsWithPaths(self, treeItem, path=""):
        leafItems = []
        for i in range(treeItem.childCount()):
            childItem = treeItem.child(i)
            item_path = f"{path}/{childItem.text(0)}" if path else childItem.text(0)
            if childItem.childCount() == 0:  # Если у элемента нет дочерних элементов, то он является конечным
                leafItems.append((item_path, childItem))
            else:
                leafItems.extend(self.GetLeafItemsWithPaths(childItem, item_path))
        return leafItems


    def BuildFiltersTree(self) :
        self.ui.tw_filters.clear()
        #Построение верхних узлов
        for topNode in EnTopNodes:
            item = QTreeWidgetItem()
            item.setText(0, topNode.value)
            self.ui.tw_filters.addTopLevelItem(item)

        countTopNodes = self.ui.tw_filters.topLevelItemCount()
        listChildEnums = [EnTypeOfData, EnDataTypes, EnAxis]
        #Построение дочерних узлов
        for indexTopNode in range(countTopNodes):
            item = self.ui.tw_filters.topLevelItem(indexTopNode)
            for child in listChildEnums[indexTopNode] :
                childItem = QTreeWidgetItem(item)
                childItem.setText(0, child.value)

        listDetailsEnum = [EnVibrationDetailes, EnDeformationDetailes]

        #Построение деталей для вибрации
        #Поиск узлового item по имени
        idxSubsys = 0
        for subsys in EnTypeOfData:
            item = self.SearchItemAtText(self.ui.tw_filters.invisibleRootItem(), subsys.value)
            for detail in listDetailsEnum[idxSubsys]:
                childItem = QTreeWidgetItem(item)
                childItem.setText(0, detail.value)
            idxSubsys += 1


    def SearchItemAtText(self, parentItem, name):
        for indexChild in range(parentItem.childCount()) :
            item = parentItem.child(indexChild)
            if item.text(0) == name:
                return item
            foundItem = self.SearchItemAtText(item, name)
            if foundItem:
                return foundItem
        return None


    def GetParentIndex(self, item):
        itemParent = item.parent()
        if itemParent is None:
            return self.ui.tw_modes.indexOfTopLevelItem(item)
        else :
            itemSuperParent = itemParent.parent()
            if itemSuperParent is None :
                return self.ui.tw_modes.indexOfTopLevelItem(itemParent)
            else :
                return itemSuperParent.indexOfChild(itemParent)


    def BuilderFlightsAndModesInTree(self, hdf5Object, filters):
        # listGroup = []
        beforeFileName = ""
        for group, flights in hdf5Object.items():

            groupItem = QTreeWidgetItem()
            groupItem.setText(0, group)

            #Построение дерева до режимов
            for flight in flights:

                flightItem = QTreeWidgetItem(groupItem)

                namesFlight = flight.name.split('/')
                nameFlight = namesFlight[len(namesFlight) - 1]
                flightItem.setText(0, flight.parent.name[1:] + "/" + nameFlight)
                #(0,1) - глубина построения дерева, 0 - начальное значение, 1 - максимаьный уровень в низ
                # мы начинаем строить с полета, один уровень это режимы
                self.BuildTreeFromHDF5(flight, flightItem, [], (0,1))

            listItems = self.GetLeafItemsWithPaths(groupItem)
            self.BuildPartTree(listItems, flights, None, filters, True)

            self.ui.tw_modes.addTopLevelItem(groupItem)
            self.ui.tw_modes.expandAll()

            # listGroup.append(groupItem.clone())
        # return listGroup


    # Функция разработана с целью уменьшения времени построения деревьев. Оптимизация производится за
    # счет копирования повторяющихся объектов во все оконечные узлы.
    # Параметры:
    # listItems  - список (путь от верхнего до оконечного узла дерева, оконечный item)
    # hdfFlights - список открытых полетов hdf файла
    # level - до какого уровня вниз строить дерево
    # widhCopy - применять ли копировние item.
    # Смысл методоа в том, что в одном hdf5 фафле во всех полетах одинаковая структура, таким образом
    # можно не строить все дерево рекурсивно, а построить первую ветку и потом скопировать получившийся
    # item во все оконечные.
    def BuildPartTree(self, listItems, hdfFlights, level, filter = None, withCopy = True):
        beforeFileName = ""
        cloneItem = QTreeWidgetItem()
        for path, item in listItems:

            delimiter = "/"
            listParts = path.split(delimiter)
            pathInFile = delimiter + listParts[0] + delimiter + listParts[1]

            for flight in hdfFlights:
                if flight.name == pathInFile:
                    pathToObj = path.split(delimiter)
                    pathToObj = delimiter.join(pathToObj[2:])
                    obj = flight[pathToObj]
                    currentFileName = obj.file.filename
                    if currentFileName != beforeFileName:
                        if withCopy is True :
                            beforeFileName = currentFileName
                            cloneItem = QTreeWidgetItem()
                            self.BuildTreeFromHDF5(obj, cloneItem, filter, level)
                            for indexChild in range(cloneItem.childCount()) :
                                item.addChild(cloneItem.child(indexChild).clone())
                        else :
                            self.BuildTreeFromHDF5(obj, item, filter, level)
                        pass
                    else:
                        for indexChild in range(cloneItem.childCount()) :
                            item.addChild(cloneItem.child(indexChild).clone())
                        pass
                    break
            pass


    def BuildTreeFromHDF5(self, hdf5Object, parentItem, filters, levels = None):
        if levels != None :
            levels = (levels[0] + 1, levels[1])
            if (levels[0] > levels[1]) :
                return
        for key in hdf5Object.keys():
            if key in filters :
                continue
            if isinstance(hdf5Object[key], h5py.Group):
                item = QTreeWidgetItem(parentItem)
                item.setText(0, key)
                if levels is not None :
                    self.BuildTreeFromHDF5(hdf5Object[key], item, filters, levels)
                else :
                    self.BuildTreeFromHDF5(hdf5Object[key], item, filters)

    def FormattingPathAndIndexForSelectedItems(self, listItemsQTreeWidget):
        listPath = {}
        for item in listItemsQTreeWidget:
            fullPathAndIndex = self.GetPathForParentItemAndIndexFlight(item)
            key = fullPathAndIndex[1].split('/')[0]
            if key not in listPath.keys() :
                listPath[key] = []
            #Отделяем от полного пути часть после имени полета, т.к. путь до имеи полета уже есть в self.__hdf5Objects
            listPath[key].append((fullPathAndIndex[1].split('/', 2)[2], fullPathAndIndex[0]))
        return listPath
    def GetPathForParentItemAndIndexFlight(self, item, path = ""):
        parentItem = item.parent()
        pathToParent = f"{item.text(0)}/{path}"
        if parentItem is None:
            return (item.indexOfChild(item.child(0)), pathToParent)
        return self.GetPathForParentItemAndIndexFlight(parentItem, pathToParent)

    def ComparePressed(self) :
        #Получение данных
        listIndexes = self.ui.tw_modes.selectedItems()
        listPath = self.FormattingPathAndIndexForSelectedItems(listIndexes)
        listDataSets = self.__hdf5Worker.GetDatasetsFromPaths(listPath, self.__hdf5Objects)
        keysGr = list(listDataSets['Группа 1'].keys())

        pass


    def StartCompare(self, listDataSets):

        filterItems = self.ui.tw_actions.selectedItems()






# Отладочные функции

    def count_nodes_recursive(self, item):
        count = 0
        # Получаем количество дочерних элементов
        child_count = item.childCount()
        count += child_count
        # Рекурсивно обходим все дочерние элементы
        for i in range(child_count):
            child_item = item.child(i)
            count += self.count_nodes_recursive(child_item)
        return count

    def compare_tree_widget_items(self, item1, item2):
        # Проверяем количество дочерних элементов
        if item1.childCount() != item2.childCount():
            return False

        # Проверяем текст и другие свойства элементов
        if item1.text(0) != item2.text(0):
            return False

        # Рекурсивно сравниваем дочерние элементы
        for i in range(item1.childCount()):
            child1 = item1.child(i)
            child2 = item2.child(i)

            if not self.compare_tree_widget_items(child1, child2):
                return False
        return True



 # Закомментированные функции использовались в первой версии, когда дерево строилось по частям.
 # пока решил оставить
    # Последняя часть дерева, включает в себя данные от системы деформации и вибрации.
    # Поскольку набор данных может меняться функция делает проход по одному разу
    # для деформации и вибрации, сохраняет данные в item'ы и для всего файла дублирует последние части
    # дерева. В новом файле также выполняет проход и далее дублирует.
    # def BuildLastPartTree(self, listItems, hdfFlights, level, filter = None, withCopy = True):
    #     beforeFileName = ""
    #     listDataTypes = {}
    #     for dataType in EnTypeOfData :
    #         listDataTypes[dataType.value] = None
    #
    #     currentDataType = ""
    #     for path, item in listItems:
    #         delimiter = "/"
    #
    #         listParts = path.split(delimiter)
    #         pathInFile = delimiter + listParts[0] + delimiter + listParts[1]
    #
    #         # Вычисляем текущий тип данных
    #         for dataType in EnTypeOfData :
    #             if dataType.value in listParts :
    #                 currentDataType = dataType.value
    #
    #         for flight in hdfFlights:
    #
    #             if flight.name == pathInFile:
    #
    #                 pathToObj = path.split(delimiter)
    #                 pathToObj = delimiter.join(pathToObj[2:])
    #                 obj = flight[pathToObj]
    #                 currentFileName = obj.file.filename
    #
    #                 if currentFileName != beforeFileName or listDataTypes[currentDataType] == None:
    #                     for dataType in EnTypeOfData:
    #                         listDataTypes[dataType.value] = None
    #                     listDataTypes[currentDataType] = QTreeWidgetItem()
    #                     if withCopy is True:
    #                         beforeFileName = currentFileName
    #                         self.BuildTreeFromHDF5(obj, listDataTypes[currentDataType], filter, level)
    #                         for indexChild in range(listDataTypes[currentDataType].childCount()) :
    #                             item.addChild(listDataTypes[currentDataType].child(indexChild).clone())
    #                     else :
    #                         self.BuildTreeFromHDF5(obj, item, filter,  level)
    #                 else:
    #                     for indexChild in range(listDataTypes[currentDataType].childCount()) :
    #                         item.addChild(listDataTypes[currentDataType].child(indexChild).clone())
    #                 break
    #         pass
    #
    # def BuilderPathToData(self, hdf5Object, filters, levels):
    #     listGroup = []
    #
    #     for group, flights in hdf5Object.items() :
    #         groupItem = QTreeWidgetItem()
    #         groupItem.setText(0, group)
    #
    #         for flight in flights:
    #             flightItem = QTreeWidgetItem(groupItem)
    #
    #             namesFlight = flight.name.split('/')
    #             nameFlight = namesFlight[len(namesFlight) - 1]
    #             flightItem.setText(0, flight.parent.name[1:] + "/" + nameFlight)
    #
    #             self.BuildTreeFromHDF5(flight, flightItem, filters, levels)
    #
    #         self.ui.tw_modes.addTopLevelItem(groupItem)
    #         listGroup.append(groupItem.clone())
    #     return listGroup