$(document).ready( function() {
  // Original structure
  var items = {
      label: 'Node Label',
      items: [
          {
              label: 'Child Node Label',
              items: [
                  {
                      label: 'Child Node Label',
                      items: [
                          {
                              label: 'Child Node Label',
                              items: [

                              ]
                          },
                          {
                              label: 'Child Node Label',
                          },
                          {
                              label: 'Leaf Node Label'
                          }
                      ]
                  }
              ]
          },
          {
              label: 'Leaf Node Label'
          }
      ]
  };

  // Condensed to better visualize structure
  var items = {label: 'Node Label',
              items: [{label: 'Child Node Label',
                      items: [{label: 'Child Node Label',
                              items: [{label: 'Child Node Label',
                                      items: []
                                      },
                                      {label: 'Child Node Label',},
                                      {label: 'Leaf Node Label'}
                              ]
                      }
                      ]
              },
              {label: 'Leaf Node Label'}
              ]
  };

  function getTree(items) {
    // treeview function takes data in an array
    var data = []
    data += [items]
    return data;
  };

  // Function to build tree
  $('#tree').treeview({data: getTree()});

});
