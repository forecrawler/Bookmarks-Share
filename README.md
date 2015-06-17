# Bookmarks.share 

Demo application built with AngularJS, Tornado and MongoDB. Share your bookmarks to everyone.

![bookmarks.share](https://raw.githubusercontent.com/kmlg/Bookmarks-Share/b6a1580c4b61f736cd0803b1e3fdc756ed925fa4/static/img/bookmarks.png)

## Installation(Ubuntu)

```bash
# Install mongodb and virtualenv
$ sudo apt-get install mongodb python-pip
$ sudo pip install virtualenv

# Create a virtual environment for your project:
$ mkdir your_project_folder && cd your_project_folder
$ virtualenv venv

# Activate the virtual environment:
$ source venv/bin/activate

# Clone project
$ git clone https://github.com/kmlg/Bookmarks-Share.git
$ cd Bookmarks-Share

# Install tornado and pymongo
$ pip install -r requirements.txt

# Running on http://localhost:8080/
$ python main.py

# Restore data(Optional)
$ mongorestore -d bookmarks --directoryperdb data/bookmarks
```

##Todo

- [ ] register page
- [ ] manage page
