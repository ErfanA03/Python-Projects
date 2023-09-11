

import os


file_Name = 'Hello.txt'


file_Path = 'C:\\A\\'


ab_Path = os.path.join(file_Path, file_Name)
print(ab_Path)
