
import numpy as np, time
from enum import Enum


# items1 = self.BuilderPathToData(self.__hdf5Objects, listFilters, None)
# end = time.time()
# print(start - end)
# start = time.time()
# построить ветку режимов
# items2 = self.BuilderFlightsAndModesInTree(self.__hdf5Objects, listFilters)
# end = time.time()
# print(start - end)

#перечисление параметров ключей сохраняются в аттрибуты суммирования
class EnSumKeysForSave(Enum) :
    F_D = "Частота дискретизации"
    STEP_HYST = "Шаг гистограммы"

class EnKeysFunct(Enum) :
    TYPE_OF_DATA = "Тип данных"

class EnValFunct(Enum) :
    SUM_DATASETS = "Суммирование наборов данных"
    AVR_DATASETS = "Усреднение наборов данных"



class Math :

    def __init__(self):
        pass

    #Метод суммирует все гистограммы в датасете
    def SumHistogramInDataset(self, dataSet):
        resultData = np.array([])
        lenMaxArray = 0
        for data, attrib in dataSet:
            if data.size > lenMaxArray:
                lenMaxArray = data.size

        resultData = np.pad(resultData, (0, lenMaxArray), 'constant')
        resultAttrib = {}

        for data, attrib in dataSet:
            if data.size < lenMaxArray:
                dataPad = np.pad(data, (0, lenMaxArray-data.size), 'constant')
                resultData = np.add(resultData, dataPad)
            else:
                resultData = np.add(data, resultData)
                resultAttrib[EnKeysFunct.TYPE_OF_DATA.value] = EnValFunct.SUM_DATASETS.value
                for keyForSave in EnSumKeysForSave:
                    if keyForSave.value in attrib.keys():
                        resultAttrib[keyForSave.value] = attrib[keyForSave.value]

        return (resultData, resultAttrib)

    # Метод усредняе все гистограммы в датасете
    def AveragingHistogramInDataset(self, dataSet):
        sumHist = self.SumHistogramInDataset(dataSet)
        finalData = np.floor_divide(sumHist[0], len(dataSet))

        resultAttrib = {}
        resultAttrib[EnKeysFunct.TYPE_OF_DATA.value] = EnValFunct.AVR_DATASETS.value;
        for keyForSave in EnSumKeysForSave:
            if keyForSave.value in sumHist[1].keys():
                resultAttrib[keyForSave.value] = sumHist[1][keyForSave.value]
        return (finalData, resultAttrib)