# Create a task list.
# A user is presented with the text below.
# Let them select an option to list all of their tasks, add a task to their list, delete a task, or quit the program.
# Make each option a different function in your program. Do NOT use Google. Do NOT use other students. Try to do this on your own.
#
# Congratulations! You're running [YOUR NAME]'s Task List program.
# What would you like to do next?
# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# 0. To quit the program
#
def main():
    problem1()

def problem1():
    # greeting and prompt to the user


    input("Congratulations! You're running Ricardo's Task List program.")
    #userinput=input("What would you like to do next?\n")
    list()



def list():
    myarray=[]
    userinput= ''

    while userinput !='0':
        if userinput == 'list':
            for itemInArray in myarray:
                print(itemInArray)
        if userinput == 'add':
            userinput=(input("what would you like to add?\n"))
            (myarray.append(userinput))

        if userinput == 'delete':
            userinput=(input("What task would you like to delete?\n"))
            (myarray.remove(userinput))
        elif userinput == 'quit':
            input("press 0 to exit!\n")
            break

        userinput=input("What would you like to do next?\n")




if __name__ == '__main__':
    main()