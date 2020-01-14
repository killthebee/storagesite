# Storage site


this site collects and interprets information about storage visits/visitors.


### How to install



Python3 should be already installed.



Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:



```
pip install -r requirements.txt
```

### Launch example



Create ```.env``` file with environment variables, as listed below. 
Launch app in command prompt. In a few moments you should be able to see storage web site running at 
http://0.0.0.0:8000/



```
python manage.py runserver
```
## Environment Variables

```PASSWORD``` For db's password

```HOST``` For db's host

```SECRET_KEY``` Web site secret key

```DEBUG``` True or False to turn on or off debug mode

### Project Goals



The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
