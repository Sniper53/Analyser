# This Python file uses the following encoding: utf-8

BORT_OPEN = 1


ERROR_OPEN_FILE = -1
BORT_NOT_FOUND = -2
BORT_ALREADY_OPEN = -3


KEY_NOT_FOUND = "Значение отсутствует"

#Список аттрибутов
ATTR_MANUFACTURY_NUMBER = "Заводской номер"
ATTR_DATE_TIME_FLIGHT = "Дата и время полета"


import h5py

class Hdf5Worker:

    __listHdf5Objects = []
    #Словарь в котором хранятся
    __listGroupsFlight = {}

    def __init__(self):
        pass

    def OpenFile(self, fileName, typeOpen = 'r+'):


        # listHistVib = [
        # "/03003/1ПИ/Висение/Данные по вибрации/ГОЭС/Гистограммы/Виброускорения/Вертикальная ось/",
        # "/03003/1ПИ/Висение/Данные по вибрации/ГОЭС/Гистограммы/Виброускорения/Продольная ось/",
        # "/03003/1ПИ/Висение/Данные по вибрации/ГОЭС/Гистограммы/Виброускорения/Поперечная ось/",
        # ]
        # listSpectVib = [
        # "/03003/1ПИ/Висение/Данные по вибрации/ГОЭС/Спектры/Виброускорения/Вертикальная ось/",
        # "/03003/1ПИ/Висение/Данные по вибрации/ГОЭС/Спектры/Виброускорения/Продольная ось/",
        # "/03003/1ПИ/Висение/Данные по вибрации/ГОЭС/Спектры/Виброускорения/Поперечная ось/",
        # ]
        # listHistDef = [
        # "/03003/1ПИ/Висение/Данные по деформации/Тяга 3ОШ/Гистограммы/Нагрузки/Вертикальная ось/",
        # ]
        # allList = []
        # detailNamesVibr = ["ИЛС", "Правое кресло"]
        # modesNames = ["Разгон", "Торможение", "Маневры"]
        # detailNamesDef = ["Тяга 1ДШ", "Тяга 2ДШ"]
        # flightsNames = ["1ПСИ", "2ПСИ", "6ПИ"]
        # delimiter = "/"
        # for flight in flightsNames:
        #     for mode in modesNames:
        #         for detail in detailNamesVibr:
        #             for hist in listHistVib:
        #                 splitStr = hist.split(delimiter)
        #                 splitStr[2] = flight
        #                 splitStr[3] = mode
        #                 splitStr[5] = detail
        #                 splitStr = delimiter.join(splitStr)
        #                 allList.append(splitStr)
        #
        #         for detail in detailNamesDef:
        #             for hist in listHistDef:
        #                 splitStr = hist.split(delimiter)
        #                 splitStr[2] = flight
        #                 splitStr[3] = mode
        #                 splitStr[5] = detail
        #                 splitStr = delimiter.join(splitStr)
        #                 allList.append(splitStr)
        #
        # file = h5py.File("Test.h5", "w")
        # for group in allList:
        #     file.create_group(group)
        # file.close()

        #Обработать момент когда файл занят
        try:
            if (self.GetIndexBortInListObjects(fileName) == BORT_NOT_FOUND) :
                if (h5py.is_hdf5(fileName)) :
                    bort = h5py.File(fileName, typeOpen)
                    self.__listHdf5Objects.append(bort)
                    # group = bort.create_group("25")
                    # group.create_group("1")
                    # group.create_group("2")
                    # group.create_group("3")
                    return BORT_OPEN
                else :
                    return ERROR_OPEN_FILE
            else :
                return BORT_ALREADY_OPEN
        except OSError:
            return ERROR_OPEN_FILE


    def CloseFile(self, fileName):
        bortIndex = self.GetIndexBortInListObjects(fileName)

        if (bortIndex != BORT_NOT_FOUND) :
            self.__listHdf5Objects[bortIndex].close()
            self.__listHdf5Objects.pop(bortIndex)
            return 1

        return BORT_NOT_FOUND

    def GetIndexBortInListObjects(self, fileName):
        index = 0
        for bort in self.__listHdf5Objects :
            if bort.filename == fileName :
                return index
            index = index + 1
        return BORT_NOT_FOUND

    #Функция добавляет аттрибут. В качестве fileObject
    #необходимо передать путь группы или датасета например file['1']
    def AddAttribute(self, fileObject, key, attribute):
        fileObject.attrs.create(key, attribute)

    def RemoveAttribute(self, fileObject, key):
        fileObject.attrs.__delitem__(key)

    def GetValueAttribute(self, fileObject, name):
        listAttr = fileObject.attrs.keys()
        if (name in listAttr) :
            value = fileObject.attrs.get(name)
            if (str(value)[:5] != "Empty") :
                return fileObject.attrs.get(name)
            else :
                return KEY_NOT_FOUND
        else :
            return KEY_NOT_FOUND

    def GetListBorts(self, fileName):
        fileName.keys()

    def GetBortsNames(self, fileName):

        indexBort = self.GetIndexBortInListObjects(fileName)
        if(indexBort == BORT_NOT_FOUND) :
            return None
        bort = self.__listHdf5Objects[indexBort]
        bortNames = list(bort.keys()) #Полкчаем имена бортов из файла
        return bortNames


    #Функция возвращает список полетов
    #fileName - имя файла
    #bortNumber - имя группы борта в HDF5-файле
    #Список полетов является словарем, где ключ имя полета, а значение его дата
    def GetListFlights(self, fileName, bortNumber):
        listFlights = []

        indexBort = self.GetIndexBortInListObjects(fileName)
        if (indexBort == BORT_NOT_FOUND) :
            return listFlights

        fileBort = self.__listHdf5Objects[indexBort]

        flightsNames = fileBort[str(bortNumber)].keys()
        flightsObj = fileBort[str(bortNumber)]

        for flight in flightsNames :
            pairFlightTime = (flight, self.GetValueAttribute(flightsObj, ATTR_DATE_TIME_FLIGHT))
            listFlights.append(pairFlightTime)
        return listFlights

    #Функция создает лист объектов hdf для выбранной группы и
    # добавляет его в словарь групп.
    # groupInfo включает в себя имя файла, имя борта и список полетов группы
    # listFlights лист кортежей [(имя файла, {имя борта в HDF : заводской}), имя полета]
    def CreateGroupFlightsObject(self, listFlights, groupName):

        groupObjets = []

        for bortsInfo, flightName in listFlights :
            indexFile = self.GetIndexBortInListObjects(bortsInfo[0])
            fileObj = self.__listHdf5Objects[indexFile]
            currentBort = bortsInfo[1]
            bortInFile = fileObj[currentBort]
            groupObjets.append(bortInFile[flightName])

        self.__listGroupsFlight[groupName] = groupObjets
        pass

    def RemoveGroupFlights(self, listGroups):
        for group in listGroups :
            del self.__listGroupsFlight[group]
        pass
    def RemoveFlights(self, listFlights):
        for group, index in listFlights :
            listFlightsInFile = self.__listGroupsFlight[group]
            del listFlightsInFile[index]
            self.__listGroupsFlight[group] = listFlightsInFile

    # Функция возвращает информацию об именах групп и индексах в группах
    # полетов для запрашиваемого борта.
    # listFileNames (имя файла, {имя в hdf5, заводской номер})
    def GetGroupNamesAndIdexFlightsInGroup(self, listFileNames):
        listFlights = []
        key = listFileNames[1]
        bortNumber = str("/" + key)
        for group, listHdf5Objects in self.__listGroupsFlight.items() :
            indexFlight = 0
            for flight in listHdf5Objects :
                if flight.file.filename == listFileNames[0] :
                     if flight.parent.name == bortNumber :
                        listFlights.append((group,  indexFlight))
                indexFlight += 1
        return listFlights

    def GetHdf5FlightObject(self):
        return self.__listGroupsFlight

    def GetDatasetsFromPaths(self, listPath, listHdfObjects):
        listDatasets = {}
        for key, idxPth in listPath.items() :
            listDatasets[key] = {}
            for path, index in idxPth :
                if path not in listDatasets[key].keys() :
                    listDatasets[key][path] = []
                if key in listHdfObjects.keys( ) :
                    # idxPth пара путь индекс, key группа. В каждой группе N объектов, к которому мы обращаемся по индексу
                    # чтобы открыть финальную группу прописываем путь. Split необходим чтобы в путе осталось имя полета
                    # для дальнейшей обработки
                    hdfObj = listHdfObjects[key][index][path.split('/',1)[1]]

                    for dataset in hdfObj.keys():
                        data = hdfObj[dataset][()].flatten()
                        attribs = {}

                        for attribName in hdfObj[dataset].attrs.keys():
                            attribs[attribName] = hdfObj[dataset].attrs[attribName]

                        listDatasets[key][path].append((data, attribs))

        return listDatasets

