# Smart Pantry

## Project Group 5 (Software 4)


### <ins>Project Description:</ins>

<p>We developed the Smart Pantry project to address the common challenges faced in home kitchens, where individuals struggle with keeping track of their kitchen stock. This often results in last-minute shopping trips, wasted food, and the hassle of manually managing inventory.

Smart Pantry is a smart fridge/pantry/kitchen inventory system that streamlines kitchen management. It eliminates the need for manual stock tracking and recipe planning. The system generates a shopping list, offers recipe suggestions based on available ingredients, and updates stock levels automatically.

Throughout the project, our team learned valuable skills in front-end (JavaScript, HTML, CSS), back-end (Python with Flask), and database management (MySQL). We also gained insights into API integration (Edamam) for recipe retrieval and implemented effective collaboration and version control strategies.</p>

### Features:

- **Automated Inventory Management:** Users can view, add, edit, and delete items effortlessly.
- **Recipe Generation:** Personalized recipe suggestions based on inventory.
- **Stock Level Updates:** Automatic notifications for low or expired items.
- **Shopping List Generation:** On-demand shopping lists based on inventory.

<br>

### <ins>Table of Contents:</ins>
<!--FIX STEPS 1-8 SYNTAX ERROR-->
1. [PreRequisites](#Pre-Requisites)
   - [Python](#Python)
   - [MySQL](#MySQL)
   - [Edamam API](#Edamam_API)
2. [Installation](#Installation) 
   - [Step 1: Clone the Repository](#Step_1:_Clone_the_Repository)
   - [Step 2: Set Up Virtual Environment (Recommended)](#Step_2:_Set_Up_Virtual_Environment_(Recommended))
   - [Step 3: Install Dependencies](#Step_3:_Install_Dependencies)
   - [Step 4: Set-Up MySQL Database](#Step_4:_Set-Up_MySQL_Database)
   - [Step 5: Configure Database Connection](#Step_5:_Configure_Database_Connection)
   - [Step 6: API Key Set-Up](#Step_6:_API_Key_Set-Up)
   - [Step 7: Run the Project](#Step_7:_Run_the_Project)
   - [Step 8: Access the Application](#Step_8:_Access_the_Application)
3. [How to Use Smart Pantry](#How_to_Use_the_Application)
4. [Meet the Team!](#Meet_the_Team)
5. [Further Information](#Further_Information)
6. [Unit Testing](#Unit_Testing)
7. [Summary](#Summary)

<br>

### <ins>How to install and run the project:</ins>


### Pre-Requisites:

<p>To ensure a smooth experience with our application, please ensure you have the following programmes installed on your machine:</p>

<br>

### Python

<p>For this project we utilised PyCharm, but depending on your needs/preferences we have attached links to several software packages suitable for this project.</p>

- Link to [Python](https://www.python.org/downloads/)
- Link to [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows)
- Link to [VS Code](https://code.visualstudio.com/download)
<br>
<p>Follow the installation instructions provided on the website to install python on your machine.

Once installed you can verify this has been successful by opening a terminal or command prompt by typing the following:</p>

```python
python --version
```

<br>

### MySQL

- Link to [MySQL](https://dev.mysql.com/doc/workbench/en/wb-installing.html)
<br>
<p>Follow the installation instructions provided by the website for your specific operating system.

During installation set up a root password and note it down. Ensure you configure MySQL to start as a service <i>if required</i>.</p>

<br>

### Edamam API
<!--WHY DOESN'T THIS WORK?-->
- <p>Link to [Edamam](https://www.edamam.com)</p>

<br>

<p>To use the Edamam API, you need to obtain an API key and store it securely.</p>

<p>This project uses the Edamam API to get nutrition data and recipes for various foods.</p>

<br>

**1. Sign Up at Edamam Developer Portal:**

- Navigate to Edamam's Developer Portal.
- Create a free account by signing up.

**2. Access the Recipe Search API:**

- Follow the link to Edamam's 'Recipe Search API'.
- Locate the 'Developer' section in the pricing table.

**3. Initiate API Key Retrieval:**

- Click on 'Get Started' in the 'Developer' section.
- Input your necessary details.

**4. Select 'Recipe Search API - Developer':**

- In the dropdown box titled 'Choose your plan,' select 'Recipe Search API - Developer.'

**5. Create Application:**

- Navigate to your Dashboard, specifically in the Applications section.

**6. Find Your API Key:**

- Once your application is created, retrieve your unique app_id and app_key.

<br>

<p>Now, you are equipped with the credentials needed to make API requests for nutrition data and recipes. Ensure to store these keys securely for the project's continued functionality.</p>

> [!NOTE]
> <p>Never share your API key publicly. 
> Consider using environment variables or a dedicated configuration file to keep your keys confidential.</p>

<br>

### Installation

<p><!--DEVELOP THIS SECTION-->
</p>

### Step 1: Clone the Repository

<p>Clone the Smart Pantry project repository using the following command in your git terminal:</p>

```bash
git clone https://github.com/somedaysmash/Software4_Group5_Smart_Pantry.git
cd Software4_Group5_Smart_Pantry
```

### Step 2: Set Up Virtual Environment (Recommended)

```python
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

<p>Install the following dependencies:

```python
pip install -r requirements.txt
```
</p>

### Step 4: Database Set-Up
<p>Create a MySQL database named Smart_Pantry.
Execute the SQL scripts as provided in the Smart PantryDB.sql file</p>

### Step 5: Configure Database Connection
<p>Edit the config.py file with your MySQL database credentials:</p>

```python
HOST = 'your_host'
USER = 'your_user'
PASSWORD = 'your_password'
```

### Step 6: API Key Set-Up
<!-- STILL NEEDS TO BE FORMATTED-->
- Create API_key.py File:

Open your preferred text editor or integrated development environment (IDE).
Create a new file named `API_key.py.`

- Obtain Edamam API Key:

Go to the Edamam Developer Portal and sign in or create an account.
Create a new application to obtain your API key.

- Retrieve API Key:

Once your application is created, locate your Edamam API key (app_id) and application key (app_key) in the developer portal.

- Write API Key in API_key.py:

Open the API_key.py file in your text editor.

Inside the file, define two variables: app_id and app_key.

- Assign your Edamam API key values to these variables:

```python
# API_key.py

app_id = "your_edamam_app_id"
app_key = "your_edamam_app_key"
```

Replace "your_edamam_app_id" and "your_edamam_app_key" with the actual values obtained from the Edamam Developer Portal.

- Save the File:

Save the API_key.py file.	

Remember to keep your API keys confidential and never share them publicly.


### Step 7: Run the Project

Navigate to the project directory and run the application
(ADD IMAGE EXAMPLE)

### Step 8: Access the Application

Once the project is running, open a web browser and navigate to the specified local address or port where the application is hosted.
 
`http://127.0.0.1:5000`

<br>

### How to Use the Application


<br>

<!--ADD TEAM MEMBERS AND GITHUB ACC LINKS HERE-->
### Meet the team
- 


<br>

### Further Information

<p>Additional links:</p>

- Project [Proposal](https://docs.google.com/document/d/1zBlx4-xmz2H0JjW7n_EPsaAGDybNqQM8rIOfrlSlX1k/edit#heading=h.z6ne0og04bp5)
- Group [Task-List](https://trello.com/b/QptFT6Rh/smart-pantry)
- Group and Project [SWOT Analyses](https://www.canva.com/design/DAF2Iuu3O6k/DcmZ1CGJk6h11gq_JfIYTg/edit)
- Project [Activity Log](https://docs.google.com/spreadsheets/d/16BXI3OMypGLyWKrMeU4gZ8Bl4-RA6mzLRpgcV_PJK54/edit#gid=67646434)
- CodePen.io [Mock-Up](https://codepen.io/Lauren_Aldridge/pen/KKJqvLo)

<br>

### Unit Testing

<br>

<!--DEVELOP THIS SECTION-->
### Summary
Smart Pantry stands out as a comprehensive solution for efficient kitchen management, offering automation, collaboration, and a user-friendly interface.
