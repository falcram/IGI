// Устанавливаем длительность обратного отсчета в миллисекундах (1 час)
const countdownDuration = 60 * 60 * 1000; // 1 час в миллисекундах

// Получаем текущее время
const now = new Date().getTime();

// Проверяем, есть ли сохраненное время в localStorage
let endTime = localStorage.getItem('countdownEndTime');

if (!endTime) {
    // Если нет, устанавливаем новое время окончания
    endTime = now + countdownDuration;
    localStorage.setItem('countdownEndTime', endTime);
} else {
    // Если есть, обновляем его в числовом формате
    endTime = parseInt(endTime, 10);
}

// Функция для обновления обратного отсчета
function updateCountdown() {
    const now = new Date().getTime();
    const timeLeft = endTime - now;

    if (timeLeft < 0) {
        // Если время закончилось, очищаем localStorage и отображаем сообщение
        clearInterval(countdownInterval);
        localStorage.removeItem('countdownEndTime');
        document.getElementById('countdown').innerHTML = "Время вышло!";
        return;
    }

    // Вычисляем часы, минуты и секунды
    const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    // Обновляем текст на странице
    document.getElementById('countdown').innerHTML = `${hours}ч ${minutes}м ${seconds}с`;
}

// Обновляем обратный отсчет каждую секунду
const countdownInterval = setInterval(updateCountdown, 1000);

// Первоначальный вызов функции для отображения времени сразу при загрузке
updateCountdown();