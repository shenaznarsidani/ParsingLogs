import csv
import threading
import sys
from concurrent.futures import ThreadPoolExecutor
class Solution(object):
    def __init__(self, protocolMappingFile, lookupFile, logFile):
        self.protocolMappingFile = protocolMappingFile
        self.lookupFile = lookupFile
        self.logFile = logFile
        self.portProtocolCount = {}
        self.tagCount = {}
        self.chunk_size = 256
        self.maxThreads = 3
        self.protocolMapping = {}
        self.lookupDict = {}
        self.mapProtocol()
        self.getLookup()
    
    def mapProtocol(self):
        with open(self.protocolMappingFile, "r") as file:
            csvReader = csv.reader(file)
            for row in csvReader:
                if row[0].isnumeric():
                    self.protocolMapping[int(row[0])] = row[1]

    def getLookup(self):
        with open(self.lookupFile, "r") as file:
            csvReader = csv.reader(file)
            for row in csvReader:
                if row[0].isnumeric():
                    dstport = int(row[0])
                    protocol = row[1].strip().upper()
                    tag = row[2].strip().upper()
                    protocolDict = self.lookupDict.get(protocol, {})
                    protocolDict[dstport] = tag
                    self.lookupDict[protocol] = protocolDict
    
    def processChunk(self, logChunk):
        for log in logChunk:
            log = log.strip()
            if log:
                tokens = log.split()
                dstport,protocol_num = int(tokens[6]), int(tokens[7])
                protocol = self.protocolMapping[protocol_num]
                tag = self.lookupDict.get(protocol,{}).get(dstport,"Untagged")

                
                with threading.Lock():
                    #Making count of Port Protocol Combination
                    protocolDict = self.portProtocolCount.get(protocol, {})
                    protocolDict[dstport] = protocolDict.get(dstport,0)+1
                    self.portProtocolCount[protocol] = protocolDict

                    # Making Tag Count  
                    self.tagCount[tag] = self.tagCount.get(tag, 0)+1
    
    def processLogs(self):
        lock = threading.Lock()
        with open(self.logFile, "r") as file:
            with ThreadPoolExecutor(max_workers=self.maxThreads) as executor:
                while True:
                    chunk = file.readlines(self.chunk_size)
                    if not chunk:
                        break
                    executor.submit(self.processChunk, chunk)
        

    def printResults(self):
        with open("OutputPortProtocolCounts.csv", mode="w") as file:
            file.write("Port/Protocol Combination Counts:\n")
            file.write("Port,Protocol,Count\n")
            for protocol, portCount in self.portProtocolCount.items():
                for port, count in portCount.items():
                    file.write(f"{port},{protocol},{count}\n")
        with open("OutputTagCounts.csv", mode="w") as file:
            file.write("Tag Counts:\n")
            file.write("Tag,Count\n")
            for tag, count in self.tagCount.items():
                file.write(f"{tag},{count}\n")
if(len(sys.argv)<4):
    print("Please pass necessay arguments as mentioned in Readme file")
    #protocolMappingFile, lookupFile, logFile = "protocol-numbers-1.csv", "Lookup.csv", "SampleLog.log"
else:
    protocolMappingFile, lookupFile, logFile = sys.argv[1], sys.argv[2], sys.argv[3]
    mySolution = Solution(protocolMappingFile, lookupFile, logFile)
    mySolution.processLogs()
    mySolution.printResults()
