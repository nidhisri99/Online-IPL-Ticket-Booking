function shiftFocus(x, y) {
    if (y.length == x.maxLength) { 
        document.getElementById("myForm").elements[8].focus();   
    }
}


setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);




// $(document).on('scroll', function()
// 	{
// 		setHeader();
// 	});

// 	function setHeader()
// 	{
// 		if($(window).scrollTop() > 127)
// 		{
// 			header.addClass('scrolled');
// 			headerSocial.addClass('scrolled');
// 		}
// 		else
// 		{
// 			header.removeClass('scrolled');
// 			headerSocial.removeClass('scrolled');
// 		}
// 	}

/*const bellBtn = document.querySelector('#bellBtn');
    const modal = document.querySelector('#notification-modal');
    const content = document.querySelector('.cModal-content');
    
    bellBtn.addEventListener('click', openModal);
    window.addEventListener('click', outsideClick);
    function openModal() {
        modal.style.display = 'block';
    }
    
    function outsideClick(e) {
        if (e.target == modal) {
            modal.style.display = 'none';
        }
    }

    $("#bellBtn").click(function (e){
      $("#content-modal").css({
        'margin-top': $(this).offset().top + $(this).height()+25
      })
      if($(window).width()>=768){
        $("#content-modal").width("30%");
      }
    });
*/

$(document).ready(function(){
  //console.log("Index page");
  $(".matchNameClass").on("click", function(){
    var dataId = $(this).children(".matchName").attr("data-id");
    var matchDate = $(this).children(".matchDate").text();
    var matchFullName = $(this).children(".matchFullName").text();
    var matchLocation = $(this).children(".matchLocation").text();
    var matchNumber = $(this).children(".matchNumber").text();
    var matchImage = $(this).children(".matchImage").attr("src");
    localStorage.setItem("MatchImage",matchImage);
    localStorage.setItem("MatchLocation",matchLocation);
    localStorage.setItem("MatchNumber",matchNumber);
    localStorage.setItem("MatchFullName",matchFullName);
    localStorage.setItem("MatchName",dataId);
    localStorage.setItem("matchDate",matchDate);

    //console.log(dataId);
});
  
});
$(document).ready(function(){

  


  var dataId =localStorage.getItem("MatchName");
  var matchDate = localStorage.getItem("matchDate");
  var d = new Date(matchDate);
  var matchDateInFormate = d.toLocaleDateString();
  console.log(d.toLocaleDateString());
  console.log(matchDateInFormate.split("/").reverse().join("-"));
  var yourdate = matchDateInFormate.split("/").reverse();
var tmp = yourdate[2];
yourdate[2] = yourdate[1];
yourdate[1] = tmp;
yourdate = yourdate.join("-");
  $("#bookingDate").val(yourdate);
  $("#matchName").val(dataId);
  

  $("#selectSeat").on("click", function(){
    $(".ticketPrice").on("click", function(){
      var arr = ["five","nine","seven"];
      $(this).addClass("btn btn-success");
      var reqid =  $(this).attr("id");
      arr.forEach(function(id){
        if(reqid != id)
        $("#"+id).removeClass("btn btn-success");
      });
      var ticketPrice = $(this).attr("data-id");
      localStorage.setItem("ticketPrice",ticketPrice);
  });
  });
 
 

});
$("#saveTicket").on("click", function(){
  var total = localStorage.getItem("ticketPrice");
    //console.log("returned ticket price"+total);
    $("#totalTicketPrice").val(total);
    getNoOfTickets();
});


function getNoOfTickets(){

  var noOfTickets =  $("#noOfTickets").val();
  var seatPrice = localStorage.getItem("ticketPrice");
  printTotalAmtForTickets(noOfTickets,seatPrice);
}
 function printTotalAmtForTickets(noOfTickets,seatPrice){
  var total = noOfTickets*seatPrice;
  localStorage.setItem("total",total);
  $("#totalTicketPrice").val(total);
 }

 function getTheSeats(){
  var seatHtml = '';
  for(var i=1; i<31; i++){
   seatHtml = seatHtml + '<label class="container-model">'+
  '<input class="single-checkbox" type="checkbox" id="a'+i+'">'+
 '<span class="checkmark">A'+i+'</span></label>';
}

var limit = 3;

  $("#seatBooking").html(seatHtml);
  $('.single-checkbox').on('change', function (e) {
    if ($('input[type=checkbox]:checked').length > 7) {
        $(this).prop('checked', false);
        alert("allowed only 5");
    }
  });
  $("#a5").attr("checked",true);
  $("#a6").attr("checked",true);

  $('#saveSeats').click(function() {
    var idSelector = function() { return this.id; };
    var selectedSeat = $(":checkbox:checked").map(idSelector).get();
    console.log(selectedSeat);
    localStorage.setItem("selectedSeat",selectedSeat);
  });
  
 }
 