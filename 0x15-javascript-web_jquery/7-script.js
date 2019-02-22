#!/usr/bin/node
// Fetches and replaces the name of the given url

$.getJSON(function (data, textStatus) {
  $('character').text(data.name);
});
