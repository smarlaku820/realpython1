import os
import glob

if __name__ == "__main__":
    base_path = "C:/Users/zc11/PycharmProjects/realpython1/part2/book1-exercises-master/chp09/practice_files/images"

    # Display full paths of all the files and folders in the base_path
    file_list = os.listdir(base_path)
    for file in file_list:
        print(os.path.join(base_path, file))

    # Display the full paths of any PNG files in the images folder by using glob.glob()
    possible_files = os.path.join(base_path, '*/*.png')
    for file in glob.glob(possible_files):
        print(file)

    # Rename any PNG files in the images folder and its subfolders to be JPG files by using os.walk()
    for current_folder, sub_folders, file_list in os.walk(base_path):
        for file in file_list:
            full_path = os.path.join(current_folder, file)
            fileName, extension = os.path.splitext(full_path)
            if extension == '.png':
                os.rename(full_path, fileName+".jpg")
                if os.path.exists(fileName+".jpg"):
                    print("Yes file exists {}".format(fileName+".jpg"))
