# table-builder
Table Builder Coding Challenge

Instructions:

Purpose
========
Build a HTML table out of json data

Exercise
==========
Refactor the code using Web Development best practices.

Notes
=======

- You are free to use any additional libraries that may be needed to simplify your code
- Bonus points for styling the page
- Additional Bonus for including any missing functionality. You are free to imagine what would make sense
if you were building this as part of an app.

- Make a list of refactorings that you have applied as a running list below:


Refactorings Applied
=====================
- Moved JavaScript to an external linked file
- Added footer for link to JavaScript files
- Added doctype
- Added character encoding
- Fixed indentation so there is another indent for each level
- Kept table structure in html page, moving data and function in js page
- Defined a function for the accounts data so it can be reused with other data
- Moved 'strong' styling on 'Total' row to an external css file
- Added JQuery and Bootstrap (additional CSS styling in table-builder.css file)
==Django==
- Moved HTML and Javascript files into the templates and static directories of
  a Django Project
- Moved data into db.sqlite database, with db_seed.py file to seed database with
  original data
- Added Django Rest Framework API for accessing data, with AJAX get request for
  all account data upon load of table-builder.html page
