# github_actions_dockerhub
GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can create workflows that build and test every pull request to your repository, or deploy merged pull requests to production.

# Project workflow: Introducing building docker images of the python application (github action_dockerhub) and then push the docker images to the docker hub usign the Github actions as the CICD pipeline.

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
13. click on new repository secret and got to vs code, copy the dockerhub-username code from the .yml file. .yml extension is the github action extension. 
14. Paste in new repository secret username column and enter the docker name
15. Repeat the above for dockerhub-password.
16. Click on actions on git hub and the code should  complete.
17. Log into dockerhub using username and password, then see the images that have been successfully pushed using the github actions cicd pipeline.

<img width="940" height="411" alt="Image" src="https://github.com/user-attachments/assets/ef48f4bc-9917-45b7-975d-ab820bd88a6d" />


<img width="935" height="423" alt="Image" src="https://github.com/user-attachments/assets/851ae70a-17b6-45a7-a308-33b4c07a36b0" />

# Challenges: 

1. Unable to log onto docker as the ussername and password was missing in github.

<img width="475" height="101" alt="Image" src="https://github.com/user-attachments/assets/f9a9f273-548e-4249-b0d6-92826c6c7f2d" />

Resolution: 
1. Click on settings, secret&variables, actions, new repository secret
2. Click on new repository secret and got to vs code, copy the dockerhub-username code from the .yml file. 
3. Paste in new repository secret username column and enter the docker name
4. Repeat the above for dockerhub-password.
5. Create a file called f1  in vs code
6. push all the codes  from vs code again the git hub.
7. click action to run codes in got hub.
