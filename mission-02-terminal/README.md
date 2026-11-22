# Mission 2 — Become Comfortable with the Terminal

## 1. Task / Objective

Use the command-line interface to inspect folders, create and manage practice files, understand flags and pipes, and explain package managers.

## 2. Work Completed

- Practised all basic Terminal operations (pwd, ls, cd, mkdir, touch, cp, mv, cat) inside the assignment repository.
- Created a `terminal-practice/` folder with practice files, added text, made backups and renamed files.
- Explored flags (`-l`, `-la`, `-lah`) and the pipe operator (`|`).
- Checked Homebrew version and listed installed packages.
- Answered all required questions about file operations.

## 3. Commands / Tools Used

| Command | Purpose |
|---------|---------|
| `pwd` | Print working directory — shows the full path of the folder I am currently in |
| `ls` | List files and folders in the current directory |
| `ls -l` | List files in a detailed (long) format showing permissions, owner, size and date |
| `ls -la` | Detailed list including hidden files (files starting with a dot) |
| `ls -lah` | Detailed list with hidden files and human-readable sizes (KB, MB instead of bytes) |
| `cd ..` | Move to the parent directory (one level up) |
| `cd mission-02-terminal` | Move into a specific folder |
| `mkdir terminal-practice` | Create a new folder called terminal-practice |
| `touch notes.txt` | Create a new empty file called notes.txt |
| `echo "first line" > notes.txt` | Write text into the file (replaces any existing content) |
| `echo "second line" >> notes.txt` | Append text to the end of the file without removing existing content |
| `cat notes.txt` | Display the contents of the file in the terminal |
| `cp notes.txt backup.txt` | Make a copy of notes.txt named backup.txt |
| `mv backup.txt archive.txt` | Rename backup.txt to archive.txt |
| `ls -la \| head -5` | Pipe the detailed listing into head, which displays only the first 5 lines |
| `brew --version` | Check the installed version of Homebrew (returned Homebrew 7.0.9) |
| `brew list` | Show all packages currently installed through Homebrew |

## 4. My Understanding

### Task 2.1 — Basic Terminal Operations

| Operation | What It Does | What I Observed |
|-----------|-------------|-----------------|
| Current-directory display (`pwd`) | Prints the absolute path of the folder I am working in | It showed `/Users/[redacted]/digital-detective-8560` |
| Directory listing (`ls`) | Lists all visible files and folders in the current location | I could see all my mission folders and README.md |
| Detailed listing (`ls -l`) | Shows permissions, owner, group, file size and modification date for each item | Each line had a string like `drwxr-xr-x` at the start, plus the file size in bytes |
| Change directory (`cd ..`) | Moves up one level to the parent folder | My prompt changed and `pwd` showed I was one folder higher |
| Create directory (`mkdir`) | Creates a new empty folder with the given name | A new folder appeared in my listing |
| Create empty file (`touch`) | Creates a new empty file, or updates the timestamp if it already exists | A file with 0 bytes appeared |
| Copy file (`cp`) | Makes a duplicate of a file with a new name | Both the original and the copy existed with the same content |
| Move / rename file (`mv`) | Moves a file to a new location or renames it in the same location | The old name disappeared and the file appeared with the new name |
| Display file contents (`cat`) | Prints everything inside a file to the terminal | I could see the text I had written earlier |

### Task 2.2 — File Changes Practice

I created a `terminal-practice/` folder inside this mission directory and did the following:

1. Created `notes.txt` using `touch`.
2. Added the first line using `echo "This is the first line" > notes.txt`.
3. Added a second line using `echo "This is the second line" >> notes.txt`.
4. Ran `cat notes.txt` and confirmed both lines were there.
5. Made a backup with `cp notes.txt backup.txt`.
6. Renamed the backup with `mv backup.txt archive.txt`.

**Answers to the questions:**

- **Difference between replacing and appending:** Using `>` replaces the entire file content with the new text. Using `>>` adds the new text at the end without touching what is already there. If I use `>` by mistake, I lose all previous content.
- **Difference between copying and moving:** Copying (`cp`) creates a second file, so both the original and the copy exist. Moving (`mv`) removes the file from the old name or location and puts it in the new one — only one copy exists after moving.
- **What does pwd provide?** It tells me exactly where I am in the file system, using the full path starting from the root. This is helpful so I do not accidentally work in the wrong folder.
- **Why is ls useful?** It lets me check what files and folders exist in a directory before I start working. Without it I would have to guess what is there.

### Task 2.3 — Flags and Pipes

**Flags:** A flag (or option) modifies how a command works. For example:
- `ls` shows just file and folder names.
- `ls -l` adds detailed information like permissions and size.
- `ls -la` also includes hidden files.
- `ls -lah` makes file sizes human-readable (e.g., `4.0K` instead of `4096`).

Each flag changes the behaviour of the same command to show more or different information.

**Pipes:** The pipe symbol `|` sends the output of one command as input to another command. For example:

```
ls -la | head -5
```

The left side (`ls -la`) produces a full detailed listing. The pipe feeds that output to `head -5`, which only displays the first 5 lines. This is useful when the output is long and I only want to see a portion of it.

### Task 2.4 — Package Managers

Homebrew is installed on my Mac (version 7.0.9). I checked the list of installed packages using `brew list` and saw packages like `git`, `gh`, `ffmpeg`, `python` and others.

A **package manager** is a tool that makes it easy to install, update and remove software from the command line. Instead of downloading files from websites and installing them manually, I can type a single command like `brew install git` and the package manager handles everything — downloading, setting up the software, and managing its dependencies. Package managers also make it simple to update all installed software at once, which helps keep the system secure and up to date.

## 5. Difficulties Faced

At first I confused `>` and `>>`. I accidentally used `>` when I meant to append, and it wiped out the first line I had written to the file.

## 6. How I Resolved Them

I remembered that `>` overwrites and `>>` appends. I re-created the file and this time used the correct operator. Now I am careful to double-check before writing to a file.

## 7. Evidence / Files

- `mission-02-terminal/README.md` — this file with all tables and explanations
- `mission-02-terminal/terminal-practice/notes.txt` — practice file with two lines of text
- `mission-02-terminal/terminal-practice/archive.txt` — renamed backup file

## 8. Commit Details

**Commit message:** "Complete Terminal and file management mission"
Work has been pushed to GitHub and verified.
