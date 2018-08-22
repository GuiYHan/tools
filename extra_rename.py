import os
def extract_all_file():
    all_file = os.listdir(".")
    all_file = [f for f in all_file if f[-3:] != ".py"]
    for each_file in all_file:
        rename_image(each_file)

def rename_image(folder_name):
    all_pics = os.listdir("./" + folder_name)
    for each in all_pics:
        old = "./" + folder_name + "/" + each
        new = "./" + folder_name + "_" + each
        os.rename(old, new)

if __name__ == "__main__":
    extract_all_file()
