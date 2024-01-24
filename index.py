import utils

tasks = []

while True:
    print('TASK MANAGER')
    print('1 - Add')
    print('2 - List')
    print('3 - Update')
    print('4 - Complete')
    print('5 - Delete')
    print('6 - Quit')

    option = input('Choose an option: ')

    if option == '1':
        task_name = input('Task to be added: ')
        utils.add_task(task_name, tasks)

    elif option == '2':
        utils.list_tasks(tasks)

    elif option == '3':
        task_index = int(input('Task to be updated(INDEX): '))
        new_task_name = input('Enter new task name: ')
        utils.update_task(task_index, new_task_name, tasks)

    elif option == '4':
        task_index = int(input('Task to be completed(INDEX): '))
        utils.complete_task(task_index, tasks)

    elif option == '5':
        task_index = int(input('Task to be deleted(INDEX): '))
        utils.delete_task(task_index, tasks)

    elif option == '6':
        print('Program closed')
        break
