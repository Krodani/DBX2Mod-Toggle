import os

path = "D:\\SteamLibrary\\steamapps\\common\\DB Xenoverse 2\\bin"
enable_Online = (path + "\\xinput1_3(DisabledMod).dll")
enable_Mods = (path + "\\xinput1_3.dll")


def EnableOnline(file):
    if file.endswith("xinput1_3.dll"):

        os.rename(enable_Mods, enable_Online)
        return "Online Enabled Suscesfuly"
    else:
        return "Online is already activated"
    

def EnableMods(file):
    if file.endswith("xinput1_3(DisabledMod).dll"):
        os.rename(enable_Online, enable_Mods)
        return "Mods Enabled Suscesfuly"
    else:
        return "Mods is already activated"


def SwitchCase(numOption):
    switcher = {
        1: EnableOnline,
        2: EnableMods,
    }
    func = switcher.get(numOption, -1)
    if func == -1:
        print("Invalid option")
    else:
        print(func(FileName()))

def FileName():
    files = []
    for i in os.listdir(path):
        if os.path.isfile(os.path.join(path,i)) and 'xinput' in i:
            files.append(i)
    return files[0]


# Menu #
print("(1) Enable Online without mods")
print("(2) Enable mods without online")
print("  Select: ", end = '')

num = input()
SwitchCase(int(num))