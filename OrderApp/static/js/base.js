$(document).ready(function () {
    $('.header__burger').click(function (event) {
        $('.header__burger, .header__menu').toggleClass('active');
        $('body').toggleClass('lock');
    });
    $('.profile').click(function (event) {
        $('.inside__links').slideToggle()
    })
});