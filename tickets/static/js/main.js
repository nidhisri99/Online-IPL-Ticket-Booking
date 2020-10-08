function shiftFocus(x, y) {
    if (y.length == x.maxLength) { 
        document.getElementById("myForm").elements[8].focus();   
    }
}

setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);

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
  console.log("Index page");
  $(".matchName").on("click", function(){
    var dataId = $(this).attr("data-id");
    localStorage.setItem("MatchName",dataId);
    console.log(dataId);
});
  
});

$(document).ready(function(){
  $(".fullmatchName").on("click", function(){
    var dataId = $(this).attr("data-id");
    localStorage.setItem("fullMatchName",dataId);
    console.log(dataId);
});
  
});