from doit import create_after, task
import os

@task
def step1():
    os.system('python script1.py')

@task
def step2():
    os.system('python script2.py')

@task
def step3():
    os.system('python script3.py')

@create_after(executed='step1')
@task
def step2():
    os.system('python script2.py')
default_tasks = ['step1', 'step2', 'step3']


if __name__ == '__main__':
    from doit.main import run
    run()
