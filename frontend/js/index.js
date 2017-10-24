function getSim(word1, word2) {}
var $TABLE = $('#table');

function swap($tr){
    var $sw1=$tr.find('.swap1').detach();
    var $sw2=$tr.find('.swap2');
    $sw2.after($sw1);
    $sw1.removeClass('swap1').addClass('swap2');
    $sw2.removeClass('swap2').addClass('swap1');
}
$(document).ready(function() {

  $('.table-add#t1').click(function () {
    var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide table-line');
    $TABLE.find('table').append($clone);
  });
  $('.swap').click(function () {
      console.log('clicked !');
      swap($(this).parent().parent());
  });
  $('.table-add#t2').click(function () {
    var $clone = $TABLE.find('tr.hide').clone(true).removeClass('hide table-line');
    $('#ta2').append($clone);
  });

  $('.table-remove').click(function () {
    $(this).parents('tr').detach();
  });

  $('.table-up').click(function () {
    var $row = $(this).parents('tr');
    if ($row.index() === 1) return; // Don't go above the header
    $row.prev().before($row.get(0));
  });

  $('.table-down').click(function () {
    var $row = $(this).parents('tr');
    $row.next().after($row.get(0));
  });
  var col=-1;
  $('#addcol').click(function() {
    $('.insertion1').after(`<th class='col${++col}' contenteditable='true'>Value <button class='rem' style='margin-left:5px'> - </button></th>`);
    $('.insertion2').after(`<td class='col${col}' contenteditable='true'></td>`);
    $('.rem').click(function() {
      var $parent=$(this).parent();
      var delclass=$parent.attr('class');
      $(`.${delclass}`).remove();
    });
  });

  $('#getfd').click(function() {
    var cols = [];
    $('tr > th').each(function() {
      var col = $(this).text();
      var col = col.split(' - ')[0];
      if (col != "")
        cols.push(col);
    });
    console.log(cols);

    for (var i = 0; i<cols.length - 1; i++) {
      for (var j = i+1; j<cols.length; j++) {
          getSim(cols[i],cols[j]);
      }
    }

  });
});