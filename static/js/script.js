// ================================
// ART GALLERY MAIN JAVASCRIPT
// ================================


// Page Loaded
document.addEventListener("DOMContentLoaded", function () {
    console.log("Art Gallery Website Loaded Successfully 🔥");

    enableTooltips();
    navbarScrollEffect();
    smoothScroll();
    productHoverMessage();
});


// ================================
// TOOLTIP ENABLE
// ================================
function enableTooltips() {
    let tooltipTriggerList = [].slice.call(
        document.querySelectorAll('[data-bs-toggle="tooltip"]')
    );

    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}


// ================================
// NAVBAR SCROLL EFFECT
// ================================
function navbarScrollEffect() {
    window.addEventListener("scroll", function () {

        let navbar = document.querySelector(".navbar");

        if (window.scrollY > 50) {
            navbar.style.background = "#000";
            navbar.style.boxShadow = "0 4px 10px rgba(0,0,0,0.2)";
        } else {
            navbar.style.background = "#111";
            navbar.style.boxShadow = "none";
        }

    });
}


// ================================
// SMOOTH SCROLL
// ================================
function smoothScroll() {

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {

        anchor.addEventListener("click", function (e) {

            e.preventDefault();

            const target = document.querySelector(this.getAttribute("href"));

            if (target) {
                target.scrollIntoView({
                    behavior: "smooth"
                });
            }

        });

    });

}


// ================================
// PRODUCT HOVER MESSAGE
// ================================
function productHoverMessage() {

    let cards = document.querySelectorAll(".product-card");

    cards.forEach(card => {

        card.addEventListener("mouseenter", function () {
            console.log("Viewing artwork ✨");
        });

    });

}


// ================================
// ADD TO CART POPUP
// ================================
function addToCartMessage() {
    alert("Artwork added to cart 🛒");
}


// ================================
// CONFIRM REMOVE ITEM
// ================================
function confirmRemove() {
    return confirm("Remove this item from cart?");
}


// ================================
// NEWSLETTER SUBMIT
// ================================
function subscribeNow() {

    let email = document.getElementById("email");

    if (email.value === "") {
        alert("Enter email first.");
        return false;
    }

    alert("Subscribed Successfully 🎉");
}