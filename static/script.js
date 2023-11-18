const form = document.getElementById('quiz-form');
let currentQuestion = 0;

function showNext() {
    const questions = document.querySelectorAll('.question');
    questions[currentQuestion].style.display = 'none';
    currentQuestion = (currentQuestion + 1) % questions.length;
    questions[currentQuestion].style.display = 'block';
}

function showPrevious() {
    const questions = document.querySelectorAll('.question');
    questions[currentQuestion].style.display = 'none';
    currentQuestion = (currentQuestion - 1 + questions.length) % questions.length;
    questions[currentQuestion].style.display = 'block';
}

form.addEventListener('submit', function (event) {
    event.preventDefault();
    // Adicione aqui a lógica para processar/enviar os dados do formulário
    // Você pode enviar os dados para um servidor ou realizar outras ações conforme necessário
});
