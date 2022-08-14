window.addEventListener('scroll', function() {
    let header = document.querySelector('.nav');
    let windowPosition = window.pageYOffset > 600 ;
    header.classList.toggle('scrolling-active', windowPosition);            
})

let mainListDiv = document.getElementById("mainListDiv"),
mediaButton = document.getElementById("mediaButton"),
navbar = document.querySelector('.nav');

mediaButton.onclick = function () {
 
    mainListDiv.style.transition = "all 0.8s ease-in-out";
    mainListDiv.classList.toggle("show_list");
    mediaButton.classList.toggle("active");
};


let icon = document.querySelector(".search");
let input = document.querySelector(" .inputsearch");

icon.addEventListener("click", (e) => {
  e.preventDefault();
   if (input.style.display === "none") {
    input.style.display = "block";
  } else {
    input.style.display = "none";
  }


});



