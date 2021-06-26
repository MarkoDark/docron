#!/bin/bash

# The main menu

while true
do
    echo 'Type: "add", "delete", "view", "help", or "exit"'
    read -p '>> ' user
    uinfo=$(whoami)


    case ${user,,} in

        add)
            if [ -f /usr/tools/docron/dadd.py ]; then
                python3 /usr/tools/docron/dadd.py
            elif [ -f ./dadd.py ]; then
                python3 ./dadd.py
            else
                for i in {1..30}; do printf '%s' '-'; done; printf '\n'
                echo "|-- Error: File not found! --|"
                for i in {1..30}; do printf '%s' '-'; done; printf '\n'
            fi
                ;;
        @)
            if [ -f /usr/tools/docron/dadd_at.py ]; then
                python3 /usr/tools/docron/dadd_at.py
            elif [ -f ./dadd_at.py ]; then
                python3 ./dadd_at.py
            else
                for i in {1..30}; do printf '%s' '-'; done; printf '\n'
                echo "|-- Error: File not found! --|"
                for i in {1..30}; do printf '%s' '-'; done; printf '\n'
            fi
                ;;

        delete)
            if [ -f /usr/tools/docron/ddelete.py ]; then
                python3 /usr/tools/docron/ddelete.py
            elif [ -f ./ddelete.py ]; then
                python3 ./ddelete.py
            else
                for i in {1..30}; do printf '%s' '-'; done; printf '\n'
                echo "|-- Error: File not found! --|"
                for i in {1..30}; do printf '%s' '-'; done; printf '\n'
            fi
                ;;



        view)
            if [ -f /usr/tools/docron/dview.py ]; then
                python3 /usr/tools/docron/dview.py
            elif [ -f ./dview.py ]; then
                python3 ./dview.py
            else
                for i in {1..30}; do printf '%s' '-'; done; printf '\n'
                echo "|-- Error: File not found! --|"
                for i in {1..30}; do printf '%s' '-'; done; printf '\n'
            fi
                ;;

        help)
            if [ -f /usr/tools/docron/dhelp.txt ]; then
                echo "$(cat /usr/tools/docron/dhelp.txt)"
            elif [ -f ./dhelp.txt ]; then
                echo "$(cat ./dhelp.txt)"
            else
                for i in {1..30}; do printf '%s' '-'; done; printf '\n'
                echo "|-- Error: File not found! --|"
                for i in {1..30}; do printf '%s' '-'; done; printf '\n'
            fi
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
            ;;
    esac

done
exit 0

