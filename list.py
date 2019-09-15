from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json
import datetime

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)


for file_list in drive.ListFile({'q':"mimeType='application/vnd.google-apps.folder'"}):
 for file1 in file_list:
  print('title: %s, id: %s ,modified: %s' % (file1['title'], file1['id'],file1['modifiedDate']))
  #parsed=json.dumps(file1,indent=4)
  #print(parsed)
