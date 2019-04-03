from emms_website_helper import EmmsWebsiteHelper
from zip_helper import ZipHelper
from emms_file_helper import EmmsFileHelper
from tracker_helper import TrackerHelper
import utils

ewh = EmmsWebsiteHelper()
zh = ZipHelper()
efh = EmmsFileHelper()
th = TrackerHelper()

def manageFile(link):
    print(link)
    # check if exists and it's status
    fileInTracker = th.fileExistsInTracker(link['name'])
    processLink = True
    if fileInTracker != None:
        if fileInTracker[1] in ['downloaded', 'extracted']:
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
    else:
        print('%s already processed' % link['name'])

ewh.getPage("http://www.nemweb.com.au/REPORTS/CURRENT/DispatchIS_Reports/")
l = ewh.getLinks()
for link in l:
    manageFile(link)

th.updateTrackerFile()