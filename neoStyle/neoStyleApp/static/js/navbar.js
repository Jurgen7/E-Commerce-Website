const shopLink = document.querySelector("#navbar > li:nth-child(2)");
const dropdownMenu = document.getElementById("dropdown-menu");
const content = document.querySelector(".content");
let navBar = document.getElementById('navbar');
let isNavBarOpen = false;

// Add "blur" class to content element when Shop link is hovered
function addBlur() {
  if (!isNavBarOpen) {
    content.classList.add("blur");
  }
}

shopLink.addEventListener("mouseenter", addBlur);
dropdownMenu.addEventListener("mouseenter", addBlur);

// Remove "blur" class from content element when mouse leaves Shop link or dropdown menu
function removeBlur() {
  if (!isNavBarOpen) {
    content.classList.remove("blur");
  }
}

shopLink.addEventListener("mouseleave", removeBlur);
dropdownMenu.addEventListener("mouseleave", removeBlur);

// Toggle navbar and blur effect on small screens
let bar = document.getElementById('bar');
let close = document.getElementById('close');

bar.addEventListener("click", () => {
  navBar.classList.add('active');
  content.classList.add("blur");
  isNavBarOpen = true;
});

close.addEventListener("click", () => {
  navBar.classList.remove('active');
  content.classList.remove("blur");
  isNavBarOpen = false;
});

