# Using Command Line Interfaces
A **command line interface** or **CLI** is a computer program which allows a user to interact via entering commands. All **Operating Systems** (OS) have a default system CLI. On Mac and Linux systems it is the Unix-based **terminal**,
and on Windows, it is **cmd.exe**. For the purposes of this class and lab, we will be using a Unix-style **terminal** for all activities regardless of OS. This will be achieved through the use of the **Git Bash** program that is installed alongside **Git** on Windows.
Git Bash emulates the Unix terminal and will allow for all commands to be identical across all platforms.

## Entering Commands
A command line interface works by entering commands into an interface using the keyboard. There are a couple of important things to know about entering and reading commands.

  * The first word of the command is the name of a program (e.g. `git`, `python`)
  * The all other words are known as **arguments** or **parameters**.
  * The program and all of its arguments are **delimited** (separated) by a space.
  * There can be multiple command arguments or none at all. For instance, the command `pwd` (print working directory) is often written by itself, whereas the command `cp` requires 2 arguments (a source file and destination directory [more on that later])
  * Some arguments of a command are optional (Unix convention dictates that these be notated with a `-` [e.g. the `-f` in the command `rm -f /home/test.txt`]).
  * Most commands have multiple methods for expressing optional arguments. The short hand method will generally start with a single `-`, however the full option will start with `--`. For instance, the command `rm -f /home/test.txt` can also be written as `rm --force /home/test.txt`.
  * If you are unsure about what as command is looking for, there are several ways to look up help. On systems with a native Unix terminal (i.e. Mac and Linux), the command `man` (or manual) followed by the command will bring up how to use the command. Other common ways are to include a `--help`, `-h`, or `?` after the command you are trying to execute. For example:
    * `man rm`
    * `rm --help`
    * `rm -h`
    * `rm ?`
    * ___Note:___ _Some of these methods will not work on some machines, these are just a general set of things to try depending on what machine you are working with._

## File Systems
In order to fully use a CLI, you must have a basic understanding of a **File System** and how to navigate it. All computers need a place to store information when a program is not currently working on it. This *secondary* memory is known as **storage**, and is typically contained on a mechanical hard drive, Solid State Drive (SSD), or flash storage (e.g. smartphone storage).
You are likely familiar with this process if you have used a desktop word processor (e.g. Microsoft Word) and have saved a document on your computer. Saving your document allows the program to close without the loss of any data. Other programs also save data to your computer's storage from time to time, and it is a very common use case that you will need to navigate your storage.


