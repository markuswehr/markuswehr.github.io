$(document).ready(function(){
    $('.header').height($(window).height());
})

//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollBottom > 20 || document.documentElement.scrollBottom > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollBottom = 0; // For Safari
  document.documentElement.scrollBottom = 0; // For Chrome, Firefox, IE and Opera
}