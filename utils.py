def add_task(task_name, tasks):
    task = { 'task': task_name, 'completed': False}
    tasks.append(task)
    print ('Success!')

def list_tasks(tasks):
    print ('Tasks:')
    for i, task in enumerate(tasks, start=1):
        status = '✔' if task['completed'] else ' '
        print (f'{i}. [{status}] {task['task']}')

def update_task(task_index, new_task_name, tasks):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['task'] = new_task_name
        print ('Success!')
    else:
        print('Invalid task index. Please choose a valid task.')

def complete_task(task_index, tasks):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        print ('Success!')
    else:
        print('Invalid task index. Please choose a valid task.')

def delete_task(task_index, tasks):
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        print ('Success!')
    else:
        print('Invalid task index. Please choose a valid task.')