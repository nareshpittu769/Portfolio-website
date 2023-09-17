let hamburger = document.getElementsByClassName('fa-bars')[0]
console.log(hamburger);
let aside = document.querySelector('.aside.sticky')
let cancel = document.querySelector('.aside.sticky .fa-xmark')
console.log(cancel);

hamburger.addEventListener('click',()=>{
    // console.log(aside);
    aside.classList.add('show')
})

cancel.addEventListener('click',()=>{
    aside.classList.remove('show')
})


window.onscroll = function() {myFunction()};

var navbar = document.getElementsByClassName("navbar")[0];

var sticky = navbar.offsetTop;

function myFunction() {
  if (window.scrollY >= sticky) {
    navbar.classList.add("sticky")
    aside.classList.add('sticky')
    
  } else {
    navbar.classList.remove("sticky");
    aside.classList.remove('sticky')
  }
}