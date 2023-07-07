def task_my_task():
    return{
        "actions":[
            "echo parametized passt > %(targets)s"
        ],
        "targets":['my_task.txt'],
        "clean":True
        
    }