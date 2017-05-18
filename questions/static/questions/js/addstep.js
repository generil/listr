i = 0;
$(document).ready(function() {
  $(".add-step").click(function(){
    // add step
    $(".step-list").append('<li><textarea class="form-control" name = "' + i + '" rows="5" placeholder="Add Step" style="margin-top:10px;" required></textarea></li>');
    var x = $(".step-list li").length + " STEPS";
    document.getElementById('step-indicator').innerText=x;
  });
});
