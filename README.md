# StatsView

An NFL Quarterback Statistics Visualization Program. This program takes in user input from a form asking what type of Quarterback comparison graph the user would like to see, and then creates a unique graph for users to visually see the Quarterback statistical differences in any category!

## Instructions to Run this Project</h2>

### Prerequisites
Must have Node.js and Python installed on computer.

If you need to install, here are links to download them:

* Python: https://www.python.org/downloads/    (**When downloading Python, ensure you click the checkbox to add it to the PATH**)

* Node.js: https://nodejs.org/en/download

### Step 1: Open Project

To open this project, fork this repository by going to the repository's main page, and click on the **Fork** button.

This will create a copy of this repository. For the sake of following these instructions, do not change the name of the repository. 

Then go to the main page of this forked repository's page, then click on the **<> Code** button.

Then copy the link to clone it using **HTTPS**.

Now open your terminal in rlogin, and navigate to the root directory and type the following command:

Enter the following command:

```bash
git clone https://github.com/{YOUR USERNAME HERE}/StatsView.git
```

This should create a new cloned copy of the project for you to have on rlogin. To open this project in VSCode, now you should be able to click **File > Open Project** and StatsView should be an option to open.

After this step, you should have the StatsView project open without a virutal environment set up yet. This is the next step.

### Step 2: Starting up the Virtual Environment

To set up the virtual environment, type the following command

Use following command to navigate into the project directory:

```bash
cd StatsView
```

To create the new virtual environment, use the following command:

```bash
python3.11 -m venv "StatsViewVenv"
```

To start the virtual environment, run:

```bash
source ./StatsViewVenv/bin/activate
```

Now your virtual environment should be ready, so kill this terminal and open a new Bash Terminal.

### Step 3: Set up the Backend

First, navigate into the backend directory by running the command:

```bash
cd backend
```
Then in order to install the python dependencies used in the project, run the command:

```bash
pip install -r requirements.txt
```
This should ensure you have all the libraries necessary to create graphs and run the server. The final step is to start the server for the backend by running the command:

```bash
flask --app server run
```

### Step 4: Set up the Frontend

Next, open another bash terminal and ensure that you are in the StatsView Root Directory, and not in the backend. If you are, simply run ```cd ..```

Then navigate into the frontend using the following command:

```bash
cd frontend
```

Then, to get React and all the dependencies installed, run the command:

```bash
npm install
```

Finally, to get the front end up and running, run the command:

```bash
npm start
```
This should finally load the program in your browser, and you should be good to go. Enjoy!
