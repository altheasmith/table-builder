

function print_accounts(accounts) {
  header_row = "<tr>\
              <th>Name</th>\
              <th>Amount</th>\
              <th>Status</th>\
              </tr>"

    table_rows = ''
    var total = 0;
    for (var i = 0; i < accounts.length; i++) {

        table_rows += '<tr>';

        table_rows += '<td>' + accounts[i].accountName + '</td>';
        table_rows += '<td>' + accounts[i].amount + '</td>';
        table_rows += '<td>' + accounts[i].status + '</td>';

        table_rows += '</tr>';

        total += accounts[i].amount;
    }
    total_row = "<tr class='total'>\
                  <td>Total</td>\
                  <td>" + total + "</td>\
                  <td></td>\
                  </tr>"
    final_table = header_row + table_rows + total_row
    document.getElementById('accounts_table').innerHTML += final_table
}

print_accounts(accounts);
