let lastSortedColumn = -1;
let sortOrder = true; // true для возрастания, false для убывания

function search() {
    const query = document.getElementById('search').value;
    window.location.href = `?search=${query}`;
}

function showDetails(name, description, phone, email) {
    const detailsDiv = document.getElementById('details');
    detailsDiv.innerHTML = `
        <h3>Детали сотрудника</h3>
        <p><strong>ФИО:</strong> ${name}</p>
        <p><strong>Описание:</strong> ${description}</p>
        <p><strong>Телефон:</strong> ${phone}</p>
        <p><strong>Почта:</strong> ${email}</p>
    `;
}

function showAddForm() {
    const form = document.getElementById('addForm');
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
}


function validateUrl(url) {
    const regex = /^(http:\/\/|https:\/\/).+\.(php|html)$/;
    return regex.test(url);
}

function validatePhone(phone) {
    const regex = /^8(\(0?29\)|029)?\d{7}$|^\+375(\(29\)|29)?\d{7}$/;
    return regex.test(phone);
}

function addEmployee(event) {
    event.preventDefault(); // Предотвращаем стандартное поведение формы

    // Получаем значения из формы
    const fullName = document.getElementById('fullName').value;
    const photoInput = document.getElementById('photo');
    const description = document.getElementById('description').value;
    const phone = document.getElementById('phone').value;
    const email = document.getElementById('email').value;

    // Получаем файл изображения
    const file = photoInput.files[0];

    // Проверяем, выбрано ли изображение
    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            // Создаем объект работника
            const newEmployee = {
                fullName: fullName,
                photo: e.target.result, // Сохраняем данные изображения
                description: description,
                phone: phone,
                email: email
            };

            // Вставьте здесь логику для добавления работника в ваш список
            console.log('Новый работник добавлен:', newEmployee);

            // Отображаем сообщение
            document.getElementById('message').innerText = 'Работник успешно добавлен!';

            // Очистка формы
            document.getElementById('employeeForm').reset();
        };

        // Читаем файл как Data URL
        reader.readAsDataURL(file);
    } else {
        alert('Пожалуйста, загрузите изображение.');
    }
}

// Привязываем функцию к событию отправки формы
document.getElementById('employeeForm').addEventListener('submit', addEmployee);

// Функция для получения токена CSRF
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function sortTable(columnIndex) {
    const table = document.getElementById("employeeTable");
    const tbody = table.tBodies[0];
    const rows = Array.from(tbody.rows);
    
    // Определение направления сортировки
    if (lastSortedColumn === columnIndex) {
        sortOrder = !sortOrder; // Меняем направление при повторном клике
    } else {
        sortOrder = true; // Сортировка по возрастанию для нового столбца
    }
    
    // Сортировка
    rows.sort((a, b) => {
        const aText = a.cells[columnIndex].innerText;
        const bText = b.cells[columnIndex].innerText;

        return (sortOrder ? aText.localeCompare(bText) : bText.localeCompare(aText));
    });

    // Очистка тела таблицы и добавление отсортированных строк
    tbody.innerHTML = "";
    rows.forEach(row => tbody.appendChild(row));

    // Обновление направления сортировки в заголовках
    Array.from(table.querySelectorAll("th")).forEach((th, index) => {
        th.classList.remove("sort-asc", "sort-desc");
        if (index === columnIndex) {
            th.classList.add(sortOrder ? "sort-asc" : "sort-desc");
        }
    });

    // Обновление текста направления сортировки
    document.getElementById("sortDirection").innerText = sortOrder ? "Sorted in ascending order" : "Sorted in descending order";
    
    // Сохранение последнего отсортированного столбца
    lastSortedColumn = columnIndex;
}