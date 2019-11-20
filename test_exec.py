import os
import sys

def run_test(project):
    CWD = os.getcwd()
    os.system('python ' + CWD + '\\' + project + '\\test.py')

def main():

    scripthelp = 'Must provide product dir: \n test_exec.py <PRODUCT DIR>'

    if len(sys.argv) == 1:
        print(scripthelp)
    else:
        run_test(sys.argv[1])

main()
