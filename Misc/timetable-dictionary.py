target = "Y13_New_Timetable.csv"

teacher_dict = {"RB": "Miss R. Biggs",
                "FEH": "Mrs F. Harvey",
                "LJN": "Mrs L. Nightingale",
                "LAR": "Dr L. Rackham",
                "PG": "Mr P. Groom",
                "SM": "Mr S. McCrink",
                "SEM": "Mrs S. Mahony",
                "SPF": "Mr S. Fairfield",
                "TJW": "Mr T. Wilson",
                "JHW": "Mrs J-H Wang"}

with open(target, "r") as csvtimetable:
    rows = [[string.replace(chr(194), chr(32)).strip() for string in row.split(",")][1:] for row in csvtimetable.readlines()[5:]]

lessons = []
for i in range(0, len(rows), 2):
    info = []
    for msg in rows[i+1]:
        splitmsg = msg.split(" ")
        if len(splitmsg) == 1:
            room = splitmsg[0]
            info.append(room)
        else:
            teacher = splitmsg[0]
            room = splitmsg[1]
            teacher = teacher_dict[teacher.upper()] if teacher.upper() in teacher_dict.keys() else teacher.upper()
            info.append(f"{room}, {teacher}")

    lessons.append(list(zip(rows[i], info)))

lessons = [[lesson if lesson != ("", "") else tuple() for lesson in row] for row in lessons]
# SIMS OUTPUT CSV CODE
#
# with open(target, "r") as csvtimetable:
#     rows = [[string.strip() for string in row.split(",")][1:] for row in csvtimetable.readlines()[1:]]
#
# lessons = []
# for i in range(0, len(rows), 3):
#     lessons.append(list(zip(rows[i], [f"{room}, {teacher}" for room, teacher in list(zip(rows[i+1], rows[i+2]))])))
#
# lessons = [[lesson if lesson != ("", ", ") else tuple() for lesson in row] for row in lessons]

# WEIRD OTHER CSV CODE

days = list(zip(*lessons))

endarray = {1: {}, 2: {}}
daysofweek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# insertMorning = {"Monday": ("HRG", days[0][0][1]),
#                  "Tuesday": ("Whole School Assembly", "LFH"),
#                  "Wednesday": ("Chapel / Assembly / Tutor",),
#                  "Thursday": ("Chapel / Assembly / Tutor",),
#                  "Friday": ("Chapel / Assembly / Tutor",)}

insertMorning = {"Monday": ("HRG", days[0][0][1]),
                 "Tuesday": ("Assembly / HRG Activity", days[0][0][1]),
                 "Wednesday": ("HRG", days[0][0][1]),
                 "Thursday": ("HRG", days[0][0][1]),
                 "Friday": ("HRG", days[0][0][1])}

for week in range(2):
    for i, day in enumerate(daysofweek):
        i += week * 5
        dayList = list(days[i]).copy()
        dayList.insert(1, insertMorning[day])
        dayList.insert(3, ("Break", "Social Spaces"))
        dayList.insert(7, ("Break", "In-lesson"))
        dayList.insert(9, ("Lunch Break", "Social Spaces"))
        endarray[week+1][day] = dayList.copy()

for weekNo, week in endarray.items():
    print(f"Week: {weekNo}")
    for dayName, day in week.items():
        print(f"\t{dayName}")
        print("\t\t" + "\n\t\t".join([str(lesson) for lesson in day]).replace("(", "[").replace(")", "]"))

print(str(endarray).replace("(", "[").replace(")", "]") + ";")
