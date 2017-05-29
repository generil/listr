i = 0;
console.log(i);
$(document).ready(function() {
  $(".add-step").click(function(){
  	console.log(i);
    // add step
    $(".step-list").append('<li><textarea class="form-control" name = "' + i + '" rows="5" placeholder="Step or Item" style="margin-top:10px;"></textarea></li><div class="form-group"><div class="input-group"><label class="input-group-btn"><span class="btn btn-default btn-block" style="border-radius: 4px;"><span id="add-t-image">Add image</span>&hellip;<input type="file" name="instruction_file_"' + i + '" style="display: none;"></span></label></div></div>');
    var x = $(".step-list li").length + " STEPS";
    document.getElementById('step-indicator').innerText=x;
  });
});
