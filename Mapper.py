from pathlib import Path

class BoardMap:

    def __init__(self, file):
        self.filepath = Path(file)
        self.loadPins()

    def loadPins(self):
        file = open(self.filepath)
        self.pins = {}
        for line in file:
            decomposedLine = line.split(',')
            lineLen = len(decomposedLine)
            if(lineLen>1):
                self.pins[decomposedLine[0].upper().strip()]=decomposedLine[1].upper().strip()
            else:
                self.pins[decomposedLine[0].upper().strip()]='*'

    def getSOCpin(self,FMCpin):
        return self.pins[FMCpin]

    def mapDeviceToSOC(self, deviceMap):
        deviceMapFile = open(Path(deviceMap))
        fmcMap = {}
        for line in deviceMapFile:
            decomposedLine = line.split(',')
            netName = decomposedLine[0].strip()
            fmcPin = decomposedLine[1].upper().strip()
            fmcMap[netName] = fmcPin
        return fmcMap


a = BoardMap('DeviceMaps/VMK-VCK_J51')
print(a.mapDeviceToSOC('Designs/TestDesign'))
