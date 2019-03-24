function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e, tag) {
            $(tag).attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#content-img").change(function(){
    readURL(this, "#content-img-tag");
});