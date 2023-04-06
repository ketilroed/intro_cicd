# Intro to CI/CD Part 2: Getting started with Github Actions

Source: Video by Shawn Hymel created for Digi-Key electronics 
https://www.youtube.com/watch?v=8pyqbYDYkRs

Recommended reading to understand Github Actions:
https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions


In this part a workflow was created in the .github/workflows/my-actions.yml file.

The main.c and test.py from part1 was copied into part2. TEST_DIR in test.py was modified to current directory.

Enable workflow:

- Choose Actions 
- Then click the relevant workflow under "All workfloes"
- Press the 3 dots and press Disable workflow.


Disable workflow (useful to not run everytime a push to this repository):

- Choose Actions 
- Then click the relevant workflow under "All workfloes"
- Press Enable workflow


https://docs.github.com/en/actions/managing-workflow-runs/disabling-and-enabling-a-workflow
