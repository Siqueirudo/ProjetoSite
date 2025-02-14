document.addEventListener("DOMContentLoaded", function () {
    // Criar o overlay e a imagem ampliada dinamicamente
    const lightbox = document.createElement("div");
    lightbox.id = "lightbox";
    lightbox.innerHTML = '<img id="lightbox-img">';
    document.body.appendChild(lightbox);

    // Selecionar todas as imagens e adicionar o evento de clique
    document.querySelectorAll(".grid-item img").forEach(img => {
        img.addEventListener("click", function () {
            document.getElementById("lightbox-img").src = this.src;
            lightbox.style.display = "flex";
        });
    });

    // Fechar o lightbox ao clicar fora da imagem
    lightbox.addEventListener("click", function (e) {
        if (e.target !== document.getElementById("lightbox-img")) {
            lightbox.style.display = "none";
        }
    });
});
