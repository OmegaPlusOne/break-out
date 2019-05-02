### Setting up matplotlib & NumPy
[matplotlib](https://en.wikipedia.org/wiki/Matplotlib) and [NumPy](https://en.wikipedia.org/wiki/NumPy) are two of the most common tools used to visualize and manipulate data.
Unfortunately, these are libraries that are not maintained by the Python foundation, and therefore, are not distributed as part of the core of Python.
The good news is that Python has a built in package manager called [pip](https://en.wikipedia.org/wiki/Pip_(package_manager)).
Pip is invoked through the command line, and applies only for your current installation of Python (i.e. The Python environment that you are currently linked to in PyCharm).
> For this lab you must be running either Python 3.6 or 3.7, otherwise the dependencies will not work.

#### Mac/Linux Setup
On Linux and Mac machines, the installation should work out of the box without much difficulty.
Simply go to your terminal, and verify your Python version with the command:
`python --version`

Verify that you are running a version of Python which is 3.6 or newer. 
Once you have verified your installation, run the following commands:

```
python -m pip install matplotlib
python -m pip install numpy
python -m pip install coverage
```

> If you are getting an error, please notify your instructor.
If you have multiple Python environments, there may be a conflict on your system.
One troubleshooting method is to invoke python as python3.
Run the commands as `python3 -m pip install matplotlib` and `python3 -m pip install numpy` 

#### Windows Setup

Depending on your Windows configuration, the installation may be easy or somewhat cumbersome.
Windows relies on a system variable known as `Path` to relate console commands to executable programs.
For instance, if you are running both Python 2.7 and 3.7 on your machine, your 2.7 installation will be located at `C:\Python27\` and your 3.7 installation will be located at `C:\Users\<your user>\AppData\Local\Programs\Python\Python37-32\` or `%AppData%\Local\Programs\Python\Python37-32\`.
This raises a problem, Windows now has to choose between your Python installations, since your OS will not know which to use, you will need to specify which version using the `Path` variable.
Inside of each of the aforementioned folders is an executable file called `python.exe`, when you invoke the `python` command from your terminal, you are really telling Windows to use the given path and run python.exe in the desired folder.
Even if you only have one Python installation, you may not be out of the woods yet!
Often when Windows installs a new program, it is not "automagically" added when running the installer (this is often due to Windows default security settings).

If your path variable is not set, your will receive this infamous message in your command line `'python' is not recognized as an internal or external command, operable program or batch file.`
If it's your first time seeing, it don't worry, you will see it many, many, many....__many!__ more times.
There are 2 ways to fix this issue, the latter being the preferred method.
You can always address your command using an __absolute path__ (i.e. You can always invoke python using `%AppData%\Local\Programs\Python\Python37-32\python`).
The other method (which is the preferred method) will take us on a trip into the Windows Environment Variable manager.

1. To start with, we will need to launce the `System Properties` menu in Windows.
To do this either hit the WIN+R and enter the program `SystemPropertiesAdvanced.exe` or type `Variable` into the Windows search bar and select the option `Edit the system environment variables`.
2. Once this menu is open you will see a button at the bottom right which says `Environment Variables...`, click this button.
3. In the `Environment Variables` window, your will see a top section and a bottom section, the top section is for variables for your current user account and the bottom is for system-wide variable.
We are only interested in the system-wide variables at this point, so disregard the top section.
4. In the bottom section, scroll down until you see the `Path` variable.
Highlight it in the list and select the `Edit...` button near the bottom.
5. If you are running Windows 8/8.1/10, the next menu will be fairly simplified, if you are still running Windows 7, your interface will be a bit different (__please notify your instructor if this is the case__).
   > If you are running Windows 7, you will also need to power cycle your machine to guarantee that the environment variable takes effect after you set it.
6. Inside of your Path variable, you are going to select the `New...` button, from there you will be asked to insert a Path.
You will enter the path of your Python 3.7 installation.
Your path your enter should look something like `%AppData%\Local\Programs\Python\Python37-32\`.
7. Once you have finished, accept the changes, and select `Apply` or `OK` for each menu until the system properties editor is closed.
8. Finally, open up a __NEW__ instance of the command line and enter the command `python --version`.
This command should return the version number for your 3.7 installation.

Now that the Python path is set correctly, we can simply run the following commands:

```
python -m pip install matplotlib
python -m pip install numpy
python -m pip install coverage
```

[Go back to the main lab](../README.md)