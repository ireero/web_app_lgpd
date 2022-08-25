//Código de troca de frase no HTML conforme a pontuação
let div_resultado = document.getElementById('resultado').innerHTML;
div_resultado = div_resultado.substring(21, 26);

if (parseFloat(div_resultado) < 3.0) {
    const text = 'Você ainda não está no caminho da conformidade com a LGPD, entre em contato conosco e deixe sua empresa na frente.';
    document.querySelector('.result-text').innerHTML = text;
}
else if (parseFloat(div_resultado) >= 3.0){
    const text = 'Você entende o que é necessário para se alinhar com a LGPD, entre em contato conosco e deixe sua empresa na frente. ';
    document.querySelector('.result-text').innerHTML = text;
}