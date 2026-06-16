# github_actions_dockerhub
GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

# Project workflow:

1. Create your project in github. clone and paste in the root directory in vs code.
2. Create the python project files.
3. Create the requirements.txt libraries using pip freeze >> requirements.txt
4. Create .gitignore, dockerfile, app.py files
5. Create a folder called  .github
6. cd .github and create a folder called workflows
7. cd to workflows
8. Create a file called python-imagebuild.yml
9. push the code to github
10. In github, click on "action"
11. To fix the error message which should show that there is no username and password or docker, perform the following steps:
12. click on settings, secret&variables, actions, new repository secret
13. click on new repository secret and got to vs code, copy the dockerhub-username code from the .yml file. 
14. Paste in new repository secret username column and enter the docker name
15. Repeat the above for dockerhub-password.
16. Click on actions on git hub and the code should  complete.
17. Log into dockerhub using username and password, then see the images that have been successfully pushed using the github actions cicd pipeline.

<img width="935" height="423" alt="Image" src="https://github.com/user-attachments/assets/851ae70a-17b6-45a7-a308-33b4c07a36b0" />

