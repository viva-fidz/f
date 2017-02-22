$(document).ready(function() {

    $( "#nav li a" ).click(function(){
        var toLoad = $(this).'#content';
           $('#content').load(toLoad);
        //alert('continue?');
        alert($(this).attr('href').length-5);
        window.location.hash = $(this).attr('href').substr(0,$(this).attr('href').length-5);
        return false; // чтобы не переходить на новую страницу
    });
});
