# Mission 6 — Git and GitHub

## 1. Task / Objective

Understand version control, stage and commit changes, create a branch, open a Pull Request, and explain the Git collaboration workflow.

## 2. Work Completed

- Inspected the repository status, staged a file, committed and viewed the history.
- Created a branch called `update-about`, added a "My Learning" section to the root README, committed and pushed it.
- Created a Pull Request from `update-about` into `main` on GitHub.
- Merged the PR and pulled the latest changes locally.
- Built a Git command glossary.

## 3. Commands / Tools Used

| Command | Purpose |
|---------|---------|
| `git status` | Check which files are modified, staged or untracked |
| `git add <file>` | Stage a specific file, preparing it for the next commit |
| `git commit -m "message"` | Save the staged changes as a snapshot with a descriptive message |
| `git log --oneline` | View a compact list of recent commits with their messages |
| `git checkout -b update-about` | Create a new branch called `update-about` and switch to it |
| `git push -u origin update-about` | Push the new branch to GitHub for the first time |
| `git checkout main` | Switch back to the main branch |
| `git pull origin main` | Download and merge the latest changes from GitHub into my local main branch |

## 4. My Understanding

### Task 6.1 — Basic Git Workflow

| Git Operation | What It Does (in my own words) |
|--------------|-------------------------------|
| Check repository status (`git status`) | Shows me which files have changed since the last commit, which files are staged and ready to be committed, and which files Git is not tracking yet. It is like a quick health check of my project. |
| Stage selected changes (`git add`) | Marks specific files to be included in the next commit. Staging is like putting items in a box before sealing it — I choose exactly what goes in. |
| Create a commit (`git commit`) | Takes everything that is staged and saves it as a permanent snapshot with a message describing what changed. Each commit gets a unique ID so I can find it later. |
| View commit history (`git log`) | Shows a list of all past commits in reverse order (newest first). I can see who made each change, when, and what they described in the commit message. |

**Difference between staging and committing:**
Staging (`git add`) is selecting which changes I want to include. Committing (`git commit`) is actually saving those selected changes as a recorded snapshot. I can stage some files and leave others out, which gives me control over what goes into each commit. It is a two-step process — first I pick, then I save.

### Task 6.2 — Create and Use a Branch

1. I created a new branch with `git checkout -b update-about`.
2. I opened the root `README.md` and added a "My Learning" section describing things I have learned so far.
3. I saved the file, ran `git status` to see it was modified, then ran `git add README.md` and `git commit -m "Add My Learning section to root README"`.
4. I pushed the branch to GitHub with `git push -u origin update-about`.

### Task 6.3 — Create a Pull Request

1. I opened my repository on GitHub.
2. GitHub showed a banner suggesting to compare and create a Pull Request for the `update-about` branch.
3. I clicked it, wrote a description explaining that I added a "My Learning" section to the root README, and created the PR.
4. I reviewed the changes shown in the PR diff — it highlighted exactly the lines I added.
5. I merged the PR into `main`.
6. Back in my Terminal, I ran `git checkout main` and then `git pull origin main` to bring the merged changes to my local copy.

**What is a branch?**
A branch is like a separate workspace within the same repository. I can make changes on a branch without affecting the main version of the project. If the changes turn out well, I can merge them back. If not, I can delete the branch without any damage to main.

**What is a Pull Request?**
A Pull Request is a way to propose merging changes from one branch into another on GitHub. It shows the differences, lets others review the code, leave comments, and approve or request changes before the merge happens. It is useful because in a team, nobody's changes go directly into the main branch without being checked first.

### Task 6.4 — Git Command Glossary

| Git Operation | One-line Explanation |
|--------------|---------------------|
| `git init` | Initialise a new Git repository in the current folder so Git starts tracking changes |
| `git status` | Show which files are changed, staged or untracked in the working directory |
| `git add` | Stage specific files or changes so they are ready for the next commit |
| `git commit` | Save all staged changes as a permanent snapshot with a descriptive message |
| `git log` | Display the history of commits, showing who changed what and when |
| `git branch` | List all branches or create a new branch with a given name |
| `git checkout` | Switch to a different branch or restore files from an earlier state |
| `git push` | Upload local commits to the remote repository on GitHub |
| `git pull` | Download and merge new commits from the remote repository into the current branch |

## 5. Difficulties Faced

When I first tried to push the new branch, I forgot to use the `-u` flag and just typed `git push`. Git gave me an error saying the branch had no upstream tracking reference.

## 6. How I Resolved Them

I re-ran the command as `git push -u origin update-about`. The `-u` flag sets up the tracking link between my local branch and the remote, so future pushes from that branch work with just `git push`.

## 7. Evidence / Files

- `mission-06-git-github/README.md` — this file with all Git explanations and the glossary
- The `update-about` branch and its merged Pull Request are visible on the GitHub repository

## 8. Commit Details

**Commit message:** "Complete Git and GitHub collaboration mission"
Work has been pushed to GitHub and verified.
