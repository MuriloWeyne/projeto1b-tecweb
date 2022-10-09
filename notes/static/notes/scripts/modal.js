document.addEventListener("DOMContentLoaded", function () {
  let modal = document.getElementsByClassName("modal");

  // Get the button that opens the modal
  let modalButtons = document.getElementsByClassName("edit-btn");

  // Get the <span> element that closes the modal
  let spans = document.getElementsByClassName("close");

  for (let i = 0; i < modalButtons.length; i++) {
    modalButtons[i].addEventListener("click", function () {
      modal[i].style.display = "block";
    });
  }
  for (let i = 0; i < spans.length; i++) {
    spans[i].addEventListener("click", function () {
      modal[i].style.display = "none";
    });
  }
    window.addEventListener("click", function (event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    });
});
