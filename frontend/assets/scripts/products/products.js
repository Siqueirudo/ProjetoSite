const priceRange = document.getElementById('priceRange');
    const currentValue = document.getElementById('current-value');

    priceRange.addEventListener('input', () => {
        currentValue.textContent = `R$ ${priceRange.value}`;
        const percent = (priceRange.value - priceRange.min) / (priceRange.max - priceRange.min) * 100;
        currentValue.style.left = `calc(${percent}% - 10px)`;
    });