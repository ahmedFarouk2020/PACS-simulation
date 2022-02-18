import os

""" Handle images in a folder [store] """

class DB:
    def __init__(self) -> None:
        pass

    def __create_new_dir(self, dir="./DB"):
        try:
            os.mkdir(dir)
        except:
            pass

    def store(self, filename: str, data: bytes):
        self.__create_new_dir()
        with open("./DB/"+filename,mode='wb') as file:
            file.write(data)
            file.close()
        print("Image is saved")