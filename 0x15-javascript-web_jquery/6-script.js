#!/usr/bin/node
// Updates the text of the tag HEADER to NEW HEADER!!! when the user clicks

$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
});
