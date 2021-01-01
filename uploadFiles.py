import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.accessToken)
    
    for root,dirs,files in os.walk(file_from):
            relativePath = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relativePath)

    with open(local_path,'rb') as f:
        dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.AofWMocyMm6Nnj-NzJjh_PzKk397Scj5DOZnpCBeLIm_kCKjF00eNG7PRqCMqubjH0e7p0QfJr1fosvRLfjfj2QA0EZ8y2HtOf11JgUY_GdcB9id7u3pwBQzG0kk53q2OOa7MmU'
    transferData = TransferData(access_token)

    file_from = input("Please enter the full path of the file you want to backup onto Dropbox: ")
    file_to = input("Enter the destination.(Ex: /foldername/filename): ")

    transferData.upload_file(file_from, file_to)

    print("File successfully transfered!!")

main()