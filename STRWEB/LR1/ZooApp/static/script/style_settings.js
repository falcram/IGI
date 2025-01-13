// script.js
document.getElementById('toggle-settings').addEventListener('change', function() {
    const settings = document.getElementById('settings');
    settings.style.display = this.checked ? 'block' : 'none';
});

// Изменение размера шрифта
document.getElementById('font-size').addEventListener('change', function() {
    document.body.style.fontSize = this.value;
});

// Изменение цвета текста
document.getElementById('text-color').addEventListener('input', function() {
    document.body.style.color = this.value;
});

// Изменение цвета фона
document.getElementById('bg-color').addEventListener('input', function() {
    document.body.style.backgroundColor = this.value;
});