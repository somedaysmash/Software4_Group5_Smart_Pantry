# Smart Pantry

## Project Group 5 (Software 4)

<br>

## Project Description:


<p>We developed the Smart Pantry project to address the common challenges faced in home kitchens, where individuals struggle with keeping track of their kitchen stock. This often results in last-minute shopping trips, wasted food, and the hassle of manually managing inventory.

Smart Pantry is a smart fridge/pantry/kitchen inventory system that streamlines kitchen management. It eliminates the need for manual stock tracking and recipe planning. The system generates a shopping list, offers recipe suggestions based on available ingredients, and updates stock levels automatically.

Throughout the project, our team learned valuable skills in front-end (JavaScript, HTML, CSS), back-end (Python with Flask), and database management (MySQL). We also gained insights into API integration (Edamam) for recipe retrieval and implemented effective collaboration and version control strategies.</p>

### Features:

- **Automated Inventory Management:** Users can view, add, edit, and delete items effortlessly.
- **Recipe Generation:** Personalized recipe suggestions based on inventory.
- **Stock Level Updates:** Automatic notifications for low or expired items.
- **Shopping List Generation:** On-demand shopping lists based on inventory.

<br>

## Table of Contents:


1. [PreRequisites](Pre-Requisites)
   - Python
   - MySQL
   - Edamam API
2. [Installation](Installation) 
   - Step 1: Clone the Repository
   - Step 2: Set Up Virtual Environment (Recommended)
   - Step 3: Install Dependencies
   - Step 4: Set-Up MySQL Database
   - Step 5: Configure Database Connection
   - Step 6: API Key Set-Up
   - Step 7: Run the Project
   - Step 8: Access the Application
3. [How to Use Smart Pantry](How_to_Use_the_Application)
4. [Meet the Team!](Meet_the_Team)
5. [Further Information](Further_Information)
   - Additional Links
6. [Project Breakdown](Project_Breakdown)
   - HTML and CSS
   - JSON
   - Python
   - MySQL
7. [Communication and Collaboration](Communication_and_Collaboration)
8. [Unit Testing](Unit_Testing)
9. [Summary](Summary)

<br>

## How to install and run the project:


### Pre-Requisites:

<p>To ensure a smooth experience with our application, please ensure you have the following programmes installed on your machine:</p>

<br>

<details>
<summary>Python</summary>

<br>

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

</details>
<br>
<details>
<summary>MySQL</summary>

