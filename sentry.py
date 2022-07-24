startup_file = open("sentry_startup.txt", "r")
contents = startup_file.read()
print(contents)

option = input()

if option == '1':
    #clear model and reset weights and redo setup
    fam_mem = input("How many family members do you live with?\n")
    #capture_faces(fam_mem)
elif option == '2':
    #sentry_mode()
