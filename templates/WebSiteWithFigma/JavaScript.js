
(function(){
const menu = document.querySelector('.header__nav');
const BurgerItem = document.querySelector('.header__burger');
BurgerItem.addEventListener('click', () => {
   menu.classList.add('header_nav_active');
});

const closure = document.querySelector('.header_nav_close')

closure.addEventListener('click',() => {
    menu.classList.remove('header_nav_active');
})
}());