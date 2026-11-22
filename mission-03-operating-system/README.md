# Mission 3 — Understand the Operating System

## 1. Task / Objective

Explore the operating system, running processes, storage, paths and file permissions, and describe what the OS is responsible for.

## 2. Work Completed

- Explored system information using Terminal commands (OS version, current user, storage, running processes).
- Identified what a process is and examined the PID column.
- Explained the difference between absolute and relative paths with examples.
- Examined file permissions using `ls -l`.
- Completed the OS responsibilities table.

## 3. Commands / Tools Used

| Command | Purpose |
|---------|---------|
| `sw_vers` | Display the macOS version and build number |
| `whoami` | Show the currently logged-in user account |
| `df -h /` | Display available and used storage space in human-readable format |
| `top -l 1 \| head -15` | Show a brief snapshot of system activity and running processes |
| `ps aux` | List all running processes with details like PID, CPU usage and memory |
| `pwd` | Print the absolute path of the current working directory |
| `cd` | Change directory to navigate between folders |
| `ls -l` | Detailed listing showing file permissions, owner and size |

## 4. My Understanding

### Task 3.1 — Explore Your Operating System

| Information Explored | What It Tells Me | My Observation (privacy-safe) |
|---------------------|-----------------|-------------------------------|
| Operating system / system details | The name and version of the OS running on this computer | macOS 27.2.1, Build 26B131, running on ARM64 architecture |
| Current account identity | Which user account is currently logged in and running commands | Displayed my username (redacted for privacy) |
| Available and used storage | How much disk space is being used and how much is free | Total: 460 GB, Used: 13 GB, Available: 380 GB — most of my storage is free |
| System activity snapshot | What programs are currently running and how much CPU and memory they are using | WindowServer was using the most CPU. Several background processes were running that I did not start manually. |

### Task 3.2 — Understand Processes

- **What is a process?** A process is a program that is currently running on the computer. When I open Chrome or VS Code, the OS creates a process for it. Even things I do not see, like background services, run as processes.

- **What does the PID column represent?** PID stands for Process Identifier. It is a unique number the OS assigns to each running process so it can keep track of it. No two processes running at the same time have the same PID.

- **Two examples of processes on my computer:**
  1. **WindowServer** — a system process that handles drawing everything on the screen. It was using the most CPU.
  2. **WhatsApp** — the messaging app I had open. It appeared in the process list with its own PID and was using some memory.

### Task 3.3 — Understand Paths and Permissions

**Absolute path vs relative path:**

- An **absolute path** starts from the root of the file system and gives the full location. Example: `/Users/[redacted]/digital-detective-8560/mission-03-operating-system`
- A **relative path** starts from wherever I currently am. Example: if I am in `digital-detective-8560/`, then `mission-03-operating-system/README.md` is a relative path to this file.

The difference is that absolute paths always point to the same location no matter where I am, while relative paths depend on my current directory.

**File permissions:**

When I ran `ls -l` on a file, I saw something like `-rw-r--r--`. The first character indicates the type (`-` for file, `d` for directory). The next three characters are the owner's permissions:

| Permission | Meaning | Example |
|-----------|---------|---------|
| `r` — Read | Allows the file's contents to be viewed | Opening a text file to read it |
| `w` — Write | Allows the file to be modified or edited | Editing a text file and saving changes |
| `x` — Execute | Allows the file to be run as a program; for directories, allows entering them | Running a Python script |

For my README file, the owner had `rw-` permissions, meaning I can read and write to it but it is not set as executable, which makes sense because it is a text file, not a script.

### Task 3.4 — Operating System Responsibilities

| OS Responsibility | My Explanation | Example |
|------------------|---------------|---------|
| Process management | The OS decides which programs get to use the CPU and for how long. It starts, pauses and stops processes. | When I open Chrome and VS Code at the same time, the OS shares CPU time between them so both can run. |
| Memory management | The OS controls how RAM is allocated to running programs. It makes sure each process gets the memory it needs and reclaims it when a process closes. | If I open many browser tabs, the OS assigns RAM to each one. If I close tabs, that memory gets freed up. |
| Device management | The OS communicates with hardware like the keyboard, display and storage through drivers so that applications do not need to know the hardware details. | When I press a key, the OS uses a keyboard driver to understand the keypress and sends it to the active application. |
| File management | The OS organises files into directories, keeps track of where data is stored on disk, and controls who can access what. | When I save a file, the OS decides where on the SSD to store it and updates the file system records. |
| User interface / shell | The OS provides a way for the user to interact with the computer, either graphically (GUI) or through a command-line shell. | The Terminal is a text-based shell. The macOS desktop with its dock and windows is the graphical interface. |
| Security and permissions | The OS controls who can read, write or run files. It enforces user accounts and prevents programs from accessing things they should not. | A file with permissions `-rw-------` can only be read and written by its owner — other users on the same computer cannot see it. |

## 5. Difficulties Faced

When I first ran `ps aux`, the output was really long and overwhelming. There were hundreds of processes and I did not recognise most of them.

## 6. How I Resolved Them

I used `ps aux | head -15` to see only the first few lines, and then looked for process names I recognised (like WhatsApp and WindowServer). I realised that most of the processes are background system services that the OS runs automatically.

## 7. Evidence / Files

- `mission-03-operating-system/README.md` — this file with all tables and explanations

## 8. Commit Details

**Commit message:** "Document operating system and file management"
Work has been pushed to GitHub and verified.
