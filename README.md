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
- Added footer for link to JavaScript files for faster loading
- Added !DOCTYPE
- Added character encoding
- Fixed indentation so there is another indent for each level
- Kept table header structure in html page, moved data and function to js page
- Defined functions for the accounts data so they can be reused with other data
- Moved 'strong' styling on 'Total' row to an external css file
- Added JQuery and Bootstrap (additional CSS styling in table-builder.css file)
==Django==
- Moved HTML and Javascript files into the templates and static directories of
  a Django Project
- Moved data into db.sqlite database, with db_seed.py file to seed database with
  original data
- Added Django Rest Framework API for accessing data, with AJAX get request for
  all account data upon load of table-builder.html page
- Wrote a suite of five tests in three files in the tests/ directory in the
  table_builder module to ensure database, webpage, and API functionality,
  and most importantly to test the output of the new page against the output of
  the old page, to ensure no functionality is lost with the refactoring
