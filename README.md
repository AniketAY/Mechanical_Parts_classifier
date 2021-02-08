<p align="center"
<img src ="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Stack_Overflow_icon.svg/768px-Stack_Overflow_icon.svg.png" width = 200px>
</p>

<h1 align = 'center'> Mechanical Parts Classifier
</h1>

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[![](https://img.shields.io/badge/Made_with-streamlit-orange?style=for-the-badge&logo=Streamlit)](https://www.streamlit.io/) 
&emsp;
[![](https://img.shields.io/badge/Hosted_on-heroku-violet?style=for-the-badge&logo=Heroku)](https://www.heroku.com/)
&emsp;
[![](https://img.shields.io/badge/IDE-Visual_Studio_Code-blue?style=for-the-badge&logo=visual-studio-code)](https://code.visualstudio.com/ "Visual Studio Code")


### :information_source: About 
<p>
This project was built as a part of internship work at K.J Somaiya College of Engineering under the guidance and mentorship of Prof. Ankit Khivsara. 
The aim of this project is to classify four common parts used widely namely, locating pin, washer, bolt and nut. 
The basic CNN model i.e. pretrained VGG16 has been used. The mdel is also built from scratch. 
However, its accuracy is a bit fluctauting, so in production, the VGG16 model has been used.
The deployed website could be viwed at https://mechanical-parts-classifier.herokuapp.com/ 
</p>

-----------------------------------
### 💻 Built with
`Resources` : Google Colaboratory, Heroku, Streamlit <br>
`Libraries` : Numpy, Pandas, Keras, tensorflow <br>
`Dataset` : Kaggle <br>

-----------------------------------

### :guide_dog: Steps to run locally

Step 1 - Clone the repository <br>
In the working directory open git bash and type:
```
git clone https://github.com/m607stars/Mechanical_Parts_classifier.git
```

Step 2 - Create a venv (Virtual Envirnoment) <br>
Close the git bash and open cmd. Type the following to create a virtual environment and activate it 
```
python -m venv --system-site-packages .\venv
.\venv\Scripts\activate
```

Step 3 - Intall the requirements.txt <br>
If the virtual environment is successfully created the cmd will show a (venv) at the beginning of the next line. 
Now type the following to install all the required packages. 
```
pip install -r requirements.txt
```

Step 4 - Run using streamlit <br>
Finally, you are set to go. Run the web app locally using the below command!
```
streamlit run streaml_web_app.py
```

------------------------------------------

### 📝 To-do List

- [ ] Improve the model to more than 90% accuracy. 
- [ ] Create App for the same. 

------------------------------------------


### :page_with_curl: Acknowledgements & References

- Dataset used for training - https://www.kaggle.com/krishna8338/mechanical-parts-data
- Deployment on heroku - https://medium.com/analytics-vidhya/how-to-deploy-a-streamlit-app-with-heroku-5f76a809ec2e 
- Using streamlit for deployment - https://www.geeksforgeeks.org/deploy-your-machine-learning-web-app-streamlit-on-heroku/
- CNNs and computer vision - https://youtube.com/playlist?list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF
