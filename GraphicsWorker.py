import matplotlib as plt
plt.use('gtk3agg')
import matplotlib.pyplot as plt
import numpy as np
from enum import Enum


class EnTypOfGraps(Enum) :
    HISTOGRAM = "Гистограммы"
    SPECTRUMS = "Спектры"

class EnKeysAttribsForAxis(Enum) :
    HIST_STEP = "Шаг гистограммы"
    F_D = "Частота дискретизации"

class GraphicsWorker:
    def __init__(self):
        pass


    def PlotHistograms(self, axisY, axisX):

        plt.bar(axisX, axisY)
        plt.grid()
        plt.xlabel("Виброускорение")
        plt.ylabel("количество значений")
        plt.show()
        pass

    #Метод возвращает ось Х для датасета в зависимости с инфрмацией в аттрибутах
    #pathWithData - [(путь, (данные, {атрибуты}))]
    def FormattingAxisForDataset(self, pathWithData):
        path, dataSetWithAttrs = pathWithData
        typeOfData = self.GetTypeOfDataFromPath(path)
        step = self.GetStepXforDataset(typeOfData, dataSetWithAttrs[1])
        axisX = np.arange(0, round(dataSetWithAttrs[0].size*step, 2), step)
        return axisX

    def GetTypeOfDataFromPath(self, path) :
        listPath = path.split("/")
        for typeData in EnTypOfGraps:
            if typeData.value in listPath :
                return typeData.value
        return None

    def GetStepXforDataset(self, typeData, attribs) :

        if typeData == EnTypOfGraps.HISTOGRAM.value :
            return attribs[EnKeysAttribsForAxis.HIST_STEP.value][0]

        elif typeData == EnTypOfGraps.SPECTRUMS.value :
            return attribs[EnKeysAttribsForAxis.F_D.value][0]

