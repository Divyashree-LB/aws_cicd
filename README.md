Implemented Continuous Integration using AWS CodeBuild and CodePipeline

Project Summary:

Developed a lightweight Flask web application and implemented a fully automated Continuous Integration (CI) pipeline using AWS CodePipeline and CodeBuild, with source code hosted on GitHub and container images stored on Docker Hub. The pipeline automatically builds, tests, containerizes, and pushes the Docker image whenever code is committed, ensuring reliable and repeatable deployments.
 
<img width="940" height="283" alt="image" src="https://github.com/user-attachments/assets/c0574c21-638a-41dd-ae83-28a2ade4652c" />

-------------------PHASE1: Build and test flask app locally-------------------------
Step1: create folder named flask in your repo and add files app.py and requirements.txt
 
<img width="940" height="241" alt="image" src="https://github.com/user-attachments/assets/4379c23a-42bf-4ee4-a494-f700c14cb1a7" />
<img width="940" height="312" alt="image" src="https://github.com/user-attachments/assets/5a6ea05e-113b-41b3-a29a-8eb934166d64" />
<img width="693" height="295" alt="image" src="https://github.com/user-attachments/assets/02baba9c-d1c1-4584-bb46-d683a88d7885" />

Step2: launch ec2 instance enable port 6000 and ssh in security group inbound traffic and login to your instance from terminal and clone your repo
 <img width="936" height="403" alt="image" src="https://github.com/user-attachments/assets/1b70b222-6e18-475b-9776-67a467970758" />

•	Login to ec2 from mobaxterm or git or any cmd and connect to ec2

ssh -i flask.pem ubuntu@15.207.55.33

step3: install all dependencies and requirements to run flask app

ssh-keygen -t rsa -b 4096 
cat ~/.ssh/id_rsa.pub   #copy key and paste in github ssh key
git clone git@github.com:Divyashree-LB/aws_cicd.git
cd aws_cicd/flask_app
sudo apt update
sudo apt install python3-pip
sudo apt install python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
<img width="803" height="262" alt="image" src="https://github.com/user-attachments/assets/76702546-2e1b-4d3b-9819-7f790d3cbacb" />
Open browser http://15.207.55.33:6000/   where as., http://<ec2 pblic ip>:6000/ 
<img width="676" height="283" alt="image" src="https://github.com/user-attachments/assets/ea13f649-5682-4e68-b91d-cc1041011358" />

•	Install docker on ec2,build and push image to dockerhub
	Install docker.io
sudo apt update
sudo apt install docker.io
sudo usermod -aG docker ubuntu
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl restart docker
sudo systemctl status docker
	Write Docker file,create,build the image
          docker build -t divyashree1129/flask_service .
          docker run -d -p 8000:8000 divyashree1129/flask_service:latest
 <img width="940" height="331" alt="image" src="https://github.com/user-attachments/assets/f3447482-9a54-462e-9dd1-16e4b43c56b6" />

	Login to Dockerhub and push image to repo
docker login -u divyashree1129
password: 
docker push divyashree1129/flask_service:latest
 <img width="940" height="242" alt="image" src="https://github.com/user-attachments/assets/eb469a0a-cc75-4c45-a4f8-2f9a886476c6" />
<img width="940" height="412" alt="image" src="https://github.com/user-attachments/assets/9556ced2-1c76-44be-9e8f-6673a2991c16" />

----------------------------Phase2: Continuous integration--------------------------
Step1: create a role in IAM 
IAM -> roles -> select aws service -> next -> create role -> give name -> grant SSMfullAccess permission -> create
 <img width="1009" height="432" alt="image" src="https://github.com/user-attachments/assets/cb924f28-a502-42a8-860b-c119a7770031" />
Step2: system manager -> parameter store -> add your docker credentials and save
 <img width="940" height="394" alt="image" src="https://github.com/user-attachments/assets/deab7324-5ff8-43cf-b85c-8ab17ce1d36e" />
Step3:  create project in codebuild
Search CodeBuild -> build project -> create project -> add all details as below snaps -> create project
 <img width="929" height="450" alt="image" src="https://github.com/user-attachments/assets/6474f410-680c-447d-82b0-3394a118a475" />

OAuth to your git repo and connect 
 <img width="940" height="226" alt="image" src="https://github.com/user-attachments/assets/de8177d1-289d-4587-8b69-f09cdae0a645" />

Select ubuntu os and below os specification
 <img width="940" height="300" alt="image" src="https://github.com/user-attachments/assets/80fac591-0efe-4d47-99ef-f612852d7f1b" />

Build your own specification or extract build.yml from repo  
Select the service we created in step1 from service role permission dropdown
  <img width="940" height="453" alt="image" src="https://github.com/user-attachments/assets/7427581a-7d3f-4933-b92d-7bcd8dffc532" />

Build the project,check and debug logs for failure
 <img width="940" height="374" alt="image" src="https://github.com/user-attachments/assets/331efe04-a644-4b72-bd0c-8e7eba22a8e8" />

Step4: create codepipeline 
Codepipeline -> create new pipeline -> custom pipeline -> provide name and select role created in step1 -> connect to git hub -> select codebuild and your project ->skip deploy ->create pipeline
	pipeline triggers all the stages and build automatically

 <img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/72e1292b-11d7-430b-935a-b62179461617" />

Make code changes in git and commit,pipeline get auto-triggered and changes reflects
Pipeline acts as web-trigger 
•	soon we made commit in github, CodePipeline auto-triggered and status changed to progress
 <img width="940" height="350" alt="image" src="https://github.com/user-attachments/assets/783554a0-653c-44ca-b0e1-9de4083eba62" />

Build is success 
 
<img width="940" height="529" alt="image" src="https://github.com/user-attachments/assets/1cf0e6a6-7f67-41a0-902a-aec2d66b42ed" />

Docker image pushed to docker hub
![Uploading image.png…]()
 




