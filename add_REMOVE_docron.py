#!/usr/bin/env python3

import subprocess
from subprocess import Popen, PIPE
import os
import re
import time
import sys

# Adding/removing Docron necessities

# ASK USER
while True:
    try:
        print('='*60)
        user = input('> You can "add" or "remove" Docron. What will it be?\n>> ')
        print('='*60)

        ################################ ADD ################################
        if user.lower() == 'add':
            print('\n-- Checking Docron necessities --\n')
            time.sleep(1)
            print('-'*30)
            ####
            iamraw = subprocess.run('whoami', capture_output=True, encoding='ascii')
            iam = iamraw.stdout.strip()

            # Get the HOME directory path from the environment variable
            home_path = os.environ['HOME']

            # If the user is using the root account
            # check whether or not .bashrc exists in the root home directory
            if iam == 'root':
                bashex = f'[ -f /root/.bashrc ] && echo "File .bashrc exists!"'

                iambash = subprocess.run(bashex, capture_output=True, encoding='ascii', shell=True)
                does_bash_exist = iambash.stdout.strip()
                if does_bash_exist == 'File .bashrc exists!':
                    print('-- File .bashrc exists --')
                else:
                    touch_bashrc = 'touch /root/.bashrc'
                    create_bashrc = subprocess.run(touch_bashrc, shell=True, encoding='ascii')
                    print('-- File .bashrc created --')

            else:
                # Check if the .bashrc exists in the USER home directory
                bashex = f'[ -f /home/{iam}/.bashrc ] && echo "File .bashrc exists!"'
                iambash = subprocess.run(bashex, capture_output=True, encoding='ascii', shell=True)
                does_bash_exist = iambash.stdout.strip()
                if does_bash_exist == 'File .bashrc exists!':
                    print('-- File .bashrc exists --')
                else:
                    touch_bashrc = f'touch /home/{iam}/.bashrc'
                    create_bashrc = subprocess.run(touch_bashrc, shell=True, encoding='ascii')
                    print('-- File .bashrc created --')
            ####
            f = open(f'{home_path}/.bashrc', 'r')
            l = f.read()
            bashre = re.search(r'alias docron.*', l)
            bpath = re.search(r'export PATH=\$PATH:/usr/tools/', l)
            f.close()
            ## Checks the path
            toolspath = '/usr/tools/docron/'
            tools = os.path.exists (toolspath)
            wbashwrite = "alias docron='/usr/tools/docron/docron.sh'"

            # ADD ALIAS
            if bashre == None:
                f1 = open(f'{home_path}/.bashrc', 'a')
                f1.write(wbashwrite)
                f1.write('\n')
                f1.close()
                rload = f'. ~/.bashrc'
                rloadcmd = subprocess.Popen(['/bin/bash', '-c', rload])
                time.sleep(2)
                #print('-'*30)
                print('-- Alias created --')
                pass
            else:
                #print('-'*30)
                print('-- Alias already exists --')
                pass

            # Makes a /usr/tools/docron/ directory
            # Checks if /usr/tools/docron/ already exists
            if tools == False:
                time.sleep(1)
                mkdir = 'sudo -S mkdir -p /usr/tools/docron/'.split()
                mkdircmd = subprocess.run(mkdir, stdout=True, encoding='ascii')
                time.sleep(1)
                chmod = 'sudo -S chmod -R 755 /usr/tools/docron/'.split()
                chmodcmd = subprocess.run(chmod, stdout=True, encoding='ascii')
                print('-- Directory created --')
                pass
            else:
                print('-- Directory already exists --')
                pass

            # COPY-PASTE FILES TO /usr/tools/docron/

            # test path
            testerpath = '/usr/tools/docron/'
            tester = os.path.exists(testerpath)

            # pwd
            pwdcmd = subprocess.run('pwd', capture_output=subprocess.PIPE, encoding='ascii')
            pwd = pwdcmd.stdout.strip()


            # Initiate actual copy-pasting 
            if tester == True:
                filethere = re.compile(r'(.*py$) | (.*sh$) | (.*txt$)')
                foundfiles = 0
                for root, dirs, files in os.walk(testerpath):
                    # Only .py .sh .txt files count!
                    for afile in files:
                        if afile.endswith('.py') or afile.endswith('.sh') or afile.endswith('.txt') == True:
                            foundfiles +=1

                # Number of found files has to be 7
                if foundfiles < 7:
                    # The full name is given in case the user already has something that
                    # coincidentally shares the same name with Docron files
                    cp = f'sudo -S cp {pwd}/add_REMOVE_docron.py {pwd}/dadd_at.py {pwd}/dadd.py {pwd}/ddelete.py {pwd}/dview.py {pwd}/docron.sh {pwd}/dhelp.txt /usr/tools/docron/'.split()
                    cpcmd = subprocess.run(cp, stdout=PIPE, stderr=PIPE, encoding='ascii')
                    print('-- Files transfered --')
                    pass
                elif foundfiles == 7:
                    print('-- Files already exist --')
                    pass
                else:
                    print('-- Interestingly, you have', foundfiles, 'out of 7 files in there --')
                    pass
            else:
                print('-- Files already exist --')
                pass

            # Adding /usr/tools/ to the PATH 
            if bpath == None:
                #cleanbpath = bpath.group()
                pathvar = 'export PATH=$PATH:/usr/tools/'
                f2 = open(f'{home_path}/.bashrc', 'a')
                f2.write(pathvar)
                f2.write('\n')
                f2.close()
                rload = f'. {home_path}/.bashrc'
                rloadcmd = subprocess.Popen(['/bin/bash', '-c', rload])
                time.sleep(2)
                print('-- PATH variable created --')
                print('-'*30)
                time.sleep(1)
                print('\n-- From now on you can just type "docron" --\n')
                print('='*60)
                sys.exit(0)

            else:
                print('-- PATH variable already exists --')
                print('-'*30)
                time.sleep(1)
                print('\n-- From now on you can just type "docron" --\n')
                print('='*60)
                sys.exit(0)



        ############################## REMOVE ##############################
        elif user.lower() == 'remove':
            print('\n-- Docron will be removed from your system --\n')
            ### Regex for docron alias
            f = open(f'{home_path}/.bashrc', 'r')
            l = f.read()
            bashre = re.search(r'alias docron.*', l)
            f.close() 

            # REMOVE ALIAS
            time.sleep(1)
            if bashre != None:
                b = open(f'{home_path}/.bashrc', 'rt')
                data = b.read()
                bashrerraw = re.search(r'alias docron.*', l)
                basher = bashrerraw.group()
                empty = ''
                rep = data.replace(basher, empty)
                b.close()
                b = open(f'{home_path}/.bashrc', 'wt')
                b.write(rep)
                b.close()
                print('-'*30)
                print('-- Alias removed --')
                pass
            else:
                print('-'*30)
                print('-- Alias already gone --')
                pass

            # REMOVE DIRECTORY
            time.sleep(1)
            toolsspath = '/usr/tools/docron'
            etools = os.path.exists (toolsspath)
            if etools == True:
                rmdir = 'sudo -S rm -r /usr/tools/docron'.split()
                rmdircmd = subprocess.run(rmdir, stdout=True, encoding='ascii')
                print('-- Directory removed --')
                pass
            else:
                print('-- Directory already gone --')
                pass

            
            # REMOVE PATH VARIABLE
            p1 = open(f'{home_path}/.bashrc', 'r')
            p1r = p1.read()
            bpath = re.search(r'export PATH=\$PATH:/usr/tools/', p1r)
            p1.close()

            if bpath == None:
                print('-- PATH variable already gone --')
                pass
            else:
                nostr = ' '
                p2 = open(f'{home_path}/.bashrc', 'rt')
                p2data = p2.read()
                bpathclean = bpath.group()
                p2datareplace = p2data.replace(bpathclean, nostr)
                p2.close()
                p3 = open(f'{home_path}/.bashrc', 'wt')
                p3.write(p2datareplace)
                p3.close()
                print('-- PATH variable removed --')
                pass
            
            # USER INSTRUCTIONS
            time.sleep(1)
            print('-'*30)
            print('\n')
            print('--> To completely remove all Docron files from the system\n    just copy-paste the following command in the terminal:\n')
            print('    sudo rm -r /usr/tools/docron/')
            print('\n')
            time.sleep(1)
            print('='*60)
            sys.exit(1)

        else:
            print('> Whatever you wanted to type was wrong... Try again!')
    except KeyboardInterrupt:
        print('\n')
        print('-'*50)
        print('-- Program has been *forcefully* terminated --')
        print('-'*50)
        sys.exit(0)
    except EOFError:
        print('\n')
        print('-'*50)
        print('-- Program has been *forcefully* terminated --')
        print('-'*50)
        sys.exit(0)
    except SystemExit:
        sys.exit(0)
    except:
        print('\n')
        print('-'*30)
        print('-- Well, something bad happened --')
        print('-'*30)
        sys.exit(0)
