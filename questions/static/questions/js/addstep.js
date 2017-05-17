$(document).ready(function() {
  $(".add-step").click(function(){
    // add step
    $(".step-list").append('<li><textarea class="form-control" rows="3" style="margin-top:10px;"></textarea></li>');
    var x = $(".step-list li").length + " STEPS";
    document.getElementById('step-indicator').innerText=x;
  });
});
