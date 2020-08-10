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

let deletePostButton = document.getElementById("deletePostButton");
let modalCloseButton = document.getElementById("modalCloseButton");
let modal = document.getElementById("modal");

deletePostButton.addEventListener("click", () =>{
    modal.style.visibility = "visible";
    modal.style.opacity = "1";
});

modalCloseButton.addEventListener("click", () => {
    modal.style.visibility = "hidden";
    modal.style.opacity = "0";
});