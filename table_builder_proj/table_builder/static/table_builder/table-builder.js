$(document).ready( function() {
  // AJAX get request to API for account information
  $.get('api/v1/Account', function(data) {
    var headers = []
    var total = 0
    $.each(data[0], function(k, v) {
      headers.push(k)
    });
    $.each(data, function() {
      $.each(this, function(k, v) {
        if (k == 'amount') {
          total += v;
        }
      });
    });
    console.log(headers, total, data)
    var table = '<tr>';
    for (i in headers) {
      table += '<td>' + headers[i] + '</td>'
    }
    table += '</tr>'
    for (account in data) {

    }
    console.log(table)
    $('#accounts_table').innerHTML = table;
  });
});
