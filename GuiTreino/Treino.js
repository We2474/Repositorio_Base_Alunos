let numeroSecreto;
let tentativas = 0;

function start() {
    numeroSecreto = Math.floor(Math.random() * 10) + 1;
    tentativas = 0;
    alert("O jogo começou! Tente adivinhar o número entre 1 e 10.");
    jogar();
}

function jogar() {
    let chute = prompt("Digite seu chute:");

    // cancela se o usuário apertar "Cancelar"
    if (chute === null) return;

    chute = Number(chute);
    tentativas++;

    if (chute > numeroSecreto) {
        alert("Tente novamente, o número é MENOR que isso!");
        jogar();
    } else if (chute < numeroSecreto) {
        alert("Tente novamente, o número é MAIOR que isso!");
        jogar();
    } else {
        alert("🎉 Parabéns! Você acertou em " + tentativas + " tentativas.");
    }
}
