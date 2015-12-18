$(document).ready( function() {
  // Changed 'label' to 'text' and 'items' to 'nodes'
  var items = {
      text: 'Node Label',
      nodes: [
          {
              text: 'Child Node Label',
              nodes: [
                  {
                      text: 'Child Node Label',
                      nodes: [
                          {
                              text: 'Child Node Label',
                              nodes: [

                              ]
                          },
                          {
                              text: 'Child Node Label',
                          },
                          {
                              text: 'Leaf Node Label'
                          }
                      ]
                  }
              ]
          },
          {
              text: 'Leaf Node Label'
          }
      ]
  };

  // Function to adjust keys
  // var items = {
  //     label: 'Node Label',
  //     items: = []
  //   }
  //
  // function changeKeys(items) {
  //   for (key, val) in items {
  //     if key == 'label':
  //   }
  // }



  function getTree(items) {
    // treeview takes dictionary for arguments which requires elements to be in
    // an array of dictionaries
    if (items instanceof Array) {
      return items;
    }
    else {
      return [items];
    }
  };

  // Function to build tree
  $('#tree').treeview({data: getTree(items)});
  $('#tree2').treeview({data: getTree(tree)});

});
