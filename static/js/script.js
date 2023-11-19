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
