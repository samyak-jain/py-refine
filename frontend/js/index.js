function getSim(word1, word2) {}
var $TABLE = $('#table');

function swap($tr){
    var $sw1=$tr.find('.swap1').detach();
    var $sw2=$tr.find('.swap2');
    $sw2.after($sw1);
    $sw1.removeClass('swap1').addClass('swap2');
    $sw2.removeClass('swap2').addClass('swap1');
}


function getdet() {
  var myRows = [];
  var headersText = [];
  var $headers = $("#ta2 th");

  // Loop through grabbing everything
  var $rows = $("#ta2 tr").each(function(index) {
    // console.log(index);
    $cells = $(this).find("td");
    myRows[index] = {};

    $cells.each(function(cellIndex) {
      // Set the header text
      if(headersText[cellIndex] === undefined) {
        headersText[cellIndex] = $($headers[cellIndex]).text();
      }
      // Update the row object with the header/cell combo
      myRows[index][headersText[cellIndex]] = $(this).text();
    });    
  });

  var colslist = [];
  $('#ta1 th').each(function(index) {
    colslist[index] = $(this).text().split(' -')[0];
  });

  colslist.splice(-2,2);
  myRows.splice(0,1);
  myRows.splice(1,1);

  // Let's put this in the object like you want and convert to JSON (Note: jQuery will also do this for you on the Ajax request)
  var myObj = {
      "myrows": myRows,
      "cols": colslist
  };

  var tosend = JSON.stringify(myObj);
  return tosend;
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
    var $clone = $("#ta2").find('tr.hide2').clone(true).removeClass('hide2 table-line');
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

  $('#norm').click(function() {
    tosend = getdet();
    console.log(tosend);
    resp = "";
    // console.log(tosend);
    $.ajax({
        contentType: 'application/json',
        crossDomain: true,
        type: 'GET',
        url: "http://localhost:8000/norm?data=" + tosend,
        // success: function(text) {
        //   response = text;
        // }
    }).done(function(data, textStatus, jqXHR){
        // console.log(data);
        
        resp = $.parseJSON(jqXHR.responseText);
        // console.log(resp);
        rels = resp['data'];
        // s = "";
        console.log(rels);
        for (var i = 0; i<rels.length; i++) {
          var $outer_temp=$(`<p class="new-tab">R${i}:</p> 
          <table class="table new-tab">
      <tr class="header-table">
            </tr>
    </table>
        `),inner_temp='';
          for (var j = 0; j<rels[i].length; j++) {
            inner_temp+=`
              <th class='fixed-header-table'>${rels[i][j]}</th>
            `;
          }
          console.log('inner - ',inner_temp);
          $outer_temp.find('.header-table').html($(inner_temp));
          $('#output').append($outer_temp);

        }
  });;
     // console.log(resp);
  });

  $('#clear').click(function() {
    $('.new-tab').remove();
  });
});