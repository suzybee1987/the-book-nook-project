$(document).ready(function () {
    $('.sidenav').sidenav({edge: "right"}, {draggable: true});
    $('.collapsible').collapsible();
    $('select').formSelect();
    // code for datetime from code institute mini project Thorin&Co 
    $("#copyright").text(new Date().getFullYear());
});

