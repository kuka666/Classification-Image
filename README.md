# Image classification service using Django and Keras![image](https://user-images.githubusercontent.com/80199144/156666050-0f00d587-e6a8-4035-887c-6ce12a629b91.png)


### Instalation
Install our repoisitory 
bash
https://github.com/kuka666/Classification_Colab_SE-2013.git
pip install -r requirements.txt

Also create table in postgresql:

Create the database with name imagepostgresql
python manage.py makemigrations python manage.py migrate python manage.py runserver

``bash
#change your setting
DATABASES = { 'default': 
              { 'ENGINE': 'django.db.backends.postgresql', 
              'NAME': 'database name', #YOUR DATABASE NAME 
              'USER': 'postgres', #USER NAME 'PASSWORD': 
              'postgresql password', #YOUR PASSWORD
              'HOST': 'localhost', } } 
              ``

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
# horse

![image](https://user-images.githubusercontent.com/80199144/156667969-ce22bbbb-eb0e-40b9-a3f2-840faba3e65e.png)

# bird
![image](https://user-images.githubusercontent.com/80199144/156668043-37c68ebb-35f3-43a5-8d71-a205465c214c.png)


## License
[MIT](https://choosealicense.com/licenses/mit/)
