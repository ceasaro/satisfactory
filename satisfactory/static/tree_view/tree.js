let caret_toggler = document.getElementsByClassName("caret");
let i;

for (i = 0; i < caret_toggler.length; i++) {
  caret_toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}