$(document).ready(function(){

    $('input').mouseenter(function(){
        $('.formula').children('form').children('ul').fadeIn(700);
    });

    $('.img').mouseenter(function(){
        $(this).children('.description').children('img').css('opacity:', '40%');
        $(this).children('.description').fadeIn(700);
    });

    $('.img').mouseleave(function(){
        $(this).children('.description').children('img').css('opacity:', '100%')
        $(this).children('.description').fadeOut(700);
    })
});
