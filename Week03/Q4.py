monday_class = {"Alice", "Bob", "Charlie", "Diana"}
wednesday_class = {"Bob", "Diana", "Eve", "Frank"}
monday_class.add("Grace")
print(f"Monday Class: {monday_class}")
print(f"Wednesday Class: {wednesday_class}")
print(f"Attend both classes: {monday_class & wednesday_class}")
print(f"Attend either classses: {monday_class | wednesday_class}")
print(f"Only Monday class: {monday_class - wednesday_class}")
print(f"Only One class: {monday_class ^ wednesday_class}")
allStudents = monday_class | wednesday_class
print("Is Monday subset of ALL students? ", monday_class <= allStudents) 