$(document).ready(function(){

    $('input').mouseenter(function(){
        $('.formula').children('form').children('ul').slideDown(700);
    });

    $('.img').mouseenter(function(){
        $(this).children('.post').animate({opacity: '0.2'}, 700);
        $(this).children('.description').fadeIn(700);
    });

    $('.img').mouseleave(function(){
        $(this).children('.post').animate({opacity: '1'}, 700);
        $(this).children('.description').fadeOut(700);

    });

});