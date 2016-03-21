$(function() {
  $("#tires").autocomplete({
    source: "/tires/api/get_tires/",
    minLength: 2,
  });
});
