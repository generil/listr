$(document).ready(function() {
  $(".add-step").click(function(){
    $(".step-list").append('<li><textarea class="form-control" rows="1" style="margin-top:10px;"></textarea></li>');
    x = $(".step-list li").length + " STEPS";
    document.getElementById('step-indicator').innerText=x;
  });
});
