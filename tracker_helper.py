import csv

# tracker row object: [filename, status, last modified timestamp]
class TrackerHelper:

    def __init__(self, trackerFileLocation = './tracker.csv'):
        self.localFileLocation = trackerFileLocation
        self.rows = {}
        self.dirtyFlag = False
        self.loaded = False

    """ def __del__(self):
        self.updateTrackerFile() """

    def downloadTrackerFile(self):
        pass

    def loadTrackerFile(self):
        try:
            with open(self.localFileLocation, 'r') as csvfile:
                c = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in c:
                    self.rows.update({row[0]: row})
            print('tracker file %s loaded' % self.localFileLocation)
            self.loaded = True
        except OSError as e:
            file =  open(self.localFileLocation, 'w')
            file.close()
            print('creating new tracker file')
        

    def updateTrackerObject(self, filename, status, timestamp):
        if self.loaded == False:
            self.loadTrackerFile()

        row = [filename, status, timestamp]
        if row[0] in self.rows.keys():
            if self.rows[row[0]] != row: 
                self.rows[row[0]] = row
                self.dirtyFlag = True
        else:
            self.rows.update({row[0]: row})
            self.dirtyFlag = True
    
    def updateTrackerFile(self):
        if self.dirtyFlag == True: # changes detected
            with open(self.localFileLocation, 'w') as file:
                for key in self.rows.keys():
                    file.write('%s\n' % (','.join(self.rows[key])))
            self.dirtyFlag = False # reset flag
        else:
            print('no changes detected')

    def fileExistsInTracker(self, filename):
        if self.loaded == False:
            self.loadTrackerFile()
            
        if filename in self.rows.keys():
            print('%s file found in tracker' % filename)
            return self.rows[filename]
        else:
            print('%s file not found in tracker' % filename)
            return None

if __name__ == '__main__':
    h = TrackerHelper()
    h.loadTrackerFile()
    h.updateTrackerObject('PUBLIC_DISPATCHIS_201903311504_0000000306165488.zip','downloaded','sometimestamp')
    #h.updateTrackerObject(['PUBLIC_DISPATCHIS_201903311505_0000000306165488.zip','downloaded','sometimestamp'])
    h.updateTrackerObject('PUBLIC_DISPATCHIS_201903311505_0000000306165488.zip','downloaded','someothertimestamp')
    h.updateTrackerFile()