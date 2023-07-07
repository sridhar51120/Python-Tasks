def task_python_help():
    return {
        "actions": [
            "python -h > %(targets)s",
        ],
        "targets": ["python.help"],
        "clean": True
    }


def task_doit_help():
    return {
        "actions": [
            "doit help > %(targets)s",
        ],
        "targets": ["doit.help"],
        "clean": True
    }
