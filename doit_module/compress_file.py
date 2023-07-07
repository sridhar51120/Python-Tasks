#  aim -> $ 7z a huge.compressed.7z huge.dat

def task_compress():

    return {
        "actions": [
             "7z a %(targets)s %(dependencies)s",
        ],
        "file_dep": ["huge.dat"],
        "targets": ["huge.compressed.7z"],
        "clean": True
    }