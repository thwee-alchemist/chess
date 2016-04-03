/*
  Joshua Marshall Moore
  joshua_marshall_moore

  108 Texas Ave
  Alamogordo, NM 88310
  United States

  April 1st, 2016
*/

$(function(){
  $('.piece').draggable();
  $('.field').droppable({
    tolerance: 'intersect',
    drop: function(event, ui) {
      var drop_p = $(this).offset();
      var drag_p = ui.draggable.offset();
      var left_end = drop_p.left - drag_p.left + 1;
      var top_end = drop_p.top - drag_p.top + 1;
      ui.draggable.animate({
          top: '+=' + top_end,
          left: '+=' + left_end
      });

      var piece = ui.draggable.attr('id');
      var field = $(this).attr('id');

      console.log(piece, field);
    }
  });

  // drag piece programmatically
  var which_to = function(which, to){
    var which = $(which);
    var to = $(to);
    
    var droppableOffset = to.offset(); 
    var draggableOffset = which.offset();
    var dx = droppableOffset.left - draggableOffset.left;
    var dy = droppableOffset.top - draggableOffset.top;

    which.simulate('drag', {
      dx: dx, 
      dy: dy
    });
  };


});

var setup_black = function(){
  var fields = $('tbody').children().not('.pieces').get();
  fields = fields.reverse();
  $('tbody').append(fields);

  pieces = $('#pieces').get();
  $('#pieces').remove();
  $('tr').first().append(pieces)
};

var setup = function(){
  var odd_fields_selector = 'tr:nth-child(odd)>td:nth-child(odd):not(.pieces)';
  var even_fields_selector = 'tr:nth-child(odd)>td:nth-child(even):not(.pieces)';
  
};



var setup_white = function(){
  // leave the board as it is, sit back and listen  
};


var odd_fields_selector = 'tr:nth-child(odd)>td:nth-child(odd):not(.pieces)';
var even_fields_selector = 'tr:nth-child(odd)>td:nth-child(even):not(.pieces)';