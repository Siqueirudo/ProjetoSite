document.addEventListener('DOMContentLoaded', () => {
    const thumbnails = document.querySelectorAll('.thumbnail');
    const currentImage = document.getElementById('current-image');
    const sizes = document.querySelectorAll('.size');

    // Função para trocar a imagem principal
    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', () => {
            // Atualiza a imagem principal
            currentImage.src = thumbnail.src;

            // Remove a classe selecionada de outras miniaturas
            thumbnails.forEach(img => img.classList.remove('selected'));
            thumbnail.classList.add('selected');
        });
    });

    // Função para selecionar tamanho
    sizes.forEach(size => {
        size.addEventListener('click', () => {
            // Remove a classe selecionada de outros tamanhos
            sizes.forEach(s => s.classList.remove('selected'));
            size.classList.add('selected');
        });
    });
});