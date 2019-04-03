import zipfile
from os.path import basename

class ZipHelper:
    #def __init__(self):

    def zipSingleFile(self, archiveFileName, singleFilePath):
        try:
            zip_file = zipfile.ZipFile(archiveFileName, 'w')
            zip_file.write(singleFilePath, basename(singleFilePath), compress_type=zipfile.ZIP_DEFLATED)
            zip_file.close()
        except zipfile.BadZipFile as e:
            print(e)

    def unzipAll(self, archiveFileName, pathToExtractTo):
        try:
            zip_file = zipfile.ZipFile(archiveFileName )
            zip_file.extractall(pathToExtractTo)
            zip_file.close()
        except zipfile.BadZipFile as e:
            print(e)

if __name__ == '__main__':
    z = ZipHelper()
    z.zipSingleFile(r'C:\Users\jmerefield\Documents\Code\EMMS\archive.zip', r'C:\Users\jmerefield\Documents\sample.txt')
    z.unzipAll(r'C:\Users\jmerefield\Documents\Code\EMMS\archive.zip', r'C:\Users\jmerefield\Documents\Code\EMMS')
