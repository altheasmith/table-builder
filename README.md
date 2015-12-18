TreeView Coding Challenge (Tree_View app in Table-Builder Project)
=========
Represent the following data structure as an expandable TreeView.


The TreeView should have the following features:

1. It should be able to read a hierarchical data-structure like the one shown above.
2. It should provide expand/collapse behavior at the node level
3. By default the TreeView should expand all levels
4. Define an API that makes it easier to use

Notes
======
- You are free to use any helper libraries
- Use best practices to write clean, well-refactored code
- Bonus points for styling the TreeView
- Bonus for writing Unit Tests
- You have 24 hours to complete the exercise


My Code
=======
- A Django model with a self-referential foreign key to represent the Tree View data
- The database is seeded through a recursive function in Python with the original JavaScript treeview object of labels/items, with their titles changed to text/nodes so they can be used with bootstrap-treeview, and the keys changed to strings so they can be processed with Python
- An AJAX request pulls the data from the database through an API, and builds the TreeView datastructure using the Foreign Key (parent node) relationships before passing it to the Bootstrap-Treeview function to be displayed on the page

Static display is [here](https://altheasmith.github.io), and the app is hosted [here](https://tablebuilder-studymed.rhcloud.com/)
