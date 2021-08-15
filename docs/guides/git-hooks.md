# Git-Hooks

If you want to execute a script (sh, python, ...) after a certain git
action (see https://git-scm.com/docs/githooks), you can put an
executeable file with the name of the git action in the
".git/hooks"-project directory.  
For example - (re-)generate the protobuf files:
**~/project/.git/hooks/post-checkout**

    #!/bin/sh

    # $0 - this shell script
    # $1 - previous HEAD reference (Hash)
    # $2 - new HEAD reference (Hash)
    # $3 - Flag:
    #           file checkout   = 0
    #           branch checkout = 1

    NAOTH_MAKE_DIR="/path/to/NaoTHSoccer/Make/"

    echo "Execute custom git hook (protobuf)!"

    if test $3 = 1
    then
        # see: http://stackoverflow.com/questions/4043609/getting-fatal-not-a-git-repository-when-using-post-update-hook-to-execut
        unset GIT_DIR
        cd $NAOTH_MAKE_DIR 1> /dev/null
        premake5 --protoc 1> /dev/null
        cd - 1> /dev/null
    fi


