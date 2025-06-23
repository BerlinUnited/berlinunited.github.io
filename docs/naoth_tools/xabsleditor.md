# Xabsleditor
Xabsleditor (eXtensive agent behavior specification language editor) is our home cooked editor with code highlighting and syntax checking for the description language XABSL.
Though it might seem complex at first, this is a powerful tool that, in combinition with recording the behavior that the robot went through during gameplay, allows for reasonably easy debugging of behavior bugs.
The .xabsl files are located inside `</path/to/mainRepo>/NaoTHSoccer/Source/Cognition/Modules/Behavior/XABSLBehaviorControl`.

!!! note
    This documentation lacks implementation details (intermediary code, gradle)

- TODO: Move and expand Xabsl documentation from the team report.

## Starting Xabsleditor
Xabsleditor is located inside its own repository.
It is started by running the gradlew executable inside.
Because it needs Java 11, either change your system Java before execution, or, if on linux:
- Download latest JDK from [here](https://adoptium.net/en-GB/temurin/releases/?version=11&os=linux&arch=x64)
- Untar to ~/.local so that the path is `~/.local/jdk-11.0.<number>`
- Now start Xabsleditor with `env JAVA_HOME=~/.local/jdk-11.<number> </path/to/XabsleditorRepo>/gradlew`
Tipp: Set yourself an [alias](https://www.geeksforgeeks.org/alias-command-in-linux-with-examples/#how-to-create-an-aliases-persistent) for this.

## Current behavior in a nutshell
TODO: Outline when init, when idle, etc.

## Xabsleditor features
### Transition graphs
Once a .xabsl file is loaded, for example /Options/Roles/role_default.xabsl (they are all located inside `</path/to/mainRepo>/NaoTHSoccer/Source/Cognition/Modules/Behavior/XABSLBehaviorControl`) you should see a state graph on the right side. Each node represents a `state {}` in your code on the left.
### Symbols
TODO
