# Git-Hooks
!!! note
    TODO: explain how to set them up on windows with cygwin.

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

**~/project/.git/hooks/pre-commit**
    
    #!/bin/sh
    
    # Reject any commit that would add a line with tabs.
    #
    # You can enable this as a repo policy with
    #
    #   git config hooks.allowtabs true
    
    allowtabs=$(git config hooks.allowtabs)
    
    if [ "$allowtabs" != "true" ] &&
       # we check only tabs that would be added by this commit
       git diff --cached '*.c' '*.h' '*.cpp' '*.hpp' | grep -E '^\+.*	'>/dev/null
    then
       cat<<END;
    [ERROR]: This commit adds TABS! Replace all tabs with spaces.
    If you know what you are doing you can force this commit with:
      git commit --no-verify
    Or change the repo policy like so:
      git config hooks.allowtabs true
    Tabs in :
    END
    
      # show all tabs
      #git grep -n --cached '	'
      
      # show only tabs that would be added in the commit
      git diff --cached '*.c' '*.h' '*.cpp' '*.hpp' | grep -E '^\+.*'
      exit 1
    fi
