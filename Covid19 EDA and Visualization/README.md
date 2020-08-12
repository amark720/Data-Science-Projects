# Secret Diary

A PHP/MySQL Web Application for creating Rich Text.

I loosely followed the MySQL section of an online <a href="https://www.udemy.com/the-complete-web-developer-course-2/">course</a> in the creation of this project to get some practice in PHP/MySQL.


## Installation
Note: I used XAMPP to set up the environment for this application on Windows. You'll have to install XAMPP or WAMP or similar yourself.

1. Setup a local server environment (e.g., XAMPP, WAMP).

2. Create a database with a name of your choice.

2. Clone this repository to your pc (If using XAMPP, then clone inside C:/xampp/htdocs).

3. Run `npm install` in at the project location in your command line.

3. Configure database settings inside app/connection.php.
```
$host = "HOSTNAME";         // Change HOSTNAME to localhost
$username = "USERNAME";     // Change USERNAME to your database user account username
$password = "PASSWORD";     // Change PASSWORD to your database user account password
$db = "DATABASE NAME";      // Change DATABASE NAME to the name from Step 2
```

5. You're set up! Go to localhost/ in your browser!

## Dependency
The following are APIs that this application is dependent on:
* [Quill](https://quilljs.com/) - [GitHub](https://github.com/quilljs/quill), [npm](https://www.npmjs.com/package/quill)

## Screenshots
Landing page  
<img src="/assets/img/landing-page.PNG" alt="Landing Page" height="80%" width="80%">

Diary page  
<img src="/assets/img/diary-page.PNG" alt="Diary Page" height="80%" width="80%">

Mobile  
<img src="/assets/img/responsive-landing-page.PNG" align="left">
<img src="/assets/img/responsive-diary-page.PNG" align="left">
