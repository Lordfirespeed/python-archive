import re
import os

path = r"C:\Users\joe\AppData\Roaming\Factorio\saves"
saveName = "SEABLOCK".lower()
fileNameMatcher = re.compile(" *%s *-* *\d\d-\d\d-\d\d-\d\d-\d\d *.zip" % saveName)
numberMatcher = re.compile("\d+")

for file in os.listdir(path):
    if re.findall(fileNameMatcher, file.lower()):
        numbers = re.findall(numberMatcher, file)
        numbers[-1] = "20" + numbers[-1]
        numbers.reverse()
        numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        newFileName = saveName + " - " + "-".join(numbers) + ".zip"
        if "n" not in input("Rename %s ?" % file).lower():
            try:
                os.rename(os.path.join(path, file), os.path.join(path, newFileName))
            except FileExistsError:
                os.remove(os.path.join(path, file))
                print("Newfile with timestamp already existed. Removing outdated...")

