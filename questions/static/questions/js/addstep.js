var i = 0;
$(document).ready(function() {
  $(".add-step").click(function(){
		i++;
    $(".step-list").append('<li><textarea class="form-control" name = "' + i + '" rows="1" style="margin-top:10px;"></textarea></li>');
    var x = $(".step-list li").length + " STEPS";
    document.getElementById('step-indicator').innerText=x;
  });
});
