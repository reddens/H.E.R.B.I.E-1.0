import todo
def task(do, query):
    if do == "create":
        todo.create_task(query, "reminder")
        return "Task: {query}, saved"
    elif do == "delete":
        todo.delete_task(query)
        return "Taks: {query}, deleted"
    elif do == "show":
         data = todo.display_data()
    else:
        return "Sorry, I didn't get that"