// MENU RETRÁTIL (LADO ESQUERDO)

document.addEventListener("DOMContentLoaded", function () {
    const headerMenu = document.getElementById("header_menu");
    const closeButton = document.getElementById("close_menu");
    const menuOverlay = document.getElementById("menu_overlay");
    const navButton = document.querySelector('.menunav-button');

    // Mostra o menu e a sobreposição
    function openMenu() {
        headerMenu.classList.add("active");
        menuOverlay.style.display = "block"; // Mostra a sobreposição
    }

    // Fecha o menu e a sobreposição
    function closeMenu() {
        headerMenu.classList.remove("active");
        menuOverlay.style.display = "none"; // Esconde a sobreposição
    }

    navButton.addEventListener("click", openMenu);

    // Clique na sobreposição também fecha o menu
    menuOverlay.addEventListener("click", closeMenu);

    // Clique no botão de fechar fecha o menu
    closeButton.addEventListener("click", closeMenu);
});

// CARRINHO RETRÁTIL (LADO DIREITO)

document.addEventListener("DOMContentLoaded", function () {
    const cartMenu = document.getElementById("cart_menu");
    const cartOverlay = document.getElementById("cart_overlay");
    const cartButton = document.querySelector(".menucart-button");
    const closeCartButton = document.getElementById("close_cart");

    // Abrir carrinho
    function openCart() {
        cartMenu.classList.add("active");
        cartOverlay.style.display = "block"; // Mostra a sobreposição
    }

    // Fechar carrinho
    function closeCart() {
        cartMenu.classList.remove("active");
        cartOverlay.style.display = "none"; // Esconde a sobreposição
    }

    // Clique no botão do carrinho
    cartButton.addEventListener("click", openCart);

    // Clique no botão de fechar
    closeCartButton.addEventListener("click", closeCart);

    // Clique na sobreposição fecha o carrinho
    cartOverlay.addEventListener("click", closeCart);
});