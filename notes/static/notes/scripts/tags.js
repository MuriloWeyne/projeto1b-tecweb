function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }
  
  document.addEventListener("DOMContentLoaded", function () {
    // Faz textarea aumentar a altura automaticamente
    // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.  
    // Sorteia classes de cores aleatoriamente para os cards
    let tags = document.getElementsByClassName("tag");
    for (let i = 0; i < tags.length; i++) {
      let tag = tags[i];
      tag.className += ` tag-color-${getRandomInt(
        1,
        5
      )} tag-rotation-${getRandomInt(1, 11)}`;
    }
  });