import win32api

list_disc = []

for x in win32api.GetLogicalDriveStrings().split("\x00")[:-1]:
    list_disc.append(x[0:3])

list_disc[0] = 'C:\\Users'
