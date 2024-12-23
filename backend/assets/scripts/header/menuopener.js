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