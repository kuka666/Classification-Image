# Image classification service using Django and Keras![image](https://user-images.githubusercontent.com/80199144/156666050-0f00d587-e6a8-4035-887c-6ce12a629b91.png)


### Instalation
Install our repoisitory 
bash
https://github.com/kuka666/Classification_Colab_SE-2013.git
pip install -r requirements.txt

Also create table in postgresql:

Create the database with name imagepostgresql
python manage.py makemigrations python manage.py migrate python manage.py runserver

bash
#change your setting
DATABASES = { 'default': 
              { 'ENGINE': 'django.db.backends.postgresql', 
              'NAME': 'database name', #YOUR DATABASE NAME 
              'USER': 'postgres', #USER NAME 'PASSWORD': 
              'postgresql password', #YOUR PASSWORD
              'HOST': 'localhost', } } 

### Usage
bash
python manage.py runserver

### 
bash
run the server in compilator 
http://127.0.0.1:8000/   to check 



### Examples

Usage examples:
python
# get the bar chart
http://127.0.0.1:8000/ 
![1](https://user-images.githubusercontent.com/80199144/152835054-e8bd79c4-bb70-4313-91a1-0f2428284d25.jpg)
python
# get rhe pie chart
http://127.0.0.1:8000/pie/
![2](https://user-images.githubusercontent.com/80199144/152835118-568cd1c0-81be-427c-806e-2ee4183cef71.jpg)


python
# get the line chart
http://127.0.0.1:8000/line/ 
![3](https://user-images.githubusercontent.com/80199144/152835154-1650e2b3-964f-4f81-8cea-b87eff05df74.jpg)





## License
[MIT](https://choosealicense.com/licenses/mit/)
