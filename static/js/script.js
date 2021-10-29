$(document).ready(function () {
    $('.sidenav').sidenav({
        edge: "right"
    }, {
        draggable: true
    });
    $('.collapsible').collapsible();
    $('select').formSelect();
    // code for datetime from code institute mini project Thorin&Co 
    $("#copyright").text(new Date().getFullYear());
    $('.carousel.carousel-slider').carousel({
        numVisible: 1
    }, {
        duration: 100
    }, {
        fullWidth: true
    });
    $('.tooltipped').tooltip();
    $('.materialboxed').materialbox();
    $('.modal').modal();
});

// I edited this function from stack overflow which plays the carousel automatically
// but when carousel is hovered over it stops to allow user to read the quote
// https://stackoverflow.com/questions/36581504/materialize-carousel-slider-autoplay
let autoplay = true;

setInterval(function () {
    if (autoplay) $('.carousel.carousel-slider').carousel('next');
}, 4500);

$('.quotes-panel').hover(function () {
    autoplay = false;
}, function () {
    autoplay = true;
});

// code from CI lesson to validate the genre dropdown in form 

validateMaterializeSelect();

function validateMaterializeSelect() {
    let classValid = {
        "border-bottom": "1px solid #4caf50",
        "box-shadow": "0 1px 0 0 #4caf50"
    };
    let classInvalid = {
        "border-bottom": "1px solid #f44336",
        "box-shadow": "0 1px 0 0 #f44336"
    };
    if ($("select.validate").prop("required")) {
        $("select.validate").css({
            "display": "block",
            "height": "0",
            "padding": "0",
            "width": "0",
            "position": "absolute"
        });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
        $(this).parent(".select-wrapper").on("change", function () {
            if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                $(this).children("input").css(classValid);
            }
        });
    }).on("click", function () {
        if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
            $(this).parent(".select-wrapper").children("input").css(classValid);
        } else {
            $(".select-wrapper input.select-dropdown").on("focusout", function () {
                if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                    if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                        $(this).parent(".select-wrapper").children("input").css(classInvalid);
                    }
                }
            });
        }
    });
}

