import csv

class EmmsFileHelper:

    def extractTables(self, fileName):
        tables = []
        tableRows = []
        tableHeader = ''
        dataset = ''
        tableName = ''
        timestamp = ''

        with open(fileName, 'r') as csvfile:
            c = csv.reader(csvfile, delimiter=',', quotechar='"')
                
            for row in c:
                #print(row[0])
                if row[0] == 'C' and row[1] == 'NEMP.WORLD': # master row, has dataset info in it
                    dataset = row[2]
                    timestamp = row[7]
                if row[0] == 'I': # header row
                    if len(tableRows) > 0: # if there are table rows then create full table object and add it to tables list
                        tables.append({'table': tableName, 'header': tableHeader, 'rows': tableRows, 'timestamp': timestamp})
                        tableRows = []

                    tableHeader = row[4:]
                    tableName = '%s_%s_%s' % (dataset, row[1], row[2])
                if row[0] == 'D': # data row
                    tableRows.append(row[4:])
                if row[0] == 'C' and row[1] == 'END OF REPORT': # final row
                    if len(tableRows) > 0: # if there are table rows then create full table object and add it to tables list
                        tables.append({'table': tableName, 'header': tableHeader, 'rows': tableRows, 'timestamp': timestamp})
                        tableRows = []
        
        return tables

    def writeTableToFile(self, table, tempdir):
        filename = '%s/%s_%s.csv' % (tempdir, table['table'], table['timestamp'])
        with open(filename, 'w') as file:
            file.write('%s\n' % ','.join(table['header']))
            for row in table['rows']:
                file.write('%s\n' % ','.join(row))
        
        return filename

if __name__ == '__main__':
    h = EmmsFileHelper()
    t = h.extractTables(r"C:\Users\jmerefield\Documents\Code\EMMS\bHVW78rcRK\PUBLIC_DISPATCHIS_201904020955_0000000306235161.CSV")
    #print(t[0])
    h.writeTableToFile(t[0], './bHVW78rcRK')