from emms_website_helper import EmmsWebsiteHelper
from zip_helper import ZipHelper
from emms_file_helper import EmmsFileHelper
from tracker_helper import TrackerHelper
from s3_helper import S3Helper
import utils

ewh = EmmsWebsiteHelper()
zh = ZipHelper()
efh = EmmsFileHelper()
th = TrackerHelper()
s3h = S3Helper()

def manageFile(link):
    print(link)
    # check if exists and it's status
    fileInTracker = th.fileExistsInTracker(link['name'])
    processLink = True
    if fileInTracker != None:
        if fileInTracker[1] in ['processed', 'uploaded']: # TBC
            processLink = False
    
    if processLink:
        # download file location
        dfl = '%s%s' % ('./downloads/', link['name'])
        # download zipped file
        ewh.downloadFile(link['href'], dfl)
        th.updateTrackerObject(link['name'], 'downloaded', utils.getCurrentTimestamp())
        # create random folder
        extractFolder = './%s' % utils.randomStringDigits(10)
        print(extractFolder)
        utils.createFolder(extractFolder)
        # extract file
        zh.unzipAll(dfl, extractFolder)
        th.updateTrackerObject(link['name'], 'extracted', utils.getCurrentTimestamp())
        # process file
        for path in utils.getCsvFilesFromDirectory(extractFolder):
            t = efh.extractTables(path)
            th.updateTrackerObject(link['name'], 'processed', utils.getCurrentTimestamp())
            #write tables to files and upload to S3
            for table in t:
                newFile = efh.writeTableToFile(table, extractFolder)
                key = 'NEW_FORMAT/%s/%s.csv' % (table['table'], table['dispatchTimestamp'])
                s3h.uploadFile(newFile, 'netsystems-emms', key)
            th.updateTrackerObject(link['name'], 'uploaded', utils.getCurrentTimestamp())
        
        # remove directory - tbd only if successful?
        utils.deleteFolder(extractFolder)
        # delete original downloaded file
        utils.deleteFile(dfl)
                
    else:
        print('%s already processed' % link['name'])

ewh.getPage("http://www.nemweb.com.au/REPORTS/CURRENT/DispatchIS_Reports/")
l = ewh.getLinks()
for link in l:
    manageFile(link)

th.updateTrackerFile()