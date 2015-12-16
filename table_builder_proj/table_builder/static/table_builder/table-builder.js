$(document).ready( function() {
  // AJAX get request to API for account information
  $.get('api/v1/Account', function(data) {

    var total = 0

    $.each(data, function() {
      $.each(this, function(k, v) {
        if (k == 'amount') {
          total += v;
        }
      });
    });

    var accounts_data = ''

    for (i in data) {
      accounts_data += '<tr>\
                        <td>' + data[i].name + '</td>\
                        <td>' + data[i].amount + '</td>\
                        <td>' + data[i].status + '</td>\
                      </tr>';
    }

    var total_data = '<tr class="total">\
                        <td>Total</td>\
                        <td>' + total + '</td>\
                        <td></td>\
                      </tr>'

    var table = accounts_data + total_data

    $('#accounts_table').append(table);

  });

});
