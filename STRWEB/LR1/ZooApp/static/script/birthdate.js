document.getElementById('check-age').addEventListener('click', function() {
    const birthdateInput = document.getElementById('birthdate').value;

    if (!birthdateInput) {
        alert("Пожалуйста, введите дату рождения.");
        return;
    }

    const birthdate = new Date(birthdateInput);
    const today = new Date();
    let age = today.getFullYear() - birthdate.getFullYear();
    const monthDiff = today.getMonth() - birthdate.getMonth();

    if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthdate.getDate())) {
        age--;
    }

    const dayOfWeek = birthdate.toLocaleString('ru-RU', { weekday: 'long' });

    if (age < 18) {
        alert("Вы несовершеннолетний. Необходимо разрешение родителей на использование сайта.");
    } else {
        alert(`Вам ${age} лет. Вы родились в ${dayOfWeek}.`);
    }
});