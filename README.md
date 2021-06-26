# Docron

docron   -   designed to make task scheduling easier

If you are daunted by cron, this program should come in handy.


# Usage

There are a couple of predefined options that can be used:

    OPTION         |       DESCRIPTION

    add    ----->  This makes a new cron job. Users will be guided and asked to respectively input values.
                   By adding additional switches you can modify the behavior of the given option.
                   Adding commas (,) and dashes (-) is not allowed, but the abbreviated forms of
                   months (jan-dec) and days (sun-sat) are. Abbreviated forms are not case-sensitive.
                   Note that year and special characters such as "L", "W", "H", "/" and "#" are not
                   supported.

    @      ----->  User is asked to input the time of the command's execution.
                   Allowed switches are: @yearly (or @annually), @monthly, @weekly, @daily,
                   @hourly, and @reboot.
                   The user will be asked to specify a command and choose the switches.
                   The leading (at) symbol has to be given;

    delete ----->  Deletes the entire cron list;

    view   ----->  See the list of cron jobs;

    help   ----->  Check the manual. Should you need help with the cron itself
                   then consult cron's manual by typing in the terminal "man cron".



# Heads Up


- If one doesn't explicitly write "no" or "n" when being asked whether or not to save the cron job,
the program will save the cron job as if one specified "yes";

- If one decides to enter a letter where the program expects a number, the "*" symbol will be added;

- Abbreviations (jan-dec | sun-sat) have to be written in the lowercase;

- If one is using the "@" option, make sure the input has the leading "@":

    DO:     > Which one will you choose: @reboot

    DON'T:  > Which one will you choose: reboot

- When "delete" is chosen, only "yes" is acceptable when it comes to removing cron jobs.
It has been purposely designed like that to hinder (or prevent an accidental) deletion.

- Slackware handles some crontab switches differently than Ubuntu does, hence some small
insignificant differences can be spotted. For example, when running the "view" option,
Ubuntu returns code 1 if there are no cron jobs, where Slackware returns code 0,
even though both of them recognize "no crontab for USERNAME" as an error.

- All .py files must be executable. If they are not, then run a simple command
( chmod 755 /usr/tools/docron/*.py ) or ( chmod 755 *.py ), depending on the 
location of Docron files

- If the program raises the error "Error: File not found", it means that it couldn't find
executable files where they are supposed to be (/usr/tools/docron or
in the current working directory - where Docron is downloaded).
In that case, check the integrity of Docron files.



# Feature (optional)

This is NOT a must!
If one wants to type "docron" regardless of the position on the system, this has to be followed.
Otherwise, one has to start the program from the directory where they have Docron downloaded.

Note: if .bashrc is not found in the home directory, it will be created.

1. Run "add_REMOVE_docron.py" -- to do so, position yourself in the directory where Docron is downloaded,
type "./add_REMOVE_docron.py", and press Enter to start the script;
2. When the script runs, type "add" so that it can make required directories and files;
3. DONE!


Note: If you do not want this option, then make sure you are running the program
from the directory where other Docron scripts are located! In that case,
the file you want to run is called "docron.sh".


Use the program with caution.    



Tested on:  Ubuntu      20.04.1 // 20.04.2
            Slackware   4.4.14

Python 3.8.5
Modified: 26.6.2021



