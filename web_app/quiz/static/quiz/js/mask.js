//Mask para o número de telefone ter um padrão
$(document).ready(function(){
    $('#id_whatsapp_colaborador').mask("(00) 00000-0000", {placeholder: "Número do representante"});
});

//Bloco para colocar placeholder no input
document.getElementById('id_nome_empresa').placeholder = 'Nome da Empresa'
document.getElementById('id_nome_colaborador').placeholder = 'Nome do representante'
document.getElementById('id_funcao_colaborador').placeholder = 'Função do representante'
document.getElementById('id_email_colaborador').placeholder = 'E-mail corporativo'
document.getElementById('id_whatsapp_colaborador').placeholder = 'Número do representante'
document.getElementById('id_senha').placeholder = 'Senha'
document.getElementById('id_senha').type = 'password';
document.getElementById('id_captcha_1').placeholder = 'Captcha'




//Tratamento do cadastro
const result = document.getElementById('form_msg').innerHTML;
let divResult = document.getElementById('form_msg');

    if(result == '1'){
        divResult.style.display = 'flex' ;
        const textSuccess = 'Cadastro Efetuado';
        divResult.style.color = 'green';
        divResult.innerHTML = textSuccess;

    }
    else if(result == '0'){
        divResult.style.display = 'flex' ;
        const textError = 'Captcha Inválido';
        divResult.innerHTML = textError;
    }
