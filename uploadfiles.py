import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BG7RMr5AcFeMG4s-boQBUjN7zW0O6XYSXpul8YGYtdOBRBdD3MQ2w7QCRAPU9Kh7K2CRWedjSuJFKq7bZ8RGgoPvnIZEX3JOMTmzGgswNZ0qmDIBK8clyT4L2fTQqn2Lm0n_ujhDrm3n'
    transferData = TransferData(access_token)

    file_from = input("enter folder path")
    file_to = input("enter the full path to upload to dropbox:- ")  

    transferData.upload_file(file_from,file_to)
if __name__ == '__main__':
    main()