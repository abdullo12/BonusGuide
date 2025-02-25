document.getElementById('education_form').addEventListener('change', function() {
    const formValue = this.value;
    const researchSection = document.getElementById('research-section');
    const sportsSection = document.getElementById('sports-section');
    
    // Если выбрана очная форма, показываем секции "Научная деятельность" и "Спортивные достижения"
    if (formValue === 'Очная') {
        researchSection.classList.remove('hidden');
        sportsSection.classList.remove('hidden');
    } else {
        // Если выбрана другая форма, скрываем эти секции
        researchSection.classList.add('hidden');
        sportsSection.classList.add('hidden');
    }
});

// Пример скрытия секции "Социальный статус" в зависимости от выбора
document.getElementById('citizenship').addEventListener('change', function() {
    const citizenshipValue = this.value;
    const socialStatusSection = document.getElementById('social-status-section');
    
    // Если выбран "Нет", скрываем социальный статус
    if (citizenshipValue === 'Нет') {
        socialStatusSection.classList.add('hidden');
    } else {
        socialStatusSection.classList.remove('hidden');
    }
});
