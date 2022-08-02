import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BMjJI-ZmQ3IbPMo9s2Dm6QRh_GuAHeEsp03avJ_YTGYIQEuD44mgjLtFGvM-CZ6jqU38lN1JqhI9M7f9KEF2QRo-WOxTqV4lgGa_qhfSXwtYHJiaX5XGjnieOSx5HlyIi-lUn2Y'
    transferData = TransferData(access_token)

    file_from = input('Enter the full part')
    file_to = 'Dylan App'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()