On your physical drive, all of the files and folders are a continuous string of 1s and 0s, however, your Operating System (OS) makes sense of these and forms them into a hierarchical structure that is easy for a human to navigate. At the very top of this hierarchy is what is known as your **root directory** (often nicknamed **root** on Unix-based systems). This is a folder which contains all of the files and folders on your machine. On Windows systems this is the root of your C drive or `C:\` (if you were wondering Windows reserves `A:\` and `B:\` for loading additional programs from temporary storage such as the *floppy disks* are are still widely used in 2019).
Under your root drive, you have folders for your programs, OS Files, and users accounts. All OSs contain user accounts and their information is stored under the respective user's folder under the root folder (e.g. `/user/matt/` on Unix systems and `C:\Users\matt` on Windows). The root directory of your user profile has a special name, it is called your **home directory**.


Files can contain both other folders and other files, the are represented in the format of a **tree**. The following shows a typical, simplified Windows directory structure (Unix-based systems will be very similar):
  * C:\ __(root)__
    * Program Files
      * (Your programs)
    * Program Files (x86)
      * (Your old/legacy programs)
    * Users
      * User1 __(User1's home directory)__
        * Documents
        * Desktop
        * ...
      * User2 __(User2's home directory)__
        * Documents
        * Desktop
        * ...
    * Windows
      * (Important OS Files)

In this example, User1's Desktop is located using the **path** `C:\Users\User1\Desktop\`, if you were to make a folder on the Desktop called `test`, it could be addressed with the **relative path** `test` if you were in the Desktop folder or by using its **absolute path**: `C:\Users\User1\Desktop\test`.
Likewise, if you were inside of the newly created `test` folder, and wanted to address User1's desktop folder, you could use the relative path: `..` or the absolute path: `C:\Users\User1\Desktop`.


From the previous examples, two things should be apparent about paths: 1.) You can always get to a folder the same way using its absolute path regardless of where you are in the file system, and 2.) It is often advantageous to use a relative path as opposed to an absolute path because it is shorter and requires much less typing.
Working with relative paths, however, will require some practice, as their rules, while consistent, may be confusing at first. As shown above, when traversing down using a relative path, you simply type the name of the folder you want to enter (this will be covered in more detail when discussing the `cd` command). If you are looking to navigate back up to a **parent directory** (also known as the containing folder), you address it using `..`.
If you are looking to skip a directory or jump down multiple directories, you will delimit/separate your folders using the **system file separator**: `/` (forward slash) on Unix-systems and `\` (backslash) on Windows (e.g. `Desktop/test`). The following also works when navigating back up a file tree (e.g. to navigate up two directories, you can use `../..`).
Finally, you will sometimes need to navigate up and back down to address a folder contained in a different branch of the file system. Using the example above, if I was in User1's Desktop/test folder and wanted to address a folder of the same name on User2's directory I would need address it as follows: `../../../User2/Desktop/test`.

> NOTE: Typing left-to-right, a forward slash leans forward to the right; a backslash leans backwards to the left.  Microsoft systems use backslash.

## Basic Commands
The most common commands that you will issue in a Unix-based CLI (including Git Bash) will involve navigating the file system. The following list is a non-comprehensive guide to get you started.
  * __pwd__ - Stands for __Print Working Directory__, this command is used to print the directory you are currently working in. It is a standalone command, most often used as `pwd`.
  * __ls__ - Stands for __list__, this command is used to print out a list of all files and folders in the directory you are currently working in. It is a standalone command, most often used as `ls`.
  * __mkdir__ - Stands for __Make Directory__, this command is used to create a specified folder in the directory you are currently working in. This command requires a folder path (e.g. `mkdir test` or `mkdir ../test`, etc).
  * __rm__ - Stands for __remove__, this command is used to delete files and folders. This is a powerful command that needs to be respected, as it does not put things into the trash or recycle bin, it permanently deletes them. This command requires a file or folder path in which it will delete. This command has several options that are relevant. It is always recommended that you enable this command's interactive mode using `-i`, this may be a minor annoyance at first, but it will undoubtedly save you later on. Another powerful option is the recursive option `-r`, this is what is used to delete entire folders, when enabled, it will start at the top of your selected folder and systematically delete everything therein. When deleting a file, use the command as `rm -i Desktop/test/test.txt`, when deleting a folder, use the command as `rm -i -r Desktop/test`.
  * __cp__ - Stands for __copy__, this is equivalent to copying a file or folder with your System's __File Explorer__. This command has two required arguments, a file or folder to copy, and the destination directory (e.g. If I was in User1's Desktop folder, and I wanted to copy a file called `test.txt` from the `test` folder to a folder of the same name in Usewr2's Desktop folder, I would issue the following command. `cp test/test.txt ../../User2/Desktop/test`).
  * __mv__ - Stands for __move__, this command is similar to copy, but deletes the file from its soource location (equivalent to a cut and paste operation). This command has two required arguments, a file or folder to copy, and the destination directory (e.g. If I was in User1's Desktop folder, and I wanted to move a file called `test.txt` from the `test` folder to a folder of the same name in Usewr2's Desktop folder, I would issue the following command. `mv test/test.txt ../../User2/Desktop/test`).
  * __man__ - Stands for __manual__, this command is used to diplay the usage of other commands. This command may have issues when using Git Bash on Windows Machines.

There are many other basic commands to master, if you are looking to expand your knowledge on using a terminal, this [Bash Wiki](http://mywiki.wooledge.org/BashGuide) may help.  There is a [Stanford guide](https://ccrma.stanford.edu/guides/planetccrma/terminal.html) that provides an good overview as well, but is for a slightly different command system. We will use *bash* in this course.

### Git
Git commands are similar to most normal commands, however the program you invoke will always be Git instead of the various system programs used to control files. The following six commands will be what you utilize most often. For a more complete Git tutorial, the following ![video](https://www.youtube.com/watch?v=HVsySz-h9r4) is an excellent resource, it is a bit long, but will help with more complex topics outside of the scope of this class.

  * `git clone [repository URL]` - used to copy a remote repository onto your local machine.
  * `git add` - used to __stage__ any changes that you have made, at this point changes may still be unstaged.
  * `git commit -m "your message"` - Used to commit all staged changes, once committed, all changes are bound to the repository. The message you add should be a synopsis of the changes you have made.
  * `git push` - Used to push your committed changes to the remote repository. This command will allow you to share your changes with others.
  * `git pull` - Used to update your local repository with chamges made to the remote repository. This is how you will download changes made by othgers.
  * `git config` - Versatile command used to configure the Git software on your local machine, you should only have to use this when setting up your Git instance or switching users on a given machine.

For reference, you may like this [Cheat Sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet), or see their beginner tutorials for a more in-depth view at [Atlassian Learn Git]([https://www.atlassian.com/git/tutorials/what-is-version-control).

[Go back to the main lab](../README.md)
