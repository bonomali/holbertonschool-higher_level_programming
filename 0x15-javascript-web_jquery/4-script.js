#!/usr/bin/node
// Toggles the class of the tag HEADER to red when the user clicks

$('#red_header').click(function () {
  $('header').toggleClass('red green');
});
