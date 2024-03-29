# Smart Pantry - *Your kitchen, simplified.*

<!--![Image of Smart Pantry logo, displaying title: Smart Pantry, slogan: "Your kitchen, Simplified" and an icon of a frying pan on a black and tan background](https://github.com/somedaysmash/Software4_Group5_Smart_Pantry/blob/main/Further%20Information/Logo.png)-->

<!--<p align="center">
  <img src="https://github.com/somedaysmash/Software4_Group5_Smart_Pantry/blob/main/Further%20Information/Logo.png" 
       alt="Image of Smart Pantry logo, displaying title: Smart Pantry, slogan: Your kitchen, Simplified, and an icon of a frying pan on a black and tan background" 
       width="300" 
       height="300"></p>-->

### Software 4 - Project Group 5

Lauren Aldridge, Amy Dangerfield, Anna Ketre, Karen Lacey, Vanessa Latchen-Smith, Dorothy McEvoy, Lauren Southall

<br>

## Project Description

<p>We developed the Smart Pantry project to address the common challenges faced in home kitchens, where individuals struggle with keeping track of 
	their kitchen stock. This often results in last-minute shopping trips, wasted food, and the hassle of manually managing inventory.

Smart Pantry is a smart kitchen inventory system that streamlines kitchen management. It eliminates the need for manual stock tracking
and recipe planning. The system generates a shopping list, offers recipe suggestions based on available ingredients, and updates stock levels automatically.

Throughout the project, our team learned valuable skills in front-end (JavaScript, HTML, CSS), back-end (Python with Flask), and database management
(MySQL). We also gained insights into API integration (Edamam) for recipe retrieval and implemented effective collaboration and version control strategies.</p>

### Features:

- **Automated Inventory Management:** Users can view, add, edit, and delete items effortlessly.
- **Recipe Generation:** Personalized recipe suggestions based on inventory.
- **Stock Level Updates:** Automatic notifications for low or expired items.
- **Shopping List Generation:** On-demand shopping lists based on inventory.

<br>

<!--## Table of Contents


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

<br>-->

## How to install and run the project

### Pre-Requisites

<p>To ensure a smooth experience with our application, please ensure you have the following programmes installed on your machine:</p>

<br>

<details>
<summary>Python</summary>

<br>

<p>For this project we utilised PyCharm, but depending on your needs/preferences we have attached links to several software packages suitable for this project.</p>

- Link to [Python](https://www.python.org/downloads/)
- Link to [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows)
- Link to [VS Code](https://code.visualstudio.com/download)
  `<br>`

<p>Follow the installation instructions provided on the website to install python on your machine.

Once installed you can verify this has been successful by opening a terminal or command prompt by typing the following:`</p>`

```python
python --version
```

<br>

</details>
<br>
<details>
<summary>MySQL</summary>

- Link to [MySQL](https://dev.mysql.com/doc/workbench/en/wb-installing.html)
  `<br>`

<p>Follow the installation instructions provided by the website for your specific operating system.

During installation set up a root password and note it down. Ensure you configure MySQL to start as a service `<i>`if required`</i>`.`</p>`

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
>
> <p>Never share your API key publicly. 
> Consider using environment variables or a dedicated configuration file to keep your keys confidential.</p>

<br>

### Installation

<p>When it comes to installing our application, the process is straightforward and user-friendly. Follow the steps outlined below to seamlessly set up and get started with our software:</p>

<br>

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
- Execute the SQL scripts as provided in the Smart PantryDB.sql file `</p>`

<br>

</details>
<details>
<summary>Step 5: Configure Database Connection</summary>

<br>

- Edit the config.py file with your MySQL database credentials:`</p>`

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
  >

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

<br>

## How to Use the Application

By following these simple steps, you'll harness the full potential of the Smart Pantry application. Enjoy delightful cooking and effortlessly manage your kitchen inventory for a stress-free culinary experience.

<br>

<details>
	<summary>Introduction</summary>

<p>Welcome to the Smart Pantry application, your smart solution for effortless kitchen inventory management, recipe generation, and streamlined shopping. 
	This quick guide will lead you through the essential features and functionalities of the application.</p>
</details>
<details>
<summary>Navigation</summary>

- **What's in my Kitchen?**
  - Navigate to your kitchen inventory by clicking on `What's in my kitchen?` in the navigation bar.
- **Generate a Random Recipe**
  - Click on `Generate a random recipe` to get culinary inspiration based on your current inventory.
- **Shopping List**
  - Access your shopping list by clicking on `Shopping list.`, the system generates this list based on low or out-of-stock items in your inventory.
- **Search for a Recipe by Ingredient**
  - Explore recipes by searching for a specific ingredient.
  - Click on `Search for a recipe by ingredient` to find delightful recipes.

</details>
<details>
<summary>Inventory Management</summary>

- **Viewing Inventory**
  - The main page displays your inventory categorized into Fridge, Pantry, and Freezer.
  - Each category has a list of items with details like name, type, quantity, and more.
- **Adding Stock**
  - To add an item to your inventory, go to the `Add Stock` section.
  - Fill in the details like stock store, item name, type of ingredient, quantity, unit of measurement, minimum quantity, and sell-by date.
  - Click `Add Stock` to update your inventory.
- **Recipe Generation**
  - Generate recipes based on your current inventory by visiting the `Generate a Random Recipe` page.
  - Choose a protein, and the system will suggest recipes along with a shopping list for missing ingredients.
- **Shopping List Management**
  - Access your shopping list from the `Shopping list` page (items are listed with checkboxes).
  - Check items you want to buy and click `Download` to get a shopping list text file.
- **Recipe Search**
  - Use the `Search for a Recipe by Ingredient` page to find recipes containing a specific ingredient.
  - Enter the ingredient and click `Search Recipes.`

</details>

<br>

<p><i>Happy cooking and organising!</i></p>

<br>

## Project Breakdown

<p>In this comprehensive project breakdown, we've meticulously organized the codebase to provide users with a transparent and insightful view into the underlying 
	structure and components that power the Smart Pantry system. The breakdown serves as a roadmap, guiding users through the intricate layers of our implementation.</p>

<br>

### Purpose of the Code Breakdown:

- **Clarity and Understanding:** The breakdown elucidates the intricate details of our HTML, CSS, Python, and MySQL components, fostering a clear understanding of their individual roles in the system.
- **Transparency in Functionality:** Each section of the breakdown delves into the functionality it encapsulates, ensuring transparency in how different technologies collaborate to deliver a seamless kitchen inventory management experience.
- **Modularity and Maintenance:** By dissecting the codebase into distinct sections, we've embraced modularity, enabling efficient maintenance and updates. Users can easily identify and modify specific components without navigating through an overwhelming monolith.
- **Educational Resource:** The breakdown serves as an educational resource, offering insights into best practices, design decisions, and the rationale behind our technological choices. It empowers users to comprehend the logic behind the Smart Pantry's development.
- **Collaborative Development:** Developers can leverage the breakdown for collaborative efforts, understanding how each team member's contributions fit into the overall structure. It promotes collaboration by providing a comprehensive overview of the entire system.
  <br>

By sharing this detailed breakdown, we aim to facilitate a deeper understanding of the Smart Pantry's inner workings, encouraging collaboration, transparency, and continuous improvement.

<br>

### JSON

<p>Our Smart Pantry project seamlessly incorporates JSON (JavaScript Object Notation) to enhance its functionality and data exchange capabilities. 
	JSON serves as a lightweight and efficient data interchange format, allowing the Smart Pantry system to communicate effortlessly with various components.</p>

<br>

### HTML

<p>This HTML code serves as the foundation for the Smart Pantry's webpage, defining key elements to establish structure and layout. The design focuses on 
	creating a user-friendly interface, ensuring a seamless and visually appealing experience for the Smart Pantry system.</p>

<br>

<details>
<summary>index.html</summary>

<br>

- `<!DOCTYPE html>`: Declares the document type and version of HTML being used (HTML5 in this case).
- `<html lang="en">`: The root element of the HTML document, indicating that the language is English.
- `<head>`: Contains meta-information about the HTML document, such as the title, character set, and external stylesheets.
- `<title>Smart Pantry</title>`: Sets the title of the HTML document to "Smart Pantry," which is displayed in the browser's title bar or tab.
- `<link rel="stylesheet" href="static/style.css"/>`: Links an external stylesheet named "style.css" located in the "static" folder to define the document's styling.
- `<body class="index_bg">`: Represents the document's content, and the class attribute assigns the class "index_bg" to the body element. This class is likely used for styling purposes.
- `<nav>`: Defines a navigation section.
- `<ul>`: Represents an unordered list (a list without numerical order).
- `<li><a href='/kitchen' class='kitchen-title-link'>What's in my kitchen?</a></li>`: Defines a list item containing a hyperlink. Clicking this link navigates to the '/kitchen' URL.

  - The link has the class "kitchen-title-link."
- `<ul class="main_button">`: Another unordered list with the class "main_button."
- `<li id="primary"><a href='/ingredient'>Generate a random recipe</a></li>`: List item representing a primary action button that, when clicked, navigates to the '/ingredient' URL.
- `<li id="secondary"><a href='/shopping'>Shopping list</a></li>`: List item representing a secondary action button that, when clicked, navigates to the '/shopping' URL.
- `<li id="search_button"><a href='/search_recipe'>Search for a recipe by ingredient</a></li>`: List item representing a search button that, when clicked, navigates to the '/search_recipe' URL.
- `</body>`: Closes the body section of the HTML document.
- `</html>`: Closes the HTML document.

  <br>

</details>
<details>
<summary>ingredient.html</summary>

<br>

#### Head Section:

- `<head>`: Represents the head of the HTML document.
- `<title>`: Sets the title of the webpage to "Smart Pantry."
- `<link rel="stylesheet" href="static/style.css"/>`: Links an external stylesheet (style.css) to the HTML document, which is located in the "static" directory.

#### Body Section:

- `<body class="ingredient_bg">`: Sets the body of the document with the class "ingredient_bg," presumably for styling purposes.
- `<nav>`: Defines a navigation section.
- `<ul class="ing_list">`: Defines an unordered list with the class "ing_list" for navigation links.
- `<li><a href="/kitchen">What's in my kitchen?</a></li>`: Creates a list item with a hyperlink to "/kitchen" for checking kitchen items.
- `<li><a href="/shopping">Shopping list</a></li>`: Another list item with a hyperlink to "/shopping" for viewing the shopping list.
- `<h1>`: Defines a heading with information about choosing a protein to generate a random recipe and automatically create a shopping list for missing products.
- `<form method="post">`: Initiates a form with the HTTP method "post."
- `<div class="wrapper_button">`: Contains elements related to user input.
- `<select name="query" id="query">`: Creates a dropdown menu for selecting a protein. It's populated with options from a loop over the "proteins" variable.
- `<button type="submit">`: Provides a submit button for the form, containing an SVG image for visual representation.
- `<hr/>`: Inserts a horizontal line as a visual separator.
- `<h2>{{ recipe.label }}</h2>`: Displays the label of the recipe, presumably dynamically obtained from the backend.
- `<ul class="ingredients">`: Defines an unordered list for displaying the ingredients of the recipe.
- `{% for i in recipe.ingredients %}`: Initiates a loop to iterate over the ingredients of the recipe.
- `<li>{{ i.text }}</li>`: Displays each ingredient as a list item.

  <br>

</details>
<details>
<summary>kitchen.html</summary>

<br>

<p>This HTML code creates a web page for the Smart Pantry application, displaying inventory information and providing a form to add new stock items. 
	The page also includes a navigation button for recipe assistance.</p>

#### Head Section:

- `<!DOCTYPE html>`: declares the document type and version of HTML being used.
- `<html lang="en">`: Defines the root element of the HTML document with the specified language attribute.
- `<head>`: Contains metadata about the document.
- `<title>`: Sets the title of the document to "Smart Pantry."
- `<link>`: Includes an external stylesheet (style.css) for styling.

#### Body Section:

- `<body class="fridge_bg">`: Sets the class of the body element to "fridge_bg," likely for styling purposes.
- `<center><a class="home_button" href="/">Home</a></center>` : A home button to return to the main page centred.
- `<div class='recipe_button'>`: Creates a division for styling purposes.
- `<a href='/ingredient'>`: Creates a hyperlink with the text "Help me choose a recipe" that links to the "/ingredient" route.

#### Data Table Section:

- `<div class="wrapper">`: Creates a wrapper division for content.
- `<div id="kitchenSection">`: Creates a division for kitchen-related content.
- `<table class="data-table">`: Defines a table with the class "data-table."
- `<thead>`: Defines the table header.
- `<tr>`: Defines a table row.
- `<th>`: Defines table header cells.
- `<tbody>`: Defines the table body.
- `{% set max_length = [fridge|length, pantry|length, freezer|length]|max %}` : to set the length of the columns
- `{% for i in range(max_length) %}`: Iterates over a range based on the maximum length of fridge, pantry, and freezer.
- `<tr>`: Defines a table row for each iteration.
- `{% for storage in [fridge, pantry, freezer] %}`: Iterates over fridge, pantry, and freezer.
- `<td class="fridge-container">`: Defines a table cell with the class "fridge-container."
- `{% if i < storage|length %}`: Checks if the current index is within the length of the storage and displays item details within a div with the class "item-row."

#### Button Section:

- `<ul>` :buttons in an unordered list
- `<class="main_button">`: a class for buttonss, created for styling purposes
- `<li>`: list element for each button
- `<a href='/add_stock'>` : anchor element behaves like a button, navigating to our add, update and delete stock forms on separate html pages

<br>

</details>
<details>
   <summary>search_recipe.html</summary>

<br>

<p>Within this HTML code enables us to visualise the webpage with a form for searching recipes by ingredient and a section to display the search results. 
	The page utilises Jinja templating syntax ({% ... %}) for dynamic content rendering.</p>

- `<!DOCTYPE html>`: Specifies the document type and version of HTML being used, in this case, HTML5.
- `<html lang="en">`: The root element of the HTML document, indicating that the document is written in English.

#### Head Section:

- `<head>`: Contains meta-information about the HTML document.
- `<meta charset="UTF-8">`: Sets the character encoding to UTF-8, ensuring proper handling of text in different languages.
- `<link rel="stylesheet" href="static/style.css" />`: External style sheet for styling.
- `<center><a class="home_button" href="/">` Anchor tag behaves like a button, linking user back to main page.Centred on page.  

#### Body Section:

- `<body>`: Contains the content of the HTML document.
- `<h1>`: Defines a top-level heading, indicating the title of the page as "Recipe Search by Ingredient."

#### Search Form:

- `<form id="ingredientForm" method="POST" action="/search_recipe">`: Defines a form with an ID, method (POST), and action (the URL where form data is sent).
- `<div class="input-container">`: Container for styling purposes.
- `<label for="ingredient">`: Label for the input field.
- `<input type="text" id="ingredient" name="ingredient" required>`: Text input for entering an ingredient, with ID, name, and a required attribute.
- `<button type="submit">`: Submit button for the form.

#### Display Results:

- `<div>`: Container for displaying search results.
- `<h2>`: Subheading for the section, indicating "Search Results."
- `<ul>`: Unordered list to contain the list of recipes.
- `{% if recipes %}`: Conditional statement checking if there are recipes to display.
- `{% for recipe in recipes %}`: Loop through each recipe in the recipes list.
- `<li>`: List item for each recipe.
- `<a href="{{ recipe['recipe']['url'] }}" target="_blank">`: Link to the recipe's URL, opening in a new tab.
- `<h3>{{ recipe['recipe']['label'] }}</h3>`: Heading displaying the recipe label.
- `{% else %}`: Executed if no recipes are found.
- `<p>No recipes found.</p>`: Paragraph indicating that no recipes were found.

<br>

</details>
<details>
<summary>shoppinglist.html</summary>

<br>

<p>The `shoppinglist.html` file is part of the Flask application for our Smart Pantry, and it dynamically generates a shopping list with checkboxes based 
	on the data provided in the text variable. The "Download" link enables the user to download the shopping list as a text file.</p>

- `<!DOCTYPE html>`: Declares the document type and version of HTML.
- `<html lang="en">`: Defines the root element of the HTML document with the language attribute set to English.
- `<head>`: Contains meta-information about the HTML document, such as character set and linked stylesheets.
- `<meta charset="UTF-8">`: Specifies the character encoding for the document as UTF-8.
- `<link rel="stylesheet" href="static/list.css"/>`: Links an external CSS stylesheet named "list.css" located in the "static" folder.
- `<body>`: Contains the content of the HTML document that will be displayed in the browser.
- `<center><a class="home_button" href="/">Home</a></center>` : anchor tag behaves like a button, linking user back to main page. Centred with HTML tags. 
- `<h1 class='para'>` : Heading informing user they are low on stock of items listed below.
- `<h2 class="shopping_list">` : Header saying 'Shopping List'
- `<ul class="list">` : Unordered list with class for styling purposes
- `{% for line in line %} ... {% endfor %}</ul>`: Uses Jinja templating to loop through items in the text variable and generate a centered unordered list.
- `<li><input type="checkbox"> {{ line }}</li>`: Creates list items with checkboxes for each line in the text variable.
- `<a href="{{ url_for('file_downloads') }}" download="Shopping_List.txt">Download</a>`: Provides a link to trigger the download of a file. The url_for function generates the URL for the "file_downloads" endpoint, and the download attribute specifies the suggested filename.

<br>

</details>

<br>

### CSS

<p>This CSS meticulously designs the Smart Pantry's webpage, specifying styles for various elements. Its goal is to establish a visually appealing layout, 
	improving the user experience and capturing the system's distinct identity. From colour schemes to layout structures, each line contributes to a 
	seamless interaction, ensuring users navigate with ease.</p>

<br>

<details>
<summary>style.css</summary>

<br>

#### Font Import:

- Imports the "DM Serif Display" font from Google Fonts for use in the project.

#### Body Styling:

- Sets margin and font styles for the entire body.
- Utilises viewport-relative units for font size responsiveness.
- Specifies the font family as 'DM Serif Display'.

#### Index Background Styling:

- Sets the background of elements with the class "index_bg" to a combination of an image and a light gray colour.

#### Header 1 Styling:

- Defines font styles for the `<h1>` element.

#### Background Styling for Fridge and Ingredient Sections:

- Sets background images for elements with the classes `fridge_bg` and `ingredient_bg`.
- Adjusts background size, repetition, and position.

#### Link Styling:

- Defines styles for `<a>` elements, setting the text color and removing underlines.

#### Navigation Styling:

- Styles the navigation bar with a flex layout, centered items, and styled list items.

#### Ingredient List Styling:

- Defines styles for lists within elements with the class `ing_list`.

#### Button Styling:

- Defines general styles for buttons, including removing borders and adding hover effects.

#### Input Styling:

- Styles for input elements, including colour, focus outline, and placeholder text.

#### Wrapper Button Styling:

- Styles for a wrapper containing an input field and a button.

####Section Styling:

- Styles for various sections like `or_navigation`, `recipe_button`, `main_button`, etc.

#### Table Styling:

- Defines styles for a data table, alternating background colours for different table cells.

####Prompt Styling:

- Styles for prompts, adding a background colour and border radius.

####Link Styling:

- Styles for links with the class `kitchen-title-link`.

<br>

</details>

<details>
<summary>new.css</summary>

<br>

#### `wbody` Selector:

```css
wbody {
    margin: 0;
    font-family: 'Arial', sans-serif;
    background-color: #f2f2f2;
}
```

- Sets the styling for the overall body of the webpage.
- Removes default margin.
- Applies 'Arial' font or sans-serif as a fallback.
- Sets the background color to a light grayish tone (#f2f2f2).

#### `.wrapper` Class:

```css
.wrapper {
    display: flex;
    justify-content: space-around;
    align-items: stretch;
    margin-top: 20px;
    gap: 20px;
    padding: 20px;
}
```

- Configures a flex container for a section of the webpage.
- Uses flex properties to distribute space around the child elements.
- Aligns items to stretch vertically.
- Adds margin, gap, and padding for spacing.

#### `.data-table` Class:

```css
.data-table {
    border-collapse: collapse;
    width: 100%;
    background-color: #fff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```

- Styles a table element to resemble a data table.
- Collapses the borders between table cells.
- Sets the width to 100%.
- Provides a white background with rounded corners and a subtle box shadow.

#### `th, td` Selectors:

```css
th, td {
    border: 1px solid #ddd;
    padding: 15px;
    text-align: left;
}
```

- Styles table header cells (th) and regular cells (td).
- Adds a 1px solid border and padding.
- Aligns text to the left.

#### `.or_navigation` Selectors:

```css
.or_navigation {
    background-color: #FF681C;
    color: white;
    padding: 15px;
    border-radius: 8px 8px 0 0;
}
```

- Styles a navigation element.
- Applies a background colour of #FF681C (orange).
- Sets white text colour.
- Adds padding and rounded corners to the top.

#### Container Classes:

```css
.fridge-container {
    background-color: #FFC18E;
}

.pantry-container {
    background-color: #B2CCB9;
}

.freezer-container {
    background-color: #53A9BE;
}
```

- Styles three different containers, representing sections of the webpage.
- Applies distinct background colors to each container.

#### `.prompt` Class:

```css
.prompt {
    margin-top: 20px;
    background-color: #FF681C;
    border-radius: 8px;
    color: white;
    padding: 15px;
    text-align: center;
}
```

- Styles a prompt element.
- Sets a background color of #FF681C (orange).
- Adds border-radius and padding.
- Sets text color to white and centers the text.

<br>

</details>

<br>

### Python

<p>Python serves as the backbone of the Smart Pantry project, providing a robust and versatile programming language for the system's functionality. Leveraging Python, 
	we harness the language's readability and efficiency to implement core features such as inventory management, recipe generation, and seamless interaction with 
	the backend. The Flask framework, built with Python, facilitates the development of a dynamic and responsive web application, ensuring a smooth user experience.</p> 
<p>With Python's extensive libraries and straightforward syntax, our team collaboratively employs the language to implement essential project components, fostering 
	maintainability and scalability. The choice of Python reflects our commitment to an effective and streamlined development process, empowering the Smart Pantry 
	system to deliver a seamless and intuitive solution for kitchen inventory management.</p>

<br>

<details>
<summary>main.py</summary>

<br>

#### Import Libraries:

- `import requests`: Imports the requests library for making HTTP requests.
- `import json`: Imports the json library for working with JSON data.
- `from flask import url_for`: Imports the url_for function from the Flask framework for constructing URLs.

#### POST REQUEST (ADD):

- Function `add_stock_item_fridge` takes input parameters for fridge stock item details.
- Constructs a dictionary `new_fridge_stock` with the provided details.
- Sends a PUT request to a specified endpoint `url_for('add_item_fridge')` with JSON data.
- Handles exceptions for different types of errors and prints relevant error messages.

#### User Interaction (`run_fridge`):

- Asks the user if they want to add stock to the fridge.
  - If yes, takes input for stock item details and calls `add_stock_item_fridge`.
  - Prints a success message after adding the item.

#### PUT REQUEST (UPDATE):

- Function `update_fridge` sends a PUT request to update the fridge.
- Prints the response status and JSON content if the status code is 201 (Created).

#### DELETE REQUEST (REMOVE):

- Function `delete_stock_item_by_name` takes input for stock store and item name.
- Sends a `DELETE` request to a specified URL for deleting the item.
- Prints the response content if the status code is 200;
  - otherwise, prints a failure message.

#### Main Execution:

- Executes `run_fridge` when the script is run.

<br>

</details>
<details>
   <summary>RecipieAPI.py</summary>

<br>

#### Import Statements:

- The code imports necessary libraries and modules, including:

  - `requests`,
  - `API_key`,
  - `math`,

  and custom modules from the utilities module such as:

  - `SqlDatabase`
  - `DbConnectionError`

#### API Key Retrieval:

- The app ID and key for the Edamam recipe API are retrieved from a separate file, `API_key.py`, which is not provided in the code snippet.
- Users need to register for a developer plan on Edamam to obtain their unique app ID and key.

#### Function to Get a Random Recipe:

- `get_random_recipe` function sends a request to the Edamam API to retrieve a random recipe based on a specified query.
- It processes the response, extracts relevant information such as recipe label and ingredients, and returns the data.

#### Function for Recipe Search by Ingredient:

- `recipe_search_by_ingredient` function searches for recipes based on a specified ingredient using the Edamam API.

#### Function for Requesting Next Page of Results:

- `next_page_request` function sends a request to the next page of results when viewing multiple recipes.

#### Function to Create a Shopping List:

- `create_shopping_list` function takes a list of missing ingredients and writes them to a text file, creating a shopping list.
  - The file is named `shopping_list.txt`.

#### Main Execution Function - run:

- Calls `recipe_search_by_ingredient` to get initial results.
- Displays the first 20 recipes to the user.
- Asks the user if they want to see more recipes.
- If the user chooses to see more, retrieves additional recipes until the user decides to stop.
- Asks the user to select a recipe and performs actions like:
  - checking stock,
  - creating a shopping list,
  - updating the pantry.

#### Functions for Stock Checking and Pantry Update:

- `check_stock_for_recipe` function checks the stock for a given list of ingredients and weights.
- `update_pantry` function updates the pantry based on the selected recipe, deducting quantities from the available stock.

#### Main Execution:

- The script runs the run function when executed, providing the user with an interactive experience to explore and manage recipes using the Edamam API.

<br>

</details>
<details>
<summary>App.py</summary>

<br>

<p>This Flask application provides routes for kitchen management, recipe handling, and shopping list functionalities. It integrates with HTML templates for rendering 
	dynamic content and utilises both POST and GET methods for data handling. The application is specifically structured for modular and maintainable code.</p>

#### Import Statements:

- The code begins with import statements, bringing in necessary functions and modules from:
  - `Flask`,
  - `utilities`,

and other custom modules:
	- `utilities`,
	- `RecipeAPI`).

#### Flask App Initialization:

- `app = Flask(__name__)`: Initializes a Flask web application.

#### Routes:

- `@app.route('/')`: Renders the `index.html` template for the root URL.
- `@app.route('/kitchen', methods=['GET', 'POST'])`: Handles requests to the '/kitchen' URL.
  - If it's a POST request, it adds an item to the kitchen inventory; otherwise, it retrieves and displays the updated stock data.

#### Fetching Recipe Ingredients:

- `@app.route('/ingredient', methods=('GET', 'POST'))`: Manages requests to '/ingredient'.
  -For GET requests, it retrieves protein data and renders the 'ingredient.html' template.
  - For POST requests, it fetches a random recipe based on the user's query and updates the template.

#### API Endpoints for Adding, Updating, and Deleting Fridge Items:

- `@app.route('/add_item_fridge', methods=['PUT'])`: Adds a new item to the fridge inventory using JSON data from a PUT request.
- `@app.route('/update/fridge', methods=['PUT'])`: Updates the fridge inventory by calling the `update_inventory` function.
- `@app.route('/delete/<stock_store>/<item_name>', methods=['DELETE'])`: Deletes an item from the specified stock store.

#### Generating Shopping List:

- `@app.route('/generate_shopping_list')`: Generates a shopping list and stores it in a text file.

#### Routes for Shopping List Display and Download:

- `/shopping`: Renders the 'shoppinglist.html' template with the content of the shopping list file.
- `/return_file`: Allows users to download the shopping list file.

#### Recipe Search:

- `@app.route('/search_recipe', methods=['GET', 'POST'])`: Handles recipe search requests.
  - For POST requests, it searches for recipes based on the provided ingredient.

#### App Run:

- `app.run(port=5002, debug=True)`: Runs the Flask app on port 5002 in debug mode.

<br>

</details>
<details>
<summary>utilities.py</summary>

<br>

#### DbConnectionError and DbQueryError Classes:

- Custom exception classes for handling database connection and query errors.
- DbQueryError includes information about the query and parameters.

#### SqlDatabase Class:

- Manages database connections using the `mysql.connector` module.
- Provides methods for connection, disconnection, executing queries, committing, rolling back, and starting transactions.

#### StockDelete Class:

- Deletes an item from a specified table in the `Smart_Pantry` database.
- Uses `SqlDatabase` for database operations.

#### ShoppingList Class:

- Manages a shopping list, populates it from the database, and allows for modifications.
- Uses the `SqlDatabase` class for database operations.

#### `assert_sell_by_date(sell_by_date)`:

- Validates the format of the sell-by date.

#### `_add_item(stock_store, values)`:

- Inserts a new item into a specified table in the `Smart_Pantry` database.
- Uses the `SqlDatabase` class for database operations.

#### `update_inventory()`:

- Updates a record in the `Smart_Pantry` database based on user input.
- Uses the `SqlDatabase` class for database operations.

#### `retrieve_stock(stock_store)`:

- Retrieves stock information from a specified table in the `Smart_Pantry` database.
- Uses the `SqlDatabase` class for database operations.

#### `fetch_protein_data()`:

- Fetches protein data from the database and displays it.

#### `low_stock()`:

- Checks ingredient quantities in the database, creates a shopping list, and allows user interaction.
- Uses the `SqlDatabase` class for database operations.

#### `ShoppingList.populate_from_database()`:

- Populates the inventory with data from the database.
- Uses the `SqlDatabase` class for database operations.

#### `ShoppingList.add_item(item, quantity)`:

- Adds an item and its quantity to the inventory.
- Checks and asserts conditions on the parameters.

#### Additional Notes:

- The code uses the mysql.connector module for MySQL database interactions.
- The database connection details are retrieved from a config module.
- Input validation and error handling are implemented throughout the code.
- SQL queries are dynamically constructed and executed.
- The code follows the principle of separating concerns by using classes for database operations and specific functionalities.

<br>

</details>

<br>

### MySQL

<p>The Smart Pantry project leverages MySQL as its relational database management system. MySQL is employed to efficiently store and manage data related to the kitchen inventory, 
	comprising details such as item names, quantities, units, expiration dates, and stock levels.</p>

<p>The use of MySQL facilitates robust data organization, retrieval, and modification, providing a reliable foundation for the seamless operation of the Smart Pantry system. With MySQL, 
	the project ensures data integrity and enables users to interact with their kitchen inventory in a structured and efficient manner.</p>

<br>

<details>
<summary>SmartPantryDB.sql</summary>

<br>

<p>This script establishes the Smart Pantry database, creates tables for different storage areas, populates them with sample data, and creates views for specific ingredient types and expiration details.</p>

#### Database Setup:

- `DROP DATABASE smart_pantry;`: Deletes the existing Smart Pantry database if it exists.
- `CREATE DATABASE IF NOT EXISTS Smart_Pantry;`: Creates the Smart Pantry database if it doesn't exist.
- `USE Smart_Pantry;`: Specifies the use of the Smart_Pantry database.

#### Table Creation:

- Three tables, Fridge, Freezer, and Pantry, are created to manage different types of ingredients.
- Each table has columns for ID:
  - IngredientName,
  - TypeOfIngredient,
  - Quantity,
  - UnitOfMeasurement,
  - MinimumQuantityNeeded,
  - SellByDate.

#### Data Insertion:

- Inserts sample stock data into each table for items (such as milk, chicken, and flour), including details like:
  - quantity,
  - unit of measurement,
  - minimum quantity needed,
  - sell-by date.

#### Views Creation:

- `ProteinView`: Combines and selects all columns from Fridge, Freezer, and Pantry tables where the TypeOfIngredient is '%Protein%'.
- `ExpiredIngredients`: Lists ingredients from all tables where the SellByDate is before the current date.
- `ExpiringIngredients`: Lists ingredients from all tables with SellByDate within the next two days.

<br>

</details>

<br>

## Unit Testing

<p>Our aim is to ensure the robustness and reliability of our codebase. Unit testing is a fundamental practice in software development that involves testing individual units or components of our code in isolation to validate their correctness. 
	By systematically examining each unit's functionality, we can identify and address potential bugs or issues early in the development process. Our commitment to thorough unit testing contributes to the overall quality of our software, 
	fostering a more stable and maintainable codebase. This section provides insights into our unit testing approach, including the tools, methodologies, and best practices we employ to guarantee the integrity of our code.</p>

<br>

<details>
	<summary>main.py</summary>
	
- `assert_sell_by_date` Function:
	- This function checks the validity of the sell-by date.
	- It ensures that the sell-by date is a string and follows the format YYYY-MM-DD.
- `_add_item` Function:
	- Inserts a new item into the specified table in the Smart_Pantry database.
	- Validates the table name, values format, and executes the insert query.
- `StockDelete Class`:
	- Deletes an item from a specified table in the Smart_Pantry database.
	- Validates the table name, item name, executes the delete query, and handles errors.
- `update_inventory_record` Function:
	- Updates a record in the Smart_Pantry database based on user input.
	- Validates table name, column name, data ID, and new value. Executes the update query.
- `retrieve_stock` Function:
	- Retrieves stock information from a specific table in the Smart_Pantry database.
	- Validates the table name, executes the select query, and prints the result.
- `fetch_protein_data` Function:
	- Fetches protein data from the database and handles potential exceptions.
- `low_stock` Function:
	- Connects to the database and retrieves low-stock items from different tables.
- `ShoppingList Class`:
	- Manages a shopping list with methods to populate from the database, display, and interact with the user.
- `populate_from_database` Function (Outside of Class):
	- Populates the inventory and shopping list from the database, handling low-stock items.
- `fetch_out_of_date` Function:
	- Fetches data from the database where ingredients are past their sell-by date.
- `fetch_expiring_ingredient_data` Function:
	- Fetches data from the database where ingredients' sell-by date is today or in the next two days.
- Example Usage Section:
	- Demonstrates the usage of the classes and functions with comments.

<br>

</details>

<details>
	<summary>App.py</summary>
	
- Welcome Route:
	- Tests the `/welcome` route to ensure a successful response with a status code of 200 and the presence of the 'Welcome' message.
- Kitchen Route:
	- Tests the `/kitchen` route with a POST request, verifying a successful response with a status code of 200 and the presence of the 'Updated Kitchen' message.
- Ingredient Route:
	- Utilizes a patch to mock the `get_random_recipe` function and tests the `/ingredient` route with a POST request. Ensures a successful response with a status code of 200 and the presence of a recipe label.
- New Item Fridge:
	- Tests the `new_item_fridge` function with a mocked input data for adding a new item to the fridge. Verifies a successful response with a status code of 200 and the returned JSON matching the input data.
- Update Fridge Stock:
	- Tests the `update_fridge_stock` function with a generic update data and another test with specific data. Ensures a successful response with a status code of 200 and the appropriate success message.
- Delete Item From Stock:
	- Tests the `delete_item_from_stock` function for both deleting an existing item and attempting to delete a nonexistent item. Verifies successful deletion and appropriate error response.

<br>

</details>

<details>
	<summary>RecipeAPI.py</summary>

  - `test_get_random_recipe`: 
    - Tests the `get_random_recipe` function, simulating a successful API response.
    - Mocks the `requests.get` method and asserts the expected data structure.

  - `test_see_more_recipes`: 
    - Tests the `see_more_recipes` function, specifically its interaction with `recipe_search_by_ingredient`.
    - Uses side effects to simulate user input and asserts the expected function calls.

  - `test_next_page_request`: 
    - Tests the `next_page_request` function, checking its behavior when making a request to the next page.
    - Mocks the `requests.get` method and asserts the expected API response.

  - `test_create_shopping_list`: 
    - Tests the `create_shopping_list` function, ensuring correct file writing.
    - Mocks the `open` method and asserts the expected file content.

  - `test_get_random_recipe_success`: 
    - Tests the `get_random_recipe` function for a successful API call.
    - Mocks the `requests.get` method and asserts the expected API response.

  - `test_get_random_recipe_failure`: 
    - Tests the `get_random_recipe` function for a failed API call (404).
    - Mocks the `requests.get` method and asserts the function's response.

  - `test_recipe_search_by_ingredient_success`: 
    - Tests the `recipe_search_by_ingredient` function for a successful API call.
    - Mocks the `requests.get` method and asserts the expected API response.

  - `test_recipe_search_by_ingredient_failure`: 
    - Tests the `recipe_search_by_ingredient` function for a failed API call (404).
    - Mocks the `requests.get` method and asserts the function's response.

<br>

</details>

<details>
	<summary>utilities.py</summary>

- DbConnectionError Tests:
	- Ensure the `DbConnectionError` instance can be created.
	- Confirm that `DbConnectionError` inherits from the base Exception class.
	- Validate the ability to provide a custom error message.
	- Verify the use of a default message when none is provided.
- DbQueryError Tests:
	- Check the creation of `DbQueryError` instances with specific properties.
	- Examine the string representation of `DbQueryError` for proper formatting.
- SetUp Tests:
	- Confirm the initialisation of SqlDatabase with a valid database name.
	- Assert an `AssertionError` when trying to initialize SqlDatabase with a None database name.
	- Validate successful connection to the database and handling of connection failure.
	- Ensure proper disconnection by mocking the connection close method.
	- Test the execution of queries, both successful and with failure.
- TestMetrifyFunction:
	- Verify the correct conversion from grams to kilograms and milliliters to liters.
	- Check for appropriate handling of invalid input and output units, negative amounts, and combinations of both.
</details>

<br>

## Meet the team

<!--
PERSONAL STATEMENT: Possible questions you can answer are: 
- "What has been your favourite/most challenging thing to do on the group project", 
- "Why is technology so important to you". 
- "What aspects of the course have you found most enjoyable?", 
- "What led you to pursue a career in tech?", 
- "What's your secret skill not many people know?" 
(This is just guidance, so please feel free to write what ever you would like to add and be creative! :) ) 
-->

### Vanessa ([@somedaysmash](https://github.com/somedaysmash))

<br>

:brain: **Project contributions:**
*<p>Created git repository; wrote class for database connection, wrote functions to add stock to database, edited data for tables and added views with accompnaying functions, added excepetions and assertions (rolled some back due to conflicts).</p>*

👩‍💻 **Personal statement:**
*<p>"Tackling three different programming languages within the first four weeks was the kind of fast-paced learning I love. After quickly finding my feet with SQL, I promptly tripped over them in Python. Our first team project was a great warm up to the main event. 
Taking on the more complex lessons in the last four weeks along with putting our new skills into practice collaboratively has more time-management and teamwork than any of the skill taught. Learning how to manipulate the database through python is the most enjoyable. The least fun is trying to troubleshoot! 
Moving into a career in technology feels long-overdue - I am ready for the challenges ahead of me! On a more personal note, I am a massive Star Wars fan: I have cosplayed as Chewbacca (in my homemade costume), our youngest padawan is named 'Orson Benedict' - 'Obi' for short!
."</p>*

<br>

### Anna ([@ketre](https://github.com/ketre))

<br>

:brain: **Project contributions:**
*<p>Responsible for initial design mock-ups in Figma and further styling implementation across pages. Rendering HTML templates through Flask routes. Helped with code cleaning and import debugging. </p>*

👩‍💻 **Personal statement:**
*<p>"The collective effort and collaboration within the team made this (at times challenging) journey worthwhile. Working as a team has brought the theoretical knowldge into the real world - a world with git commits and collaborative software development.</p><p>This group project allowed me to push my limits and challenge myself with each and every sprint we've done. I'm thrilled to see the website come to live from what was just an idea a month ago - and am grateful to have the most hard-working and collaborative team to have achieved this with."</p>*

<br>

### Karen ([@klace00](https://github.com/klace00))

<br>

:brain: **Project contributions:**
*<p>Collaborative code development in Python, Individual SWOT analysis, Debugging and problem-solving, Contribution to project document.</p>*

👩‍💻 **Personal statement:**
*<p>"Embarking on the CFGDegree as a career changer in my forties was initially daunting and I often struggled with imposter syndrome. Over the duration of the course I've been amazed at how much I've grown in both skill and confidence. A particular highlight of this journey has been our group project. Here, I have found myself part of a fantastic group who have worked with a strong collaborative spirit with every member contributing significantly. Our project has pushed the boundaries of my coding abilities, often delving into areas that felt complex beyond my scope. However, as a team we have embraced this challenge and turned our errors into learning opportunities which enabled us to progress towards our goal. I feel so incredibly proud of what we've achieved as a team and I know I can take my learning from this experience forward into my future endeavors in this industry."</p>*

<br>

### Lauren A ([@Laurenhomeridge](https://github.com/Laurenhomeridge))

<br>

:brain: **Project contributions:**
*<p>Generated the project concept, Created the Trello board, Individual SWOT analysis, Python functions, De-bugging, Cleaning code</p>*

👩‍💻 **Personal statement:**
*<p>"During my collaborative experience within our dynamic team, I thrived in a synergistic environment that fostered creativity, innovation, and effective communication. Working collectively towards our common goals, I actively contributed my skills while embracing diverse perspectives within the team. This collaborative journey not only enhanced my ability to adapt and learn from my peers but also underscored the significance of teamwork in achieving remarkable outcomes. I am proud to have been a part of this cohesive team, that not only met challenges head-on but also celebrated shared successes, shaping an invaluable chapter of personal and professional growth in my journey."</p>*

<br>

### Amy ([@Amy-Dangerfield](https://github.com/Amy-Dangerfield))

<br>

:brain: **Project contributions:**
*<p>Code for Edamam API calls, python functions, HTML templates, CSS, flask routes, individual SWOT analysis.</p>*

👩‍💻 **Personal statement:**
*<p>"I have thorougly enjoyed working within the team towards this project. Due to the supportive attitudes of the team, I certainly felt more confident about taking on challenges and seekng answers. I have learnt a lot from my team members as collaboration within the team has been excellent. I also have benefited from my team members existing skils and experience, as it meant the project and task delegation has been very well managed. I'm excited to start a meaningful career and build on the skills developed over the past 16 weeks."</p>*

<br>

### Dorothy ([@dotmcevoy](https://github.com/dotmcevoy))

<br>

:brain: **Project contributions:**
*<p>Meeting note taker, created SQL database, various python functions, de-bugging, created Trello board for SWOT analysis, individual SWOT analysis, presentation slide leader, project documentation editor</p>*

👩‍💻 **Personal statement:**

*<p>"Throughout the CFG degree and group project, my favorite aspect has been the collaborative journey with my fellow career changers. Tackling new and exciting problems together has not only led to day-by-day improvements in my own skills but also in the growth of my fellow team members, which has been inspiring to see.</p> <p>Technology is integral to my life, and my desire to learn and advance in the field is fueled by a passion for collaborating with innovative software engineers and making a tangible impact for companies. My decision to pursue a tech career is rooted in a goal to satisfy my technical and analytical curiosity, aligning perfectly with the dynamic nature of this space. This final team project has been a wonderful end to the CFG degree and welcome to the collaborative and problem-solving nature of being a software engineer!</p> <p>To end this on a personal note, a not-so-well-known fact about me is that I used to compete in hip hop crew competitions. Even today, I never shy away from a dance battle when out with friends."</p>*

<br>

### Lauren S ([@Lor9538](https://github.com/Lor9538))

<br>

:brain: **Project contributions:**
*<p>Python functions, unit testing, individual and project SWOT analysis, README.md, communication and collaboration booklet</p>*

👩‍💻 **Personal statement:**
*<p>"In our group project, the most challenging yet rewarding task was diving into the intricate world of unit testing for our Python files in the Smart Pantry application. Implementing robust testing strategies added a layer of complexity, but the satisfaction of ensuring our code's reliability was worth the effort.</p> <p>Throughout the course, I've found immense joy in the process of continuously enhancing my skills. Whether it's independently exploring new technologies or collaborating within the group, the journey of learning is what I find most enjoyable.</p> <p>My passion for technology stems from its dynamic and diverse nature. It's not just about coding; it's the gateway to endless creativity and innovation. Technology has this incredible power to turn groundbreaking ideas into tangible realities, and being part of that transformation is what makes pursuing a career in tech so important to me.</p> <p>...and finding new ways to torment my family with my two new best friends, Python and AlexaDeveloperConsole - that's if I ever get my Alexa access back!"😉*</p>

<br>

## Further Information

<details>
<summary>Project Proposal</summary>
<br>

Please click [here](https://docs.google.com/document/d/1zBlx4-xmz2H0JjW7n_EPsaAGDybNqQM8rIOfrlSlX1k/edit#heading=h.z6ne0og04bp5) to view our Project Proposal.

<br>

</details>
<details>
<summary>Sprint Minutes</summary>
<br>

<details>
	<summary>Sprint 1 of 5</summary>
	<br>

 The idea is:

- App where we can input shopping. Updated and stored in inventory.
  - Then we can generate recipe based on available ingredie3nts.
  - And generate shopping list based on that. Or we can add stuff that aren’t low or aren’t in the inventory – adjustable shopping list.
- Automatically update inventory once we select the recipe we want to use.
- 3 separate stock for cupboard, fridge, freezer. Able to click on those and you can see what’s inside.
  - Linked to SQL database. -> by default we will fill with random quantities and ingredients = starting stock.
  - Able to update or delete ingredients.
- Anna K to try out a demo on Figma to brainstorm and ensure we are only on the same page for how we want it to look and function.
- Log in page to elevate code. -> another database to store user info in SQL (desirable).
- Basic Functions:
  - JS, HTML, CSS – button clicking, webpages,
  - Python
  - SQL: DOT TO CREATE
    - Fridge stock table
    - Freezer stock table
    - Cupboard stock table
    - Ingredient
    - Quantity
    - Type/Description
    - Min needed for stock
    - Sell by date
  - Storage location
- User info table (desirable)
- Edamame API – filter recipes through that.
- Code will need to filter through available ingredients and then go through API for recipe.
- User can specify main protein or thing: ‘what do you want tonight’, ‘chicken’, ‘ok here’s a recipe for chicken wings’
- Order proteins by sell by date:
  - Chicken
  - Beef
  - Tofu
  - Fish
  - Pork
  - Egg
- Surprise me button! (desirable)
- option for high protein meals or low calorie etc (desirable)
- Function to control range for example: where if less than 1 protein in fridge suggest another protein to buy
- When recipe is suggested have button for ‘Yes, I cooked this’ so that stock can update.
- There should be a function where we have alerts when things go below certain stock level e.g. milk
- Python functions to make calls to API:
- Function to connect to API: Amy
- Python function to add, delete, update etc the SQL:
- Python function to add: Vanessa
- Python function to delete: Karen
- Python function to update: Lauren
- Lauren has done HTML and CSS
- We can create a logo and brand identity.
- Vanessa created repo on GitHub
- First function: let’s generate a random recipe first.
- Python function to add to inventory
- START with SQL stock database
- Reconnect: Sunday 20th at 4pm or we may adjust for USA time
- Lauren has made a merged activity log so we can monitor our progress – it's pinned on slack.

<br>

</details>
<details>
	<summary>Sprint 2 of 5</summary>
	<br>

- Put files in .gitignore.
- API connection is working but Amy still wants to completely finish it.
- Will need to put in exceptions / insertions
- Clarify – should we be using lots of classes? Should everything we write now be a class?
- Go over class recording showing previous cohort project to check if they used lots of classes?
- For HW2 we will tackle it next week but we may assign Qs to each other or just each take a stab at the questions and put together a whole complete file.
- Make sure we are filling in the activity logs!
- Add, update, delete item functions are complete.
- Next function we want to do is iterate through what we have through stock and find and generate random recipe.
- Base it on proteins – ask user to select protein from list of what’s in stock. Query will find proteins, display, and then search the API. Start with a list of 10. Then select an item. Then we see what we need to buy to complete the recipe and what we already have.
- We may need a unit converter – everything in the API can be in grams.... We may just change our database to show only grams – check where the word decimal is coming from when show all.
- Code: look at proteins and select = Lauren S
- Search API and show list of 10 = Lauren A
- Search stock based on the recipe ingredients = Dorothy
- Function shows true and false on whether we have items= Dorothy
  - and if false then add to a shopping list. = Vanessa
- Code to present shopping list = Anna
- When recipe is used – update stock levels = Karen
  `<br>`

</details>
<details>
	<summary>Sprint 3 of 5</summary>
	<br>

- Some over spill from spring 2 – Karen has Wed planned for this
- Need to check the DB (GRAMS!) - Dot!!
- We should all try giving the code a look over – Lauren A says she will check it after our meeting
- How do we get the code to run – why is PyCharm mean to us
- Need to include Test file – unit tests – Lauren S says she will try and get some basics in. Like a separate directory of files? Lauren S will share some resources on this in slack also.
- Need to tidy it up
- This sprint will be focused on getting the project to run and understanding what each of us have done.
- We should do a group retrospective – also what happened to our SWOT analysis? - another Trello for this so we can all put our SWOTs in there – Dot focus on making this diagram
- Run file (ap.py) - you’ll see website, once you click on generate recipe, you’ll see new page …etc
- Debugging focus this sprint. Remember to comment out codes to check what functions are having issues.
- Lauren S idea: Put code that isn’t used in separate file to showcase our thinking process and how we changed over time!
- Error handling – Vanessa
- Presentation slides start – Dot
- Screen record pages - Anna
- Update meeting – Wednesday after class
  `<br>`

</details>
<details>
	<summary>Sprint 4 of 5</summary>
	<br>

Continuation with overflow from sprint 3 with main focus on:

- Unit testing and collating swot analysis to file - Lauren S,
- Debugging and functionality - Dorothy, Karen, Amy, Lauren A
- Front-end (HTML, CSS) - Anna
- Design presentation - Dorothy
- Smart Pantry flow diagram - Vanessa
- SQL DB maintenance - Vanessa
  `<br>`

</details>
<details>
	<summary>Sprint 5 of 5</summary>
	<br>

- Trying to fix and debug - all hands on deck.
- Try to front load work this week as many people have busy weekends coming up!
- Fetching protein data is a bit fidgety – if it isn’t working for you, check your SQL table as Vanessa updated it to include a protein label.
- Make sure shopping list function works and can produce a txt file – Anna to make this shown in the HTML
- Transaction to roll back or commit shopping list function – Dorothy to do
- Data units adjust - Dorothy
- More data to be added to database – Vanessa
- What can we do with the shopping list – Karen
- Read me file – what to install, how to run, what to run in which order. - Lauren S to do. Government website has advice on the readability of this (linked in slack).
- Retrospective document – will be adding lots of screenshots and info e.g. SWOT. - Lauren S to do. `</p>`
  `<br>`

</details>
<br>

Minutes from each sprint are also available as a[PDF](https://github.com/somedaysmash/Software4_Group5_Smart_Pantry/Further_Information/Sprint_Minutes.pdf).

<br>

</details>
<details>
<summary>Group Task-List</summary>
<br>

Please click [here](https://trello.com/b/QptFT6Rh/smart-pantry) to access the task Trello board.

<br>

</details>
<details>
<summary>Project Activity Log</summary>
<br>

Please click [here](https://docs.google.com/spreadsheets/d/16BXI3OMypGLyWKrMeU4gZ8Bl4-RA6mzLRpgcV_PJK54/edit#gid=67646434) to view the Project Activity Log.

<br>

</details>
<details>
<summary>Smart Pantry Wireframes</summary>
<br>

[Draft wireframe](https://codepen.io/Lauren_Aldridge/pen/KKJqvLo)
<br>

[Final wireframe](https://www.figma.com/file/jcAyhESnTwMatxPtUYRRtp/Untitled?type=design&node-id=0-1&mode=design&t=gdudk9G8huLayTVl-0)

<br>

</details>
<details>
<summary>Smart Pantry Flowchart</summary>
<br>

![An image of a flowchart providing a visual representation of the logical flow and sequence of processes within the Smart Pantry application](https://github.com/somedaysmash/Software4_Group5_Smart_Pantry/blob/main/Further%20Information/Application%20Flowchart.png)

<br>

</details>
<details>
<summary>Team and Project SWOT Analyses</summary>
<br>

Please click [here](https://www.canva.com/design/DAF2Iuu3O6k/DcmZ1CGJk6h11gq_JfIYTg/edit?utm_content=DAF2Iuu3O6k&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) to view our independent and project SWOT analyses.

<br>

</details>
<details>
<summary>Team Collaboration and Communication</summary>
<br>

A booklet showing how we have been able to communicate and collaborate as a team througout this project can be accessed [here](https://www.canva.com/design/DAF3DJfNaks/_pmt_z7WhDnLPmtTW2lSmw/edit?utm_content=DAF3DJfNaks&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

<br>

</details>
<details>
<summary>Code Evolution and Breakdown</summary>
<br>

<p>This section is intended to show how our code has changed and evolved through the progression of our project.</p>

The file with our stale code can be found [here](https://github.com/somedaysmash/Software4_Group5_Smart_Pantry/blob/main/Further%20Information/Extra%20Code).

<br>

### RecipeAPI.py

Function: `get_random_recipe(query)`

- Commented-out Code:
  - It includes using URL parameters instead of a long URL.
  - There are attempts to extract recipe details like name, ingredients, and weight from the API response.
  - Zipping ingredients and weights into a dictionary and writing to a CSV file is also commented out.

Function: `run()`

- Commented-out Code:
  - It includes accessing and printing recipe labels and URLs.

Function: `check_stock_for_recipe(ingredients_and_weight)`

- Commented-out Code:
  - Queries for checking stock in the fridge, freezer, and pantry are commented out.

### Utilities.py

Redundant Function: `add_item_fridge()`, `add_item_freezer()`, `add_item_pantry()`

- Redundant Code:
  - Duplicate functions for adding items to the fridge, freezer, and pantry databases.
  - Each function follows a similar structure, connecting to the database and executing an INSERT query.

Redundant Function: `fetch_protein_data_db()`

- Redundant Code:
  - The function fetches protein data from a SQL database.
  - The function is not used elsewhere in the code.

Redundant Code for Class: `SHOPPINGLIST`

- Redundant Code:
  - A method for connecting to a MySQL database is commented out.

<p>Please note that some contextual information might be missing, and the code might not be fully functional without the uncommented sections or additional context.</p>

</details>
<br>

> [!NOTE]
> All evidence and documentation can be found in the 'Further Information' folder within our repository.

## Summary

<p>Smart Pantry emerges as an all-encompassing answer to streamline kitchen operations effectively. This innovative solution excels in providing automation features, fostering seamless collaboration, 
	and presenting users with a remarkably user-friendly interface. Through its sophisticated design and functionality, Smart Pantry aims to revolutionise kitchen management, making it not only 
	efficient but also accessible and intuitive for users. Whether through automated inventory tracking, collaborative recipe generation, or an intuitive user interface, Smart Pantry stands at the 
	forefront of modern kitchen management solutions, catering to the needs of households with its user-centric approach.</p>

<br>

## Resources

- [Canva](https://www.canva.com/)
- [Code Pen](https://www.codepen.io/)
- [Feedough](https://www.feedough.com/swot-analysis-generator/)
- [Figma](https://www.figma.com/)
- [GitHub Docs](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Google Sheets](https://www.docs.google.com/spreadsheets/)
- [gov.uk Content Design](https://www.gov.uk/guidance/content-design/writing-for-gov-uk)
- [gov.uk Writing Style Guide](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/451510/AGO_Writing_Style_Guide.pdf)
- [Government Digital Service Style Guide](https://www.gov.uk/guidance/style-guide)
- [Hemingway](https://hemingwayapp.com/)
- [Jet Brains](https://www.jetbrains.com/help/pycharm/creating-tests.html)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [Miro](https://www.miro.com/)
- [Mozilla Developers Network](https://developer.mozilla.org/en-US/)
- [Mural](https://www.mural.co/blog/sprint-retrospective)
- [Python Tutor](https://pythontutor.com/render.html#mode=edit)
- [Sadra](https://imsadra.me/unit-testing-in-python-and-best-practices)
- [Scaler](https://www.scaler.com/)
- [Trello](https://www.trello.com/)
- [W3Schools](https://www.w3schools.com/)
