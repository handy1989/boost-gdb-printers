#!/bin/bash
if [ -x test ] && [ test -nt test.cpp ];then
    echo 'test exist'
else
    echo 'test compiling'
    g++ -g test.cpp -o test || 
    {
        echo 'compilation failed!'
        exit 1
    }
fi
gdb ./test -x ./test.gdb
