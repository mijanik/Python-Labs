from PIL import Image
import os

def main():
    convert(r"pictures\", ".jpg", ".png")

def convert(path, old_extension, new_extension):
    count = 0
    for file in os.listdir(path):
        if file.endswith(old_extension):
            count += 1
            myimage = Image.open(path + file)
            newfile = file.replace(old_extension, new_extension)
            myimage.save(path + newfile)
            print("konwertowanie do " + new_extension + " : " + file)

    print("liczba skonwertowanych plików: " + str(count))

if __name__ == "__main__":
    main()