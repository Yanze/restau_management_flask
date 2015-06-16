$(function() {
  dialog_new_table = $( "#dialog-form-start-table" ).dialog({
    autoOpen: false,
    height: 150,
    width: 300,
    modal: true
  });

   dialog_release_table = $( "#dialog-form-release-table" ).dialog({
    autoOpen: false,
    height: 150,
    width: 300,
    modal: true
  });

  $( "#start-table" ).button().on( "click", function() {
    dialog_new_table.dialog( "open" );
  });

  $( "#release-table" ).button().on( "click", function() {
    dialog_release_table.dialog( "open" );
  });

});