- Link to [MySQL](https://dev.mysql.com/doc/workbench/en/wb-installing.html)
<br>
<p>Follow the installation instructions provided by the website for your specific operating system.

During installation set up a root password and note it down. Ensure you configure MySQL to start as a service <i>if required</i>.</p>
</details>
<br>

<details>
<summary>Edamam API</summary>

<br>
   
- Link to [Edamam](https://www.edamam.com)

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

<br>

</details>

<br>

> [!NOTE]
> <p>Never share your API key publicly. 
> Consider using environment variables or a dedicated configuration file to keep your keys confidential.</p>


<br>

## Installation


<p><!--ADD INTRODUCTORY PARAGRAPH-->
</p>

<details>
<summary>Step 1: Clone the Repository</summary>

<br>

<p>Clone the Smart Pantry project repository using the following command in your git terminal:</p>

```bash
git clone https://github.com/somedaysmash/Software4_Group5_Smart_Pantry.git
cd Software4_Group5_Smart_Pantry
```
<br>

</details>
<details>
   
<summary>Step 2: Set Up Virtual Environment (Recommended)</summary>

<br>

```python
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

<br>

</details>
<details>
<summary>Step 3: Install Dependencies</summary>

Install the following dependencies:

   ```python
   pip install -r requirements.txt
   ```

<br>

</details>
<details>
<summary>Step 4: Database Set-Up</summary>
   
   <br>
   
- Create a MySQL database named Smart_Pantry.
- Execute the SQL scripts as provided in the Smart PantryDB.sql file</p>

<br>

</details>
<details>
<summary>Step 5: Configure Database Connection</summary>

<br>
   
- Edit the config.py file with your MySQL database credentials:</p>

   ```python
   HOST = 'your_host'
   USER = 'your_user'
   PASSWORD = 'your_password'
   ```

<br>

</details>
<details>
<summary>Step 6: API Key Set-Up</summary>

<br>

- Create API_key.py File:

   - Open your preferred text editor or integrated development environment (IDE).
   - Create a new file named `API_key.py.`

<br>

- Obtain Edamam API Key:

   - Go to the Edamam Developer Portal and sign in or create an account.
   - Create a new application to obtain your API key.

<br>

- Retrieve API Key:

   - Once your application is created, locate your Edamam API key (`app_id`) and application key (`app_key`) in the developer portal.

<br>

- Write API Key in API_key.py:

   - Open the API_key.py file in your text editor.
   - Inside the file, define two variables: app_id and app_key.

- Assign your Edamam API key values to these variables:

   ```python
   # API_key.py
   
   app_id = "your_edamam_app_id"
   app_key = "your_edamam_app_key"
   ```

   - Replace `your_edamam_app_id` and `your_edamam_app_key` with the actual values obtained from the Edamam Developer Portal.

- Save the File:

   - Save the API_key.py file.	

   > [!NOTE]
   > Remember to keep your API keys confidential and never share them publicly.

<br>

</details>
<details>
<summary>Step 7: Run the Project</summary>

<br>

- Navigate to the project directory and run the application
(ADD IMAGE EXAMPLE)

<br>
</details>
<details>
<summary>Step 8: Access the Application</summary>

- Once the project is running, open a web browser and navigate to the specified local address or port where the application is hosted.
 
   `http://127.0.0.1:5000`

<br>

</details>

## How to Use the Application
<!--SECTIONS TO BE ADDED-->


<br>

## Meet the team:

<!--
PERSONAL STATEMENT: Possible questions you can answer are: 
- "What has been your favourite/most challenging thing to do on the group project", 
- "Why is technology so important to you". 
- "What aspects of the course have you found most enjoyable?", 
- "What led you to pursue a career in tech?", 
- "What's your secret skill not many people know?" 
(This is just guidance, so please feel free to write what ever you would like to add and be creative! :) ) 
-->

#### Vanessa L-S:
[@somedaysmash](https://github.com/somedaysmash)
- **Project contributions:** *Add Text Here*
- **Personal statement:** *Add Text Here*
<br>

#### Anna K:
[@ketre](https://github.com/ketre)
- **Project contributions:** *Add Text Here*
- **Personal statement:** *Add Text Here*
<br>

#### Karen L:
[@klace00](https://github.com/klace00)
- **Project contributions:** *Add Text Here*
- **Personal statement:** *Add Text Here*
<br>

#### Lauren A:
[@Laurenhomeridge](https://github.com/Laurenhomeridge)
- **Project contributions:** *Add Text Here*
- **Personal statement:** *Add Text Here*
<br>

#### Amy D:
[@Amy-Dangerfield](https://github.com/Amy-Dangerfield)
- **Project contributions:** *Add Text Here*
- **Personal statement:** *Add Text Here*
<br>

#### Dorothy M:
[@dotmcevoy](https://github.com/dotmcevoy)
- **Project contributions:** *Add Text Here*
- **Personal statement:** *Add Text Here*
<br>

#### Lauren S:
[@Lor9538](https://github.com/Lor9538)
- **Project contributions:** *Add Text Here*
- **Personal statement:** *Add Text Here*

<br>

## Project Breakdown:
<!-- SECTIONS TO BE ADDED-->

### HTML and CSS:

<details>
   <summary>index.html</summary>
   <br>
   
</details>
<details>
   <summary>ingredient.html</summary>
   <br>
   
</details>
<details>
   <summary>kitchen.html</summary>
   <br>
   
</details>
<details>
   <summary>search_recipe.html</summary>
   <br>
   
</details>
<details>
   <summary>shoppinglist.html</summary>
   <br>
   
</details>

<br>

### JSON:

<details>
   <summary>launch.json</summary>
   <br>

</details>

<br>

### Python:

<details>
   <summary>main.py</summary>
   <br>
   
</details>
<details>
   <summary>RecipieAPI.py</summary>
   <br>
   
</details>
<details>
   <summary>App.py</summary>
   <br>
   
</details>
<details>
   <summary>utilities.py</summary>
   <br>
   
</details>
<details>
   <summary>API_Key.py</summary>
   <br>
   
</details>

<br>

### MySQL:

<details>
   <summary>SmartPantryDB.sql</summary>
   <br>

</details>

<br>

## Communication and Collaboration:
<!--SECTIONS TO BE ADDED-->

<br>

## Further Information:


<p>Additional links:</p>

- Project [Proposal](https://docs.google.com/document/d/1zBlx4-xmz2H0JjW7n_EPsaAGDybNqQM8rIOfrlSlX1k/edit#heading=h.z6ne0og04bp5)
- Group [Task-List](https://trello.com/b/QptFT6Rh/smart-pantry)
- Group and Project [SWOT Analyses](https://www.canva.com/design/DAF2Iuu3O6k/DcmZ1CGJk6h11gq_JfIYTg/edit)
- Project [Activity Log](https://docs.google.com/spreadsheets/d/16BXI3OMypGLyWKrMeU4gZ8Bl4-RA6mzLRpgcV_PJK54/edit#gid=67646434)
- CodePen.io [Mock-Up](https://codepen.io/Lauren_Aldridge/pen/KKJqvLo)
- Team and Project [SWOT Analyses](https://www.canva.com/design/DAF2Iuu3O6k/DcmZ1CGJk6h11gq_JfIYTg/edit?utm_content=DAF2Iuu3O6k&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
- Team [Collaboration and Communication]()

<br>

## Unit Testing:
<!--IN PROGRESS-->
<br>

<!--DEVELOP THIS SECTION-->
## Summary:


Smart Pantry stands out as a comprehensive solution for efficient kitchen management, offering automation, collaboration, and a user-friendly interface.
