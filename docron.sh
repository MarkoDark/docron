#!/bin/bash

# The main menu

while true
do
    echo 'Type: "add", "delete", "view", "help", or "exit"'
    read -p '>> ' user
    uinfo=$(whoami)


    case ${user,,} in

        add)
            python3 /usr/tools/docron/dadd.py || ./dadd.py
            ;;
        @)
            python3 /usr/tools/docron/dadd_at.py || ./dadd_at.py
            ;;
            
        delete)
            python3 /usr/tools/docron/ddelete.py || ./ddelete.py
            ;;

        view)
            python3 /usr/tools/docron/dview.py || ./dview.py
            ;;

        help)
            echo "$(cat /usr/tools/docron/dhelp.txt)" || echo "$(cat ./dhelp.txt)"
            ;;

        exit)
            for i in {1..30}; do printf '%s' '-'; done; printf '\n'
            echo '> Bye '$uinfo''
            for i in {1..30}; do printf '%s' '-'; done; printf '\n'
            exit 1    
            ;;
        *)
            for i in {1..30}; do printf '%s' '-'; done; printf '\n'
            echo "> Whatever you did was not nice..."
            for i in {1..30}; do printf '%s' '-'; done; printf '\n'
    esac

done
exit 0

