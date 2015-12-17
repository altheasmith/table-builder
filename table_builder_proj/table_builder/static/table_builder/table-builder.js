$(document).ready( function() {

  // Function to sum account amounts
  function total(data) {
    var total = 0;

    $.each(data, function() {
      $.each(this, function(k, v) {
        if (k == 'amount') {
          total += v;
        };
      });
    });
    return total;
  };

  // Function to get html for the Total row in the table
  function total_html(total) {
    var total_html = '<tr class="total">\
                        <td>Total</td>\
                        <td>' + total + '</td>\
                        <td></td>\
                      </tr>';
    return total_html;
  };

  // Function to get html for table rows with account data
  function account_html(data) {
    var account_html = '';

    for (i in data) {
      account_html += '<tr>\
                        <td>' + data[i].name + '</td>\
                        <td>' + data[i].amount + '</td>\
                        <td>' + data[i].status + '</td>\
                      </tr>';
    }
    return account_html;
  };

  // AJAX get request to API for account information
  $.get('/api/v1/Account', function(data) {

    // Running functions
    total = total(data)
    total_html = total_html(total)
    account_html = account_html(data)

    // Consolidating output
    var table = account_html + total_html;

    // Appending table rows
    $('#accounts_table').append(table);

    // TESTS:
    var $table_data = $('#accounts_table').html()
    console.log($table_data)

  });

});
