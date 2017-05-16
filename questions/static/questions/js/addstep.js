var i = 0;
$(document).ready(function() {
  $(".add-step").click(function(){
    // add step
    // alert($(this).text()); // gets text contents of clicked li
    // console.log(i);
		i++;
    $(".step-list").append('<li><textarea class="form-control" name = "' + i + '" rows="1" style="margin-top:10px;"></textarea></li>');
    var x = $(".step-list li").length + " STEPS";
    document.getElementById('step-indicator').innerText=x;
  });
});
