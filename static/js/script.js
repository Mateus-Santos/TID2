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


function validarNumero() {
    var inputNumero = document.getElementById("idade");
    var numero1 = inputNumero.value;
    var inputNumero = document.getElementById("peso");
    var numero2 = inputNumero.value;
    // Verifica se é um número inteiro positivo
    if (!Number.isInteger(Number(numero1)) || Number(numero1) <= 0 || !Number.isInteger(Number(numero2)) || Number(numero2) <= 0) {
      alert("Por favor, digite um número inteiro positivo.");
      inputNumero.value = "";  // Limpa o campo
      inputNumero.focus();     // Coloca o foco de volta no campo
    }
}

function mostrarSelecao() {
    var selectElement = document.getElementById("opcoes");
    var selectedOption = selectElement.options[selectElement.selectedIndex].value;

    alert("Opção selecionada: " + selectedOption);
  }