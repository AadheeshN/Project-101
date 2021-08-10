import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "r2QHYw50mfMAAAAAAAAAARML_2-Wzavp-4Nu6CgwZKrKBD0Qm9KoZ3MhGqJLvDej"
    transferData = TransferData(access_token)   
    file_from = input("Enter the File Path to Transfer to: ")
    file_to = input("Enter the Full Dropbox Path to Transfer File: ") 
    transferData.upload_file(file_from, file_to)
    print("File has been moved to Dropbox!")

main()