#!/usr/bin/node
// Update the text color of the tag HEADER to red when the user clicks on it

$('#red_header').click(function () {
  $('header').css('color', '#FF0000');
});
