import csv

class EmmsFileHelper:

    def extractTables(self, fileName):
        tables = []
        tableRows = []
        tableHeader = ''
        dataset = ''
        tableName = ''

        with open(fileName, 'r') as csvfile:
            c = csv.reader(csvfile, delimiter=',', quotechar='"')
                
            for row in c:
                print(row[0])
                if row[0] == 'C' and row[1] == 'NEMP.WORLD': # master row, has dataset info in it
                    dataset = row[2]
                if row[0] == 'I': # header row
                    if len(tableRows) > 0: # if there are table rows then create full table object and add it to tables list
                        tables.append({'table': tableName, 'header': tableHeader, 'rows': tableRows})
                        tableRows = []

                    tableHeader = row[4:]
                    tableName = '%s_%s_%s' % (dataset, row[1], row[2])
                if row[0] == 'D': # data row
                    tableRows.append(row[4:])
                if row[0] == 'C' and row[1] == 'END OF REPORT': # final row
                    if len(tableRows) > 0: # if there are table rows then create full table object and add it to tables list
                        tables.append({'table': tableName, 'header': tableHeader, 'rows': tableRows})
                        tableRows = []
        
        return tables


if __name__ == '__main__':
    h = EmmsFileHelper()
    t = h.extractTables(r"C:\Users\jmerefield\Documents\Code\EMMS\downloads\PUBLIC_DISPATCHIS_201903280905_0000000306037619.CSV")
    print(t)