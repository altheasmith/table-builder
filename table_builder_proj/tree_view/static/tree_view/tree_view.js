$(document).ready( function() {
  // Changed 'label' to 'text' and 'items' to 'nodes' for bootstrap-treeview
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

  // Adding data with static data above
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

  // Helper Function for AJAX call
  function findChildNodes(data, node) {
    for (i in data) {
      if (data[i].parentNode == node.id) {
        node['node_ids'].push(data[i].id);
      };
    };
    return node;
  };

  // Recursive function for finding parent nodes
  function findParent(tree_data, node) {
    for (i in tree_data) {
      if ($.inArray(node.id, tree_data[i].node_ids) != -1) {
        tree_data[i].nodes.push(node);
        nodes_added.push(node);
        console.log(node.parentNode, 'added to', tree_data[i]);
        console.log('nodes added', nodes_added);
        if (tree_data[i].node_ids.length == tree_data[i].nodes.length) {
          delete tree_data[i].node_ids;
        }
      } else if (tree_data[i].nodes.length > 0) {
        findParent(tree_data[i].nodes, node);
      }
    }
    return nodes_added
  }

  //AJAX call to database to return data
  $.get('/api/v1/TreeNode', function(data) {
    var tree_data = [];
    var nodes_searched = [];
    nodes_added = []

    for (i in data) {
      data[i]['nodes'] = []
      data[i]['node_ids'] = []
      nodes_searched.push(findChildNodes(data, data[i]));
      count = nodes_searched.length;
    }

    for (i in data) {
      if (data[i].parentNode == null) {
        tree_data.push(data[i]);
        console.log(data[i].text, 'added');
        nodes_added.push(data[i]);
      }
      else {
        nodes_added = findParent(tree_data, data[i]);
      }
    }
    console.log(tree_data)
    $('#tree').treeview({data: getTree(tree_data)});
  });

  // Function to build tree without AJAX/API
  // $('#tree').treeview({data: getTree(items)});

});
