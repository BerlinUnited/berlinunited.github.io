# NaoSCP
NaoSCP is a tool created by us which helps to deploy our code to the NAO. We provide it as a netbeans project inside
our NaoTH repository. The netbeans project is located at `<NaoTH-Projekt/Naoth-2020>/NaoSCP`. Inside netbeans you can
open it with: File->Import Project `<ProjectDir>`/NaoSCP  

If you don't like netbeans or can't use it you can also compile and run it directly with gradle:
```bash 
./gradlew.bat clean build
```
To run it manually you can execute ONE of the following commands:

``` sh title="Run NaoSCP"
./gradlew.bat run
./dist/naoscp.bat
java -jar dist/lib/NaoSCP-1.1.jar
```
You should see something like this
![NaoSCP startscreen](../img/naoscp/naoscp_start.png)

- TODO add nao scp docu in extra site here and remove it from teamreport
- TODO: add note about alias in bashrc for gradle run/build naoscp