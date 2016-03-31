$(function() {
  dialog_new_table = $( "#dialog-form-start-table" ).dialog({
    autoOpen: false,
    height: 150,
    width: 300,
    modal: true
  });

  dialog_release_table = $( ".releaseTable" ).dialog({
    autoOpen: false,
    height: 150,
    width: 300,
    modal: true,
    buttons:{
      "yes": function(){
        $(this).dialog("close");
        callback();
      },
      "no": function(){
        $(this).dialog("close");
      }
    }
  });

  dialog_order_dishes = $("#dialog-form-order-dishes").dialog({
    autoOpen: false,
    height: 220,
    width: 300,
    modal: true,
  });

  $( "#start-table" ).button().on( "click", function() {
    dialog_new_table.dialog( "open" );
  });


  var groupID;
  $(".confirmation").click(function(){
    groupID = $(this).data("groupid");
    dialog_release_table.dialog("open");
  });

  function callback(){
    window.location.href = "/release-table-v2/" + groupID;
  }

  $("#order-dishes").click(function(){
    dialog_order_dishes.dialog("open");
  });

});


