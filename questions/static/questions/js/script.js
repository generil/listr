var i = 0;
$(document).ready(function() {
  $(".add-step").click(function() {
    i++;
    $(".step-list").append('<li><textarea class="form-control" name = "' + i + '" rows="1" style="margin-top:10px;"></textarea></li>');
    var x = $(".step-list li").length + " STEPS";
    document.getElementById('step-indicator').innerText = x;
  });
});

$(document).on('change', ':file', function() {
  var input = $(this),
    numFiles = input.get(0).files ? input.get(0).files.length : 1,
    label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);

  document.getElementById('add-t-image').innerText = 'Change avatar';
  var img = document.getElementsByClassName('imagepreview');
  img[0].style.display = 'block';
});

$(document).ready(function() {
  $(':file').on('fileselect', function(event, numFiles, label) {
    var input = $(this).parents('.input-group').find(':text'),
      log = numFiles > 1 ? numFiles + ' files selected' : label;
    if (input.length) {
      input.val(log);
    } else {
      if (log) alert(log);
    }
  });
});

function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function(e) {
      $('#preview').attr('src', e.target.result);
    }
    reader.readAsDataURL(input.files[0]);
  }
}

$('input[type="file"]').change(function() {
  readURL(this);
});
