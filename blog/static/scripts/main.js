let navMenuButton = document.getElementById("navMenuButton");
let navCloseButton = document.getElementById("navCloseButton");
let navContainer = document.getElementById("navContainer");

navMenuButton.addEventListener("click", () =>{
    navContainer.style.width = "50%";
    navContainer.style.opacity = "1";
});

navCloseButton.addEventListener("click", () =>{
    navContainer.style.width = "0";
    navContainer.style.opacity = "0"
});