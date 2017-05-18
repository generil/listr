$(document).ready(function() {
  $(".add-step").click(function(){
    // add step
    $(".step-list").append('<li><textarea class="form-control" name="0" rows="5" id="textarea" placeholder="Step or Item" style="margin-top:10px;" required></textarea></li>');
    var x = $(".step-list li").length + " STEPS";
    document.getElementById('step-indicator').innerText=x;
  });
});
