
# labels for user convience
print("we have three programs students_to_teacher,battleship and exam_stats")
print("please enter a/A for battleship")
print("please enter b/B for students_to_teacher")
print("please enter c/C for exam_stats")


choice = input("enter your choice::")# to take input from user
if choice =="a" or choice=="A":
	import battleship
	battleship.main_of_battleship() # it will call the battleship program

elif choice =="b" or choice=="B":
	import students_to_teacher
	students_to_teacher.main_of_students_teacher() # it will call students_to_teacher program

elif choice =="c" or choice=="C":
	import exam_stats
	exam_stats.main_of_examstats() # it will call exam_stats program

else:
	print("wrong choice") #if user does not enter acc to requirement
