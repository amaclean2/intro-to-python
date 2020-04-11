# Writing Your First Program

Python is extremely simple to get started, but first we're going to get introduced to a couple applications.

On your computer, there's an application called terminal. Terminal is a command line editor for your computer. Everything you can do on your computer, you can do in terminal. You just have to learn the commands for what you want to do. We'll start with a couple simple ones first.

A side note, when you're talking in computer science, folders are called directories, so that's what we'll refer to them as.

```
    cd       "change directory" lets you navigate between directories on your computer
    mkdir    "make directory" creates a new directory in the current location
    ls       "list" lists all the contents of the directory you are currently in
    python   runs a Python script
    git      executes a git command
    ~        "home" a shortcut for your home directory
```

You're going to make sure you have Git installed by running this command in your terminal

```
    git --version
```

If it tells you a version number, you're fine, otherwise follow these steps to install git.

[git instructions](https://www.atlassian.com/git/tutorials/install-git)

Once you open your terminal, we're going to open this code.
Type this command into your terminal.

```
    mkdir ~/code
    cd ~/code
    git clone https://github.com/amaclean2/intro-to-python.git
```

Now once it's cloned, you should be able to type this and execute your first program.

```
    cd intro-to-python
    python intro.py
```

If you look inside the intro-to-python directory, you should see two files, a ```README.md```, which is what you're reading, and ```intro.py```.
The intro file is your actual python code and what we'll be editing.

When you typed in ```python intro.py```, you ran this file which told the computer to print "Hello World"

## Some Notes

To look at the code you are writing, it's really useful to have a text editor. On a Mac, the default is XCode which tends to be cumbersome for writing something like Python, but it's perfectly acceptable. I use Visual Studio Code which you can download in the link, or Sublime Text is another good editor, but it prompts you for a donation every so on. These are just a couple and there's lots, so feel free to explore with what you like.

[Visual Studio Code](https://code.visualstudio.com/download)

[Sublime](https://www.sublimetext.com/3)

[Atom](https://atom.io/)

## Some other resources of what we went over

https://www.w3schools.com/python/python_getstarted.asp

https://www.learnpython.org/en/Hello%2C_World%21

https://www.geeksforgeeks.org/python-language-introduction/
