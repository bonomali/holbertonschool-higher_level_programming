#!/usr/bin/node
// Adds a list element to a list when the user clicks on the add item tag

$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li>Item</li>');
});
